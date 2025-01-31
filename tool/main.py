import requests
import pyfiglet
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print("Webhook successfully deleted.")
        else:
            print("Error deleting webhook.")
    except requests.exceptions.RequestException:
        print("Error executing request.")
    input("Press Enter to continue...")
    clear_console()

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None

def send_message(webhook_url, message, count):
    payload = {"content": message}
    for _ in range(count):
        response = requests.post(webhook_url, json=payload)
        print(f"Sent! Response code: {response.status_code}")
    input("Press Enter to continue...")
    clear_console()

# ASCII art title
ascii_art = pyfiglet.figlet_format("x4fo", font="slant")
print(ascii_art)

webhook_url = input("Enter Discord webhook URL: ")

while True:
    print("Select an action:")
    print("1 - Get webhook information")
    print("2 - Spam webhook")
    print("3 - Delete webhook")
    print("4 - Exit")
    choice = input("Enter action number: ")
    
    clear_console()
    print(ascii_art)
    
    if choice == "1":
        webhook_data = get_webhook_info(webhook_url)
        if webhook_data:
            print("Webhook information:")
            print(f"Name: {webhook_data.get('name', 'Unknown')}")
            print(f"ID: {webhook_data.get('id', 'Unknown')}")
            print(f"Channel: {webhook_data.get('channel_id', 'Unknown')}")
            print(f"Guild: {webhook_data.get('guild_id', 'Unknown')}")
        else:
            print("Error: Failed to retrieve webhook information.")
        input("Press Enter to continue...")
        clear_console()
    elif choice == "2":
        message = input("Enter message to send: ")
        count = int(input("How many messages to send?: "))
        send_message(webhook_url, message, count)
    elif choice == "3":
        confirm = input("Press Enter to delete the webhook, or any other key to cancel: ")
        if confirm == "":
            delete_webhook(webhook_url)
        else:
            print("Deletion canceled.")
            input("Press Enter to continue...")
            clear_console()
    elif choice == "4":
        break
    else:
        print("Invalid input, please try again.")
        input("Press Enter to continue...")
        clear_console()

input("Press Enter to exit...")
