import os

API_KEY = os.getenv("BIBLIA_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "BIBLIA_API_KEY not set. Please export it as an environment variable."
    )

BASE_URL = "https://api.biblia.com/v1/bible/content/KJV.html"
READING_PLAN_FILE = "data/reading_plan.json"
PROGRESS_FILE = "data/progress.json"
