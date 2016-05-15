import requests
import itertools


def search_recipes(ingredients):
    combs_final = []
    maxSubset = min(3, len(ingredients))
    combs = list(itertools.combinations(ingredients, maxSubset))

    #for c in combs:

    #    url = 'https://api2.bigoven.com/recipes?include_ing=pasta%2C%20tomatoes%2C%20apples%2C%20vinegar%2C%20asparagus%2C%20augbergine&api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W%''
    return combs


def get_recipe(recipe_id):
    url = 'https://api2.bigoven.com/recipe/' + recipe_id + '?api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W'
    data = requests.get(url)
    recipe = {}
    if data.ok:
        data = data.json()
        recipe['Title'] = data['Title']
        recipe['Category'] = data['Category']
        recipe['Subcategory'] = data['Subcategory']
        maxImageSq = str(data['MaxImageSquare'])
        recipe['ImageURL'] = data['ImageURL'] + '?h=' + maxImageSq + '&w=' + maxImageSq
        recipe['Description'] = data['Description']



    return recipe


c = search_recipes(['pears', 'tomato', 'pasta', 'cheese', 'milk'])
for i in c[0]:
    print i