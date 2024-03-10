seconds = int (input ("Enter the duration in seconds : \n"))
hours = seconds // 3600
#الدقائق اي باقي القسمة
minutes = ( seconds % 3600 ) // 60
#قسمت الثواني على 3600 طلعت الساعات 
#تجاهلت الرقم الصحيح شفت قدي ضل العدد الي لا يمكن ادماجه في الدقائق هو الثواني اي اقل من 60
remaining_seconds = seconds % 60
print (f"The duration is : {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
