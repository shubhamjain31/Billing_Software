from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Bill_App:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1800x900+0+0")
		self.root.title("Billing Software")

		img = Image.open("images/b1.jpg")
		img = img.resize((500, 130), Image.ANTIALIAS)
		self.photoimg = ImageTk.PhotoImage(img)


if __name__ == '__main__':
	root = Tk()
	obj = Bill_App(root)
	root.mainloop()