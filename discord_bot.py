
import discord
from discord.ext import commands
from config.config import Config
from logger.logger_config import logger


def run_bot_service():
    # Enable intents, or bot is not able to read channel text
    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True
    intents.message_content = True

    bot = commands.Bot(command_prefix="--", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"✅ Bot 已上线！当前登录为：{bot.user}")

    async def load_cogs():
        await bot.load_extension("cmds.praise_cog")
        await bot.load_extension("cmds.profanity_cog")
        await bot.load_extension("cmds.snide_cog")

    @bot.event
    async def setup_hook():
        await load_cogs()

    @bot.event
    async def on_message(message):
        # Process message on all user input
        # May be used in future
        if message.author == bot.user:
            return

        await bot.process_commands(message)

    # Run bot
    bot.run(Config.discord_bot_token)


if  __name__ == "__main__":
    run_bot_service()


