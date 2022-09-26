from datetime import datetime, timedelta


data1 = datetime(2006, 8, 14).strftime('%d/%m/%Y')
data2 = datetime(2006, 8, 14).strftime('%d/%m/%Y')
print(data1 == data2)