from random import randint

def generate_random_population() -> list[dict]:
    random_population = []
    for i in range(20):
        random_subject = {"id": i, "gen": ""}
        for allel_index in range(10):
            random_subject["gen"] += str(randint(0,1))

        random_population.append(random_subject)

    return random_population
