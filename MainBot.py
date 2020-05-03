import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Azure Community TM') )
  print(f'Im online on {len(client.guilds)} server.')
  
  
@client.command()
  async def PingPong(ctx):
   await ctx.send(f"Pong the latency is: {round(client.latency * 1000)}ms")
return




client.run("token")
