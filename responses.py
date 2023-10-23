import random 
import responselists as x
import discord


def handle_response(message,username) -> str:
    
    p_message =  message.lower()
    responses = x.stelle_responses(username)
    if p_message == "user message here":
        return responses[random.randrange(0,len(responses))]
    elif p_message == "user message here":
        return "message here"

def wheelspin(message) -> str:
    #generate a random number range from 0 - arraylist max
    p_message = message.lower()

    gamelist = p_message.split("-")
    x = gamelist[random.randrange(0, len(gamelist))]
    return x if x != "" else "Invalid input"

def dota_call_to_arms():
    a = x.dota_userlist()
    response = "message here"
    for i in a:
        response = response + " " + i

def dota_call_to_arms(extra_player):
    a = x.dota_userlist()
    response = "message here"
    for i in a:
        response = response + " " + i
    response = response + " with " + extra_player
    
    print(response)
    return response