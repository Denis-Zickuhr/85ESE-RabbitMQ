import requests
import time
import random
import publish

def get_random_users(number_of_users):
    url = f"https://randomuser.me/api/?results={number_of_users}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Failed to fetch users")
        return []

def main(queue_name):
    min_users = 1
    max_users = 5
    min_interval = 10
    max_interval = 30

    try:
        while True:
            number_of_users = random.randint(min_users, max_users)
            users = get_random_users(number_of_users)

            print(f"retrieved {len(users)} users!")

            for user in users:
                publish.publish_channel(queue_name, user)

            print(f"published users to queue!")

            interval = random.randint(min_interval, max_interval)
            time.sleep(interval)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Stopping the script...")

if __name__ == "__main__":
    main('users-queue')