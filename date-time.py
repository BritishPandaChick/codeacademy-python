from datetime import datetime 
now = datetime.now() 

print '%02d/%02d/%04d %02d:/%02d:%02d' % 
(now.month, now.day, now.year, now.hour, now.minute, now.hour)

print now.hour 
print now.minute 
print now.second