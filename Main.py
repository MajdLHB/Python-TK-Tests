import tkinter as tk

index = tk.Tk()

index.geometry("800x500")
index.title("Majd's First Test App: Fake login")

Label = tk.Label(index, text="Welcome to SRT TV", font=('segeo ui semibold', 20))
Label.pack(padx=20, pady=20)

USTX = tk.Label(index, text="Username", font=('segeo ui', 19))
USTX.pack(padx=10, pady=0)
Username = tk.Entry(index, font=('segeo ui', 16))
Username.pack(padx=10, pady=0)

PSTX = tk.Label(index, text="Password", font=('segeo ui', 19))
PSTX.pack(padx=10, pady=0)
Pass = tk.Entry(index, font=('segeo ui', 16))
Pass.pack(padx=10, pady=0)

LBU = tk.Button(index, text="Log In", font=('segeo ui', 18))
LBU.pack(padx=20, pady=10)
tectbox = tk.Text(index, font=('segeo ui', 18))
tectbox.pack(pady= 40)


index.mainloop()