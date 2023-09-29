student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
e = []

#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    
import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.read_csv("Day26\phoenetic-alphabet-NATO\phonetic_alphabet_nato.csv")

dict_nato = {row.letter:row.code for (index, row) in nato_data_frame.iterrows() }
print(dict_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What you want to say about?")

list_user_input = [dict_nato[letter.upper()] for letter in list(user_input)]

print(list_user_input)