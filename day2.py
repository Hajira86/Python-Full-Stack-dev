
######1.FOR LOOP#######
#for i in range(5): 
  #print("Hello")

#####2.WHILE LOOP######
#i=1
#while i<=5:
 #   print("Good morning") 
  #  i+=1

######3.DEF FUNCTION#######
#def add(a,b):
      # result=a+b
       #print(result)
#add (10,20)
#add (10,20)


#######4.LINKED LISTS#######
#students = ["hajira","lipika","poorvika","athiya"]
#students.append("gowri")
#students.remove("athiya")
#students.insert(1,"object")
#print(students)

##########5.TUPLES##############
#student_details=("hajira",20,90,True)
#print(student_details[2])

########6.DICTIONARY############
#student={"name":"hajira","age":20,"marks":95.1,"passed":"true" ,"usn":48,"dept":"CSE","semester":5}
#student["course"]="python programming"
#student["marks"]=90
#student["usn"]=48
#student["dept"]="CSE"
#student["semester"]= 5
#print(student["name"])
#print(student["usn"])
#print(student["marks"])
#print(student["semester"])
#print(student["dept"])
#print(student["course"])

##############7.CLASSS #############
#class Student:
    #def display(self):
        #print("HELLO EVERYONE")
       # print("WELCOME TO PYTHON")
#s1=Student()
#s1.display()

###########8.CONSTRUCTOR###########
#class student:
    #def __init__(self,name,age,marks):
        #self.name=name
        #self.age=age
        #self.marks=marks
   # def display(self):
      #  print("Name",self.name)
       # print("age",self.age)
      # print("marks",self.marks)
#s1=student("hajira",23,90)
#s2=student("athiya",19,88)
#s1.display()
#s2.display()

################9. ENCAPSULATION EXAMPLE: BANK ACCOUNT ################
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.__balance = balance   # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
#         else:
#             print("Insufficient balance or invalid amount")

#     def get_balance(self):
#         return self.__balance

#     def display(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: {self.__balance}")


# # Example usage
# acc1 = BankAccount("Hajira", 5000)
# acc1.display()
# acc1.deposit(1000)
# acc1.withdraw(2000)
# print("Current balance:", acc1.get_balance())

# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         print("STUDENT MARKS:", self.__marks)


# S1 = student()
# S1.set_marks(90)
# S1.get_marks()

##########INHERITENCE EXAMPLE##########
# class grandfather:
#     def land(self):
#         print("grandfather has land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")
# class son(father):
#         def car(self):
#             print("son has a car")
# s=son()
# s.land()
# s.house()
# s.car()

########## MULTIPLE INHERITANCE EXAMPLE##########
# class Father:
#     def show_father(self):
#         print("This is Father's method")
#
# class Mother:
#     def show_mother(self):
#         print("This is Mother's method")
#
# class Child(Father, Mother):
#     def show_child(self):
#         print("This is Child's method")
#
# c = Child()
# c.show_father()
# c.show_mother()
# c.show_child()

##########HIERARCHICAL INHERITANCE EXAMPLE##########
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Cat(Animal):
#     def meow(self):
#         print("Cat is meowing")
# dog = Dog()
# dog.eat()
# dog.bark()
# cat = Cat()
# cat.eat()
# cat.meow()

###########polymorphism example############
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     animal.sound()

# Dog=Dog()
# Cat=Cat()
# Dog.sound()
# Cat.sound()

##########Abstract class example###########
# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class UPI(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using UPI")
# class creditCard(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using credit card")
# p1=UPI()
# p2=creditCard()
# p1.pay(1000)
# p2.pay(2000)