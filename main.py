import asyncio
import json
import os
import discord
from discord.ext import commands

class CL40AgencyBot(commands.Bot):
    def __init__(self, bot_index, token):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)
        self.bot_index = bot_index
        self.token = token

    async def on_ready(self):
        print(f"👉 [Bot #{self.bot_index}] Active & Connected: {self.user.name} ({self.user.id})")
        await self.change_presence(activity=discord.Game(name="CL40.WORLD | Official Agency"))

    async def on_message(self, message):
        if message.author.bot:
            return

        # Auto-Moderation System
        spam_keywords = ["scam", "hack", "discord.gg/fake"]
        if any(word in message.content.lower() for word in spam_keywords):
            await message.delete()
            await message.channel.send(f"⚠️ {message.author.mention} Message removed by CL40 Security.", delete_after=5)
            return

        await self.process_commands(message)

async def launch_agency():
    if not os.path.exists("tokens.json"):
        print("❌ Error: tokens.json file missing!")
        return

    with open("tokens.json", "r") as f:
        tokens = json.load(f)

    print(f"⚡ Starting CL40 Agency with {len(tokens)} Bots...")

    tasks = []
    for idx, token in enumerate(tokens, start=1):
        clean_token = token.strip()
        if clean_token:
            bot = CL40AgencyBot(bot_index=idx, token=clean_token)
            tasks.append(bot.start(clean_token))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(launch_agency())
