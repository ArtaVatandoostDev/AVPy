import requests

url = "https://api.tala.ir/json"
data = requests.get(url, timeout=10).json()
ounce = data["ounce"]["price"]
print(f"هر اونس طلا: {ounce} دلار")
