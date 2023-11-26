import json
import matplotlib.pyplot as plt
from kafka import KafkaConsumer

# Configura el consumidor de Kafka
consumer = KafkaConsumer('test', bootstrap_servers='localhost:9092', api_version=(0,11,5))

# Listas para almacenar datos
x = []  # Valores en el eje X (puede ser una lista de índices si prefieres)
regular_prices = []  # Valores de precios regulares
premium_prices = []  # Valores de precios premium
diesel_prices = []  # Valores de precios de diesel

# Crear una figura de Matplotlib
fig, ax = plt.subplots()


# Bucle para consumir mensajes y agregar datos a las listas
for message in consumer:

    data = message.value  # Decodificar el mensaje
    data_json = json.loads(data)

    for entry in data_json:
        regular = float(entry['regular'])
        premium = float(entry['premium'])
        diesel = float(entry['diesel'])
        x.append(len(x) + 1)  # Agrega un índice secuencial para el eje X
        # Almacena los valores en las listas
        regular_prices.append(regular)
        premium_prices.append(premium)
        diesel_prices.append(diesel)
            
        ax.clear()
        # Actualiza el gráfico
        ax.plot(x, regular_prices, label='Regular')
        ax.plot(x, premium_prices, label='Premium')
        ax.plot(x, diesel_prices, label='Diesel')

        ax.set_xlabel('Muestra')
        ax.set_ylabel('Precio')
        ax.legend()  # Agrega una leyenda al gráfico
        plt.pause(0.1)  # Para mostrar la gráfica en tiempo real

# Finalmente, muestra el gráfico completo
plt.show()
