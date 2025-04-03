# from app.database import initialize_db
# from app.search_stream import search_and_process

# # Step 1: Initialize DB
# initialize_db()

# # Step 2: Pull recent tweets and flag them
# search_and_process()

import schedule
import time
from datetime import datetime
from app.database import initialize_db
from app.search_stream import search_and_process

# Step 1: Initialize DB once
initialize_db()

# Step 2: Define wrapper function with log
def run_job():
    print(f"⏰ Running tweet scan at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    search_and_process()

# Step 3: Schedule every 5 minutes
schedule.every(5).minutes.do(run_job)

print("🚀 Tweet monitoring started... (scanning every 5 minutes)")
run_job()  # Run immediately at start

# Step 4: Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(60)
