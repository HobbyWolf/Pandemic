import tkinter
from NewMaster import Master


class Pandemic(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.pop = tkinter.Label(self, text='Enter population density ')
        self.pop.grid(column=0, row=0, sticky='EW')
        self.pop_num = tkinter.StringVar()
        self.pop_entry = tkinter.Entry(self, textvariable=self.pop_num)
        self.pop_entry.grid(column=1, row=0, sticky='EW')
        self.pop_num.set(u"100")

        self.dist = tkinter.Label(self, text='Enter max distance in km ')
        self.dist.grid(column=0, row=1, sticky='EW')
        self.dist_pop = tkinter.StringVar()
        self.dist_entry = tkinter.Entry(self, textvariable=self.dist_pop)
        self.dist_entry.grid(column=1, row=1, sticky='EW')
        self.dist_pop.set(u"1")

        self.infec = tkinter.Label(self, text='Enter initial no.of infected people ')
        self.infec.grid(column=0, row=2, sticky='EW')
        self.infec_pop = tkinter.StringVar()
        self.infec_entry = tkinter.Entry(self, textvariable=self.infec_pop)
        self.infec_entry.grid(column=1, row=2, sticky='EW')
        self.infec_pop.set(u"10")

        self.nod = tkinter.Label(self, text='No.of days ')
        self.nod.grid(column=0, row=3, sticky='EW')
        self.nod_pop = tkinter.StringVar()
        self.nod_entry = tkinter.Entry(self, textvariable=self.nod_pop)
        self.nod_entry.grid(column=1, row=3, sticky='EW')
        self.nod_pop.set(u"300")

        self.infecprob = tkinter.Label(self, text='Enter infective probability in % ')
        self.infecprob.grid(column=0, row=4, sticky='EW')
        self.infecprob_pop = tkinter.StringVar()
        self.infecprob_entry = tkinter.Entry(self, textvariable=self.infecprob_pop)
        self.infecprob_entry.grid(column=1, row=4, sticky='EW')
        self.infecprob_pop.set(u"40")

        self.socialdis = tkinter.Label(self, text='Enter percent social distancing ')
        self.socialdis.grid(column=0, row=5, sticky='EW')
        self.socialdis_pop = tkinter.StringVar()
        self.socialdis_entry = tkinter.Entry(self, textvariable=self.socialdis_pop)
        self.socialdis_entry.grid(column=1, row=5, sticky='EW')
        self.socialdis_pop.set(u"0")


        self.button = tkinter.Button(self, text=u"Let's Go",
                                command=self.OnButtonClick)
        self.button.grid(column=2, row=2)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())

    def OnButtonClick(self):
        Master(self.pop_num.get(), self.dist_pop.get(), self.infec_pop.get(), self.nod_pop.get(),
               self.infecprob_pop.get(), self.socialdis_pop.get())
        print("Done")


if __name__ == "__main__":
    app = Pandemic(None)
    app.title('Pandemic')
    app.mainloop()


##########################################
## Trash code ##

# self.entryVariable = tkinter.StringVar()
# self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
# self.entry.grid(column=1, row=0, sticky='EW')
# self.entry.bind("<Return>", self.OnPressEnter)
# self.entryVariable.set(u"Enter text here.")

# def OnPressEnter(self, event):
#     self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)")
#     self.entry.focus_set()
#     self.entry.selection_range(0, tkinter.END)