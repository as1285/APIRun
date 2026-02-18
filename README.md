# 接口自动化测试框架（API Run）

## 概述
- 数据驱动的接口自动化测试框架，核心基于 Excel + requests + unittest + DDT + HTMLTestRunner。
- 用例无需编写代码，全部在 Excel 中配置即可执行。
- 支持多客户端与环境登录，自动获取并复用 token，支持用例依赖、参数依赖与断言。
- 适配微商城、新零售 APP、骑手 APP、电商云后台等客户端。

## 核心能力
- 封装 HTTP 请求与统一日志，自动输出请求/响应明细。
- Excel 驱动用例：参数、断言、依赖关系集中配置。
- 支持用例依赖（case_depend）、数据依赖（data_depend/field_depend，基于 JSONPath）。
- 批量执行与可视化报告：生成 report/result.html 与 result.xls。
- 邮件通知：执行后可将报告与日志作为附件发送。
- 多端登录：按客户端类型（app/wei/rider/cloud）自动获取并缓存 token。

## 目录结构
- conf：配置与数据
  - settings.py：路径、环境、账号与邮件配置
  - set_token.py：多端登录与 token 管理
  - data_conf.py：Excel 字段位置信息
  - case.xls：用例数据
- common：公共能力
  - run_method.py：requests 封装与日志
  - operation_excel.py、readexcel.py、writeexcel.py：Excel 读写
  - get_data.py：从 Excel 提取用例字段
  - depend_data.py：用例/数据依赖处理（jsonpath-rw）
  - assert_result.py：简单断言
- case：unittest 收口用例（test_api.py）
- logs：运行日志（all.logs，按日切分）
- report：测试报告（result.html、result.xls）
- run.py：控制台执行与日志输出
- run_this.py：生成 HTML 报告并发送邮件

## 环境要求
- Python 3.7+
- 操作系统：Windows/macOS/Linux
- 依赖（建议使用虚拟环境）：
  - requests
  - ddt
  - xlrd==1.2.0（处理 .xls；2.x 不支持 .xls）
  - xlutils（写回 Excel，依赖 xlwt）
  - xlwt
  - jsonpath-rw
  - beautifulsoup4、html5lib（邮件正文/报告处理可选）

安装示例：

```bash
pip install requests ddt xlrd==1.2.0 xlutils xlwt jsonpath-rw beautifulsoup4 html5lib
```

## 快速开始
- 配置环境
  - 安装依赖。
  - 在 conf/settings.py 中配置报告、日志路径与各客户端 host/账号，完善邮件服务器信息。
  - 将用例维护在 conf/case.xls 的 Sheet1 中。
- 执行用例
  - 生成 HTML 报告并发送邮件：
    ```bash
    python run_this.py
    ```
  - 控制台运行（日志输出到 logs）：
    ```bash
    python run.py
    ```
- 查看结果
  - 可视化报告：report/result.html
  - Excel 结果：report/result.xls
  - 运行日志：logs/all.logs

## Excel 字段规范（Sheet1）
- case_id：用例 ID
- client_type：客户端类型，app | wei | rider | cloud
- description：用例描述
- host：接口主机地址
- api：接口路径
- run：是否执行（yes 执行）
- method：请求方法（get | post）
- header：请求头（JSON 字符串）
- case_depend：用例依赖（被依赖用例的 case_id）
- data_depend：依赖响应中的 JSONPath 表达式
- field_depend：将依赖值写入到请求体的字段名
- body：请求体（JSON 字符串）
- expect：断言表达式，形如 JSONPATH=期望值；支持分号分隔多断言
- result：失败时写入返回内容，成功显示“测试通过”
- db、setup_sql、teardown_sql：预留数据库校验/准备与回滚（按需扩展）

示例（多断言）：
- $.msg=操作成功;$.code=100000

## 最小可运行 Excel 用例模板

