total_minutes = input (" Please type the numer of minutes :\n")
#convert type
int_minutes = int (total_minutes)
#متغير يمثل عدد الساعات
hours = int_minutes // 60
#متغير يمثل عدد الدقائق
minutes = int_minutes % 60
print(" The course is :"  + str(hours)+ "hours and"+ str(minutes)+ "minutes long"        )