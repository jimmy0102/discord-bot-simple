# Discord Bot

シンプルなDiscord Botです。メッセージに反応して定型文を返します。

## 機能

- 「こんにちは」と送ると「こんにちは！良い一日を！」と返信
- 「おはよう」と送ると「おはようございます！」と返信
- 「こんばんは」と送ると「こんばんは！今日もお疲れ様でした！」と返信
- `!ping`コマンドで「Pong!」と返信

## セットアップ

1. 依存関係をインストール：
   ```bash
   pip install -r requirements.txt
   ```

2. `.env.example`を`.env`にコピーして、Botトークンを設定：
   ```bash
   cp .env.example .env
   ```
   `.env`ファイルを編集して`DISCORD_BOT_TOKEN`に実際のトークンを設定

3. Discord Developer PortalでBotの設定：
   - [Discord Developer Portal](https://discord.com/developers/applications/)にアクセス
   - 「Bot」セクションで「MESSAGE CONTENT INTENT」を有効化

4. Botを起動：
   ```bash
   python bot.py
   ```

## 必要な権限

- Send Messages
- Read Message History
- View Channels

## 環境変数

- `DISCORD_BOT_TOKEN`: Discord BotのトークンThe user opened the file /Users/jimmy/20250720_discord_bot/README.md in the IDE. This may or may not be related to the current task.