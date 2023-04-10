import tkinter as tk
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def Prefect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        return n


def armstrong(n):
    sum = 0
    val = n
    while n >0 :
        rem = n % 10
        sum = sum + (rem*rem*rem)
        n = n // 10

    if val == sum:
        return val


def check_number():
    n = int(entry.get())
    if prime_button_var.get() == 1:

        if prime(n):
            result_label.config(text=f"{n} is prime number")
        else:
            result_label.config(text=f"{n} is not a prime number")

    elif perfect_button_var.get() == 1:
        if Prefect(n):
            result_label.config(text=f"{n} is a perfect number. ")
        else:
            result_label.config(text=f"{n} is not a perfect number.")
    elif armstrong_button_var.get() == 1:
        if armstrong(n):
            result_label.config(text=f"{n} is a armstrong number. ")
        else:
            result_label.config(text=f"{n} is not a armstrong number.")



root = tk.Tk()
root.title("Number Checker")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Enter a number:")
entry_label.pack()

entry = tk.Entry(frame)
entry.pack()

prime_button_var = tk.IntVar()
prime_button = tk.Radiobutton(frame, text="Prime", variable=prime_button_var, value=1)
prime_button.pack()

perfect_button_var = tk.IntVar()
perfect_button = tk.Radiobutton(frame, text="Perfect", variable=perfect_button_var, value=1)
perfect_button.pack()

armstrong_button_var = tk.IntVar()
armstrong_button = tk.Radiobutton(frame, text="Armstrong", variable=armstrong_button_var, value=1)
armstrong_button.pack()

check_button = tk.Button(frame, text="Check", command=check_number)
check_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()