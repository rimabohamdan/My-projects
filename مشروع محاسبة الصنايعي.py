str_length = input ("Please type length : \n")
str_width = input ("Please type width : \n")
#convert type
length = float(str_length)
width = float(str_width)
#احسب مساحة الغرفة عن طريق ضرب الطول بالعرض 
area = length * width
str_area = str(area)
print ("The total area is :" + str_area)
#print ("The total area is :" + area)