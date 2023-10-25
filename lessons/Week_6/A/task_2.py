day_to_full_name = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}


def dayName(day: str) -> str:
    if day.lower() not in day_to_full_name:
        raise Exception("Days not in months")

    return day_to_full_name[day.lower()]


print(dayName("Mon"))
