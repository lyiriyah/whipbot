#!/usr/bin/env python3

from discord.ext import commands
import os, discord, logging

logging.basicConfig()

configfile = os.getcwd() + "/config.conf"
with open(configfile, "r") as f:
    for l in f:
        words = l.split()
        if words[0].startswith("#"): pass
        else: exec(' '.join(words).replace(" ", ""))

try:
    x = bot_token
    x = prefix
    del x
except NameError:
    raise NameError("You haven't set your bot token/prefix at all/correctly. Check your config.")

try:
    x = mp_role_id
    x = whip_role_id
    del x
except NameError:
    raise NameError("You haven't set your MP/whip role ID at all/correctly. Check your config.")

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Ready as {bot.user}")

@has_role(whip_role_id)
@bot.command()
async def whip(ctx, ayeno, url):
    for user in ctx.message.guild.get_role(mp_role_id).members:
        if ayeno.lower() not in aye_no_opts:
            await ctx.send(f"{ayeno} invalid argument for aye/no (must be one of {aye_no_opts}."))
            return
        if user.name not in dont_dm and user not in ctx.message.guild.get_role(whip_role_id):
            try:
                await user.send(f"The Party wants you to vote {ayeno} on this bill: {url}. Do it, or we will be sad.")
            except discord.errors.HTTPException:
                await ctx.send(f"Could not DM {user.mention}.")

bot.run(bot_token)
