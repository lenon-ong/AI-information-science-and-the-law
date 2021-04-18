# The first for-loop prints the first column of each row containing
# "str(row) + "x"" for row in range(1,11), with 4 tab spaces.
for row in range(1,11):
    print(str(row) + "x", end="\t \t \t \t")
# The second for-loop prints a total of 10 columns of row*col for row and col in range(1,11), with 2 tab spaces.
# .rjust to ensure that the 2nd - 11th columns are justified rightwards
    for col in range(1,11):
        print((str(row*col)).rjust(10), end="\t")
    print()