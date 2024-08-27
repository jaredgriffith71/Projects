import os
import asyncio  # Import asyncio module
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import re

LAST_MESSAGE_ID_FILE = 'last_message_id.txt'

async def read_telegram_messages(api_id, api_hash, phone_number, channel_name, last_message_id):
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.start(phone_number)
        entity = await client.get_entity(channel_name)

        # Fetch messages in correct order from oldest to newest to sync the last message ID
        if last_message_id is None:
            messages = client.iter_messages(entity, limit=1, reverse=True)
            async for message in messages:
                last_message_id = message.id
                break

        while True:
            # Continuously fetch new messages
            messages = client.iter_messages(entity, min_id=last_message_id, reverse=True)
            async for message in messages:
                if message.id <= last_message_id:
                    continue

                token_address = extract_token_address_from_message(message.text)
                wallet_address = extract_wallet_address(message.text)
                token_supply = extract_token_supply_from_message(message.text)
                token_name = extract_token_name_from_message(message.text)

                if token_address and wallet_address and token_supply and token_name:
                    yield (message.id, token_address, wallet_address, token_supply, token_name)

                last_message_id = message.id
                with open(LAST_MESSAGE_ID_FILE, 'w') as f:
                    f.write(str(last_message_id))

            print("Waiting for new messages...")
            await asyncio.sleep(3)

def extract_token_address_from_message(message_text):
    match = re.search(r"https?://solscan\.io/token/([A-Za-z0-9]+)", message_text)
    return match.group(1) if match else None

def extract_wallet_address(message_text):
    match = re.search(r"Owner: \[([A-Za-z0-9]+)\]", message_text)
    return match.group(1) if match else None

def extract_token_supply_from_message(message_text):
    match = re.search(r"Supply:\s*([0-9,]+)", message_text)
    if match:
        return int(match.group(1).replace(',', ''))
    return None

def extract_token_name_from_message(message_text):
    match = re.search(r"^(.*?)(\n)", message_text)
    return match.group(1).strip() if match else "Unknown Token"

async def send_telegram_message(api_id, api_hash, phone_number, channel_name, message):
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.start(phone_number)
        entity = await client.get_entity(channel_name)
        await client(SendMessageRequest(entity, message))
