def print_pair(dictionary, target):
    for i in dictionary:
        if i == target:
            print("Key: " + i)
            print("Value: " + dictionary[i])
            return
    
    print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")