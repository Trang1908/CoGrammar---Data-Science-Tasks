# Save the sentence as a single string and print it out
new_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(new_sentence)
print()

# Replace "!" with a blank space and reprint the sentence
replaced_sentence = new_sentence.replace("!", " ")
print(replaced_sentence)
print()

# Use the upper() function to reprint the sentence
upper_sentence = replaced_sentence.upper()
print(upper_sentence)
print()

# Print the sentence in reverse
reversed_sentence = upper_sentence[::-1]
print(reversed_sentence)