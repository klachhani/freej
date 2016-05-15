import requests
import itertools
import threading


def search_recipes(ingredients):
    maxSubset = min(3, len(ingredients))
    combs = list(itertools.combinations(ingredients, maxSubset))
    delim = '%2C'
    recipe_ids = []


    def worker(url):
        data = requests.get(url)
        if data.ok:
            data = data.json()
            recipes = data['Results']
            for r in recipes:
                recipe_ids.append(r['RecipeID'])


    threads = []
    for c in combs:
        query = ''
        for i in c:
            query += i + delim
        query = query[:-3]
        url = 'https://api2.bigoven.com/recipes?include_ing=' + query + '&api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W'
        t = threading.Thread(target=worker, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return recipe_ids


def get_recipe(recipe_id):
    url = 'https://api2.bigoven.com/recipe/' + str(recipe_id) + '?api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W'
    data = requests.get(url)
    recipe = {}
    if data.ok:
        data = data.json()
        recipe['id'] = recipe_id
        recipe['Title'] = data['Title']
        recipe['Category'] = data['Category']
        recipe['Subcategory'] = data['Subcategory']
        maxImageSq = str(data['MaxImageSquare'])
        recipe['ImageURL'] = data['ImageURL'] #+ '?h=' + maxImageSq + '&w=' + maxImageSq
        recipe['Description'] = data['Description']
        recipe['YieldNumber'] = data['YieldNumber']
        #recipe['Servings'] = data['Servings']
        recipe['Instructions'] = data['Instructions']


        ingandprep = []
        ingredients = data['Ingredients']
        for i in ingredients:
            name = i['Name']

            metric = str(i['MetricQuantity']) + ' | ' + i['MetricUnit']
            unit_i = i['Unit'] if i['Unit'] != None else ''
            imperial = str(i['Quantity']) + ' | ' + unit_i
            if i['Name'].lower() in ['salt', 'pepper']:
                metric = imperial
            prep = str(i['PreparationNotes']) if i['PreparationNotes'] != None else ''

            ingandprep.append(name.title() + ' | ' + metric + '; ' + prep.capitalize())

        recipe['Ingredients'] = ingandprep

    return recipe