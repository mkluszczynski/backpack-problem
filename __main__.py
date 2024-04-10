from random import choices, randint

from src.calc_subject_value import calc_subject_value
from src.generate_random_population import generate_random_population
from src.choose_parents import choose_parents
from src.create_child import create_child

items = [
    {"id": 1, "wight": 4, "value": 12},
    {"id": 2, "wight": 6, "value": 3},
    {"id": 3, "wight": 14, "value": 3},
    {"id": 4, "wight": 2, "value": 12},
    {"id": 5, "wight": 5, "value": 14},
    {"id": 6, "wight": 3, "value": 15},
    {"id": 7, "wight": 8, "value": 12},
    {"id": 8, "wight": 16, "value": 3},
    {"id": 9, "wight": 4, "value": 1},
    {"id": 10, "wight": 12, "value": 10},
]

max_value = 68


if __name__ == "__main__":

    subjects = generate_random_population()

    for population_id in range(20):

        for subject in subjects:
            subject["value"] = calc_subject_value(subject, items, max_value)

        new_gens = []
        for i in range(20):
            parents = choose_parents(subjects)
            child = create_child(parents)
            new_gens.append(child)

        new_population = []
        for id, new_gen in enumerate(new_gens):
            new_population.append({
                "id": id,
                "gen": new_gen
            })

        subjects = new_population


    for subject in subjects:
        subject["value"] = calc_subject_value(subject, items, max_value)
        print(f"{subject['id']}, {subject['gen']}, {subject['value']}")
