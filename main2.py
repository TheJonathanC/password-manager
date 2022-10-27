import mysql.connector
import random

#connection to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tiger",
  database="passwordsmanager"
)
mycursor = mydb.cursor()

class adata():
  def menu():
    while True:
      print("Data Menu:")
      print("1. View data")
      print("2. Add data")
      print("3. Remove data")
      print("4. Exit")
      optada = int(input("Enter option: "))
      if optada == 1:
        adata.view()
      elif optada == 2:
        adata.new()
      elif optada == 3:
        adata.rem()
      elif optada == 4:
        print("Exiting data menu...")
        break
      else:
        print("ERROR!")

  def view():
    print("Enter your id: ")
    idi = input("> ")
    sql3 = "select id,account,username,password from data where id=%s"
    val3 = (idi,)
    mycursor.execute(sql3, val3)
    data3 = mycursor.fetchall()
    print(data3)
    print("\n")

  def new():
    print("Enter your id: ")
    idi = input("> ")
    print("Enter Account (eg. instagram): ")
    acn = input("> ")
    print("Enter Username: ")
    usrn = input("> ")
    print("Enter password: ")
    pasw = input("> ")
    sql4 = "insert into data (id,account,username,password) values (%s,%s,%s,%s)"
    val4 = (idi,acn,usrn,pasw)
    mycursor.execute(sql4, val4)
    mydb.commit()
    print("Data has been stored")
    print(idi,"|",acn,"-",usrn,"-",pasw)
    print("\n")

  def rem():
    print("Enter id:")
    idi = input("> ")
    print("Account to be deleted: ")
    acn = input("> ")
    sql5 = "delete from data where id=%s and account=%s"
    val5 = (idi,acn)
    mycursor.execute(sql5, val5)
    mydb.commit()
    print("Account deleted")


class dets():
  def menu():
    while True:
      print("Details Menu:")
      print("1. Check details")
      print("2. Enter new details")
      print("3. Exit menu")
      optdet = int(input("Enter option: "))
      if optdet == 1:
        dets.check()
      elif optdet == 2:
        dets.entry()
      elif optdet == 3:
        print("Exiting details menu...")
        break
      else:
        print("ERROR!")


  def check():
    print("\nREMEMBER YOUR ID!")
    print("Enter your name: ")
    nam = input("> ")
    var1 = nam.upper()
    sql1 = "select name,id from details where name=%s"
    val1 = (var1,)
    mycursor.execute(sql1, val1)
    data1 = mycursor.fetchall()
    print(data1)
    print("\n")

  def entry():
    print("\nREMEMBER YOUR ID!")
    print("Enter your name (make sure to remember this name because this can be used to refer your id later):")
    print("(also do not put any numbers orr special characters)")
    idr = random.randint(11111,99999)
    nam = input("> ")
    var2 = nam.upper()
    sql2 = "insert into details (id,name) values (%s,%s)"
    val2 = (idr,var2)
    mycursor.execute(sql2, val2)
    mydb.commit()
    print("Your deatails have been stored:")
    print(var2,"-",idr)
    print("\n")


while True:
  print("\nPASSWORD MANAGER")
  print("------------------------")
  print("Choose from the below options:")
  print("1. Details options")
  print("2. Data options")
  print("3. Exit")
  opt = int(input("Enter your option: "))
  if opt == 1:
    print("\n")
    dets.menu()
  elif opt == 2:
    print("\n")
    adata.menu()
  elif opt == 3:
    print("\n")
    print("Thank you!")
    break
  else:
    print("\n")
    print("Wrong input! try again.\n")