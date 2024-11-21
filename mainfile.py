import tkinter as tk
from tkinter import messagebox

# Bank data (user info and balance)
bank_data = {
    9347266756: "Shiva",
    9534757617: "Sanjev Yadav",
    9306011724: "Arpit",
    9358276767: "Devender Singh",
    8950596240: "Shivang",
    9335960949: "Vivek Yadav",
    9555046498: 'Himanshu Pal',
    7985926222: 'Abhishek Yadav',
    9565909747: "Vinod Kumar Yadav",
    9696525854: "Chetan Kumar",
    6306854328: "Sudhir Yadav"
}

available_money = {
    9347266756: 100, 9306011724: 20000, 9534757617: 2000,
    9358276767: 5000, 8950596240: 500, 9335960949: 750,
    9555046498: 450, 7985926222: 10000, 9565909747: 300000,
    9696525854: 550, 6306854328: 1200
}

user_pin = {
    9534757617: 1290, 9347266756: 5050, 9306011724: 7272,
    9358276767: 9080, 8950596240: 6767, 9335960949: 9565,
    9555046498: 7090, 7985926222: 5604, 9565909747: 1315,
    9696525854: 5854, 6306854328: 8090
}

logged_in_user = None

def set_grid_weights(window, rows, columns):
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for i in range(columns):
        window.grid_columnconfigure(i, weight=1)

def login_window():
    login_win = tk.Tk()
    login_win.title("ATM Login")
    login_win.geometry("400x300")
    login_win.configure(bg="#2C3E50")

    set_grid_weights(login_win, 3, 2)

    tk.Label(login_win, text="Enter Your ATM Card Number:", font=("Helvetica", 10, "bold"), bg="#2C3E50", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    atm_entry = tk.Entry(login_win, justify="center", font=("Helvetica", 10))
    atm_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(login_win, text="Enter Your PIN:", font=("Helvetica", 10, "bold"), bg="#2C3E50", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    pin_entry = tk.Entry(login_win, show="*", justify="center", font=("Helvetica", 10))
    pin_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def login():
        global logged_in_user
        try:
            atm_card = int(atm_entry.get())
            pin = int(pin_entry.get())

            if atm_card in bank_data and user_pin.get(atm_card) == pin:
                logged_in_user = atm_card
                messagebox.showinfo("Login Successful", f"Welcome {bank_data[atm_card]}")
                login_win.destroy()
                transaction_window()
            else:
                messagebox.showerror("Error", "Invalid ATM Card Number or PIN")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    login_button = tk.Button(login_win, text="Login", command=login, font=("Helvetica", 10, "bold"), bg="#1ABC9C", fg="white")
    login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    login_win.mainloop()

def transaction_window():
    trans_win = tk.Tk()
    trans_win.title("ATM Transactions")
    trans_win.geometry("400x300")
    trans_win.configure(bg="#34495E")

    set_grid_weights(trans_win, 4, 1)

    tk.Label(trans_win, text="Select a Transaction:", font=("Helvetica", 10, "bold"), bg="#34495E", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def check_balance():
        messagebox.showinfo("Available Balance", f"Your available balance is ₹{available_money[logged_in_user]}")
        trans_win.destroy()
        login_window()

    def withdraw_money():
        trans_win.destroy()
        import atm_withdraw_and_transfer
        atm_withdraw_and_transfer.withdraw_window()

    def transfer_money():
        trans_win.destroy()
        import atm_withdraw_and_transfer
        atm_withdraw_and_transfer.transfer_window()

    balance_button = tk.Button(trans_win, text="Check Balance", command=check_balance, font=("Helvetica", 10, "bold"), bg="#3498DB", fg="white")
    balance_button.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

    withdraw_button = tk.Button(trans_win, text="Withdraw Money", command=withdraw_money, font=("Helvetica", 10, "bold"), bg="#E74C3C", fg="white")
    withdraw_button.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

    transfer_button = tk.Button(trans_win, text="Transfer Money", command=transfer_money, font=("Helvetica", 10, "bold"), bg="#9B59B6", fg="white")
    transfer_button.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")

    trans_win.mainloop()

login_window()
