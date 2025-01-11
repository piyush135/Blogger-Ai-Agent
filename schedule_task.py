import schedule
import time
from main import main

# Schedule the blog generation and posting task
schedule.every().day.at("10:00").do(main)

if __name__ == "__main__":
    print("Starting scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)
