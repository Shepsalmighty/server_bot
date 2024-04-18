import slack
from slack_sdk import WebClient
import slack_bolt
from slack_bolt.async_app import AsyncApp
import server_main
from BOT_TOKEN import (SLACK_BOT_TOKEN,
                       SLACK_CLIENT_ID,
                       SLACK_SECRET)

import pyotp

count = 0

hotp =  pyotp.HOTP('base32secret3232')

# app = App(token="SLACK_BOT_TOKEN")
app = AsyncApp()

client = WebClient(SLACK_CLIENT_ID)



@app.command("/serverup")
async def serverup(ack, respond):
    await ack()
    # server_main.ServerControls.serverUp()
    await respond("server started")

@app.command("/servercreate")
async def servercreate(ack, respond):
    if hotp.verify():
        count += 1
        await ack()
        # server_main.ServerControls.serverCreate()
        await respond("new server created")
    else:
        await respond("authentication failed")

@app.command("/serverdelete")
async def serverdelete(ack, respond):
    if hotp.verify():
        count += 1
        await ack()
        # server_main.ServerControls.serverDel()
        await respond("server deleted")
    else:
        await respond("authentication failed")




