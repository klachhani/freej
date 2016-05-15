# https://api2.bigoven.com/recipe/406264?api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W

import requests

url="https://api2.bigoven.com/recipe/907360?api_key=jA6APRL318vmXZf4GxUn6059YRwvWZ6W"
data=requests.get(url)

seasoning = ['salt', 'pepper']


if data.ok:
    data=data.json()
    ingredients=data['Ingredients']
    for i in ingredients:
        name = i['Name']

        metric = str(i['MetricQuantity']) +  ' | ' + i['MetricUnit']
        unit_i = i['Unit'] if i['Unit'] != None else ''
        imperial = str(i['Quantity']) + ' | ' + unit_i
        if i['Name'].lower() in seasoning:
            metric = imperial
        prep = str(i['PreparationNotes']) if i['PreparationNotes'] != None else ''

        print name.title() + ' | ' + metric + '; ' + prep.capitalize()