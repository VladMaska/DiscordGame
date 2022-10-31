import config
import discord 
from discord.ext import commands

import game as g
import control as c
    
# logger = settings.logging.getLogger("bot")
    
def run():

    message = None

    intents = discord.Intents.all()
    intents.message_content = True
    
    bot = commands.Bot( command_prefix="!", intents=intents )
    
    @bot.event 
    async def on_ready():
        print('Logged as {0}!'.format( "BOT" ) )

    @bot.command()
    async def game(ctx):
        c.message = await ctx.send( g.GetArea() )
        await c.message.add_reaction("⬆️")
        await c.message.add_reaction("⬅️")
        await c.message.add_reaction("⬇️")
        await c.message.add_reaction("➡️")
        # print( c.message )
    
    @bot.command()
    async def test(ctx):
        new_msg = await ctx.send("hello!")
        await new_msg.add_reaction("⬆️")
        await new_msg.add_reaction("⬅️")
        await new_msg.add_reaction("⬇️")
        await new_msg.add_reaction("➡️")

    @bot.command()
    async def up(ctx):
        c.Up()
        await c.message.edit( content=g.GetArea() )

    @bot.command()
    async def left(ctx):
        c.Left()
        await c.message.edit( content=g.GetArea() )
    
    @bot.command()
    async def down(ctx):
        c.Down()
        await c.message.edit( content=g.GetArea() )

    @bot.command()
    async def right(ctx):
        c.Right()
        await c.message.edit( content=g.GetArea() )

    @bot.event
    async def on_raw_reaction_add( payload ):

        id = c.message.id

        if id == payload.message_id:

            emoji = payload.emoji.name

            if emoji == '⬆️':
                c.Up()
                await c.message.edit( content=g.GetArea() )
            if emoji == '⬅️':
                c.Left()
                await c.message.edit( content=g.GetArea() )
            if emoji == '⬇️':
                c.Down()
                await c.message.edit( content=g.GetArea() )
            if emoji == '➡️':
                c.Right()
                await c.message.edit( content=g.GetArea() )

    @bot.event
    async def on_raw_reaction_remove( payload ):

        id = c.message.id

        if id == payload.message_id:

            emoji = payload.emoji.name

            if emoji == '⬆️':
                c.Up()
                await c.message.edit( content=g.GetArea() )
            if emoji == '⬅️':
                c.Left()
                await c.message.edit( content=g.GetArea() )
            if emoji == '⬇️':
                c.Down()
                await c.message.edit( content=g.GetArea() )
            if emoji == '➡️':
                c.Right()
                await c.message.edit( content=g.GetArea() )
        
        
    bot.run( config.TOKEN, root_logger=True )

if __name__ == "__main__":
    run()