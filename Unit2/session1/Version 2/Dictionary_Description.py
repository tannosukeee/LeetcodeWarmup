def get_description(info, keys):
    for key in keys:
        if key in info:
            print(info[key])
        else:
            print(None)
          
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)