# [PYTHON PROJECT] : Email Validation using String Functions

# Creating a variable in order to store the user input. 
email = input("Enter Your Email ID: ")
k , j , d = 0 , 0 , 0       # Assigning the initial values for string iteration as "Zero". 
if len(email) >= 6:         # Conditional "if" statement that checks the length of the email which must be greater than or equal to "Six" characters.
    if email[0].isalpha():  # Conditional "if" statement that checks the character at index[0] is an alphabet.
        if ("@" in email) and (email.count("@") == 1):      # Conditional "if" statement with "AND" operator that checks whether an "@" is present within the user entered email.
            if (email[-4] == ".") ^ (email[-3] == "."):     # Conditional "if" statement with "^" [XOR Operator] which has the same properties as "OR" Operator, but the only difference is "^" [XOR Operator] returns False incase both the conditions are true.
                for item in email:                  # The use of "for" loop is for the purpose of iterating through the characters of the user entered email.
                    if item == item.isspace():      # Conditional "if" statement that checks after the iteration is carried out, whether the user entered email has " " [Empty Spaces], incase it does the initial value of variable "k" is assigned as "1" [i.e. k = 1].
                        k = 1
                    elif item.isalpha():            # Conditional "elif" statement is used to re-iterate through the loop for further in-depth validation checks.
                        if item == item.upper():    # Conditional "if" statement that checks after the iteration is carried out, incase the user entered email contains any alphabets of upper casing, if it does the initial value of variable "j" is assigned as "1" [i.e. j = 1].
                            j = 1
                    elif item.isdigit():            # Conditional "elif" statement that checks whether the user entered email consists of a digit, incase it does the loop continues.
                        continue
                    elif item == "_" or item == "." or item == "@":    # Conditional "elif" statement that checks whether the user entered email consists of special characters [i.e. "_" ; "." and "@"], if this evaluates to be True the loop continues.
                        continue
                    else:       # Conditional "else" statement that gets executed incase any other special characters are present [i.e. ">" ; "<" ; "*" ; "#" etc.] within the user entered email, incase it does the initial value of variable "d" is assigned as "1" [i.e. d = 1].
                        d = 1
                if k == 1 or j == 1 or d == 1:      # Conditional "if" statement with "OR" operator that checks and returs a message "INVALID EMAIL" incase any of the variable [i.e. k , j , d] is assigned as 1
                    print("Invalid Email, an Email must not contain any empty spaces, uppercased alphabets or special characters other than \'_\'  \';\'  \'.\' or \'@)\'.")
            else:
                print("Invalid Email, an Email with invalid domain.")
        else:
            print("Invalid Email, an Email must contain atmost one \'@\'.")
    else:
        print("Invalid Email, an Email ID must must begin with an alphabet.")
else:
    print("Invalid Email, please enter a valid Email ID.")