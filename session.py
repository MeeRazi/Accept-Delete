from pyrogram import Client
from bot import API_KEY, API_HASH

print('Required pyrogram V2 or greater.')
with Client(name='USS', api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())