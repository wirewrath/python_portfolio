"""SET total to 0

FOR each price in list of prices

  ADD price to total

IF total is greater than 100

  PRINT "You get free shipping!"

PRINT "Total is " and total"""
total = 0 #set total to 0
prices = [] #create a list of prices since we are calling for one

for price in prices: #for each price in list of prices
    total = price + total #add price to total
if total > 100: #if total is greater than 100
    print("You get free shipping!") #print you get free shipping
print("Total is", total) #print "Toal is" and total

# ASK user for their age
age_input = input("Enter your age: ")
age = int(age_input)

# IF age is at least 18
if age >= 18:
    # PRINT "You are an adult"
    print("You are an adult")
# ELSE
else:
    # PRINT "You are a minor"
    print("You are a minor")