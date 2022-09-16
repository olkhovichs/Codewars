def cakes(recipe, available):
    num_cakes = []
    shared_keys = set(recipe.keys()).intersection(set(available.keys()))
    curr = 0
    if recipe.keys() - available.keys() != set():
        return 0
    else:
        for key in shared_keys:
            num_cakes.append(available[key] // recipe[key])
        return min(num_cakes)