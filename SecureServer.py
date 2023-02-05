#Testing qualifications to see if allowed into secure server. #Took Python last semester so!

#lists of all acceptable answers. Will and can be called!
level = ["High", "Medium", "Low"];
degree = ["Bachelors", "Masters", "Doctoral"];
positions = ["Partner", "Sr Manager", "Manager", "Deputy Manager", "Associate", "Analyst", "Assistant"];
todaysyear = 2023;

#Welcoming to the server. Have to answer some questions.
print("Welcome to this server. Answer some questions");

while True: #While True: all of these will contineously run until False or told to stop.

 #Age variable is receiving the input and using the input, subtracting variable todaysyear (2023) with age,
 #resulting in the persons age. Currentage is then used to tell the person their current age.
 #IF the personsage is more than or equal to 18, the loop continues on. Elif they're less, loop stops.
 age = input("What year were you born? ");
 personsage = todaysyear - int(age);
 currentage = personsage;
 print("You're", currentage);
 if personsage >= 18:
     print("Next question");
 elif personsage < 18:
     print("Sorry. Access Not Granted");
     break

 #Given the choices High, Medium, or Low, security clearance is told by variable clearance.
 #IF the input is 0 in the levels list, that means they are high clearance, which is allowed, and so the loop continues.
 #ELIF the input is EITHER 1 (Medium) OR 2 (LOW), loop stops. OR is if one condition comes true, experession is good. But
 #if the input is 1 or 2 from the level list, the loop stops as access isnt granted.
 print("\nHigh \nMedium \nLow")
 clearance = input("Current security clearence? ");
 if clearance == level[0]:
  print("Great! Next question!");
 elif clearance == level[1] or level[2]:
   print("Sorry. Access Not Granted");
   break

 #Choices and similair to above. If the input from the variable degreelevel IS 1 or 2 from the list degree,
 #THEN the loop continues on as thats a met requirement to continue. ELIF its 0 (Bachelors), loop stops.
 print("\nBachelors \nMasters \nDoctoral")
 degreelevel = input("Degree held? ");
 if degreelevel == degree[1] or degree [2]:
    print("Next question");
 elif degreelevel == degree[0]:
    print("Sorry. Access Not Granted");
    break

 #Receive input of years with variable security. IF security is equal to or greater than 5:
 #Then the loop continues BUT ELIF security is less than 5, loop stops. 5 is an integer so to
 #be read as a string, putting str is required. It'll read it as a string.
 security = input("Years of experience? ");
 if security >= str(5):
    print("Next question");
 elif security < str(5):
    print("Sorry. Access Not Granted");
    break

 #Given choices to put in as the input. IF input IS 1, 2, 3, 4, 5, or 6 of list positions, access is granted.
 #All requirements have been met at that point. ELIF its 0, or Partner, loop stops and access isn't granted.
 print("\nPartner \nSr Manager \nManager \nDeputy Manager \nAssociate \nAnalyst \nAssistant");
 positionlevel = input("Current position? ");
 if positionlevel == positions[1] or positions[2] or positions[3] or positions[4] or positions[5] or positions[6]:
     print("Access Granted!");
 elif positionlevel == positions[0]:
    print("Sorry. Access Not Granted");
    break

 #Stops the While loop. Would've continued without it. 
 break




