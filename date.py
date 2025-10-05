from datetime import datetime , timedelta

start = datetime.now()
end = start + timedelta(days=30)
x = end - start 
print (start)
print (end)
print (x)