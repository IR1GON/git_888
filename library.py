


def type_definitions(value):
    if '.' in value:
        return float(value)
    else:
        return int(value)

def cm_to_inches(santimeters):
    santimeters = float(santimeters)
    inches = santimeters / 2.54
    return str(inches)

def round_number(number, decimal_places=0):

    rounded = round(number, decimal_places)
    return int(rounded)