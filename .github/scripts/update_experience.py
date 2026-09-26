"""Update the years-of-experience value in README.md.

Counts full years since the start date and rewrites:
  - the text between <!--YEARS--> and <!--/YEARS--> markers
  - the "Experience" shields.io badge
Exits without changes if the value is already current.
"""
import re
from datetime import date
from pathlib import Path

START = date(2021, 11, 1)  # Started professional work: November 2021
README = Path(__file__).resolve().parents[2] / "README.md"


def full_years(start: date, today: date) -> int:
    years = today.year - start.year
    if (today.month, today.day) < (start.month, start.day):
        years -= 1
    return years


def main() -> None:
    years = full_years(START, date.today())
    text = README.read_text(encoding="utf-8")
    updated = re.sub(r"<!--YEARS-->\d+<!--/YEARS-->", f"<!--YEARS-->{years}<!--/YEARS-->", text)
    updated = re.sub(r"EXPERIENCE-\d+%2B%20YEARS", f"EXPERIENCE-{years}%2B%20YEARS", updated)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"README updated: {years}+ years")
    else:
        print(f"No change: already {years}+ years")


if __name__ == "__main__":
    main()
