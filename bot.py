from pyrogram import Client, filters
import os

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

@app.on_chat_join_request(filters.chat(AUTH_GROUP))
async def accept_all_members(bot, update):
    try:
        await bot.approve_all_chat_join_requests(chat_id=AUTH_GROUP)
    except Exception as e:
        print(e)    

app.run()