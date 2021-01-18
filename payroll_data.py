# Program 1 reads a text file and takes names and calculates total pay
"""
print() sets the format to display in output.
"""
print("\n %-10s %-10s %-10s %-10s" % ("NAME", "RATE", "HOURS", "TOTAL PAY"))

with open("payroll_data.txt", "r") as f:
    """
    with open() opens the text file as read and names it "f"
    """
    for line in f:
        #"iterates over each line in f and stores it in line"
        line = line.strip()
        #trailing white spaces are removed

        if line != "":
            # if line is not blank
            (name, rate, hours) = line.split()
            #split the line and capture each group

            rate = float(rate)
            hours = float(hours)
            #convert rate and hours from string to float. name is left unchanged since it is a string already.
            total_pay = rate * hours
            #calculates pay

        print("%-10s %-10.2f %-10.2f %-10.2f" % (name, rate, hours, total_pay))
        # Displays the output with the desired output and decimal point
