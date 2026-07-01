def can_place_flowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if i == 0:
                if flowerbed[i + 1] == 0:
                    count += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    count += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
    if n <= count:
        return True
    else:
        return False

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)
print(approved2)