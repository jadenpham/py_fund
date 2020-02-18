# print("Hello World")

# name = "bob"
# print("hello", name)
# print("hello " + name)

# name = 24
# print("hello", name)
# # print("hello " + 24)

# food1 = "pho"
# food2 = "shabu"
# print("I love {} and {}".format(food1, food2))
# print(f"I love {food1} n {food2}")

# def to150():
#     for i in range(151):
#         print(i)
# # to150()

# def multof5():
#     for i in range(0, 1001, 5):
#         print(i)
# # multof5()

# def countingdojo():
#     for i in range(101):
#         if(i%5 ==0 and i%10!=0):
#             print("coding", i)
#         elif(i%10==0):
#             print("dojo", i)
# # countingdojo()

# def huge():
#     sum = 0
#     for i in range(0, 500000):
#         if(i%2!=0):
#             sum+=i
#     print(sum)
# huge()

# def backwards():
#     for i in range(2018, 0, -4):
#         print(i)
# # backwards()

# def flex(low, high, mult):
#     lowNum = low
#     highNum = high
#     mult = mult
#     for i in range(lowNum, highNum, mult):
#         print(i)

# flex(2,9,3)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bal = 100
    def withdraw(self, amount):
        self.bal -= amount
        return(self.bal)
    def display_bal(self):
        return(self.bal)
    def transfer_money(self, amount, user):
        self.bal -= amount
        user.bal += amount
        print(user.name + " received" + str(amount) + " now has " + str(user.bal))

# bob = User("bob", "bob@cd.com")
# kevin = User("Kevin", "kevin@cd.com")
# print(bob.name + " " + bob.email)
# # print(bob.withdraw(75))
# # print(bob.display_bal)
# print(bob.display_bal())
# bob.transfer_money(50, kevin)

# class BankAcc:
#     def __init__(self, int_rate, bal):
#         self.rate = int_rate
#         self.bal = bal
#     def deposit(self, amount):
#         self.bal += amount
#         print(self.bal)
#         return self
#     def withdraw(self, amount):
#         self.bal -= amount
#         print(self.bal)
#         return self
#     def display_info():
#         print(f"{self.bal} has interest rate of {self.rate}")
#     def yield_int(self):
#         self.bal += self.bal * self.rate
#         print(self.bal)
#         return self
    
# chase = BankAcc(.02, 100)
# chase.deposit(1000)
# chase.yield_int()

import urllib.request
resp = urllib.request.urlopen("http://www.codingdojo.com")
html = resp.read()
print(html)