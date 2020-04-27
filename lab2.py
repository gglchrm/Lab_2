'''
Протарифицировать абонента с IP-адресом 217.15.20.194 
с коэффициентом k: 0,5руб/Мб
'''
import csv

user_ip = "217.15.20.194"
bytes_count = 0


data_file = open('data_net_csv.txt', 'r')
data = csv.DictReader(data_file, delimiter=',')
for line in data:
	if line.get('da') == user_ip:
		bytes_count += int(line.get('ibyt'))

print(bytes_count)
print("BILL", user_ip, ":", (bytes_count/2048)/1024, "рублей")
	



	