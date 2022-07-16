import tkinter as tk
from itertools import cycle


class App(tk.Tk):
    def __init__(self, image_files, x, y, delay):
        tk.Tk.__init__(self)

        self.geometry('+{}+{}' .format(x, y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_delay = tk.Label(self)
        self.picture_delay.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_delay.config(image=img_object)

        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set time in milliseconds b/w slides
delay = 4000
image_files = [
    "p.gif",
    "p1.gif",
    "p2.gif",
    "p3.gif",
    "p4.gif",
    "p5.gif",
    "p6.gif",
]
x = 700
y = 350
app = App(image_files, x, y, delay)
app.show_slides()
app.run()
