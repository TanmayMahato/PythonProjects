
'''

BY- TANMAY MAHATO .... ROLL NO -54
    DEBRAJ BOSE   ....ROLL NO -18
    PIYUSH RAJ SINGH DEO....ROLL NO -37

    CLASS - XII A1 .... 2021-22

FOR - SCHOOL PROJECT... PROJECT NAME- EMPLOYEE MANAGEMENT SYSTEM

TO - PADMA LAKSHMI MA'AM

'''





import csv


"""ARRANGED IN THREE STUCTURES - 1> SET OF SMALL FUNCTIONS 
                                 2> BIG FUNCTIONS 
                                 3> MAIN MENU / OPTION SELECTOR """


'''                                             #SMALL FUNCTIONS
                                            ----------------------                                                  '''


# TELLS US THAT THERE ARE 10 DIGITS IN THE PHONE NO OR NOT                                                      SM 1

def digicnt(phno) :
    count = 0
    while (phno > 0):
        count = count + 1
        phno = phno // 10

        if count == 10 :
            return 3



# CHECKS THE ID NO IN THE CSV FILE                                                                              SM 2

def IDcheck(x) :
    with open("empdetails.csv","r") as obj0 :
        dataw = csv.reader(obj0)
        for i in dataw :
            if i[0] == x :
                return 2



# HOLDS THE SALARY FOR DIFFERENT POSITIONS                                                                     SM 3

def salaryinfo(x):
    if x == "Junior Employee":
        sal = 35000
    elif x == "Senior Employee":
        sal = 50000
    elif x == "Supervisor":
        sal = 75000
    elif x == "Manager":
        sal = 125000
    elif x == "General Manager":
        sal = 175000
    else :
        return 0
    return  sal

'''                                                      # BIG FUNCTIONS 
                                                        ---------------------                                    '''


# ADDS THE EMPLOYEE DATA IN THE CSV FILE                                                                   FUNCTION NO 1


def employeeAdd() :
    with open("empdetails.csv","a") as obj1 :
        data = csv.writer(obj1)

        while True :
            while True :
                idno=(input("ID no.(Note- only integer type id is accepted)==> "))
                if IDcheck(idno) == 2:
                    print("This ID is already taken")
                else :
                    break
            name =input('Name ==>')
            gender = input('Gender ==> ')
            while True :
                phno = int(input("Phone No ==> "))
                if digicnt(phno) == 3 :
                    break
                print("Enter a valid 10 digit Phone no--")
            emid=input('Email id ==> ')
            add = input('Short Address ==>')

            record =[idno,name,gender,phno,emid,add]
            data.writerow (record)

            ch = int(input('{ 1-Enter More Data } \n{ 2-Exit }\nChose One( 1or2 ) ==> '))
            if ch == 2:
                break




# EDITS THE EMPLOYEE INFO


def moddata() :
   f=open("empdetails.csv","r")
   csvr =csv.reader(f)
   found = 0
   ml =[]
   idno = input("Enter ID no. to modify ==> ")
   for r in csvr :
       if r[0] == idno :
           print("Current Info==> Id-",r[0],", Name-",r[1],", Gender-",r[2],", Phone NO-",r[3],", Email ID-",r[4],", Address-",r[5])
           print(" Enter the new data below.\n")
           r[1] = input("Name ==> ")
           r[2] = input("Gender ==>")
           while True:
               r[3] = input("Phone No ==> ")
               X=int(r[3])
               if digicnt(X) == 3:
                   break
               print("Enter a valid 10 digit Phone no ..")
           r[4] = input("Emil id ==> ")
           r[5] = input("Short Address ==> ")

           found = 1
       ml.append(r)
   f.close()

   if found == 0 :
       print("Data not found")
   else :
       f=open("empdetails.csv","w",newline='')
       csvw=csv.writer(f)
       csvw.writerows(ml)
       print('File modified successfully')
       f.close()




#DELETES THE EMPLOYEE FROM THE CSV FILE                                                                    FUNCTION NO 2


def deldata():
    f = open("empdetails.csv", "r")
    csvr = csv.reader(f)
    found = 0
    ml = []
    idno = input("Enter the ID no.==>")
    for i in csvr:
        if (i[0] != idno):
            ml.append(i)
        else:
            found = 1
    if found == 0:
        print("Data not Found")
        f.close()
    else:
        f = open("empdetails.csv", "w", newline='')
        csvr = csv.writer(f)
        csvr.writerows(ml)
        print("Data got deleted")
        f.close()




# GIVES "JUNIOR EMPLOYEE" POSITION TO EVERY NEW ADDED EMPLOYEE                                             FUNCTION NO 3



def position() :

   i=open("emp-position-2.csv","w")
   csva=csv.writer(i)
   h=open("empdetails.csv","r")
   csve=csv.reader(h)
   k=open("emp-position-1.csv","w")
   csvi =csv.writer(k)

   for r in csve :
          ps = "Junior Employee"
          record=[r[0],r[1],r[3],ps]
          csva.writerow(record)
          csvi.writerow(record)

   print('Newly Added Employees Got The Position Of "Junior Employee" ')
   h.close()
   i.close()
   k.close()



# helps us not getting any error

