import csv
import logging
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

client = Client(api_key, api_secret)

logging.basicConfig(
    filename='transferencias.log'
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

output_files = 'resultado_transferencias.csv'

with open(output_file, mode='w', newline='') as result_file:
    writer = csv.writer(result_file)
    writer.writerow(['Endereço', 'Valor', 'Status'])

def realizar_transferencias(input_csv):
    with open('pagamentos.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            endereco = row['Endereço']
            valor = row['Valor']

            try:
                result = client.withdraw(
                    coin='USDT',
                    address=endereco,
                    amount=valor,
                    network='BSC'
                )
                logging.info(f"Transação enviada com sucesso: Endereço={endereco}, Valor={valor}")
                status = 'Sucesso'
            except Exception as e:
                logging.error(f"Erro ao enviar para {endereco}: {e}")
                status = f'Erro: {e}'

            with open(output_file, mode='a', newline='') as result_file:
                writer = csv.writer(result_file)
                writer.writerow([endereco, valor, status])

input_csv = 'transferencias.csv'
realizar_transferencias(input_csv)
