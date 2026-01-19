from tkinter import *
import hashlib
import time

# -------------------------------------------------
# SMART CONTRACT SIMULATION
# -------------------------------------------------
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
# -------------------------------------------------
contract = SimpleStorage()

# -------------------------------------------------
# GUI FUNCTIONS
# -------------------------------------------------
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
        status_label.config(
            text="Please enter a valid number ❌",
            fg="red"
        )

def get_value():
    value = contract.get()
    result_label.config(text=f"Stored Value: {value}")

def update_history():
    history_box.delete(0, END)
    for i, tx in enumerate(contract.transactions):
        history_box.insert(
            END,
            f"{i+1}. Value: {tx['value']} | Time: {tx['time']}"
        )


# -------------------------------------------------
# GUI DESIGN
# -------------------------------------------------
root = Tk()
root.title("Simple Storage Smart Contract (Python Simulation)")
root.geometry("650x520")

Label(
    root,
    text="Simple Storage Smart Contract",
    font=("Arial", 16, "bold")
).pack(pady=10)

Label(root, text="Enter Value").pack()
entry = Entry(root, width=30)
entry.pack(pady=5)

Button(
    root,
    text="Store Value (Transaction)",
    width=25,
    command=store_value
).pack(pady=8)

Button(
    root,
    text="Get Stored Value",
    width=25,
    command=get_value
).pack(pady=5)

status_label = Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

hash_label = Label(
    root,
    text="Transaction Hash:",
    wraplength=600,
    justify="left",
    font=("Courier", 9)
)
hash_label.pack(pady=10)

Label(
    root,
    text="Transaction History",
    font=("Arial", 12, "bold")
).pack(pady=5)

history_box = Listbox(root, width=90, height=8)
history_box.pack(pady=5)

root.mainloop()
