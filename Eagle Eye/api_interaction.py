import requests

def fetch_token_supply(mint_address, api_key):
    url = f"https://api.helius.dev/v1/tokens/supply/{mint_address}"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers)
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        data = response.json()
        return data.get('supply', None)
    else:
        print(f"Failed to fetch supply for {mint_address}: {response.text}")
        return None


def fetch_wallet_balance(wallet_address, mint_address, api_key):
    url = f"https://api.helius.dev/v1/accounts/{wallet_address}/tokens"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers)
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        data = response.json()
        for token in data.get('tokens', []):
            if token['mint'] == mint_address:
                return token['amount']
        print(f"Token {mint_address} not found in wallet {wallet_address}")
        return None
    else:
        print(f"Failed to fetch balance for {wallet_address}: {response.text}")
        return None
