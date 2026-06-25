def return_book(title, library):
    if title not in library:
        library[title] = 1
        return library

    for key in library:
        if key == title:
            library[key] += 1
            return library

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib) 