import datetime

now = datetime.datetime.now()
print(now.strftime("%d.%m.%Y %H:%M:%S"))

date_today = now.strftime("%a %b %d 8:00:00 %Y")
date_today = datetime.datetime.strptime(date_today, "%a %b %d %H:%M:%S %Y")
date_today_f = date_today.strftime("%d.%m.%Y %H:%M:%S")


def expiration_date(number_of_hours):
    date_plus_hours = date_today + datetime.timedelta(hours=number_of_hours)
    return date_today_f, number_of_hours, date_plus_hours.strftime("%d.%m.%Y %H:%M:%S")


print(expiration_date(36))
print(expiration_date(72))
