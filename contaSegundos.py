segs = input("Por favor, entre com o número de segundos que deseja converter: ")
total = int(segs)

dias = total // 86400
seg_rest = total % 86400
horas = seg_rest // 3600
seg_restantes = seg_rest % 3600
minutos = seg_restantes // 60
segundos = seg_restantes % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
