def water_state(temp):
    if temp == 0:
        return 'Solid'
    elif 0 < temp < 100:
        return 'Liquid'
    elif temp >= 100:
        return 'Gas'
