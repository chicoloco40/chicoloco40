import os
import asyncio
import discord
from discord.ext import commands
import tweepy
from fastapi import FastAPI, BackgroundTasks
import uvicorn

# Architecture Matrix Setup for Global Deployment
app = FastAPI(title="CL40 World Global Master Cloud Node")

# 🔒 Fetching the international token directly from global system environment
X_INTERNATIONAL_TOKEN = os.getenv("X_INTERNATIONAL_MASTER_TOKEN")

try:
    # Initializing the Master Publisher via the secured international token
    if X_INTERNATIONAL_TOKEN:
        x_client = tweepy.Client(bearer_token=X_INTERNATIONAL_TOKEN)
        print("🌍 [Global Engine]: International security token validated safely.")
    else:
        print("⚠️ [Global Engine]: Waiting for international token transmission.")
except Exception as e:
    print(f"❌ [Global Engine] Encryption error: {e}")

active_bots = {}

class InternationalCorporateBot(commands.Bot):
    def __init__(self, name):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot_name = name
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"📡 [CL40 World]: Worker active -> {self.bot_name}")
        active_bots[self.bot_name] = self

# 🌐 ---- International HTTP Router Endpoint ----

@app.post("/publish")
async def publish_global_news(payload: dict, background_tasks: BackgroundTasks):
    text = payload.get("text")
    channel_id = payload.get("channel_id")
    
    if not text:
        return {"status": "rejected", "reason": "Empty payload"}

    # 1. Pushing directly to X/Twitter globally using the international token
    try:
        if x_client:
            x_client.create_tweet(text=text)
    except Exception as e:
        print(f"❌ X Network Broadcast Failure: {e}")

    # 2. Asynchronous broadcast loop to all active Discord nodes
    if channel_id:
        for name, bot_instance in active_bots.items():
            if bot_instance.is_ready():
                channel = bot_instance.get_channel(int(channel_id))
                if channel:
                    background_tasks.add_task(channel.send, f"📰 **[Global Broadcast via HTTP]:** {text}")

    return {"status": "broadcasted", "scope": "international"}

async def run_bot_worker(token, name):
    bot = InternationalCorporateBot(name=name)
    try:
        await bot.start(token)
    except Exception as e:
        print(f"❌ Worker offline [{name}]: {e}")

async def main():
    # Production Infrastructure Mapping
    infrastructure_bots = {
        "CL40 World Bot": os.getenv("DISCORD_TOKEN_CL40_WORLD"),
        "Chico Loco 40 Bot": os.getenv("DISCORD_TOKEN_CHICO_LOCO"),
        "Global NSW Bot": os.getenv("DISCORD_TOKEN_GLOBAL_NSW")
    }

    bot_tasks = [run_bot_worker(token, name) for name, token in infrastructure_bots.items() if token]

    # Server configuration for high speed delivery nodes
    port = int(os.getenv("PORT", 8080))
    config = uvicorn.Config(app=app, host="0.0.0.0", port=port, loop="asyncio")
    server = uvicorn.Server(config)

    await asyncio.gather(server.serve(), *bot_tasks)

if __name__ == "__main__":
    asyncio.run(main())
