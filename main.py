class GoldGym():
    """This is a Gold Gym class"""

    def __init__(self):
        print(("%")*124)
        print(('*')*50,"WELCOME TO GOLD GYM!!!",('*')*50)
        print(("%") * 124)
        self.member = {}
        self.regimen = {}

    def create_user(self,name,age,gender,number,email,bmi,duration):
        """This is a method to create members for Gym"""
        self.member[number] =  {}
        self.member[number]["Name"] = name
        self.member[number]["Age"] = age
        self.member[number]["Gender"] = gender
        self.member[number]["Email"] = email
        self.member[number]["BMI"] = bmi
        if duration in [1,3,6,12]:
            self.member[number]["Membership Duration"] = duration
        else:
            self.member[number]["Membership Duration"] = 1

    def view_allmembers(self):
        """This is a method to view all the members of Gold Gym"""
        print("\n")
        print(" {: ^7} {: ^20} {: ^10} {: ^10} {: ^15} {: ^30} {: ^10} {: ^10}".format("Sr.No", "Name", "Age", "Gender","Number", "Email", "BMI", "Duration"))
        print(("-") * 118)
        sr = 1
        for item in self.member:
            print(" {: ^7} {: ^20} {: ^10} {: ^10} {: ^15} {: ^30} {: ^10} {: ^10}".format(sr, self.member[item]["Name"],
                                                                                self.member[item]["Age"],
                                                                                self.member[item]["Gender"],
                                                                                item,
                                                                                self.member[item]["Email"],
                                                                                self.member[item]["BMI"],
                                                                                self.member[item]["Membership Duration"]))
            sr +=1

    def view_member(self):
        """This is a method to view a particular member of Gym"""
        vi = int(input("Enter the member's Contact number to view details:\n"))
        if vi in self.member:
            print(f"Name: {self.member[vi]['Name']}")
            print(f"Age: {self.member[vi]['Age']}")
            print(f"Gender: {self.member[vi]['Gender']}")
            print(f"Email: {self.member[vi]['Email']}")
            print(f"BMI: {self.member[vi]['BMI']}")
            print(f"Membership Duration: {self.member[vi]['Membership Duration']}")
        else:
            print("No Member Found!!! Try Again")




    def update_member(self):
        """This is a method to update the membership of gym members"""
        no = int(input("Enter the Member's contact number to update: \n"))
        if no in self.member:
            up = int(input("\nPress 0 ==> Revoke Membership"
                           "\nPress 1 ==> To update the duration to 1/3/6/12 Months: \n"))
            if up == 0:
                self.member[no]["Membership Duration"] = 0
                print("Successfully Revoked the Membership")
            elif up == 1:
                du = int(input("Enter the updated Membership Duration: \n"))
                if du in [1,3,6,12]:
                    self.member[no]["Membership Duration"] = du
                    print("Successfully Updated the membership")
                else:
                    print("Enter a valid Membership Duration")
            else:
                print("Invalid Input")




    def delete_member(self):
        """This is a method to delete a member from Gym members list """
        de = int(input("Enter the Member's contact number to delete: \n"))
        if de in self.member:
            self.member.pop(de)
            print("Successfully Deleted the Member")
        else:
            print("No Member Found!!!\n Try Again")



    def create_regimen(self,bmi):
        """This is a method to create Regimen for members using BMI"""
        self.regimen[bmi] = {}
        if bmi < 18.5:
            self.regimen[bmi]["Mon"] = "Chest"
            self.regimen[bmi]["Tue"] = "Biceps"
            self.regimen[bmi]["Wed"] = "Rest"
            self.regimen[bmi]["Thu"] = "Back"
            self.regimen[bmi]["Fri"] = "Triceps"
            self.regimen[bmi]["Sat"] = "Rest"
            self.regimen[bmi]["Sun"] = "Rest"
            print(f"Successfully Created Regimen for BMI {bmi}")

        elif (bmi >= 18.5) and (bmi < 25):
            self.regimen[bmi]["Mon"] = "Chest"
            self.regimen[bmi]["Tue"] = "Biceps"
            self.regimen[bmi]["Wed"] = "Cardio/Abs"
            self.regimen[bmi]["Thu"] = "Back"
            self.regimen[bmi]["Fri"] = "Triceps"
            self.regimen[bmi]["Sat"] = "Legs"
            self.regimen[bmi]["Sun"] = "Rest"
            print(f"Successfully Created Regimen for BMI {bmi}")

        elif (bmi >= 25) and (bmi < 30):
            self.regimen[bmi]["Mon"] = "Chest"
            self.regimen[bmi]["Tue"] = "Biceps"
            self.regimen[bmi]["Wed"] = "Abs/Cardio"
            self.regimen[bmi]["Thu"] = "Back"
            self.regimen[bmi]["Fri"] = "Triceps"
            self.regimen[bmi]["Sat"] = "Legs"
            self.regimen[bmi]["Sun"] = "Cardio"
            print(f"Successfully Created Regimen for BMI {bmi}")

        elif bmi >= 30:
            self.regimen[bmi]["Mon"] = "Chest"
            self.regimen[bmi]["Tue"] = "Biceps"
            self.regimen[bmi]["Wed"] = "Cardio"
            self.regimen[bmi]["Thu"] = "Back"
            self.regimen[bmi]["Fri"] = "Triceps"
            self.regimen[bmi]["Sat"] = "Cardio"
            self.regimen[bmi]["Sun"] = "Cardio"
            print(f"Successfully Created Regimen for BMI {bmi}")

    def view_regimen(self):
        """This is a method to view a Regimen of all the members"""
        for i in self.regimen:
            print("\n")
            print(f"""For BMI: {i} ==>""")
            print(f"""\tMonday: {self.regimen[i]["Mon"]}""")
            print(f"""\tTuesday: {self.regimen[i]["Tue"]}""")
            print(f"""\tWednesday: {self.regimen[i]["Wed"]}""")
            print(f"""\tThursday: {self.regimen[i]["Thu"]}""")
            print(f"""\tFriday: {self.regimen[i]["Fri"]}""")
            print(f"""\tSaturday: {self.regimen[i]["Sat"]}""")
            print(f"""\tSunday: {self.regimen[i]["Sun"]}""")

    def update_regimen(self):
        """This is a method to update the Regimen of Gym Members"""
        up = float(input("Enter the BMI of Regimen you want to Update:\n"))
        if up in self.regimen:
            print("Select a Day you want to update")
            print("\tPress 1 => Monday")
            print("\tPress 2 => Tuesday")
            print("\tPress 3 => Wednesday")
            print("\tPress 4 => Thursday")
            print("\tPress 5 => Friday")
            print("\tPress 6 => Saturday")
            print("\tPress 7 => Sunday")
            day = int(input("==> "))
            if day == 1:
                self.regimen[up]["Mon"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 2:
                self.regimen[up]["Tue"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 3:
                self.regimen[up]["Wed"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 4:
                self.regimen[up]["Thu"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 5:
                self.regimen[up]["Fri"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 6:
                self.regimen[up]["Sat"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            elif day == 7:
                self.regimen[up]["Sun"] = input("Enter your Workout or Rest: \n")
                print("Successfully Update the Regimen")
            else:
                print("Invalid Input!!! Try Again")



    def delete_regimen(self):
        """This is a method to delete a Regimen from the Regimen list of Members"""
        de = float(input("Enter the BMI for deletion of regimen:\n"))
        if de in self.regimen:
            self.regimen.pop(de)
            print("Successfully Deleted the Regimen")
        else:
            print("No BMI Found in list!!! Try Again")



    def user_profile(self,num):
        """This is a User method to view his/her profile"""
        print()
        print(f"Name: {self.member[num]['Name']}")
        print(f"Contact Number: {num}")
        print(f"Age: {self.member[num]['Age']}")
        print(f"Gender: {self.member[num]['Gender']}")
        print(f"Email: {self.member[num]['Email']}")
        print(f"BMI: {self.member[num]['BMI']}")
        print(f"Membership Duration: {self.member[num]['Membership Duration']}")

    def user_regimen(self,num):
        """This is a User method to view his/her Regimen """
        x = self.member[num]["BMI"]
        if x in self.regimen:
            print()
            print("Please follow the below Regimen to get Fit!!!")
            print(f"""\tMonday: {self.regimen[x]["Mon"]}""")
            print(f"""\tTuesday: {self.regimen[x]["Tue"]}""")
            print(f"""\tWednesday: {self.regimen[x]["Wed"]}""")
            print(f"""\tThursday: {self.regimen[x]["Thu"]}""")
            print(f"""\tFriday: {self.regimen[x]["Fri"]}""")
            print(f"""\tSaturday: {self.regimen[x]["Sat"]}""")
            print(f"""\tSunday: {self.regimen[x]["Sun"]}""")
        else:
            print("Ask Super User to create a Regimen for your BMI")


    def menu(self):
        """This is method which runs all the Methods/Functions according to Users Input"""
        print("\t\t\tPress 1 ==> Super User")
        print("\t\t\tPress 2 ==> User")
        print("\t\t\tPress 0 ==> Exit")
        ans = input("Enter here ==> ")
        if ans == '1':
            self.Super = True
        elif ans == '2':
            self.user = True
        elif ans == '0':
            self.Super = False
            self.user = False
            print("See ya!!!")
        else:
            print("Invalid Selection")
            self.menu()


        if self.Super:
            print("Welcome Super User!!!")
            a = True
            while a:
                try:
                    print("\n\t\t\t\t\t 1 => Create Member\n\t\t\t\t\t "
                          "2 => View List of All Members\n\t\t\t\t\t "
                          "3 => View Details of a Particular Member\n\t\t\t\t\t "
                          "4 => Delete Member\n\t\t\t\t\t "
                          "5 => Update Member\n\t\t\t\t\t "
                          "6 => Create Regimen\n\t\t\t\t\t "
                          "7 => View Regimen\n\t\t\t\t\t "
                          "8 => Update Regimen\n\t\t\t\t\t "
                          "9 => Delete Regimen\n\t\t\t\t\t "
                          "0 => Exit To Main Menu")
                    input1 = input("Press 1/2/3/4/5/6/7/8/9/0 accordingly: \n")
                    if input1 == "1":
                        name = input("Enter Name: \n")
                        age = int(input("Enter Age: \n"))
                        gender = input("Enter Gender: \n").upper()
                        number = int(input("Enter Number: \n"))
                        email = input("Enter Email: \n")
                        bmi = float(input("Enter BMI: \n"))
                        duration = int(input("Enter Membership Duration 1/3/6/12: \n"))
                        self.create_user(name,age,gender,number,email,bmi,duration)
                    elif input1 == "2":
                        self.view_allmembers()
                    elif input1 == "3":
                        self.view_member()
                    elif input1 == "4":
                        self.delete_member()
                    elif input1 == "5":
                        self.update_member()
                    elif input1 == "6":
                        num = int(input("Enter the Contact Number of Member you want to create regimen for: \n"))
                        bmi = self.member[num]["BMI"]
                        self.create_regimen(bmi)
                    elif input1 == "7":
                        self.view_regimen()
                    elif input1 == "8":
                        self.update_regimen()
                    elif input1 == "9":
                        self.delete_regimen()
                    elif input1 == "0":
                        self.Super = False
                        a = False
                        self.menu()
                    else:
                        print("Enter a Valid Input")

                except Exception as e:
                    print(e)


        elif self.user:
            print("Welcome User!!!")
            num = int(input("Enter your Contact Number: \n"))
            if num in self.member:
                print("Welcome Member")
                a = True
                while a:
                    try:
                        print("\n\t\t\t\t\t 1 => View Profile\n\t\t\t\t\t "
                              "2 => View Regimen\n\t\t\t\t\t "
                              "0 => Exit To Main Menu")
                        en = input("Press 1/2/0 accordingly: \n")
                        if en == "1":
                            self.user_profile(num)
                        elif en == "2":
                            self.user_regimen(num)
                        elif en == "0":
                            self.user = False
                            a = False
                            self.menu()

                    except Exception as e:
                        print(e)
            else:
                print("Ask Super User to Create your Membership first!!!")

        else:
            print("You don't dare to have cheat meal!!!!\n Stick to the Routine!!!")


c = GoldGym()
c.menu()






















