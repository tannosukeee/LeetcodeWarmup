def convertTemp(celsius):
    ans = []
    ans.append(round(celsius + 273.15, 2))
    ans.append(round(celsius * 1.80 + 32, 2))
    return ans

temperatures = convertTemp(23.00)
print(temperatures)