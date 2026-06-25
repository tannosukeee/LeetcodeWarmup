def average_book_ratings(book_ratings):
    sum = 0
    for key in book_ratings:
        for i in book_ratings[key]:
            sum += i
        n = sum / len(book_ratings[key])
        book_ratings[key] = n
        sum = 0
    return book_ratings

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}

print(average_book_ratings(book_ratings))