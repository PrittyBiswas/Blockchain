# Hyperledger Fabric – Comparative Exploration
# Objective
# To study and practically explore Hyperledger Fabric by setting
# up a basic Fabric test network, deploying a simple chaincode, and
# comparing Hyperledger Fabric with a public blockchain
# (Ethereum) based on architecture, consensus, privacy,
# performance, and use cases.
# Requirements
# Software Requirements
# • Operating System: Ubuntu 20.04 / Windows (with WSL) /
# macOS
# • Docker & Docker Compose
# • Git
# • cURL
# • Node.js (v16+) or Go (for chaincode)
# • Hyperledger Fabric binaries and samples
# Hardware Requirements
# • Minimum 8 GB RAM
# • Internet connection
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
# Hyperledger Fabric: A Comparative Blockchain Exploration
# Objective
# To study and practically explore Hyperledger Fabric by setting
# up a basic Fabric test network, deploying a simple chaincode, and
# comparing Hyperledger Fabric with a public blockchain
# (Ethereum) based on architecture, consensus, privacy,
# performance, and use cases.
# Requirements
# Software Requirements
# • Operating System: Ubuntu 20.04 / Windows (with WSL) /
# macOS
# • Docker & Docker Compose
# • Git
# • cURL
# • Node.js (v16+) or Go (for chaincode)
# • Hyperledger Fabric binaries and samples
# Hardware Requirements
# • Minimum 8 GB RAM
# • Internet connection
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
# Hyperledger Fabric: A Comparative Blockchain Framework
# Study
# Objective
# To study and practically explore Hyperledger Fabric by setting
# up a basic Fabric test network, deploying a simple chaincode, and
# comparing Hyperledger Fabric with a public blockchain
# (Ethereum) based on architecture, consensus, privacy,
# performance, and use cases.
# Requirements
# Software Requirements
# • Operating System: Ubuntu 20.04 / Windows (with WSL) /
# macOS
# • Docker & Docker Compose
# • Git
# • cURL
# • Node.js (v16+) or Go (for chaincode)
# • Hyperledger Fabric binaries and samples
# Hardware Requirements
# • Minimum 8 GB RAM
# • Internet connection give python code
from tkinter import *
import time
# Simulated blockchain storage
blockchain_storage = {
    "value": None,
    "history": []
}

# Function to simulate storing a value in the smart contract
def store_value():
    value = entry.get()
    if value:
        # Simulate a transaction
        tx = {
            "value": value,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        blockchain_storage["value"] = value
        blockchain_storage["history"].append(tx)
        status_label.config(text="Value stored successfully!")
        hash_label.config(text=f"Transaction Hash: {hash(str(tx))}")
        update_history()
    else:
        status_label.config(text="Please enter a value to store.")
# Function to simulate retrieving the stored value
def get_value():
    value = blockchain_storage["value"]
    if value is not None:
        result_label.config(text=f"Stored Value: {value}")
    else:
        result_label.config(text="No value stored yet.")
# Function to update the transaction history display
def update_history():
    history_text = "Transaction History:\n"
    for tx in blockchain_storage["history"]:
        history_text += f"{tx['time']}: Stored {tx['value']}\n"
    history_label.config(text=history_text)
# GUI setup
root = Tk()
root.title("Simple Storage Contract Simulation")
entry = Entry(root, width=20)
entry.pack(pady=10)
store_button = Button(root, text="Store Value", command=store_value)
store_button.pack(pady=5)
get_button = Button(root, text="Get Stored Value", command=get_value)
get_button.pack(pady=5)
status_label = Label(root, text="")
status_label.pack(pady=5)
hash_label = Label(root, text="")
hash_label.pack(pady=5)
result_label = Label(root, text="")
result_label.pack(pady=5)
history_label = Label(root, text="Transaction History:")
history_label.pack(pady=10)
root.mainloop()
from tkinter import *
import time
