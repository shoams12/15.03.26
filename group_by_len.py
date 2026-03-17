#Exercise 1 – Group words by length
#Write a function that groups words by number of letters
# ["apple","banana","kiwi","grape","melon","pear"]
#
# -> {
#     5: ["apple","grape","melon"],
#     6: ["banana"],
#     4: ["kiwi","pear"]
# }

def group_words_by_length(fruits: list) -> dict:
    new_fruits = {}
    f_len = 0
    for fruit in fruits:
        f_len = len(fruit)
        if f_len not in new_fruits.keys():
            new_fruits[f_len] = []
        new_fruits[f_len].append(fruit)
    return new_fruits


print(group_words_by_length(["apple","banana","kiwi","grape","melon","pear"]))


