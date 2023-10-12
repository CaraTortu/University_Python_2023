time = int(input("Seconds: "))

hours = time // 3600
time -= hours * 3600

minutes = time // 60
time -= minutes * 60

print(f"{hours}hrs {minutes}mins {time}secs")