def fake_position() :

   i=open("emp-position-2.csv","w")
   csva=csv.writer(i)
   h=open("empdetails.csv","r")
   csve=csv.reader(h)
   k=open("emp-position-1.csv","w")
   csvi =csv.writer(k)

   for r in csve :
          ps = "Junior Employee"
          record=[r[0],r[1],r[3],ps]
          csva.writerow(record)
          csvi.writerow(record)

   h.close()
   i.close()
   k.close()







# EDIT THE EMPLOYEE'S POSITION                                                                             FUNCTION NO 4





def highposition() :
   position()

   f=open("emp-position-1.csv","r")
   csvr =csv.reader(f)
   found = 0
   ml =[]
   idno = input("Enter ID no. to modify ==> ")
   for r in csvr :
       if (r[0] == idno ):

          i = input("\nSelect a number for giving corresponding position to the employee\n{1-Juior Employee,2-Senior Employee,3-Supervisor,4-Manager,5-General Manager\n ===> ")
          if int(i) == 1:
             i = "Junior Employee"
          elif int(i) == 2:
             i = "Senior Employee"

          elif int(i) == 3:
             i = "Supervisor"

          elif int(i) == 4:
             i = "Manager"

          elif int(i) == 5:
             i = "General Manager"

          r[3] = i
          print("\n\n{",r[1],"} Is Now The",i,"Of Our Company\n")
          found = 1
       ml.append(r)
   f.close()

   if found == 0 :
       print("Data not found")
   else :
       f=open("emp-position-1.csv","w",newline='')
       csvw=csv.writer(f)
       csvw.writerows(ml)
       print('File modified successfully')
       f.close()





# GIVES THE SALARY ACC TO THE POSITION                                                                     FUNCTION NO 5


def salary():

    hh=fake_position()
    a = open("empdetails.csv", "r")
    datasea = csv.reader(a)
    r = open("emp-position-1.csv", "r")
    datpos = csv.reader(r)

    id=input("Enter the employee id ==> ")


    for i in datpos :
         if i[0] == id :

             print("Salary of ",i[1],"is ",salaryinfo(i[3]))

         else :
             print("No Data Found")

    a.close()
    r.close()




#SEARCHES THE EMPLOYEE AND GIVE ALL INFO ABOUT THAT EMPLOYEE                                               FUNCTION NO 6


def searchID() :
   fwef=fake_position()
   a=open("empdetails.csv","r")
   datas=csv.reader(a)
   r = open("emp-position-1.csv", "r")
   datpos = csv.reader(r)

   x= int(input("Enter the Employee ID ==> "))

   for e in datas :
        if int(e[0]) == x :
            print("========"," Employee Details ","=========================================================")
            print("Name: " + e[1])
            print("ID no.: " + e[0])
            print("Gender: " + e[2])
            print("Phone no.: " + e[3])
            print("Email Id: " + e[4])
            print("Short Address: " + e[5])
            for i in datpos :
                if e[0] == i[0] :
                    print("Position in Company: " + i[3],'\n')

        else :
            print("No Data Found")

   a.close()
   r.close()




#GIVES ALL EMPLOYEES DETAILS                                                                               FUNCTION NO 7


def print_employee():
    sdsvf=fake_position()    #just for the support
    q=open("empdetails.csv","r")
    dataemp=csv.reader(q)
    r= open("emp-position-1.csv","r")
    datpos=csv.reader(r)

    for emp in dataemp:
        print("="*20)
        print("Name :" + emp[1])
        print("ID no.: " + emp[0])
        print("Gender: " + emp[2])
        print("Phone no.: " + emp[3])
        print("Email Id: " + emp[4])
        print("Short Address: " + emp[5])

    q.close()
    r.close()






"""                                             [    MAIN  MENU    ] 
                                                  ----------------                                               """


def main():

    while True:
        print('===================================================\n')
        print('      Welcome to the Employee Management System    -\n')
        print('===================================================\n')
        print('[1] Add an Employee: \n')
        print('[2] View All Employees: \n')
        print('[3] Search Employees by ID no.: \n')
        print('[4] Edit Employees information: \n')
        print("[5] Delete An Employee's Complete Information : \n")
        print("[6] Change Employee's Position in Company : \n")
        print("[7] Check The Salary")
        print('\n[8]  Exit ')
        user_option = input("\nPlease select an option ==> ")
        if user_option == "1":
            employeeAdd()
        elif user_option == "2":
            print("\n======================================================================================")
            print("                         EMPLOYEE  DETAILS                                            ")
            print("========================================================================================")

            print("\n")
            print_employee()
            print("\n"*1)
        elif user_option == "3":
            x=searchID()

        elif user_option == "4":
            moddata()

        elif user_option == "5":
            deldata()

        elif user_option == "6":
            highposition()

        elif user_option == "7":
            salary()
        elif user_option == "8" :
            break
        else:
            print("\nPlease select a valid option...")

        x=int(input("\n[1]-Back to main menu\n[2]-Exit ==> "))
        if x == 2 :
           break


#  MAIN CODING

x=0
while x==0 :

    x=int(input("\n[1]-GO TO MAIN MENU..[2]-EXIT \nCHOOSE ONE OPTION ==> "))
    if x== 1 :
        main()
    elif x==2 :
        break
    else :
        input("CHOOSE THE CORRECT OPTION")



