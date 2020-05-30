def rabbit_hole(d, animal):
    visited_animals = [animal]
    proceed = True
    while proceed:
        if animal in d:
            animal = d[animal]
            if animal not in visited_animals:
                proceed = True
            else:
                proceed = False
            visited_animals.append(animal)
        else:
            proceed = False
    if animal not in d:
        return animal
    else:
        return False

d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rap", "rap":"rat"}
print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))
