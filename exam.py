from web3 import Web3
import tkinter as tk

# Public RPC (no Infura needed)
w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.org"))

# Wallet (use test wallet only)
private_key = "0xabc123456789abcdef123456789abcdef123456789abcdef123456789abcdef"
account = w3.eth.account.from_key(private_key)

# Check balance
def balance():
    bal = w3.eth.get_balance(account.address)
    bal = w3.from_wei(bal, 'ether')
    label_bal.config(text="Balance: " + str(bal) + " ETH")

# Send ETH
def send():
    to = entry_to.get()
    amt = float(entry_amt.get())

    tx = {
        'nonce': w3.eth.get_transaction_count(account.address),
        'to': to,
        'value': w3.to_wei(amt, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('10', 'gwei')
    }

    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)

    label_bal.config(text="Sent! Hash: " + tx_hash.hex())

# GUI
root = tk.Tk()
root.title("Mini DApp")

tk.Label(root, text=account.address).pack()

label_bal = tk.Label(root, text="Balance: ")
label_bal.pack()

tk.Button(root, text="Check Balance", command=balance).pack()

entry_to = tk.Entry(root)
entry_to.pack()
entry_to.insert(0, "Receiver address")

entry_amt = tk.Entry(root)
entry_amt.pack()
entry_amt.insert(0, "Amount in ETH")

tk.Button(root, text="Send ETH", command=send).pack()

root.mainloop()