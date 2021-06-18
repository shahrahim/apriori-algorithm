import random

# items = [
#     "diapers", "diapers", "diapers",
#     "candy-bar", "candy-bar",
#     "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk", "milk",
#     "cerial", "cerial", "cerial", "cerial", "cerial",
#     "chips", "chips", "chips",  "chips", "chips", "chips",
#     "soda", "soda"
#     "paper-towels", "paper-towels", "paper-towels", "paper-towels", "paper-towels", "paper-towels", "paper-towels", "paper-towels", "paper-towels",
#     "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper", "toilet-paper",
#     "tooth-brush", "tooth-brush",
#     "tooth-paste", "tee-shirt", "shorts", "jacket", "fish",
#     "ice-cream", "ice-cream", "ice-cream", "ice-cream", "ice-cream", "ice-cream", "ice-cream",
#     "bread", "bread", "bread", "bread", "bread", "bread",
#     "water", "water", "water", "water", "water", "water", "water", "water", "water", "water", "water", "water",
#     "apples", "apples",
#     "oranges", "oranges",
#     "camera", "tv", "laptop", "pillow", "pillow-sleeve",
#     "paper", "pencil", "pen", "notebook", "folder", "calculator"]

# for k in range(5):
#     filename = os.path.join(os.getcwd(), f"db_{k}.csv")
#     with open(filename, "a") as file:
#         file.write("TID, Items \n")
#         for i in range(20):
#             transaction = list(set(random.sample(items, random.randint(2,9))))
#             file.write(f"{i}, {','.join(transaction)}\n")
#         file.close()

test_items = [
    "1,3,4", "2,3,5", "1,2,3,5", "2,5", "1,3,5"
]
with open("apriori_test.csv", "a") as file:
    file.write("TID, Items \n")
    for i in range(len(test_items)):
        file.write(f"T{i+1},{test_items[i]}\n")
    file.close()


