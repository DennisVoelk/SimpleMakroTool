import tkinter as tk
import tkinter.ttk as ttk

class MainGUI(object):
    def __init__(self, cbFunctions):
        self.cbFunctions = cbFunctions
        self.keys = []

        root = tk.Tk()
        root.minsize(400,200)
        root.title("Automatio")


        #Menu
        menu = tk.Menu(root)
        root.config(menu=menu)

        fileMenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="Save")
        fileMenu.add_command(label="Save as")

        exportMenu = tk.Menu(fileMenu)
        exportMenu.add_command(label="Single executable file", command=self.exportSingle)
        exportMenu.add_command(label="Dynamic executable file & config", command=self.exportMulti)
        fileMenu.add_cascade(label='Export', menu=exportMenu, underline=0)


        #SequenceContainer
        self.sequenceContainer = tk.Canvas(root)
        self.sequenceContainer.pack(padx=5, pady=5, expand=True, fill="both")
        self.sequenceList = tk.Canvas(self.sequenceContainer)
        self.sequenceList.pack(expand=True, fill="both")

        #Controls
        self.controlsContainer = tk.Canvas(root, height=60)
        self.controlsContainer.pack(padx=5, pady=5, expand=True, fill="both")

        self.controlsContainer.rowconfigure(0, weight=1)
        self.controlsContainer.columnconfigure(0, weight=1)
        self.controlsContainer.columnconfigure(1, weight=1)
        self.controlsContainer.columnconfigure(2, weight=1)

        ttk.Separator(self.controlsContainer, orient="horizontal").grid(row=0, column=0, sticky="ew", columnspan=100, pady=5)
        tk.Label(self.controlsContainer, text="Press ESC to finish key-recording").grid(row=1, column=0, padx=5, sticky="ew",columnspan=100)
        recBtn = tk.Button(self.controlsContainer, text="Record key-sequence", command=self.record)
        recBtn.grid(row=2, column=0, padx=5, sticky="e")
        recBtn = tk.Button(self.controlsContainer, text="Record single key")
        recBtn.grid(row=2, column=1, padx=5, sticky="ew")
        resetBtn = tk.Button(self.controlsContainer, text="Reset", bg="red", fg="white")
        resetBtn.grid(row=2, column=2, padx=5, sticky="w")

        root.mainloop()

    def exportSingle(self):
        self.cbFunctions["exportSingle"](self.keys)

    def exportMulti(self):
        self.cbFunctions["exportMulti"](self.keys)


    def updateKeyDisplay(self):
        #Changing Controls
        #self.controlsContainer.pack_forget()
        self.sequenceList.pack_forget()
        self.sequenceList = tk.Canvas(self.sequenceContainer)
        self.sequenceList.pack(expand=True, fill="both")

        #Adding SequenceContainer Items
        for i in range(0,len(self.keys)):
            color="gray76"
            if(i%2==0):
                color="gray61"
            container = tk.Canvas(self.sequenceList, height=10, bg=color)
            container.pack(expand=True, fill="both")
            tk.Label(container, text=self.keys[i], bg=color).grid(row=0, column=0, padx=5, pady=5, sticky="w")
            container.grid_columnconfigure(0, weight=1)
            tk.Button(container, text="X").grid(row=0, column=1, padx=5, pady=5, sticky="e")
        return None

    def record(self):
        self.keys = self.cbFunctions["recordKeys"]()
        self.updateKeyDisplay()