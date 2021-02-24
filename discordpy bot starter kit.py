#u need to install discord.py -> pip install discord.py
import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!') #this is your bot prefix, with client u make your commands and events!
client.run('YOUR BOT TOKEN')

#this is first bot event, which triggers when you run your bot, also u can set your bot status and activity from here.
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("your bot status"))
    print ('your bot name logged in.')
    

#let's make your first command which is a ping command, that returns some text.
#what's coming after async def, it's your command name!

@client.command()
async def ping(ctx):
    await ctx.send ('pong')

#also let's make a command to soo your bot latency.
#remember! always use @client.command() for a command!
@client.command()
async def latencyNotEmbed(ctx):
    await ctx.send (f'my latency is {round (client.latency * 1000)} ms.') #i used here *1000 because latency is transmited in seconds, but we want it in ms

#if you want your text to look better you can use embed for your bot to send messages
#let's do this on latency command.
#also in client.command brackets u can add aliases and your bot will respond to these alliases with this command
@client.command(aliases = ['latency', 'lat'])
async def latencyEmbed(ctx):
    embed = discord.Embed{(description= f"**My latency is {round (client.latency * 1000)} ms.**", color=discord.Color.blue())}
    await ctx.send(embed= embed, delete_after=20)

#i strongly reccomand you to study discord.py API which can be found here 'https://discordpy.readthedocs.io/en/latest/', and join discord.py server,
#i've learned a lot of things from here, people always help and a lot of people can help you with your code. i hope i helped you
