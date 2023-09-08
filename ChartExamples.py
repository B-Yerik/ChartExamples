#пример построения графиков

import tkinter as tk

#funkicya zakrytiya
def do_close():
    window.destroy()

#sozdanie novogo okna
window = tk.Tk()
window.geometry("450x450")
window.title("Primery postroenie grafikov")

#dobavlenir knopki zakrytiya
btnClose = tk.Button(window, text='Close', font=('Helvetica',10,'bold'),command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

#Zapusk cikla mainloop
window.mainloop()



