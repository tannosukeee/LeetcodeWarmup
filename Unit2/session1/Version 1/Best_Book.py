def highest_rated(books):
    max = 0
    index = 0

    for i in range(len(books)):
        if books[i]["rating"] > max:
            max = books[i]["rating"]
            index = i
        
    return books[index]

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))