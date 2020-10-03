"""Boilerplate code for prompts using bullet module"""

from bullet import Bullet, YesNo

STYLE = {
    "indent": 0,
    "margin": 2,
    "align": 5,
    "shift": 0,
    "bullet": "⊙",
    "pad_right": 5,
}

VALID_CITY_CHOICES = ["Chicago", "New York City", "Washington"]
VALID_MONTH_CHOICES = ["January", "February", "March", "April", "May", "June"]
VALID_DAY_CHOICES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
VALID_FILTER_CHOICES = ["Month", "Day", "Both", "None"]


def bullet_prompt(question, choices):
    return Bullet(question, choices, **STYLE)


def yes_no_prompt(question):
    return YesNo(question)


city_prompt = bullet_prompt("\nPlease choose a city: ", VALID_CITY_CHOICES)

filter_prompt = bullet_prompt(
    "\nWould you like to filter data by month, day, both or not at all? ",
    VALID_FILTER_CHOICES,
)

month_prompt = bullet_prompt("\nWhich month? ", VALID_MONTH_CHOICES)


day_prompt = bullet_prompt("\nWhich day? ", VALID_DAY_CHOICES)
