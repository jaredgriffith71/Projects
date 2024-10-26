This code works as a token scanner on the Solana blockhain.
Newly minted tokens are alerted to a telgram channel.
This code parses these messages for tokens where the creator's wallet holds a balance of 20-30% of the total supply.
If a token meets this criteria it sends an alert to the user's desired telegram channel.
To get alerts to your telegram channel, you will need to create a telegram bot with Botfather.

In order to run this program make sure the necessary files are installed from requirements.txt

Swap out the required information in eagle_eye:

apikey1/2/3/...
YOUR_API_ID
YOUR_API_HASH
YOUR_PHONE_NUMBER (including country code)
DESIRED_TELEGRAM_CHANNEL (for parsing newly minted tokens)

Swap out the required information in telegram_bot:
YOUR_API_TOKEN (for telegram bot)
YOUR_CHAT_ID (output chat channel)

Swap out the required information in last_message_id.txt:
This file should only contain the most recent token id (message id from telegram channel)
