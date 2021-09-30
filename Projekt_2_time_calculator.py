def add_time(start, add, days=""):
    lista = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    x = start.split(" ")
    y = add.split(":")
    hour_minutes = x[0].split(":")
    h = int(hour_minutes[0])
    m = int(hour_minutes[1])
    day_part = x[1]
    h_1 = int(y[0])
    m_1 = int(y[1])
    hour = h + h_1
    minute = m + m_1

    if minute >= 60:
        add_h = str(minute / 60).split(".")
        hour += int(add_h[0])
        minute -= (int(add_h[0]) * 60)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    divider = hour / 12
    if hour % 12 == 0:
        final_hour = "12"
    else:
        divider_part = str(divider).split(".")
        final_hour = hour - (int(divider_part[0]) * 12)
    a = ""
    day_final = ""
    dodani_sati = hour
    while True:
        if dodani_sati < 12:
            break
        if dodani_sati == 12:
            if day_part == "PM":
                day_part = "AM" + " (next day)"
                break
            if day_part == "AM":
                day_part = "PM"
                break
        if dodani_sati > 12:
            count = dodani_sati / 12
            counter = str(count).split(".")
            for_days = str(dodani_sati / 24).split(".")

            if int(for_days[1]) >= 5:
                day_add = 1
                day_final += str(int(for_days[0]) + day_add)
            elif int(for_days[1]) < 5:
                day_final = int(for_days[0])

            if day_part == "AM":
                if int(day_final) == 1:
                    a = ""
                elif int(day_final) == 2:
                    a += " (next day)"
                else:
                    a += " (" + str(day_final) + " days later)"
            elif day_part == "PM":
                if int(day_final) == 1:
                    a += " (next day)"
                else:
                    a += " (" + str(day_final) + " days later)"
            if int(counter[0]) % 2 != 0:
                if day_part == "AM":
                    day_part = "PM"
                    break
                if day_part == "PM":
                    day_part = "AM"
                    break
            else:
                break

    d = days.lower()
    day_guess = ""
    for x in lista:
        if x == d:
            current_day = x
            br_u_listi = lista.index(current_day)
            while True:
                if day_part == "AM" or day_part == "PM":
                    day_guess = ", " + current_day[0].upper() + current_day[1:]
                    break
                if a == " (next day)" or day_part == "AM (next day)":
                    odmak = 1
                else:
                    odmak = day_final

                get_day = br_u_listi + int(odmak)
                if get_day < 7:
                    day_predict = lista[int(get_day)]
                    day_guess = ", " + day_predict[0].upper() + day_predict[1:]
                    break
                else:
                    x = get_day % 7
                    day_predict = lista[int(x)]

                    day_guess = ", " + day_predict[0].upper() + day_predict[1:]
                    break

    if len(days) > 0:
        return str(final_hour) + ":" + str(minute) + " " + day_part + day_guess + a
    if len(a) < 1:
        return str(final_hour) + ":" + str(minute) + " " + day_part + day_guess     # 12:04 PM, Wednesday
    if len(days) < 1:
        return str(final_hour) + ":" + str(minute) + " " + day_part + a     # 12:04 PM (9 days later)
    else:
        return str(final_hour) + ":" + str(minute)      # 12:04 PM


print(add_time("11:00 AM", "13:00", "Monday"))
