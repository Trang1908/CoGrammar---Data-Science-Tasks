# Request the name of a user's favourite restaurant and store it in a variable called string_fav
string_fav = input("Please enter your favourite restaurant: ")
# Print out string_fav
print(string_fav)
print()

# Request user's favourite number. Use casting to store it in an integer variable called int_fav
int_fav = int(input("Please enter your favourite number: "))
# Print out int_fav
print(int_fav)
print()

# Cast string_fav to an integer
cast_string_fav = int(string_fav)
# There is an error when cast string_fav to an integer. ValueError: invalid literal for int()
# Because the string is a character without number, so cannot cast to integer type