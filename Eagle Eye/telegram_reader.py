import os
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.functions.channels import GetFullChannelRequest

LAST_MESSAGE_ID_FILE = 'last_message_id.txt'

def read_telegram_messages(api_id, api_hash, phone_number, channel_name, last_message_id):
    with TelegramClient('anon', api_id, api_hash) as client:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone_number, input('Enter the code: '))
        
        entity = client.get_entity(channel_name)
        messages = client.iter_messages(entity, limit=100)
        new_last_message_id = last_message_id if last_message_id else 0
        
        for message in messages:
            if last_message_id and message.id <= last_message_id:
                continue
            
            token_address = extract_token_address_from_message(message.text)
            wallet_address = extract_wallet_address(message.text)
            
            if token_address and wallet_address:
                yield (message.id, token_address, wallet_address)
            
            new_last_message_id = max(new_last_message_id, message.id)
        
        if new_last_message_id > last_message_id:
            with open(LAST_MESSAGE_ID_FILE, 'w') as f:
                f.write(str(new_last_message_id))

def extract_token_address_from_message(message_text):
    import re
    match = re.search(r"https?://solscan\.io/token/([A-Za-z0-9]+)", message_text)
    return match.group(1) if match else None

def extract_wallet_address(message_text):
    import re
    match = re.search(r"Owner: \[([A-Za-z0-9]+)\]", message_text)
    return match.group(1) if match else None

def send_telegram_message(api_id, api_hash, phone_number, channel_name, message):
    with TelegramClient('anon', api_id, api_hash) as client:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone_number, input('Enter the code: '))
        
        entity = client.get_entity(channel_name)
        client(SendMessageRequest(entity, message))
