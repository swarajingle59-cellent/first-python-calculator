import tkinter as tk


def calculate():
    try:
        result = eval(entry.get())
        answer.config(text=str(result))
    except:
        answer.config(text="Invalid calculation")


# Create window
root = tk.Tk()
root.title("GUI Calculator")


# Calculator input
entry = tk.Entry(root, width=25, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


# Calculator buttons
buttons = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["0", ".", "=", "/"]
]

for row, button_row in enumerate(buttons, start=1):
    for column, button in enumerate(button_row):
        if button == "=":
            command = calculate
        else:
            command = lambda value=button: entry.insert(tk.END, value)

        tk.Button(root, text=button, command=command, width=5).grid(
            row=row, column=column, padx=2, pady=2
        )

answer = tk.Label(root, text="Result")
answer.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
