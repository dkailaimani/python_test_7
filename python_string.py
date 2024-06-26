# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for 
# keywords such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.",
 "The performance of this product is excellent. Highly recommended!",
  "I had a bad experience with this product. It didn't meet my expectations.", 
  "Poor quality product. Wouldn't recommend it to anyone.",
   "The product was average. Nothing extraordinary about it." ]

def findReview():
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        newReview = review
        for j in keywords:
            if j in newReview:
                newReview = newReview.replace(j, j.upper())
        print(newReview)

findReview()

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tallyReview():
    positive = 0
    negative = 0

    for review in reviews:
        singleReview = review
        for j in positive_words:
            if j in singleReview:
                positive = positive + 1
        for k in negative_words:
            if k in singleReview:
                negative = negative + 1
    print(f"# of Positive Words: {positive}")
    print(f"# of Negative Words: {negative}")      
tallyReview()

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
#  Ensure that the summary does not cut off in the middle of a word.

def createSummary():
    newReviewL = []
    for review in reviews:
        for keyword in review.split():
            for key in keyword:
                if len(newReviewL) + len(keyword) < 30:
                    newReviewL.append(key)
                elif len(newReviewL) + len(keyword) == 30:
                    newReviewL.append("...")    
        break             
    print(newReviewL)
createSummary()

#  User Input Data Processor
# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. 
# The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number.
# If the password does not meet these criteria, print a message explaining the complexity requirements.

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

def checkName():
    firstName = input("Enter first name: ")
    while not len(firstName) >= 2:
        print("ERROR: First name must be at least 2 characters long!")
        firstName = input("Enter first name: ")
    
    lastName = input("Enter last name: ")
    while not len(lastName) >= 2:
        print("ERROR: Last name must be at least 2 characters long!")
        lastName = input("Enter last name: ")

    print(f"User's Full Name: {firstName}" + " " + f"{lastName}")   
checkName()

def passwordChecker():
    password = input("Enter password: ")

    if len(password) >= 8:
        for char in password:
            if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
                return "Password confirmed"
            else:
                return "ERROR: Password must contain at least one number, and an upper and lowercase letter"
    else:
        return "ERROR: Password must contain at least 8 characters"
print(passwordChecker())

def emailFormatter():
    email = input('Enter email address: ')
    email = email.upper()
    if len(email) >= 22:
        if "@CODINGTEMPLE.COM" in email:
            return "Email Approved"
    else:
        return "ERROR: Must add more characters before @ in email AND/OR the ending must contain @codingtemple.com"
print(emailFormatter())

# Interactive Help Desk Bot
# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands
#  (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", 
# "performance", "error", etc. Print out the category of the issue for the support team.

def commandParser():
    userCommand = input("How can I help you? ")

    if "help" in userCommand:
        print("Navigate to the FAQ page for assistance.")
    elif "issue" in userCommand:
        print("Here is the link to submit a ticket: https://ticket.helpdesk.com")
    elif "contact support" in userCommand:
        print("Here is the directory with a list of employees to help: https://directory.helpdesk.com")
    else:
        print("Please send an email for better communication: helpdesk@email.com")
commandParser()

def issueParser():
    userCommand = input("How can I help you? ")
    if "issue" in userCommand:
        userCommand = input("Do you need help with login, performance, or an error message? ")
        if "login" in userCommand:
            print("Have you tried resetting your password?")
        elif "performance" in userCommand:
            print("Close all applications that are NOT in use.")
        elif "error" in userCommand:
            print("Here is the link to submit a ticket: https://ticket.helpdesk.com")
        return userCommand
print(f"Issue Category: {issueParser()}")


