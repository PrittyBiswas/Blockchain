# Hyperledger Fabric Problem Solving
# Objective
# To design and implement a simple Hyperledger Fabric smart
# contract (chaincode) that manages a personal asset portfolio on a
# blockchain network. The practical focuses on problem-solving
# using Fabric concepts such as assets, transactions, ledger state, and
# queries.
# Problem Statement
# Implement a basic blockchain-based portfolio system where a user
# can:
# • Create assets (e.g., certificates, projects, or tokens)
# • View all assets stored on the blockchain
# • Transfer asset ownership between users
# This practical demonstrates how Hyperledger Fabric solves real-
# world problems like data immutability, transparency, and secure
# ownership transfer.
# Requirements
# Software Requirements
# • Operating System: Windows / Linux / macOS
# • Node.js (v16 or later)
# • Docker & Docker Compose
# • Git
# • VS Code (with Docker and JavaScript extensions)
# Blockchain Platform
# • Hyperledger Fabric test network
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
# Understanding problem-solving approaches with Hyperledger
# Fabric
# Objective
# To design and implement a simple Hyperledger Fabric smart
# contract (chaincode) that manages a personal asset portfolio on a
# blockchain network. The practical focuses on problem-solving
# using Fabric concepts such as assets, transactions, ledger state, and
# queries.
# Problem Statement
# Implement a basic blockchain-based portfolio system where a user
# can:
# • Create assets (e.g., certificates, projects, or tokens)
# • View all assets stored on the blockchain
# • Transfer asset ownership between users
# This practical demonstrates how Hyperledger Fabric solves real-
# world problems like data immutability, transparency, and secure
# ownership transfer.
# Requirements
# Software Requirements
# • Operating System: Windows / Linux / macOS
# • Node.js (v16 or later)
# • Docker & Docker Compose
# • Git
# • VS Code (with Docker and JavaScript extensions)
# Blockchain Platform
# • Hyperledger Fabric test network
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
# Problem Analysis and Solution Design Using Hyperledger
# Fabric
# Objective
# To design and implement a simple Hyperledger Fabric smart
# contract (chaincode) that manages a personal asset portfolio on a
# blockchain network. The practical focuses on problem-solving
# using Fabric concepts such as assets, transactions, ledger state, and
# queries.
# Problem Statement
# Implement a basic blockchain-based portfolio system where a user
# can:
# • Create assets (e.g., certificates, projects, or tokens)
# • View all assets stored on the blockchain
# • Transfer asset ownership between users
# This practical demonstrates how Hyperledger Fabric solves real-
# world problems like data immutability, transparency, and secure
# ownership transfer.
# Requirements
# Software Requirements
# • Operating System: Windows / Linux / macOS
# • Node.js (v16 or later)
# • Docker & Docker Compose
# • Git
# • VS Code (with Docker and JavaScript extensions)
# Blockchain Platform
# • Hyperledger Fabric test network
# #give python code
import hashlib
import time

# -------------------------------------------------
# SMART CONTRACT SIMULATION
class SimpleStorage:
    def __init__(self):
        self.stored_value = 0
        self.transactions = []

    def set(self, value):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        tx_hash = self.generate_hash(value, timestamp)

        self.stored_value = value

        transaction = {
            "value": value,
            "hash": tx_hash,
            "time": timestamp
        }

        self.transactions.append(transaction)
        return transaction

    def get(self):
        return self.stored_value

    def generate_hash(self, value, timestamp):
        data = f"{value}{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()
    
# -------------------------------------------------
# CONTRACT OBJECT (DEPLOYMENT)
contract = SimpleStorage()
# -------------------------------------------------
# GUI FUNCTIONS
def store_value():
    try:
        value = int(entry.get())
        tx = contract.set(value)

        status_label.config(
            text="Transaction Successful ✔",
            fg="green"
        )

        hash_label.config(
            text=f"Transaction Hash:\n{tx['hash']}"
        )

        update_history()

    except ValueError:
        status_label.config(text="Please enter a valid integer.", fg="red")
def get_value():
    value = contract.get()
    result_label.config(text=f"Stored Value: {value}")
def update_history():
    history_text = "Transaction History:\n"
    for tx in contract.transactions:
        history_text += f"{tx['time']}: Stored {tx['value']} (Hash: {tx['hash']})\n"
    history_label.config(text=history_text)
# -------------------------------------------------
# GUI SETUP
from tkinter import *
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
