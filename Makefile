.PHONY: up down logs ps help

# デフォルトターゲット
help:
	@echo "AIryss vNext - 開発用コマンド"
	@echo ""
	@echo "使い方:"
	@echo "  make up      - サービスをバックグラウンドで起動"
	@echo "  make down    - サービスを停止・削除"
	@echo "  make logs    - ログをフォロー表示"
	@echo "  make ps      - サービスの状態を表示"

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps
