# https://www.geeksforgeeks.org/python-import-from-parent-directory/
import os, sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from generators.user.user_generator import UserGenerator
from generators.store.store_generator import StoreGenerator
from generators.item.item_generator import ItemGenerator

user_gen = UserGenerator()
store_gen = StoreGenerator()

user = user_gen.generate()
store = store_gen.generate()

print("User Information:")
print(user)
print("\nStore Information:")
print(store)

item_gen = ItemGenerator()

print("\nItem Information:")
coffee = item_gen.generate_coffee()
print(coffee)

juice = item_gen.generate_juice()
print(juice)

cake = item_gen.generate_cake()
print(cake)

item = item_gen.generate()
print(item)
