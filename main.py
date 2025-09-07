import tkinter as tkinter

root = tkinter.Tk()
root.title("Counter App")
root.geometry("400x300")
root.configure(bg="lightblue")

counter = 0

def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Counter: {counter}")

def reset_counter():
    global counter
    counter = 0
    counter_label.config(text=f"Counter: 0")

title_label = tkinter.Label(root, text="Welcome to My GUI Program", bg="lightblue", font=("Arial", 16))
title_label.pack(pady=10)

counter_label = tkinter.Label(root, text="Counter: 0", bg="lightblue", font=("Arial", 14))
counter_label.pack(pady=10)

increment_button = tkinter.Button(root, text="Increment Counter", command=increment_counter, bg="white", font=("Arial", 12))
increment_button.pack(pady=5)

reset_button = tkinter.Button(root, text="Reset Counter", command=reset_counter, bg="white", font=("Arial", 12))
reset_button.pack(pady=5)

exit_button = tkinter.Button(root, text="Exit", command=root.quit, bg="red", fg="white", font=("Arial", 12))
exit_button.pack(pady=20)
root.mainloop()

