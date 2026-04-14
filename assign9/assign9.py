# Interacting with DeFi Protocols (Testnet)
# Objective
# To interact with a decentralized finance (DeFi) protocol on a
# blockchain testnet by writing and executing a smart contract that
# deposits and withdraws tokens, demonstrating basic DeFi
# operations without real funds.
# Requirements
# • Install Node.js and npm
# • Install VS Code
# • Install VS Code extensions:
# o Solidity
# o Hardhat
# • Use a testnet (Sepolia / Goerli / Mumbai)
# • Create a smart contract and a script to interact with a
# DeFi protocol (mock lending contract)
# • Use functions for deposit and withdrawal
# • Test interactions using test tokens
# • Add inline comments explaining the logic
# Tools & Technologies
# • Solidity
# • Hardhat
# • JavaScript (Node.js)
# • Ethereum Testnet (Sepolia)
# • MetaMask (Testnet account)
# Practical Description
# In this practical, we simulate interaction with a DeFi protocol by
# creating a simple lending contract where:
# • Users can deposit ETH
# • Users can withdraw ETH
# • Contract tracks balances internally
# This represents how DeFi protocols like Aave or Compound work
# on testnets.
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
# Assignment Number: 02/12
# Q. No. Question Expected Time
# to complete
# 1
# Interacting with Decentralized Finance (DeFi) Protocols on a
# Test Network
# Objective
# To interact with a decentralized finance (DeFi) protocol on a
# blockchain testnet by writing and executing a smart contract that
# deposits and withdraws tokens, demonstrating basic DeFi
# operations without real funds.
# Requirements
# • Install Node.js and npm
# • Install VS Code
# • Install VS Code extensions:
# o Solidity
# o Hardhat
# • Use a testnet (Sepolia / Goerli / Mumbai)
# • Create a smart contract and a script to interact with a
# DeFi protocol (mock lending contract)
# • Use functions for deposit and withdrawal
# • Test interactions using test tokens
# • Add inline comments explaining the logic
# Tools & Technologies
# • Solidity
# • Hardhat
# • JavaScript (Node.js)
# • Ethereum Testnet (Sepolia)
# • MetaMask (Testnet account)
# Practical Description
# In this practical, we simulate interaction with a DeFi protocol by
# creating a simple lending contract where:
# • Users can deposit ETH
# • Users can withdraw ETH
# • Contract tracks balances internally
# This represents how DeFi protocols like Aave or Compound work
# on testnets.
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
# Assignment Number: 03/12
# Q. No. Question Expected Time
# to complete
# 1
# Interacting with DeFi protocols on a blockchain test network
# for learning and experimentation.
# Objective
# To interact with a decentralized finance (DeFi) protocol on a
# blockchain testnet by writing and executing a smart contract that
# deposits and withdraws tokens, demonstrating basic DeFi
# operations without real funds.
# Requirements
# • Install Node.js and npm
# • Install VS Code
# • Install VS Code extensions:
# o Solidity
# o Hardhat
# • Use a testnet (Sepolia / Goerli / Mumbai)
# • Create a smart contract and a script to interact with a
# DeFi protocol (mock lending contract)
# • Use functions for deposit and withdrawal
# • Test interactions using test tokens
# • Add inline comments explaining the logic
# Tools & Technologies
# • Solidity
# • Hardhat
# • JavaScript (Node.js)
# • Ethereum Testnet (Sepolia)
# • MetaMask (Testnet account)
# Practical Description
# In this practical, we simulate interaction with a DeFi protocol by
# creating a simple lending contract where:
# • Users can deposit ETH
# • Users can withdraw ETH
# • Contract tracks balances internally
# This represents how DeFi protocols like Aave or Compound work
# # on testnets.give python code for this
from tkinter import *
import time

# Simulated Smart Contract
class SimpleStorageContract:        
    def __init__(self):
        self.value = 0
        self.transactions = []

    def store(self, new_value):
        self.value = new_value
        tx = {
            "value": new_value,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        self.transactions.append(tx)
        return tx

    def retrieve(self):
        return self.value

# GUI Application
class SimpleStorageApp:
    def __init__(self, root):
        self.contract = SimpleStorageContract()
        self.root = root
        self.root.title("Simple Storage Contract Simulation")

        # Input field
        self.entry = Entry(root, width=20)
        self.entry.pack(pady=10)

        # Store button
        self.store_button = Button(root, text="Store Value", command=self.store_value)
        self.store_button.pack(pady=5)

        # Status label
        self.status_label = Label(root, text="")
        self.status_label.pack(pady=5)

        # Transaction hash label
        self.hash_label = Label(root, text="")
        self.hash_label.pack(pady=5)

        # History label
        self.history_label = Label(root, text="Transaction History:")
        self.history_label.pack(pady=10)

    def store_value(self):
        try:
            value = int(self.entry.get())
            tx = self.contract.store(value)
            self.status_label.config(text="Value stored successfully!", fg="green")
            self.hash_label.config(text=f"Stored Value: {tx['value']}\nTime: {tx['time']}")
            self.update_history()
        except ValueError:
            self.status_label.config(text="Please enter a valid integer.", fg="red")

    def update_history(self):
        history_text = "Transaction History:\n"
        for tx in self.contract.transactions:
            history_text += f"Value: {tx['value']} | Time: {tx['time']}\n"
        self.history_label.config(text=history_text)
if __name__ == "__main__":
    root = Tk()
    app = SimpleStorageApp(root)
    root.mainloop()
    # increase size of the window and add a button to retrieve the stored value and display it in a label.