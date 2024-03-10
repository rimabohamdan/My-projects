str_length = input (" Please type length : \n")
str_width = input ("Please typy width : \n")
str_price = input ("How mach for 1 meter ? : \n")
#convert type
length = float (str_length)
width = float (str_width)
price = float (str_price)
area = length*width
total_price = price*area
str_area = str (area)
str_total_price = str (total_price)
print ("The total area is : " + str_area)
print ("Give the guy : $" + str_total_price)
