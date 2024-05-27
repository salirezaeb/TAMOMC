import numpy as np

lengths = [10, 5, 5, 10, 10,7,7,9,8,20]  
densities = [17, 32, 18, 35, 52,90,79,21,18,4]  

travel_time = float(input(">>. welcome to efficiency program .<< \n please Enter your travel time (minutes): "))


efficiencies = []
for i in range(len(lengths)):
    efficiency = lengths[i] / (travel_time * densities[i] / 60)  # تقسیم بر 60 برای تبدیل دقیقه به ساعت
    efficiencies.append(efficiency)


print("your Efficiencies:")
print(efficiencies)
input('\nplease enter to exit ...')