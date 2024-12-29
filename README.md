# Binance USDT Payments

This repository contains a Python script designed for performing bulk cryptocurrency transfers using the Binance API. The script reads transaction data from a CSV file, processes each transfer, and logs the results for auditing and troubleshooting purposes.

## Features

- **Bulk Transfers**: Processes multiple cryptocurrency transfers in one execution.
- **Logging**: Records success and failure details for each transaction in a log file.
- **CSV Input/Output**: Reads input data from a CSV file (`pagamentos.csv`) and generates a CSV report (`resultado_transferencias.csv`) with the transaction statuses.
- **Binance API Integration**: Utilizes the Binance API for handling cryptocurrency withdrawals.
- **Error Handling**: Captures and logs errors for failed transactions.

---

## Prerequisites

Before using this script, ensure you have the following:

1. **Python**: Python 3.8 or later.
2. **Binance API Keys**: Access to Binance API keys (`api_key` and `api_secret`).
3. **Dependencies**: Install the required Python packages:
   ```bash
   pip install python-binance python-dotenv
4. **.env File**: Create a `.env` file in the project directory and add your Binance API credentials:
   ```plaintext
   api_key=your_api_key_here
   api_secret=your_api_secret_here

---
  
## Input CSV Format

The script reads transfer details from a file named `pagamentos.csv`. The CSV file must have the following format:

| Endereco          | Valor |
|--------------------|-------|
| Recipient_Address | Amount |

- **Endereco**: The recipient's wallet address.
- **Valor**: The amount of cryptocurrency to transfer (in USDT).

### Example `pagamentos.csv`
```csv
Endereco,Valor
0x123abc...789,10
0x456def...012,25
```

---

## Output CSV Format

After execution, the script generates a file named `resultado_transferencias.csv`, which contains the status of each transfer:

| Endereco          | Valor | Status         |
|--------------------|-------|----------------|
| Recipient_Address | Amount | Success/Error  |

---

## Binance API Setup

To use this project, you must enable API access in your Binance account and generate API credentials (API Key and API Secret). Follow these steps to set up your Binance API:

1. **Log in to Binance**:
   - Visit [Binance](https://www.binance.com) and log in to your account.

2. **Go to API Management**:
   - Navigate to your account settings and select "API Management" from the options.

3. **Create a New API Key**:
   - Provide a label for the API key (e.g., "BulkTransfers").
   - Complete the required security verifications (such as 2FA).

4. **Set API Permissions**:
   - Ensure you enable the following permissions for the API key:
     - **Enable Withdrawals**: Required to process cryptocurrency transfers.
     - **Read-Only**: Allows the script to access account details if needed.
   - **Warning**: Be cautious when enabling withdrawal permissions. Only use these keys in a secure environment.

5. **Save Your API Key and Secret**:
   - After creation, you will see your API Key and API Secret. Copy and save them securely.
   - You will need to add these credentials to the `.env` file in the project directory.

6. **Secure Your API Keys**:
   - Bind the API key to specific IP addresses if possible to enhance security.
   - Avoid sharing your API credentials with anyone.

### Example `.env` File
```plaintext
api_key=your_api_key_here
api_secret=your_api_secret_here
```

---

## How to Run

1. **Prepare the Input File**:
   Ensure `pagamentos.csv` is correctly formatted and placed in the same directory as the script.

2. **Dependencies**: Install the required Python packages:
   ```bash
   pip install python-binance python-dotenv
   
3. **.env File**: Create a `.env` file in the project directory and add your Binance API credentials:
   ```plaintext
   api_key=your_api_key_here
   api_secret=your_api_secret_here
   
4. **Execute the Script**:
   Run the script using the following command:
   ```bash
   python index.py

---

## Logging

All transactions are logged in the `transferencias.log` file with the following details:

- **Timestamp**: The date and time of each transaction attempt.
- **Transaction Details**: Includes the recipient address and the amount transferred.
- **Status**:
  - For successful transactions, it logs a confirmation message.
  - For failed transactions, it logs the error message returned by the Binance API.

This log is essential for auditing and troubleshooting any issues during the transfer process.

### Example Log Entry
```plaintext
2024-12-29 10:00:00 - INFO - Transacao enviada com sucesso: Endereco=0x123abc...789, Valor=10
2024-12-29 10:05:00 - ERROR - Erro ao enviar para 0x456def...012: 'Insufficient balance'
```

---

## Notes

- Ensure the wallet addresses and network (`BSC` in this script) are correct to avoid loss of funds.
- Test the script in a controlled environment with small transactions before processing high-value transfers.
- Binance API transaction limits and withdrawal fees may apply.

---

## Disclaimer

This script is for educational purposes only. Use it at your own risk. Always ensure compliance with Binance API terms of use and applicable cryptocurrency regulations. The author is not responsible for any losses or damages resulting from its use.

---

## Contributions

Feel free to submit pull requests or issues for improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

