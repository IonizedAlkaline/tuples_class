weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in weather:
    if i == 1:
        rainy = rainy + 1
    else:
        sunny = sunny + 1
answer = rainy - sunny
if answer < 0:
    print("it will be sunny")
elif answer > 0:
    print("it will be rainy")
else:
    print("it will be normal weather")
