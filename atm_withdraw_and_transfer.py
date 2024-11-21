import tkinter as tk
from tkinter import messagebox

# Bank data (user info and balance)
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

logged_in_user = 9534757617  # Example user for testing

def set_grid_weights(window, rows, columns):
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for i in range(columns):
        window.grid_columnconfigure(i, weight=1)

def withdraw_window():
    withdraw_win = tk.Tk()
    withdraw_win.title("Withdraw Money")
    withdraw_win.geometry("400x300")
    withdraw_win.configure(bg="#2ECC71")

    set_grid_weights(withdraw_win, 2, 2)

    tk.Label(withdraw_win, text="Enter amount to withdraw:", font=("Helvetica", 10, "bold"), bg="#2ECC71", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    amount_entry = tk.Entry(withdraw_win, justify="center", font=("Helvetica", 10))
    amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def withdraw():
        try:
            amount = int(amount_entry.get())
            if amount <= available_money[logged_in_user]:
                available_money[logged_in_user] -= amount
                messagebox.showinfo("Success", f"Withdrawal successful! Your remaining balance is ₹{available_money[logged_in_user]}")
                withdraw_win.destroy()
                import atm_login_and_transactions
                atm_login_and_transactions.login_window()
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    withdraw_button = tk.Button(withdraw_win, text="Withdraw", command=withdraw, font=("Helvetica", 10, "bold"), bg="#1ABC9C", fg="white")
    withdraw_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    withdraw_win.mainloop()

def transfer_window():
    transfer_win = tk.Tk()
    transfer_win.title("Transfer Money")
    transfer_win.geometry("400x300")
    transfer_win.configure(bg="#9B59B6")

    set_grid_weights(transfer_win, 3, 2)

    tk.Label(transfer_win, text="Enter receiver's ATM number:", font=("Helvetica", 10, "bold"), bg="#9B59B6", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    receiver_entry = tk.Entry(transfer_win, justify="center", font=("Helvetica", 10))
    receiver_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(transfer_win, text="Enter amount to transfer:", font=("Helvetica", 10, "bold"), bg="#9B59B6", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    amount_entry = tk.Entry(transfer_win, justify="center", font=("Helvetica", 10))
    amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def transfer():
        try:
            receiver = int(receiver_entry.get())
            amount = int(amount_entry.get())
            
            if receiver not in bank_data:
                messagebox.showerror("Error", "Receiver's account not found.")
                return

            if amount <= available_money[logged_in_user]:
                available_money[logged_in_user] -= amount
                available_money[receiver] += amount
                messagebox.showinfo("Success", f"₹{amount} transferred to {bank_data[receiver]} successfully!")
                transfer_win.destroy()
                import atm_login_and_transactions
                atm_login_and_transactions.login_window()
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    transfer_button = tk.Button(transfer_win, text="Transfer", command=transfer, font=("Helvetica", 10, "bold"), bg="#8E44AD", fg="white")
    transfer_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    transfer_win.mainloop()
