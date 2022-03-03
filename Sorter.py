import os
import random
import shutil
import tkinter

def Sorting(cantidad):
    directory_check = os.path.isdir("sorted")

    if directory_check:
        pass
    else:
        os.mkdir("sorted")

    amount = int(cantidad.get())
    directory = os.path.dirname(os.path.realpath(__file__))


    for num in range(amount):
        files = os.listdir(directory)
        
    
        try:
            files.remove("Sorter.py")
            files.remove("Sorter.exe")
            files.remove("sorted")
        except:
            pass

        number = len(files)
        
        if number == 0:
            break
        
        number = number - 1

        chosen = random.randint(0, number)
        shutil.move(directory+"/"+files[chosen], directory+"/sorted")

def Window():
    root = tkinter.Tk()
    root.title('Sorter')
    cantidad = tkinter.StringVar()
    cantidad.set(1)

    entryLabel = tkinter.Label(root, text="Cantidad a mover:")
    entryLabel.grid(column=0, row=0)

    entryNumber = tkinter.Entry(root, textvariable=cantidad)
    entryNumber.grid(column=1, row=0)

    doit = tkinter.Button(root, text="Sortear", command=lambda: Sorting(cantidad))
    doit.grid(column=0, row=1, columnspan=2)

    root.mainloop()


Window()