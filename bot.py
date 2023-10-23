import discord
import responses   
import responselists as r
import ai_generate as ai

async def send_message(message, user_message, username):
    try:
        response = responses.handle_response(user_message, username)
        await message.channel.send(response)
    except Exception as e:
        print(e)

async def wheelSpin(message, user_message):
    try:
        response = responses.wheelspin(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)



##main
def run_discord_bot():
    TOKEN = ""
   
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message)
        username = str(message.author)
        user_message = str(message.content)
        channel =  str(message.channel)
       
        print(f"username: {username} - Message: {user_message} - Channel: {channel}"  )
        if user_message[0:10] == "!wheelspin":
            print("Wheelspin detected")
            await wheelSpin(message, user_message[11:])
        if user_message == "!dota":
           await message.channel.send(responses.dota_call_to_arms())
        
        if user_message == "!dota+":
            await message.channel.send(responses.dota_call_to_arms(""))

        if user_message[0:6] == "!image":
            await message.channel.send("Feature has been removed.")

        else:
            await send_message(message, user_message, username)

    client.run(TOKEN)

