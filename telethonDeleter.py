import os
from telethon import TelegramClient

def _get_env(name):
    return os.environ.get(name.upper())

if not _get_env('api_id'):
    raise SystemExit('Environment variable `API_ID` is not set')

if not _get_env('api_hash'):
    raise SystemExit('Environment variable `API_HASH` is not set')

client = TelegramClient("rm-rf", _get_env('api_id'), _get_env('api_hash'))

async def main():
    me = await client.get_me()
    print(f'Logged in as {me.first_name} (id: {me.id})')

with client:
    client.loop.run_until_complete(main())
