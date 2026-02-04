import json
import os
from config.settings import PROGRESS_FILE

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return 0

    with open(PROGRESS_FILE, "r") as f:
        data = json.load(f)
        return data.get("last_day_completed", 0)


def save_progress(day):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"last_day_completed": day}, f, indent=2)
