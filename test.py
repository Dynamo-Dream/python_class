seconds = 4800
hour = int(seconds/3600)
remainder = seconds % 3600 # remainder
minutes = int(remainder/60)
seconds = remainder % 60
print("HOUR: ", hour)
#print(remainder)
print("MINUTES: ", minutes)
print("SECONDS:", seconds)
print(type(hour))