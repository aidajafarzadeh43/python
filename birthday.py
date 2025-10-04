def convert(day, month, year):
    if not (month < 10 or  (month == 10 and day <= 10)):
        birthday=year+622
    else:
        birthday=year+621
    print(f"your birthday year is {birthday}")
    
day=int(input('enter day:'))
month=int(input('enter month:'))
year = int(input('enter year:'))

convert(day, month, year)
   
# def convert(day, month, year):
#     if month > 10 or (month == 10 and day > 10):
#         birthday = year + 622
#     else:
#         birthday = year + 621
#     print(f"your birthday year is {birthday}")

# # گرفتن ورودی از کاربر
# day = int(input('enter day: '))
# month = int(input('enter month: '))
# year = int(input('enter year: '))

# # فراخوانی تابع با مقادیر عددی
# convert(day, month, year)
