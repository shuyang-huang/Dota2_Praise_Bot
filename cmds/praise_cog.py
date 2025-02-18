import discord
from discord.ext import commands
import argparse

from dota2_data_puller.stratz import Stratz
from llm.llm import Llm


class PraiseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="夸")
    async def praise(self, ctx, user: discord.Member, *, args: str = ""):
        """
        Praise a user with the hero!
        --hero      hero name
        --match_id  match id
        --word      word count
        """
        try:
            parsed_args = self.parse_args(args)

            hero = parsed_args.hero or "Invalid Hero"
            match_id = parsed_args.match_id or "Invalid Match Id"
            word_cnt = parsed_args.word or "Invalid word count"

            await ctx.send(f"You played so good {user.mention} 🎉!!!!\n"
                           f"Hero: {hero}\n"
                           f"Match_ID: {match_id}\n"
                           f"Word count: {word_cnt}")

            # Generate the praise
            match_data = Stratz.get_match_data(match_id)
            praise_word = Llm.get_praise(match_data, hero, word_cnt, word_cnt * 3)

            await ctx.send(f"{user.mention} 😘 🥰 😍 😊 {praise_word}\n")

        except Exception as e:
            await ctx.send(f"❌ Invalid input: {str(e)}")


    def parse_args(self, args: str):
        """
        --hero      hero name
        --match_id  match id
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--hero", type=str, nargs="+", default=None, help="hero name")
        parser.add_argument("--match_id", type=str, nargs="?", default=None, help="match id")
        parser.add_argument("--word", type=int, nargs="?", default=300, help="word count")

        tokens = args.split()
        parsed_args = parser.parse_args(tokens)

        if parsed_args.hero:
            parsed_args.hero = " ".join(parsed_args.hero)

        return parsed_args


async def setup(bot):
    await bot.add_cog(PraiseCog(bot))