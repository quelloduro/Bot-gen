                                                            ######################
                                                            # Made by quelloduro #
                                                            # Give credits ty <3 #
                                                            # Leave a star ty <3 #
                                                            ######################

import discord
from discord.ext import commands
import random
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.',intents=intents)


spotify_accounts = [line.strip() for line in open('account/spotify.txt', 'r').readlines()]
netflix_accounts = [line.strip() for line in open('account/netflix.txt', 'r').readlines()]
roblox_accounts = [line.strip() for line in open('account/roblox.txt', 'r').readlines()]
disney_accounts = [line.strip() for line in open('account/disney+.txt', 'r').readlines()]
microsoft_accounts = [line.strip() for line in open('account/microsoft.txt', 'r').readlines()]
tiktok_accounts = [line.strip() for line in open('account/tiktok.txt', 'r').readlines()]
xbox_accounts = [line.strip() for line in open('account/xbox.txt', 'r').readlines()]
crunchyroll_accounts = [line.strip() for line in open('account/crunchyroll.txt', 'r').readlines()]
steam_accounts = [line.strip() for line in open('account/steam.txt', 'r').readlines()]

@bot.event
async def on_ready():
    print(f'{bot.user} is online')

@bot.command()
async def gen(ctx, platform):
    if platform.lower() == 'spotify':
        if not spotify_accounts:
            await ctx.send('No more Spotify accounts available!')
            return
        account = random.choice(spotify_accounts)
        spotify_accounts.remove(account)
    elif platform.lower() == 'netflix':
        if not netflix_accounts:
            await ctx.send('No more Netflix accounts available!')
            return
        account = random.choice(netflix_accounts)
        netflix_accounts.remove(account)
    elif platform.lower() == 'roblox':
        if not roblox_accounts:
            await ctx.send('No more Roblox accounts available!')
            return
        account = random.choice(roblox_accounts)
        roblox_accounts.remove(account)
    elif platform.lower() == 'disney+':
        if not disney_accounts:
            await ctx.send('No more Disney+ accounts available!')
            return
        account = random.choice(disney_accounts)
        disney_accounts.remove(account)
    elif platform.lower() == 'microsoft':
        if not microsoft_accounts:
            await ctx.send('No more Microsoft accounts available!')
            return
        account = random.choice(microsoft_accounts)
        microsoft_accounts.remove(account)
    elif platform.lower() == 'tiktok':
        if not tiktok_accounts:
            await ctx.send('No more TikTok accounts available!')
            return
        account = random.choice(tiktok_accounts)
        tiktok_accounts.remove(account)
    elif platform.lower() == 'xbox':
        if not xbox_accounts:
            await ctx.send('No more Xbox accounts available!')
            return
        account = random.choice(xbox_accounts)
        xbox_accounts.remove(account)
    elif platform.lower() == 'crunchyroll':
        if not crunchyroll_accounts:
            await ctx.send('No more Crunchyroll accounts available!')
            return
        account = random.choice(crunchyroll_accounts)
        crunchyroll_accounts.remove(account)
    elif platform.lower() == 'steam':
        if not steam_accounts:
            await ctx.send('No more Steam accounts available!')
            return
        account = random.choice(steam_accounts)
        steam_accounts.remove(account)
    else:
        await ctx.send('Invalid option!')
        return


    with open('spotify.txt', 'w') as f:
        for account in spotify_accounts:
            f.write(account + '\n')
    with open('netflix.txt', 'w') as f:
        for account in netflix_accounts:
            f.write(account + '\n')
    with open('roblox.txt', 'w') as f:
        for account in roblox_accounts:
            f.write(account + '\n')
    with open('disney+.txt', 'w') as f:
        for account in disney_accounts:
            f.write(account + '\n')
    with open('microsoft.txt', 'w') as f:
        for account in microsoft_accounts:
            f.write(account + '\n')
    with open('tiktok.txt', 'w') as f:
        for account in tiktok_accounts:
            f.write(account + '\n')
    with open('xbox.txt', 'w') as f:
        for account in xbox_accounts:
            f.write(account + '\n')
    with open('crunchyroll.txt', 'w') as f:
        for account in crunchyroll_accounts:
            f.write(account + '\n')
    with open('steam.txt', 'w') as f:
        for account in steam_accounts:
            f.write(account + '\n')

    try:
        await ctx.author.send(f"f'Generated account of {platform}: {account}")
        await ctx.send("Your account credentials have been sent to your dm ")
    except discord.Forbidden:
        await ctx.send("I can't send you the account because you have dm closed")

@bot.command()
async def stock(ctx):
    embed = discord.Embed(title="Account in stock", color=discord.Color.blue())

    embed.add_field(name="Spotify", value=f"{len(spotify_accounts)}", inline=False)
    embed.add_field(name="Netflix", value=f"{'No accounts' if not netflix_accounts else len(netflix_accounts)}", inline=False)
    embed.add_field(name="Roblox", value=f"{'No accounts' if not roblox_accounts else len(roblox_accounts)}", inline=False)
    embed.add_field(name="Disney+", value=f"{'No accounts' if not disney_accounts else len(disney_accounts)}", inline=False)
    embed.add_field(name="Microsoft", value=f"{'No accounts' if not microsoft_accounts else len(microsoft_accounts)}", inline=False)
    embed.add_field(name="TikTok", value=f"{'No accounts' if not tiktok_accounts else len(tiktok_accounts)}", inline=False)
    embed.add_field(name="Xbox", value=f"{'No accounts' if not xbox_accounts else len(xbox_accounts)}", inline=False)
    embed.add_field(name="Crunchyroll", value=f"{'No accounts' if not crunchyroll_accounts else len(crunchyroll_accounts)}", inline=False)
    embed.add_field(name="Steam", value=f"{'No accounts' if not steam_accounts else len(steam_accounts)}", inline=False)

    await ctx.send(embed=embed)


bot.run('token here')