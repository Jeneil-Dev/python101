# print("hello world")

# learner = "Donald Duck: Python read top to botton. Stored in the piece od data calle learner is this message =)"
# print(learner)

# #  data type = integer
# ideal_num_of_pets = 2
# print("ideal_num_of_pets: ", ideal_num_of_pets)
# # my first comment =)  it will not show up in terminal. 
# # to make this coment use command forward slash -> cmd /

# # data tpye = float
# cost_of_banana = 10.99
# print("The cost of a banana is a float: ", cost_of_banana)

# # data type = boolean (true/false)
# #  is our pet vaccinated ? 
# vaccinated = True
# print(vaccinated)

# # printing data types
# print(type(learner))
# print(type(ideal_num_of_pets))
# print(type(cost_of_banana))
# print(type(vaccinated))

# its_a_num = 333
# is_this_a_num = "333"

# # more on type
# print(type(its_a_num))
# print(type(is_this_a_num))

# statement = "I want two dogs" #string

# puppy_name = "Vincent" #string

# age = "2" #string

# is_line_36_true = True #boolean

# zipcode = "10001" #string

# #  mathematics

# print(5+3)
# print(5*3)
# print(5-3)
# print(5/3)
# print(5%3)

# # division vs modulo (remainder)
# print(10/3)
# print(10%3)

# # power

# print(2**5)
# # print(1^3) we are unsure what this is actually doing

# #  find the area of a rectangle l*w
# # length = 3
# length = int(input("Enter a length "))
# width = 4

# area = length * width
# print("area is: ", area)

# price = 20

# tax = price * .08

# print("tax = ", tax)

# fav_color = input("Enter your fav color: ")
# print(fav_color)
# # f strings
# print(f"Your fav color is {fav_color}")

# #  testing multiple inpute 
# print("Per Scholas is Unlocking Potential and Changing the Face of Tech")
# print(10+90)
# print(300.5+0.5)
# print(12, 24, -2, sep=':')
# print('but', 'not', 'including', sep='**')
# print('but', 'not', 'including', sep='')
# print('but', 'not', 'including', sep=' ')

# # Get the user's name
# name = input("What is your user name?")
# print("Hello My name is ",name)
# # Get two numbers from the user
# mb= input("Enter your Mobile number:")
# print("Mobile number is ",mb)

# ph = input("Enter your Phone number:")
# print("Phone number is ", ph)


#                                   #
#                                   #
# PYTHON PRACTICE: CUSTOMER RECEIPT #
#                                   #
#                                   #
customerName = "Storm White"
itemPrice = 15.59
quantity = 2
totalCost = itemPrice * quantity
roundedCost = round(totalCost, 2)
print("Receipt")
print("----------------------")
print(f"NAME: {customerName}")
print(f"PRICE: {itemPrice}")
print(f"QUANTITY: {quantity}")
print(f"TOTAL: ${totalCost}")
print(f"TOTAL: ${roundedCost}")

# updating

customerName2 = input("Input customer's name? ")
itemPrice2 = int(input("What is the item price? "))
quantity2 = int(input("Enter quantity "))
totalCost2 = int(f"The total cost of the order is {itemPrice2 * quantity2}")
# roundedCost2 = round(totalCost2, 2)
print("Receipt 2")
print("----------------------")
print(f"NAME: {customerName2}")
print(f"PRICE: {itemPrice2}")
print(f"QUANTITY: {quantity2}")
print(f"TOTAL: ${totalCost2}")
# print(f"TOTAL: ${roundedCost2}")

print("creating this for an update")
print("practice")