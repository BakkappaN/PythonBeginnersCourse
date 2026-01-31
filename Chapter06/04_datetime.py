# Import datetime module
from datetime import datetime, timedelta

print('Date time : ', datetime.now()) # current date & time
print('Date  : ', datetime.now().date()) # only current date
print('Time : ', datetime.now().time()) # only current time

now = datetime.now()
print('Year-Month-Date : ', now.strftime("%Y-%m-%d")) # formated date Year-Month-Date
print('Date-Month-Year :', now.strftime("%d-%m-%Y")) # formated date Date-Month-Year
print('Hour:Minutes:Seconds : ', now.strftime("%H:%M:%S")) # formated date Hour:Minutes:Seconds

print('Year/Month/Date : ', now.strftime("%Y/%m/%d")) # formated date Year/Month/Date
print('Date/Month/Year : ', now.strftime("%d/%m/%Y")) # formated date Date/Month/Year

today = datetime.now()
futureDate = today +timedelta(days=10)
print('Future date : ', futureDate) 

# Days difference between given dates 
date1 = datetime(2026,2,1)
date2 = datetime(2026,2,28)
diff = date2 - date1
print('Difference b/w given dates : ', diff.days)



