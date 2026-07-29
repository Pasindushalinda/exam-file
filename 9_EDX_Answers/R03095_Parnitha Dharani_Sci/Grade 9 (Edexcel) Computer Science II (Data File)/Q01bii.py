animals = ["cat", "dog", "cat", "cat", "dog",

           "cat", "dog", "cat", "dog", "cat",

           "dog", "cat", "cat"]


cat_count = 0

dog_count = 0
for animal in animals:

    if animal == "cat":

        cat_count = cat_count + 1

    if animal == "dog":

        dog_count = dog_count + 1

 
total = cat_count + dog_count
for animal in animals:

    if animal == "cat":

        cat_count = cat_count + 1

    if animal == "dog":

        dog_count = dog_count + 1

 

total = cat_count + dog_count
print("Cats:  " + cat_count + " animals")

print("Dogs:  " + int(dog_count )+ " animals")

print("Total: " + total + " animals")
