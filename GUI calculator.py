import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())   # eval evaluates math expression
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Error")

# Create window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x200")

# Input box
entry = tk.Entry(window, width=25)
entry.pack(pady=10)

# Calculate button
btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack(pady=5)

# Result label
label_result = tk.Label(window, text="Result: ")
label_result.pack(pady=5)

# Run the app
window.mainloop()
