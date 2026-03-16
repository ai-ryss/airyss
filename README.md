# AIryss vNext

AIryss は「人間が AI エージェントを仲介・統治しながら開発を進める」ブラウザ IDE / オーケストレーション基盤です。
実装エージェント Iryss と設計レビューエージェント Aryss を人間が監督・調整することで、品質と自律性を両立させます。

---

## エージェント・責務モデル

### Iryss（実装エージェント）
- 具体的なコーディング・リファクタリング・テスト作成を担当
- Human から与えられたタスクを実際にファイルへ反映する
- 実行結果（差分・エラー・テスト結果）を Human に返す

### Aryss（設計レビューエージェント）
- Iryss の成果物に対して設計・品質・一貫性の観点でレビューを行う
- アーキテクチャ上の問題点・改善案を Human に提示する
- 実装はせず、判断材料と代替案の提供に専念する

### Human（仲介・統治者）
- Iryss へのタスク指示と成果物の承認
- Aryss のレビュー結果を評価し、次のアクションを決定
- 両エージェントの出力を統合し、最終的な意思決定を行う

### AIryss（統合 IDE / オーケストレーション基盤）
- Iryss・Aryss・Human の協働を支えるプラットフォーム
- ブラウザ上で会話・コード編集・実行環境を一元提供
- エージェントへのプロンプト管理・コンテキスト制御・認証を担う

---

## monorepo 構成

```
airyss/
├── apps/
│   ├── web/                  # フロントエンド (Next.js 予定)
│   └── api/                  # バックエンド API (FastAPI 予定)
├── workers/
│   └── workspace-runner/     # ワークスペース管理ワーカー (Python 予定)
├── infra/
│   ├── nginx/                # リバースプロキシ設定
│   ├── postgres/             # DB 初期化スクリプト
│   ├── redis/                # Redis 設定
│   └── workspace-images/     # ワークスペース用 Docker イメージ
│       └── base/
├── prompts/
│   ├── iryss/                # Iryss 用システムプロンプト
│   └── aryss/                # Aryss 用システムプロンプト
├── docs/
│   ├── architecture/         # アーキテクチャ設計文書
│   ├── api/                  # API 仕様書
│   └── infra/                # インフラ設計文書
├── compose.yaml              # Docker Compose 定義
├── Makefile                  # 開発用タスクランナー
└── .env.example              # 環境変数テンプレート
```

---

## ローカル開発開始方法

> ※ 現在準備中です。以下は予定されている手順です。

```bash
# 1. 環境変数を設定
cp .env.example .env

# 2. サービスを起動
make up

# 3. ログを確認
make logs
```

ブラウザで http://localhost にアクセスしてください。
