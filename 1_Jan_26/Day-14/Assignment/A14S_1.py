FREZZING_POINT = 0
BOILING_POINT = 100

def water_state(temp):
    if temp == FREZZING_POINT:
        return 'Solid'
    elif FREZZING_POINT < temp < BOILING_POINT:
        return 'Liquid'
    elif temp >= BOILING_POINT:
        return 'Gas'
