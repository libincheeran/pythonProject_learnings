def gender_converter(gender: str) :
    gender = gender.upper()
    if gender == "M":
        return "Male"
    elif gender == "F":
        return "female"
    else:
        return "unknown"