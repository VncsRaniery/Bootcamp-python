from datetime import datetime, timedelta

tipo_carro = 'p'
tempo_pequeno = 30
tempo_medio = 60
tempo_grande = 90
data_atual = datetime.today()

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print("O carro chegou: {data_atual} e sairá: {data_estimada")
elif tipo_carro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print("O carro chegou: {data_atual} e sairá: {data_estimada")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print("O carro chegou: {data_atual} e sairá: {data_estimada")