### 1. 表头示例（第 1 行）
- 列顺序需要与上面的“字段规范”保持一致，列名可以按团队习惯调整。
- 推荐表头（从 A 列开始）：

```text
case_id | client_type | description | host | api | run | method | header | case_depend | data_depend | field_depend | body | expect | result
```

### 2. 第一条用例示例（第 2 行）
以下示例展示一个“无依赖”的最小用例，只要你的接口在当前环境可访问并返回约定字段，即可直接运行：

| 列名         | 示例值            | 说明 |
| ------------ | ----------------- | ---- |
| case_id      | DEMO_001          | 用例唯一标识 |
| client_type  | app               | 使用 app 端配置与 token（见 conf/settings.py 与 conf/set_token.py） |
| description  | 健康检查接口成功 | 用例描述 |
| host         | （留空即可）     | 当前主流程由 client_type + api 决定 URL，此列可暂时忽略 |
| api          | apis/demo/health | 你的接口路径，例如 /apis/demo/health |
| run          | yes               | 标记执行该行用例 |
| method       | get               | 请求方法：get 或 post |
| header       | {}                | 预留字段，当前实现主要使用框架自动生成的 header，可先写 {} |
| case_depend  | （留空）          | 本示例无用例依赖 |
| data_depend  | （留空）          | 本示例无数据依赖 |
| field_depend | （留空）          | 本示例无数据依赖注入 |
| body         | {}                | GET 场景可为空对象；POST 时填请求体 JSON |
| expect       | $.code=100000     | 期望响应 JSON 中 code 字段为 100000，根据你的接口调整 |
| result       | （留空）          | 执行后由框架写入“测试通过”或失败时的响应文本 |

> 提示：示例中的 `apis/demo/health` 和 `$.code=100000` 仅为演示，请替换成你环境中真实存在且容易验证的接口与期望值。

### 3. 执行步骤演示
- 步骤 1：按上述表头与示例，在 conf/case.xls 的 Sheet1 中配置第 1、2 行。
- 步骤 2：确认 conf/settings.py 中已正确配置 app_host、账号以及邮件相关配置（如需发邮件）。
- 步骤 3：在项目根目录执行：

```bash
python run_this.py
```

- 步骤 4：执行完成后：
  - 在 report/result.html 中查看可视化测试报告；
  - 在 report/result.xls 中查看该条用例的执行结果；
  - 在 logs/all.logs 中查看完整请求/响应日志。

## 执行流程简述
- case/test_api.py 使用 DDT 逐行读取 Excel 并驱动执行。
- run.RunTest.go_on_run：
  - 读取 client_type、api、method、header、body、expect 等字段。
  - 自动获取/缓存对应客户端的 token。
  - 若设置 case_depend/data_depend/field_depend，则按 JSONPath 从依赖用例响应中提取值并注入本用例请求体。
  - 发起请求、匹配断言、写回 Excel 与报告/日志。

## 报告与通知
- HTML 报告位于 report/result.html，包含用例通过/失败统计与详细日志跳转。
- Excel 结果写入 report/result.xls，便于追踪与二次分析。
- 邮件发送（conf/send_email.py）会附加报告与日志，请在 settings.py 中配置邮件服务器与收件人。

## 最佳实践与注意事项
- Excel 中所有 JSON 字段请使用双引号，例如：{"key":"value"}。
- 由于 case.xls 为 .xls 格式，需固定使用 xlrd==1.2.0 与 xlutils/xlwt。
- 请勿在仓库提交真实账号、密码、数据库与邮件凭据。将敏感信息置于本地配置或环境变量。
- 如需扩展到更多客户端/环境，请在 conf/settings.py 与 conf/set_token.py 中新增对应配置与登录流程。

## 规划与扩展
- Jenkins/CI 集成，定时任务与多环境矩阵执行。
- 数据构造脚本与低耦合数据依赖（减少对线上/共享数据的依赖）。
- 可视化管理：用例/任务/报告面板。
