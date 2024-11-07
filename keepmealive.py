import requests

def keep_alive():
    url = "https://growmate-rojj.onrender.com/"  # Replace with your app's URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Ping successful!")
        else:
            print(f"Ping failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    keep_alive()
