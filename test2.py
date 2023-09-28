import tkinter as tk 

main= tk.Tk()

main.title("Test 2")
main.geometry("500x500")

Title = tk.Label(main, text="Test 2 Window", font=('Arial', 20))
Title.pack()

Label = tk.Label(main, text="Result", font=('Arial', 18))
Label.pack()

BFrame = tk.Frame(main)
BFrame.columnconfigure(0, weight=1)
BFrame.columnconfigure(1, weight=1)
BFrame.columnconfigure(2, weight=1)
BFrame.columnconfigure(3, weight=1)

B1 = tk.Button(BFrame, text="1", font=('Arial', 18))
B1.grid(row=0, column=0, sticky=tk.W+tk.E)

B2 = tk.Button(BFrame, text="2", font=('Arial', 18))
B2.grid(row=0, column=1, sticky=tk.W+tk.E)

B3 = tk.Button(BFrame, text="3", font=('Arial', 18))
B3.grid(row=0, column=2, sticky=tk.W+tk.E)

B4 = tk.Button(BFrame, text="4", font=('Arial', 18))
B4.grid(row=2, column=0, sticky=tk.W+tk.E)

B5 = tk.Button(BFrame, text="5", font=('Arial', 18))
B5.grid(row=2, column=1, sticky=tk.W+tk.E)

B6 = tk.Button(BFrame, text="6", font=('Arial', 18))
B6.grid(row=2, column=2, sticky=tk.W+tk.E)

B7 = tk.Button(BFrame, text="7", font=('Arial', 18))
B7.grid(row=3, column=0, sticky=tk.W+tk.E)

B8 = tk.Button(BFrame, text="8", font=('Arial', 18))
B8.grid(row=3, column=1, sticky=tk.W+tk.E)

B9 = tk.Button(BFrame, text="9", font=('Arial', 18))
B9.grid(row=3, column=2, sticky=tk.W+tk.E)

B10 = tk.Button(BFrame, text="+", font=('Arial', 18))
B10.grid(row=0, column=3, sticky=tk.W+tk.E)

B11 = tk.Button(BFrame, text="-", font=('Arial', 18))
B11.grid(row=2, column=3, sticky=tk.W+tk.E)

B12 = tk.Button(BFrame, text="*", font=('Arial', 18))
B12.grid(row=3, column=3, sticky=tk.W+tk.E)



BFrame.pack(fill='x')



main.mainloop()