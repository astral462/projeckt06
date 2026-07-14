from tkinter import *

window = Tk()
window.title("КАЛЬКУЛЯТОР")
window.geometry("350x550")

Entry(window, width=20, font=("Arial", 20)).grid(row=0, column=0, columnspan=4)


Button(window, text="7").grid(row=1, column=0)
Button(window, text="8").grid(row=1, column=1)
Button(window, text="9").grid(row=1, column=2)
Button(window, text="/").grid(row=1, column=3)

Button(window, text="4").grid(row=2, column=0)
Button(window, text="5").grid(row=2, column=1)
Button(window, text="6").grid(row=2, column=2)
Button(window, text="*").grid(row=2, column=3)

Button(window, text="1").grid(row=3, column=0)
Button(window, text="2").grid(row=3, column=1)
Button(window, text="3").grid(row=3, column=2)
Button(window, text="-").grid(row=3, column=3)

Button(window, text="0").grid(row=4, column=0)
Button(window, text=".").grid(row=4, column=1)
Button(window, text="=").grid(row=4, column=2)
Button(window, text="+").grid(row=4, column=3)


window.mainloop()