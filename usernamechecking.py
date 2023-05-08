import requests
username = input("Enter a username: ")
response = requests.get(f"https://www.instagram.com/{username}/")
if response.status_code == 404:
    print(f"Instagram: @{username} is available")
else:
    print(f"Instagram: @{username} is taken")
response = requests.get(f"https://twitter.com/{username}/")
if response.status_code == 404:
    print(f"Twitter: @{username} is available")
else:
    print(f"Twitter: @{username} is taken")
response = requests.get(f"https://github.com/{username}/")
if response.status_code == 404:
    print(f"GitHub: @{username} is available")
else:
    print(f"GitHub: @{username} is taken")
response = requests.get(f"https://www.google.com/search?q={username}")
if response.status_code == 200 and f"No results found for {username}" in response.text:
    print(f"Google: {username} is available")
else:
    print(f"Google: {username} is taken")
