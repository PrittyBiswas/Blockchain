# Exploring Layer 2 – Testnet
# Objective
# To understand and explore Layer 2 blockchain networks by
# deploying and interacting with a simple smart contract on a Layer
# 2 Testnet (e.g., Polygon Mumbai / Arbitrum Sepolia), and observe
# reduced gas fees and faster transactions compared to Layer 1.
# Requirements
# • Basic understanding of blockchain and smart contracts
# • MetaMask wallet installed (browser extension)
# • Testnet ETH/MATIC from faucet
# • VS Code (with Solidity extension installed)
# • Node.js and npm installed
# • Hardhat development framework
# Tools & Technologies Used
# • Blockchain Type: Layer 2 Testnet
# • Network: Polygon Mumbai Testnet (or Arbitrum Sepolia)
# • Language: Solidity
# • Framework: Hardhat
# • Wallet: MetaMask
# Execution Key is:-
# 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
# SCHOOL OF COMPUTER SCIENCE AND
# ARTIFICIAL INTELLIGENCE
# DEPARTMENT OF COMPUTER SCIENCE
# ENGINEERING
# Program Name: B. Tech Assignment Type: Lab Academic Year: 2025-26
# Course Coordinator Name Dr. Jagjit Singh Dhatterwal
# Instructor(s) Name Dr. Jagjit Singh Dhatterwal
# Course Code 21CS127 Course Title Blockchain Engineering
# Year/Sem III/II Regulation R22
# Date and Day
# of Assignment Time(s)
# Duration 2 Hours Applicable to
# Batches
# Assignment Number: 2/12
# Q. No. Question Expected Time
# to complete
# 1
# To explore Layer 2 blockchain technology using a testnet
# environment.
# Objective
# To understand and explore Layer 2 blockchain networks by
# deploying and interacting with a simple smart contract on a Layer
# 2 Testnet (e.g., Polygon Mumbai / Arbitrum Sepolia), and observe
# reduced gas fees and faster transactions compared to Layer 1.
# Requirements
# • Basic understanding of blockchain and smart contracts
# • MetaMask wallet installed (browser extension)
# • Testnet ETH/MATIC from faucet
# • VS Code (with Solidity extension installed)
# • Node.js and npm installed
# • Hardhat development framework
# Tools & Technologies Used
# • Blockchain Type: Layer 2 Testnet
# • Network: Polygon Mumbai Testnet (or Arbitrum Sepolia)
# • Language: Solidity
# • Framework: Hardhat
# • Wallet: MetaMask
# Execution Key is:-
# 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
# SCHOOL OF COMPUTER SCIENCE AND
# ARTIFICIAL INTELLIGENCE
# DEPARTMENT OF COMPUTER SCIENCE
# ENGINEERING
# Program Name: B. Tech Assignment Type: Lab Academic Year: 2025-26
# Course Coordinator Name Dr. Jagjit Singh Dhatterwal
# Instructor(s) Name Dr. Jagjit Singh Dhatterwal
# Course Code 21CS127 Course Title Blockchain Engineering
# Year/Sem III/II Regulation R22
# Date and Day
# of Assignment Time(s)
# Duration 2 Hours Applicable to
# Batches
# Assignment Number: 3/12
# Q. No. Question Expected Time
# to complete
# 1
# Studying Layer 2 scaling solutions by deploying and testing
# applications on a blockchain testnet.
# Objective
# To understand and explore Layer 2 blockchain networks by
# deploying and interacting with a simple smart contract on a Layer
# 2 Testnet (e.g., Polygon Mumbai / Arbitrum Sepolia), and observe
# reduced gas fees and faster transactions compared to Layer 1.
# Requirements
# • Basic understanding of blockchain and smart contracts
# • MetaMask wallet installed (browser extension)
# • Testnet ETH/MATIC from faucet
# • VS Code (with Solidity extension installed)
# • Node.js and npm installed
# • Hardhat development framework
# Tools & Technologies Used
# • Blockchain Type: Layer 2 Testnet
# • Network: Polygon Mumbai Testnet (or Arbitrum Sepolia)
# • Language: Solidity
# • Framework: Hardhat
# • Wallet: MetaMask
# Execution Key is:-
# 0x742d35Cc6634C0532925a3b844Bc454e4438f44e give python code
from tkinter import *
from datetime import datetime

# Simulated Smart Contract
class SimpleStorageContract:
    def __init__(self):
        self.value = 0
        self.transactions = []

    def store_value(self, new_value):
        self.value = new_value
        tx_hash = f"0x{hash((new_value, datetime.now())):064x}"
        self.transactions.append({
            "value": new_value,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hash": tx_hash
        })
        return tx_hash

    def get_value(self):
        return self.value
    
# GUI Application
class SimpleStorageApp:
    def __init__(self, root):
        self.contract = SimpleStorageContract()
        self.root = root
        self.root.title("Simple Storage Contract Simulation")

        self.entry = Entry(root, width=20)
        self.entry.pack(pady=10)

        self.store_button = Button(root, text="Store Value", command=self.store_value)
        self.store_button.pack(pady=5)

        self.status_label = Label(root, text="")
        self.status_label.pack(pady=5)

        self.hash_label = Label(root, text="")
        self.hash_label.pack(pady=5)

        self.history_label = Label(root, text="Transaction History:")
        self.history_label.pack(pady=10)

        self.history_text = Text(root, height=10, width=50)
        self.history_text.pack()

    def store_value(self):
        try:
            new_value = int(self.entry.get())
            tx_hash = self.contract.store_value(new_value)
            self.status_label.config(text="Value stored successfully!", fg="green")
            self.hash_label.config(text=f"Transaction Hash: {tx_hash}")
            self.update_history()
        except ValueError:
            self.status_label.config(text="Please enter a valid integer.", fg="red")

    def update_history(self):
        self.history_text.delete(1.0, END)
        for tx in self.contract.transactions:
            self.history_text.insert(END, f"Value: {tx['value']}, Time: {tx['time']}, Hash: {tx['hash']}\n")
if __name__ == "__main__":
    root = Tk()
    app = SimpleStorageApp(root)
    root.mainloop()
    