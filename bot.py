import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Botの設定
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました')

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return

    # メッセージに反応して返信
    if 'こんにちは' in message.content:
        await message.channel.send('こんにちは！良い一日を！')
    elif 'おはよう' in message.content:
        await message.channel.send('おはようございます！')
    elif 'こんばんは' in message.content:
        await message.channel.send('こんばんは！今日もお疲れ様でした！')

    # コマンドも処理できるようにする
    await bot.process_commands(message)

# コマンドの例
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Botを起動
if __name__ == '__main__':
    # 環境変数からトークンを取得
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print('エラー: DISCORD_BOT_TOKENが.envファイルに設定されていません')
        exit(1)
    
    bot.run(token)
