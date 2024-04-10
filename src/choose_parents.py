from random import choices


def choose_parents(subjects: list[dict]):
    values = []

    for subject in subjects:
        values.append(subject["value"])

    parents = [subjects[0], subjects[0]]
    while(parents[0]["id"] == parents[1]["id"]):
       parents = choices(subjects, list(map(lambda subject: int(subject["value"]), subjects)), k=2)

    return parents
