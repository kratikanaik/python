## hiring people for different companies

skillset=str(input("Tell us ur skill: "))
project=int(input("Enter the number of projects u have completed:"))
if skillset=="python" or skillset=="c" and project>=2:
    print("You are placed in 'EVERY INDIA'")
elif skillset=="java" or skillset=="python" and project>=3:
    print("You are placed in 'TATA CONSULTANCIES'")
elif skillset=="c" or skillset=="java" and project>=4:
    print("You are placed in 'INFOSYS'")
elif skillset=="c++" or skillset=="c" and project>=5:
    print("You are placed in 'EVERY INDIA'")
else:
    print("Sorry ur not placed")
