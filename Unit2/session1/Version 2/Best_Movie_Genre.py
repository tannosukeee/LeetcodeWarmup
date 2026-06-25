def most_popular_genre(movies):
    max = 0
    index = 0

    for i in range(len(movies)):
        if movies[i]["rating"] > max:
            max = movies[i]["rating"]
            index = i
    
    return movies[index]["genre"]

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))