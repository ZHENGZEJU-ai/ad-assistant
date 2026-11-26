# AD Assistant

静电吸附与电粘附文献助手。项目沿用 `esfm-assistant` 的轻量技术栈：FastAPI、SQLite FTS5、可选的语义向量检索，以及 DeepSeek / 通义千问模型接口。

## 当前状态

- 已放入 `PDFs/electroadhesion/` 的 144 篇本地 PDF。
- SQLite 数据库已初始化为空库；建库和全文抽取后可进行关键词检索。
- 配置百炼 Embedding API Key 后，可生成语义向量并启用混合检索。
- API 密钥保存在本地 `.env`，不会提交到 Git。

## 启动与建索引

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
cp .env.example .env
# 在 .env 填入 DASHSCOPE_API_KEY 和所选对话模型的 API Key
python scripts/ingest_pdfs.py
python scripts/build_vectors.py
uvicorn app.main:app --reload
```

服务启动后访问 http://127.0.0.1:8000。仅用 SQLite 关键词检索时，可以跳过向量构建；设置百炼 API Key 后运行 `build_vectors.py` 以启用语义检索。

## 目录

- `app/`：FastAPI 服务、检索、问答和页面。
- `scripts/`：PDF 导入、向量构建及维护工具。
- `data/library.db`：独立初始化的空 SQLite 文献库；索引由本地 PDF 导入生成。
- `PDFs/electroadhesion/`：当前整理的电粘附 PDF 语料。
- `render.yaml`：Render 部署配置模板；部署时需在服务设置中配置 API Key。

## 配置

复制 `.env.example` 为 `.env`，设置 `DASHSCOPE_API_KEY`，并选择 `LLM_PROVIDER=deepseek` 或 `LLM_PROVIDER=qwen`。不要将 `.env` 提交到版本库。

