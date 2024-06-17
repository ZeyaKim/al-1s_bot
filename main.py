import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# .env 파일 로드
load_dotenv()

# 환경 변수에서 토큰 가져오기
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠 접근 허용

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


# 가져온 토큰을 사용하여 봇 실행
bot.run(TOKEN)
