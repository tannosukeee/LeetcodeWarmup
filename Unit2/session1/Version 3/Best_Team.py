def team_with_best_average_score(games):
    max = 0
    index = 0
    for i in range(len(games)):
        if games[i]["score"] > max:
            max = games[i]["score"]
            index = i

    return games[index]["team_name"]

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))