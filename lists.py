# simple list

cars = ['bmw', 'audi', 'tesla', 'benz', 'bugatti']
print(cars)

# Accessing Elements in a List

print(cars[2])
print(cars[1].title())
print(cars[-1].title())

# Using Individual Values from a List

message = f"my first car is {cars[2].title()}"
print(message)

# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[1] = 'tvs'
print(motorcycles)

# Adding Elements to a List

motorcycles.append('hero')
print(motorcycles)

# Inserting Elements into a List

motorcycles.insert(1, 'ducati')
print(motorcycles)

# Removing Elements from a List

del motorcycles[2]
print(motorcycles)

# Removing an Item Using the pop() Method

motorcycles_pop = motorcycles.pop()
print(motorcycles)
print(motorcycles_pop)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"last owned motorcycle is {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"first owned motorcycle is {first_owned.title()}.")

# Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

# print reason for removing from list

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive} is too expensive for me")

# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function

print(f"sorted list {sorted(cars)}")
print(f"original list {cars}")

# Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))
