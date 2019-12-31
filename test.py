from datetime import datetime

now = datetime.now()
print(now)
date = now.strftime('%d/%m/%Y %H:%M:%S')
print(date)