OZ_TO_ML = 750 / 25.3605
OZ_TO_LBS = 6.5 / 100
OZ_TO_BOTTLES = 1 / 25.3605
OZ_TO_HANDLES = 1 / 59.17454

CORPSE_REVIVER = {
    'gin': (.75, OZ_TO_HANDLES, 'handles'),
    'cointreau': (.75, OZ_TO_ML, 'ml'),
    'lillet': (.75, OZ_TO_ML, 'ml'),
    'lemon': (.75, OZ_TO_ML, 'ml'),
    'orange_peel': (1, 1, 'peels'),
    'absinthe': (1, 1, 'dashes'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
PAPER_PLANE = {
    'rye': (.75, OZ_TO_ML, 'ml'),
    'aperol': (.75, OZ_TO_ML, 'ml'),
    'amaro': (.75, OZ_TO_ML, 'ml'),
    'lemon': (.75, OZ_TO_ML, 'ml'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
LAST_WORD = {
    'basil_vodka': (.75, OZ_TO_ML, 'ml'),
    'chartreuse': (.75, OZ_TO_ML, 'ml'),
    'maraschino': (.75, OZ_TO_ML, 'ml'),
    'lemon': (.75, OZ_TO_ML, 'ml'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}

ROSEMARY_GIMLET = {
    'gin': (2, OZ_TO_HANDLES, 'handles'),
    'rosemary_simple': (.5, OZ_TO_ML, 'ml'),
    'lime': (.5, OZ_TO_ML, 'ml'),
    'angostura': (2, 1, 'dashes'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
SPICY_MARGARITA = {
    'tequila': (1.5, OZ_TO_ML, 'ml'),
    'cointreau': (1, OZ_TO_ML, 'ml'),
    'lime': (.5, OZ_TO_ML, 'ml'),
    'jalapeno_slice': (1, 1, 'slices'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
AVIATION = {
    'gin': (2, OZ_TO_HANDLES, 'handles'),
    'creme_de_violette': (.5, OZ_TO_ML, 'ml'),
    'maraschino': (.5, OZ_TO_ML, 'ml'),
    'lemon': (.75, OZ_TO_ML, 'ml'),
    'cherry': (1, 1, 'cherries'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
NEGRONI = {
    'gin': (1, OZ_TO_HANDLES, 'handles'),
    'sweet_vermouth': (1, OZ_TO_ML, 'ml'),
    'campari': (1, OZ_TO_ML, 'ml'),
    'orange_peel': (1, 1, 'peels'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
ANGELS_LIPS = {
    'baileys': (1.5, OZ_TO_ML, 'ml'),
    'benedictine': (1.5, OZ_TO_ML, 'ml'),
    'ice': (3.5274 / 2, OZ_TO_LBS, 'lbs'),
}

DARK_AND_STORMY = {
    'dark_rum': (2, OZ_TO_ML, 'ml'),
    'ginger_beer': (3.5, OZ_TO_ML, 'ml'),
    'lime_wedge': (1, 1, 'wedges'),
    'ice': (3.5274, OZ_TO_LBS, 'lbs'),
}
PIMMS_CUP = {
    'pimms': (2, OZ_TO_ML, 'ml'),
    'lemon': (.75, OZ_TO_ML, 'ml'),
    'cucumber_simple': (.5, OZ_TO_ML, 'ml'),
    'ginger_ale': (3.5, OZ_TO_ML, 'ml'),
    'cucumber_slice': (1, 1, 'slices'),
    'ice': (3.5274 * 2, OZ_TO_LBS, 'lbs'),
}


ALL_DRINKS = [
    CORPSE_REVIVER,
    PAPER_PLANE,
    LAST_WORD,
    ROSEMARY_GIMLET,

    SPICY_MARGARITA,
    AVIATION,
    NEGRONI,
    ANGELS_LIPS,

    DARK_AND_STORMY,
    PIMMS_CUP
]


GUESTS = 80
NUM_DRINKS_PER_GUEST = 4
TOTAL_DRINKS = GUESTS * NUM_DRINKS_PER_GUEST


def main():
    unique_ingredients = set([])
    for drink in ALL_DRINKS:
        for ingredient in drink.keys():
            unique_ingredients.add(ingredient)

    for ingredient in unique_ingredients:
        total = 0
        for drink in ALL_DRINKS:
            drink_tuple = drink.get(ingredient, (0, 1, 'none'))
            if drink_tuple[0] > 0:
                amount_per_drink, conversion, units = drink_tuple
                num_this_drink = 1.0 / len(ALL_DRINKS) * TOTAL_DRINKS
                total += amount_per_drink * num_this_drink * conversion

        print 'Total amount of {} is {} {}'.format(ingredient, total, units)

if __name__ == '__main__':
    main()
