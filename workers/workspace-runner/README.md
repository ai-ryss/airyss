# workers/workspace-runner

ワークスペース管理ワーカー（Python 予定）

## 概要

- 言語: Python 3.12+
- キューシステム: Redis (RQ または Celery 予定)
- Docker SDK: docker-py

## 役割

1. Redis キューからワークスペース操作ジョブを受信
2. Docker API でコンテナを起動・停止・削除
3. ワークスペースの状態を postgres に書き戻す

## セットアップ（準備中）

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python worker.py
```

> ※ 現在はプレースホルダです。
