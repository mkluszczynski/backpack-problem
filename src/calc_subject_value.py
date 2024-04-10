def calc_subject_value(subject: dict, items: list[dict], max_value: int):
    value = 0
    for index, allel in enumerate(str(subject["gen"])):
        if allel == "0":
            continue

        value += items[index]["value"]

    if value > max_value:
        value = 0

    return value
