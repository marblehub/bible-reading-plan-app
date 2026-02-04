import requests
from config.settings import API_KEY, BASE_URL


def chapters_to_biblia_format(chapters):
    if not chapters:
        return ""

    book = chapters[0].split()[0]
    chapter_nums = [int(ch.split()[1]) for ch in chapters]

    ranges = []
    start = prev = chapter_nums[0]

    for num in chapter_nums[1:]:
        if num == prev + 1:
            prev = num
        else:
            ranges.append(
                f"{book} {start}" if start == prev else f"{book} {start}-{prev}"
            )
            start = prev = num

    ranges.append(
        f"{book} {start}" if start == prev else f"{book} {start}-{prev}"
    )

    return ",".join(ranges)


def fetch_passage(chapters):
    passage_str = chapters_to_biblia_format(chapters)

    params = {
        "passage": passage_str,
        "style": "fullyFormattedWithFootnotes",
        "redLetter": "true",
        "fullText": "true",
        "citation": "true",
        "footnotes": "true",
        "key": API_KEY
    }

    try:
        r = requests.get(BASE_URL, params=params, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        return f"<h3>Error fetching passage</h3><p>{e}</p>"
