def rabbit_hole(d, animal):
    first_animal = animal
    proceed = True
    while proceed:
        proceed = False
        try:
            animal = d[animal]
            if animal != first_animal:
                proceed = True
            else:
                return False
        except KeyError:
            return animal



d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rap", "rap":"rat"}
print(rabbit_hole(d, "rat"))
print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))

