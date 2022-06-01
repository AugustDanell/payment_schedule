def whole_hour_mapping(pay):
    d = {}
    for i in range(60):
        d[i] = pay
    return d

def fill_hours(s,e,d, p):
    for i in range(s, e+1):
        d[i] = whole_hour_mapping(p)
    return

# In case you want to format the output somehow.
def format_pay(f):
    return f

def give_pay(sh, sm, eh, em, day, d):
    s = 0
    for i in range(sh, eh):
        for j in range(0, 60):
            s += ((d[day])[i])[j]

    for j in range(sm, em):
        s += ((d[day])[eh])[j]

    return format_pay(s/60)

if __name__ == '__main__':
    time_mapping = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {}
    }

    money_sum = 0
    total_h = 0
    total_m = 0
    fill_hours(0, 23, time_mapping[1], 100)

    day = ""
    while(not day == "abort"):
        day = input("Enter in a day in the format:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")
        day = day.lower()
        if (day == "abort"):
            break

        day_mapping = {"monday" : 1, "tuesday" : 2, "wednesday" : 3, "thursday" : 4, "friday" : 5, "saturday" : 6, "sunday" : 7}
        day_id = day_mapping[day]

        start_hour, start_min = list(map(int, input("Starting time in the format (HH:MM)").split(":")))
        end_hour, end_min = list(map(int, input("Ending time in format (HH:MM)").split(":")))

        money_sum += give_pay(start_hour, start_min, end_hour, end_min, day_id, time_mapping)
        total_h += (end_hour - start_hour)%24
        total_m += (end_min - start_min)%60

    print("You have worked %s hours and %s minutes and earned: %d sek" %(total_h, total_m, money_sum))
