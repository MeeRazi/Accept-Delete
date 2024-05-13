from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os, asyncio, logging

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")
AUTH_GROUP = os.getenv("AUTH_GROUP")

app = Client(
    "JoinAccepter",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

@app.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

# command to delete all messages
@app.on_message(filters.me & filters.command("clearchat", prefixes="."))
async def clearchat(_, message):
    chat_id = message.chat.id

    # send msg to show that bot is working
    await message.edit("Deleting all messages...")
    await asyncio.sleep(2)

    # get all messages
    async for msg in app.get_chat_history(chat_id):
        try:
            # delete message
            await app.delete_user_history(chat_id, msg.from_user.id)
        except FloodWait as e:
            # wait for a while
            print(e)
            await asyncio.sleep(e.x)
        except Exception as e:
            print(e)
            pass


app.run()
