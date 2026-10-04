from datetime import datetime
appointments=[]
name=input("enter your name:")
age=int(input("enter your age:"))
print("enter your gender in (male),(female),(others)")
gen=input("enter your gender:").strip().lower()
print("1.Dr.Purna--2.Dr.kalyan--3.Dr.gahi")
doc=input("select your doctor :").strip().lower()
print("enter the date of appointment in the format of (DD-MM-YYYY)")
date=datetime.strptime(input("enter the date of appointment:"),"%d-%m-%Y").date()
print("enter the time of the appointment in the format of (HH:MM) and mention AM/PM:")
timea=input("enter the time of the appointment(HH:MM AM/PM):")
timea=datetime.strptime(timea.upper(),"%I:%M %p")
country=input("enter the country code:")
mn=input("enter your mobile number:")
print("the reason can be a single word!")
reason=input("enter the reason for the appointment:")
appointments.append((name,age,gen,doc,date,timea,country,mn,reason))
print(appointments)






