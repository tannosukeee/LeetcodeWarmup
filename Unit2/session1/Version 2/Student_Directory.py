def student_directory(student_names):
    result = {}
    for i in range(1, len(student_names) + 1):
        result[student_names[i - 1]] = i
    
    return result

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))