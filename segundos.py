segundos = input("Por favor entre com o número de segundos que deseja converter:")
total_segs = int(segundos)

dias = total_segs // 86400
sec = total_segs % 86400
horas = sec // 3600
sec2 = sec % 3600
minutos = sec2 // 60
sec3 = sec2 % 60

print(dias, "Dias, ", horas, " horas, ", minutos, " minutos e", sec3, "segundos.")
