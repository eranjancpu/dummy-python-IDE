from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

compiler = Tk()
compiler.title("Dummy Python")
compiler.geometry("800x800")
compiler.call('wm', 'iconphoto', compiler.w, PhotoImage(file='images/python.png'))

file_path = ""


def setFilePath(p):
    global file_path
    file_path = p


def save():
    if file_path == "":
        path = asksaveasfilename(filetypes=[("python files", "*.py")])
    else:
        path = file_path
    code = editor.get("1.0", END)
    with open(path, "w") as file2:
        file2.write(code)
        file2.close()
        setFilePath(path)


def saveCode():
    path = asksaveasfilename(filetypes=[("python files", "*.py")])
    code = editor.get("1.0", END)
    with open(path, "w") as file2:
        file2.write(code)
        file2.close()
        setFilePath(path)


def openFile():
    path = askopenfilename(filetypes=[("python files", "*.py")])
    with open(path, "w") as file1:
        code = file1.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        setFilePath(path)


def runCode():
    code = editor.get("1.0", END)
    exec(code)


def about():
    aboutSC = Tk()
    aboutSC.title("about")
    labelO = Label(aboutSC, text="dummy python IDE")
    labelT = Label(aboutSC, text="by Jeenath Yapa")
    v = Label(aboutSC, text="v1.0")
    labelO.grid(row=1, column=1)
    labelT.grid(row=1, column=2)
    v.grid(row=2, column=1)


menu = Menu(compiler)

run = Menu(menu, tearoff=0)
file = Menu(menu, tearoff=0)
aboutV = Menu(menu, tearoff=0)

file.add_command(label="save", command=save)
file.add_command(label="save as", command=saveCode)
file.add_command(label="open", command=openFile)
run.add_command(label="run", command=runCode)
aboutV.add_command(label="about", command=about)

menu.add_cascade(label="file", menu=file)
menu.add_cascade(label="run", menu=run)
menu.add_cascade(label="help", menu=aboutV)

compiler.config(menu=menu)

editor = Text()
editor.pack(side=LEFT, fill=BOTH, expand=YES)
compiler.mainloop()
