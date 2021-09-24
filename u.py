import ujson


#open all JSON`s you need
firstJSON = []
with open('firstJSON.json') as f:
    firstJSON = ujson.load(f)

secondJSON = []
with open('secondJSON.json') as f:
    secondJSON = ujson.load(f)

thirdJSON = []
with open('thirdJSON.json') as f:
    thirdJSON = ujson.load(f)

fourthJSON = []
with open('fourthJSON.json') as f:
    fourthJSON = ujson.load(f)

#creating new dict to save there all JSON`s
dict = []
dict = firstJSON + secondJSON + thirdJSON + fourthJSON

#changing elements in sum of all  JSON`s
#in my tasks i changed 'pk' to import in SQLite 
for i, item in enumerate(dict):
    dict[i]['pk'] = i
    
    #saving new JSON in file u.json with package ujson - 
    #because its faster than simple json, also if you need better speen use orjson, but orjson doesn`t support dump() and load()
    #so you need to change your code
    
    with open('u' + '.json', 'w+') as json_file:
            ujson.dump(dict, json_file, indent=4, ensure_ascii=False,)

       



