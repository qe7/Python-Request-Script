import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_user_input(prompt):
    return input(f"{prompt}: ")


def make_request(url, headers):
    try:
        with requests.get(url, headers=headers):
            pass  # You can process the response if needed
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = get_user_input("URL")
    amount = int(get_user_input("Amount of requests"))
    workers = int(get_user_input("Amount of workers (recommended = 8)"))
    throttle = float(get_user_input("Throttle time (seconds)"))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }

    counter = 0

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(amount):
            executor.submit(make_request, url, headers)
            counter += 1
            print(f"{counter}/{amount}")
            time.sleep(throttle)  # Throttle the rate of requests
