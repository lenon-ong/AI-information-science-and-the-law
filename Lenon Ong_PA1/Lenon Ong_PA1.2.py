import re # importing re for re.match

# empty lists are created to store user inputs
full_list = []
username_list = []
company_list = []
tld_list = []

x = True

while x: # The "While" loop to always enable input prompt until break
    email_address = input("What is your email address? ")
    if re.match(r"^[A-Za-z0-9.]+@+[A-Za-z0-9.]+.+[A-Za-z0-9.]$", email_address):
        # if user input matches the format of [^@]@[^@].TLD
        username_only = email_address.split('@')[:-1] # variable to store username list (everything before "@")
        domain_name = email_address.split('@')[1:] # variable to store domain_name list (everything after "@")
        tld_only = str(email_address.split('.')[-1]) # variable to store TLD only
        dot_tld = "." + tld_only # variable to store "." + str(TLD)
        company_name_only = str(domain_name[0]).replace(dot_tld, "") # variable to remove .TLD from domain name and make it a string
        full_list.append(email_address) # append to list containing all full email addresses
        username_list.append(username_only[0]) # append to list containing username only
        company_list.append(str(company_name_only)) # append to list containing company name only
        tld_list.append(tld_only) # append to list containing TLD only
    elif email_address == "Quit": # when user types "Quit"
        for i in range(0, len(username_list)):
            print(str(full_list[i]), str(username_list[i]), str(company_list[i]), str(tld_list[i]), sep = ", ")
            # printing the required output from lists
        break # break once user types "Quit".
    else:
        # break when input is not in the format of username@company.TLD
        print("invalid input")
        break