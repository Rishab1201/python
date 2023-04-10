import tkinter as tk

DIGIT_WORDS = {
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

def display_digit():
    n = entry.get()
    digit_text.delete('1.0',tk.END)
    for digit in n:
        digit_word = DIGIT_WORDS.get(digit, '?')
        digit_text.insert(tk.END, f"{digit_word}\n")

root = tk.Tk()

label =tk.Label(text='Enter a number : ')
label.pack()

entry = tk.Entry()
entry.pack()

submit = tk.Button(root, command=display_digit, text='Display Digits ')
submit.pack()

digit_text = tk.Text(root)
digit_text.pack()

root.mainloop()