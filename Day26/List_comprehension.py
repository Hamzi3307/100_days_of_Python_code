numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print("Given List: ", numbers)

# EXERCISE: 26.1
# squared_numbers=[]
# for n in numbers:
#     sqr_num = n*n
#     squared_numbers.append(sqr_num)
# print(squared_numbers)


squared_numbers = [n*n for n in numbers]

print("squared_numbers: ", squared_numbers)

# EXERCISE: 26.2
# even_numbers=[]
# for n in numbers:
#     if n%2 == 0:
#         even_numbers.append(n)
# print(even_numbers)


even_numbers = [n for n in numbers if n%2==0]

print("even_numbers: ",even_numbers)

# EXERCISE: 26.3
# take two files with numbers and print matching number in a list named result
with open("Day26/file1.txt") as file:
    file1 = file.readlines()

with open("Day26/file2.txt") as file:
    file2 = file.readlines()

result = [int(n) for n in file1 if n in file2]
print("Matching in both txt: ",result)