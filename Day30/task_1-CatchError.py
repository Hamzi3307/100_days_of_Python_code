fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(3)
make_pie(2)
# try:
#     make_pie(3)
#     make_pie([3])
# except IndexError as errormessage:
#     print(f"error {errormessage} occured but program continued")
# except TypeError as errormessage:
#     print(f"error {errormessage} occured but program continued")
# else:
#     print("Another error")
