# 商业分析项目模板

## 目录结构

- `data/raw/`：原始数据，只读保存，不提交 Git
- `data/processed/`：清洗后的数据，不提交 Git
- `notebooks/`：探索性分析和 Notebook
- `sql/`：SQL 查询
- `src/`：可复用 Python 代码
- `outputs/`：图表、报表和导出结果
- `tests/`：测试代码

## 使用方式

VS Code 应自动选择项目中的 `.venv`。如未自动选择，运行命令面板中的
`Python: Select Interpreter`，然后选择 `.venv\Scripts\python.exe`。

安装项目依赖前，先确认需要哪些库：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

运行分析模板：

```powershell
.\.venv\Scripts\python.exe src\analysis_template.py
```

## 数据安全

不要将客户数据、个人信息、账号密码、API Key 或数据库连接字符串提交到 GitHub。
需要共享结构时，使用脱敏样本数据和 `.env.example`。
