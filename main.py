from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Bill_App:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1800x900+0+0")
		self.root.title("Billing Software")

		img = Image.open("images/image.jpg")
		img = img.resize((500, 130), Image.ANTIALIAS)
		self.photoimg = ImageTk.PhotoImage(img)

		lbl_img = Label(self.root, image=self.photoimg)
		lbl_img.place(x=0, y=0, width=500, height=130)

		img_1 = Image.open("images/image(1).jpg")
		img_1 = img_1.resize((500, 130), Image.ANTIALIAS)
		self.photoimg_1 = ImageTk.PhotoImage(img_1)

		lbl_img_1 = Label(self.root, image=self.photoimg_1)
		lbl_img_1.place(x=500, y=0, width=500, height=130)

		img_2 = Image.open("images/image(2).jpg")
		img_2 = img_2.resize((500, 130), Image.ANTIALIAS)
		self.photoimg_2 = ImageTk.PhotoImage(img_2)

		lbl_img_1 = Label(self.root, image=self.photoimg_2)
		lbl_img_1.place(x=1000, y=0, width=500, height=130)

		img_3 = Image.open("images/image(3).jpeg")
		img_3 = img_3.resize((500, 130), Image.ANTIALIAS)
		self.photoimg_3 = ImageTk.PhotoImage(img_3)

		lbl_img_3 = Label(self.root, image=self.photoimg_3)
		lbl_img_3.place(x=1500, y=0, width=500, height=130)

		lbl_title = Label(self.root, text="BILLING SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
		lbl_title.place(x=0, y=130, width=1950, height=45)

		Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
		Main_Frame.place(x=0, y=175, width=1950, height=620)

		Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
		Cust_Frame.place(x=10, y=5, width=350, height=140)

		self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white")
		self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

		self.entry_mob = ttk.Entry(Cust_Frame, text="Mobile No.", font=("times new roman", 10, "bold"), width=24)
		self.entry_mob.grid(row=0, column=1)

		self.lblCustName = Label(Cust_Frame ,text="Customer Name", font=("times new roman", 12, "bold"), bg="white", bd=4)
		self.lblCustName.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.txtCustName = ttk.Entry(Cust_Frame, text="", font=("arial", 10, "bold"), width=24)
		self.txtCustName.grid(row=1, column=1, stick=W, padx=5, pady=2)

		self.lblEmail = Label(Cust_Frame ,text="Email", font=("times new roman", 12, "bold"), bg="white", bd=4)
		self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

		self.txtEmail = ttk.Entry(Cust_Frame, text="", font=("arial", 10, "bold"), width=24)
		self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)



if __name__ == '__main__':
	root = Tk()
	obj = Bill_App(root)
	root.mainloop()