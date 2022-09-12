#for loop

from itertools import count


str = 'Looping'

# i is the place holder of the index
for i in str:
    print(i)

fevorites = ["Kaduna", "Kano", "Zamfara", "Katsina", ]

for i in range(len(fevorites)):
    print(fevorites[i])


for dessert in fevorites:
    print('One of my favorite desserts is', dessert)


# while loop

count = 0

while count < len(fevorites):
    print(fevorites[count])
    count += 1
