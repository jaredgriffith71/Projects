import requests

def fetch_wallet_balance(wallet_address, token_address, api_key):
    url = f"https://api.helius.xyz/v0/addresses/{wallet_address}/balances?api-key={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 429:
            raise requests.exceptions.RequestException("429 Too Many Requests")
        response.raise_for_status()
        data = response.json()

        for token in data.get('tokens', []):
            mint_address = token.get('mint')
            if mint_address == token_address:
                token_amount_str = token.get('amount', '0')
                token_decimals_str = token.get('decimals', '0')

                try:
                    token_amount = float(token_amount_str)
                    token_decimals = int(token_decimals_str)

                    token_balance = token_amount / (10 ** token_decimals)
                    return token_balance  # Return as a float

                except ValueError as e:
                    print(f"ValueError while processing amount or decimals: {e}")
                    return None
                except Exception as e:
                    print(f"Error calculating balance: {e}")
                    return None

        print(f"Token not found in response for address: {wallet_address}")
        return None

    except requests.RequestException as e:
        print(f"Request error: {e}")
        raise  # Re-raise to handle in the caller
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


        print(f"Token not found in response for address: {wallet_address}")
        return None

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
