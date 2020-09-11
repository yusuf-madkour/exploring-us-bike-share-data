"""Boilerplate code for prompts using bullet module"""

from bullet import Bullet, YesNo

STYLE = {"indent" : 0, "margin" : 2, "pad_right" : 5, "align" : 5, "shift" : 0, "bullet" : "⊙", "pad_right" : 5}

VALID_CITY_CHOICES = ["Chicago", "New York City", "Washington"]
VALID_MONTH_CHOICES = ["January", "February", "March", "April", "May", "June"]
VALID_DAY_CHOICES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
VALID_FILTER_CHOICES = ["Month", "Day", "Both", "None"]

city_prompt = Bullet(
        prompt = "\nPlease choose a city: ",
        choices = VALID_CITY_CHOICES,
        **STYLE
    )

filter_prompt = Bullet(
        prompt = "\nWould you like to filter data by month, day, both or not at all? ",
        choices = VALID_FILTER_CHOICES,
        **STYLE
    )

month_prompt = Bullet(
        prompt = "\nWhich month? ",
        choices = VALID_MONTH_CHOICES,
        **STYLE
    )


day_prompt = Bullet(
        prompt = "\nWhich day? ",
        choices = VALID_DAY_CHOICES,
        **STYLE
    )

def yes_no_prompt(question):
    return YesNo(question)
        
