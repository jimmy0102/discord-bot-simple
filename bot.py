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
    try:
        synced = await bot.tree.sync()
        print(f'{len(synced)}個のコマンドを同期しました')
    except Exception as e:
        print(f'コマンドの同期に失敗しました: {e}')

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # 特定のチャンネルIDかつ、Botがメンションされているかリプライされている場合のみ返信
    if message.channel.id == 1396236494301298801:
        # Botがメンションされているか、メッセージがBotへのリプライかチェック
        if bot.user in message.mentions or (message.reference and message.reference.resolved and message.reference.resolved.author == bot.user):
            # メンションを除去してメッセージ内容を取得
            content = message.content.replace(f'<@{bot.user.id}>', '').strip()
            if content:
                await message.channel.send(f'「{content}」が入力されました。')
            else:
                await message.channel.send('何も入力されていません。')

    # コマンドも処理できるようにする
    await bot.process_commands(message)

# コマンドの例
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# スラッシュコマンド: ヘルプ
@bot.tree.command(name='help', description='このBotの使い方を表示します')
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title='Discord Bot ヘルプ',
        description='このBotの使い方を説明します',
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name='基本機能',
        value='このBotは全てのメッセージに「こんにちは！良い一日を！」と返信します。',
        inline=False
    )
    
    embed.add_field(
        name='コマンド一覧',
        value='**`/help`** - このヘルプメッセージを表示\n**`!ping`** - Botの応答を確認（Pong!と返信）',
        inline=False
    )
    
    embed.add_field(
        name='必要な権限',
        value='• メッセージの送信\n• メッセージ履歴の表示\n• チャンネルの表示',
        inline=False
    )
    
    embed.set_footer(text='Discord Bot v1.0')
    
    await interaction.response.send_message(embed=embed)

# Botを起動
if __name__ == '__main__':
    # 環境変数からトークンを取得
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print('エラー: DISCORD_BOT_TOKENが.envファイルに設定されていません')
        exit(1)

    bot.run(token)
