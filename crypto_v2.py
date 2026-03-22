import requests

coins = input("Enter coins (comma separated): ")
coin_list = coins.lower().split(",")

for coin in coin_list:
    coin = coin.strip()

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    if coin in data:
        print(f"{coin.capitalize()} Price, {data[coin]["usd"]} USD")
    else:
        print("Error in", coin)
