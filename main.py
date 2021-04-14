#show the message of Intro
print("Welcome to the Tip calculator");

#save the input total bill in variable totale
totale = float(input("what was the total bill $"));

#save the input percentage in variable percentage
percentage = float(input("what percentage tip would you like to give? 10, 12, or 15? "));

#save the input number of peaple in variable person
person=float(input("How many peaple to split the bill? "));

# calculat the result
resultat = round((totale/person) * (1+(percentage / 100)),2);

#show the result
print("Each person should pay : $" + str(resultat));

