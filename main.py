vowels = ['a', 'e', 'i', 'o', 'u']

string = "programming"

count = 0

for char in vowels:
      if char in string:
            count += 1

print(count)

string = "programming"
count = 0

# for char in string:
#       if char == "m":
#             count += 1
# print(f"m:{count}")

print()

for index, value, in enumerate(string, start=7):
      if value == "m":
            count += 1
            print(count)
          





from collections import Counter

string = "programming"

numbers = Counter(string)

for char, total in numbers.items():
      print(f" char: {char} total: {total}")



print()


counts = {}

for index, char in enumerate(string):
      counts[char] = counts.get(char, 0) + 1
      print(f"Index: {char} Number_of_occurrence: {counts[char]}")