# Request from a participant the time (in minutes) for swimming event of the triathlon
swimming_time = int(input("Please enter the time (in minutes) for your swimming event of the triathlon: "))

# Request from a participant the time (in minutes) for cycling event of the triathlon
cycling_time = int(input("Please enter the time (in minutes) for your cycling event of the triathlon: "))

# Request from a participant the time (in minutes) for running event of the triathlon
running_time = int(input("Please enter the time (in minutes) for your running event of the triathlon: "))

# Calculate and display the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time
print("Your total time taken to complete the triathlon is: {} minutes.".format(total_time))

# The award a participant receives
if total_time >=0 and total_time <= 100:
    print("You will receive Provincial Colours Award.")
elif total_time >= 101 and total_time <= 105:
    print("You will receive Provincial Half Colours Award.")
elif total_time >= 106 and total_time <= 110:
    print("You will receive Provincial Scroll Award.")
else:
    print("You will not receive any Award.")