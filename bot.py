import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f":p")
    )
    

@client.event
async def on_presence_update(bef, now):
    try:
        if now.activity.name == "Genshin Impact":
            print("Genshin Impact detected")
            channel = client.get_channel(CHANNEL_ID)
            await channel.send(f"This pedophile{now.mention} open genshin impact, call authorities",file=discord.File('jaja.png'))
    except:
        pass
        
client.run(TOKEN)