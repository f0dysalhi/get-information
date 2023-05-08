import requests

ip_address = input("Enter an IP address: ")
api_key = "02310e2c56a9f1" 
url = f"https://ipinfo.io/{ip_address}?token={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("City:", data.get("city"))
    print("Region:", data.get("region"))
    print("Country:", data.get("country"))
    print("Location:", data.get("loc"))
    print("Timezone:", data.get("timezone"))
    print("Device Type:", data.get("device_type"))
    print("Network Name:", data.get("org"))
else:
    print("Error:", response.status_code)
