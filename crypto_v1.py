import requests

coin = input("Enter coin: ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

response = requests.get(url)
data = response.json()

if coin in data:
    print(f"{coin.capitalize()} Price: {data[coin]['usd']} USD")
else:
    print("Coin not found ❌")
