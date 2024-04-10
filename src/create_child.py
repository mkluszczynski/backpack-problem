from random import randint


def create_child(parents: list) -> str:
    should_cross = randint(1, 10) > 2
    should_mutate = randint(1, 10) <= 2

    new_gens = ["", ""]
    if should_cross:
        gen_len = len(parents[0]["gen"])
        div = gen_len // randint(2, gen_len // 2)
        new_gens[0] += parents[0]["gen"][:div]
        new_gens[0] += parents[1]["gen"][div:]
        new_gens[1] += parents[1]["gen"][:div]
        new_gens[1] += parents[0]["gen"][div:]

    else:
        new_gens[0] = parents[0]["gen"]
        new_gens[1] = parents[1]["gen"]

    child = new_gens[randint(0,1)]

    if should_mutate:
        mutation_index = randint(0, int(len(child)) - 1)
        if child[mutation_index] == "0":
            list(child)[mutation_index] = "1"
            child = str(child)

        else:
            list(child)[mutation_index] = "0"
            child = str(child)

    return child
