# algoritmo de colonias

def transformar_hora(cadena):
    y=cadena.split(':')
    hora=int(y[0])
    min=int(y[1])/60
    hora_def=hora+min
    return hora_def
# transformar_hora("")
print("INFO ALGORITMO COLONIA DE HORMIGAS")
print("")
recorrido_ant=['Pasto', 'Bogota', 'Bucaramanga', 'Cúcuta', 'Valledupar', 'Soledad', 'Barranquilla', 'Cartagena', 'Montería', 'Medellín', 'Manizales', 'Pereira', 'Armenia', 'Tuluá', 'Palmira', 'Pasto']

num_km_ant=[837,429,197,541,296,16.4,119,258,405,211,53.6,46.1,87.2,72.4,401]
num_horas_ant=[transformar_hora("17:28"),transformar_hora("09:04"),transformar_hora("05:17"),
             transformar_hora("10:25"),transformar_hora("04:54"),transformar_hora("00:31"),
             transformar_hora("02:14"),transformar_hora("04:21"),transformar_hora("08:08"),
             transformar_hora("05:25"),transformar_hora("01:19"),transformar_hora("01:04"),
             transformar_hora("01:35"),transformar_hora("01:15"),transformar_hora("04:36")]

num_peajes_ant=[14,8,3,4,5,0,3,8,8,3,3,1,2,2,6]

num_valor_total_peajes_ant=[128000,60400,17300,33100,48700,0,24900,73500,80200,28300,35200,14500,20400,18400,46600]

total_km_ant=sum(num_km_ant)
total_horas_ant=sum(num_horas_ant)
total_peajes_ant=sum(num_peajes_ant)
total_valor_peajes_ant=sum(num_valor_total_peajes_ant)
print(f'el total de km en algoritmo de la colonia de hormigas es de : {total_km_ant} km')
print(f'el total de horas en todo el recorrido en el algoritmo de la colonia de hormigas es de: {total_horas_ant}')
print(f'el total de puestos de peajes en el algoritmo de la colonia de hormigas es de: {total_peajes_ant}')
print(f'el total valor en peajes en algoritmo de la colonia de hormigas es de : {total_valor_peajes_ant} pesos')

# algoritmo genetico
print("")
print("INFO ALGORITMO GENETICO")
print("")
recorrido_gen=['Palmira', 'Tuluá', 'Pereira', 'Montería', 'Barranquilla', 'Soledad', 'Cartagena', 'Valledupar', 'Medellín', 'Bucaramanga', 'Cúcuta', 'Bogota', 'Manizales', 'Armenia', 'Pasto', 'Palmira']

num_km_gen=[72.4,118,614,357,16.4,129,369,749,388,197,558,290,98.4,554,401]
num_horas_gen=[transformar_hora("01:15"),transformar_hora("02:02"),transformar_hora("12:38"),
             transformar_hora("06:13"),transformar_hora("00:31"),transformar_hora("02:21"),
             transformar_hora("06:19"),transformar_hora("12:56"),transformar_hora("07:46"),
             transformar_hora("05:17"),transformar_hora("12:13"),transformar_hora("07:18"),
             transformar_hora("02:14"),transformar_hora("10:55"),transformar_hora("04:36")]
num_peajes_gen=[2,2,13,7,0,3,6,11,8,3,7,4,9,9,6]

num_valor_total_peajes_gen=[18400,22100,131800,48500,0,24900,52400,103000,73600,17300,42700,40800,49700,76300,46600]

# print(len(num_km_gen))
# print(len(num_valor_total_peajes_gen))
total_km_gen=sum(num_km_gen)
total_horas_gen=sum(num_horas_gen)
total_peajes_gen=sum(num_peajes_gen)
total_valor_peajes_gen=sum(num_valor_total_peajes_gen)
print(f'el total de km en algoritmo genetico es de : {total_km_gen} km')
print(f'el total de horas en todo el recorrido en el algoritmo genetico es de: {total_horas_gen}')
print(f'el total de puestos de peajes en el algoritmo genetico es de: {total_peajes_gen}')
print(f'el total valor en peajes en algoritmo genetico es de : {total_valor_peajes_gen} pesos')