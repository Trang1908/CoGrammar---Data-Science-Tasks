# Ask the user to enter a sentence using the input() method. Save the user's response in a variable called str_manip
str_manip = input("Please enter a sentence: ")
print()

# Calculate and display the length of str_manip
sentence_length = len(str_manip)
print(f"The length of your sentence is: {sentence_length}")
print()

# Find the last letter in str_manip sentence 
last_letter = str_manip[-1]
print("The last letter of your sentence is: {}".format(last_letter))
print()
# Replace every occurrence of this letter in str_manip with ‘@’
replaced_sentence = str_manip.replace(last_letter, "@")
print(replaced_sentence)
print()

# Print the last 3 characters in str_manip backwards
backwards_three_letter = str_manip[-1:-4:-1]
print(backwards_three_letter)
print()

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip
first_three_characters = str_manip[:3]
last_two_characters = str_manip[(sentence_length-2):]
print(first_three_characters + last_two_characters)

