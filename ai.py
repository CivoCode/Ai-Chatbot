
import nextcord
import random
from nextcord.ext import commands
from neuralintents import GenericAssistant

chatbot = GenericAssistant('Discordbot/intents.json')
chatbot.train_model()
chatbot.save_model()


#THIS IS IN A COG JUST CHANGE commands.Cog.Listsner() to bot.event if u want it in the main file and remove self
class Ai(commands.Cog):
    def __init__(self, client: commands.Client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message, client):

        if message.author == client.user:
            return

        if message.content.startswith("bot"):
            response = chatbot.request(message.content[2:])
            await message.channel.send(response)
