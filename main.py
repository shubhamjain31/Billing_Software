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
		Main_Frame.place(x=0, y=175, width=1950, height=800)

		# Customer LabelFrame
		Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
		Cust_Frame.place(x=10, y=5, width=550, height=140)

		self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white")
		self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

		self.entry_mob = ttk.Entry(Cust_Frame, text="Mobile No.", font=("times new roman", 10, "bold"), width=54)
		self.entry_mob.grid(row=0, column=1)

		self.lblCustName = Label(Cust_Frame ,text="Customer Name", font=("times new roman", 12, "bold"), bg="white", bd=4)
		self.lblCustName.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.txtCustName = ttk.Entry(Cust_Frame, text="", font=("arial", 10, "bold"), width=54)
		self.txtCustName.grid(row=1, column=1, stick=W, padx=5, pady=2)

		self.lblEmail = Label(Cust_Frame ,text="Email", font=("times new roman", 12, "bold"), bg="white", bd=4)
		self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

		self.txtEmail = ttk.Entry(Cust_Frame, text="", font=("arial", 10, "bold"), width=54)
		self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)

		# Product LabelFrame
		Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white", fg="red")
		Product_Frame.place(x=620, y=5, width=680, height=140)

		self.lbl_Category = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Select Categories", bd=4)
		self.lbl_Category.grid(row=0, column=0, stick=W, padx=5, pady=2)

		self.Combo_Category = ttk.Combobox(Product_Frame, font=("times new roman", 10, "bold"), width=24, state="readonly")
		self.Combo_Category.grid(row=0, column=1, stick=W, padx=5, pady=2)

		self.lbl_SubCategory = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Sub Category", bd=4)
		self.lbl_SubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.Combo_SubCategory = ttk.Combobox(Product_Frame, font=("times new roman", 10, "bold"), width=24, state="readonly")
		self.Combo_SubCategory.grid(row=1, column=1, stick=W, padx=5, pady=2)

		self.lbl_product = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Product Name", bd=4)
		self.lbl_product.grid(row=2, column=0, stick=W, padx=5, pady=2)

		self.Combo_Product = ttk.Combobox(Product_Frame, font=("times new roman", 10, "bold"), width=24, state="readonly")
		self.Combo_Product.grid(row=2, column=1, stick=W, padx=5, pady=2)

		self.lbl_price = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Price", bd=4)
		self.lbl_price.grid(row=0, column=2, stick=W, padx=5, pady=2)

		self.Combo_Price = ttk.Combobox(Product_Frame, font=("times new roman", 10, "bold"), width=24, state="readonly")
		self.Combo_Price.grid(row=0, column=3, stick=W, padx=5, pady=2)

		self.lbl_qty = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Quality", bd=4)
		self.lbl_qty.grid(row=1, column=2, stick=W, padx=5, pady=2)

		self.entry_qty = ttk.Entry(Product_Frame, font=("times new roman", 10, "bold"), width=26)
		self.entry_qty.grid(row=1, column=3, stick=W, padx=1)

		# Search LabelFrame
		Search_Frame = Frame(Main_Frame, bg="white", bd=2)
		Search_Frame.place(x=1370, y=15, width=480, height=570)

		self.lbl_bill = Label(Search_Frame, font=("arial", 12, "bold"), bg="red", fg="white", text="Bill Number")
		self.lbl_bill.grid(row=0, column=0, stick=W, padx=5, pady=2)

		self.txt_entry_search = ttk.Entry(Search_Frame, font=("arial", 10, "bold"), width=40)
		self.txt_entry_search.grid(row=0, column=1, stick=W, padx=2)

		self.btn_search = Button(Search_Frame, text="Search", font=("arial", 10, "bold"), bg="orangered", fg="white", bd=2, width=8, cursor="hand2")
		self.btn_search.grid(row=0, column=3)

		# Bill LabelFrame
		Bill_Frame = LabelFrame(Main_Frame, text="Bill Area", font=("times new roman", 12, "bold"), bg="white", fg="red")
		Bill_Frame.place(x=1370, y=55, width=480, height=570)

		scroll_y = Scrollbar(Bill_Frame, orient=VERTICAL)
		self.textarea = Text(Bill_Frame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("times new roman", 12, "bold"))
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=self.textarea.yview)
		self.textarea.pack(fill=BOTH, expand=1)

		# Bill Count LabelFrame
		Bill_Counter_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white", fg="red")
		Bill_Counter_Frame.place(x=0, y=615, width=1850, height=125)

		self.lbl_subTotal = Label(Bill_Counter_Frame, font=("times new roman", 12, "bold"), bg="white", text="Sub Total", bd=4)
		self.lbl_subTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

		self.entry_subTotal = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=24)
		self.entry_subTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

		self.lbl_tax = Label(Bill_Counter_Frame, font=("times new roman", 12, "bold"), bg="white", text="Gov Tax", bd=4)
		self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.txt_tax = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=24)
		self.txt_tax.grid(row=1, column=1, stick=W, padx=5, pady=2)

		self.lbl_amountTotal = Label(Bill_Counter_Frame, font=("times new roman", 12, "bold"), bg="white", text="Total", bd=4)
		self.lbl_amountTotal.grid(row=2, column=0, stick=W, padx=5, pady=2)

		self.txt_amountTotal = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=24)
		self.txt_amountTotal.grid(row=2, column=1, stick=W, padx=5, pady=2)

		# Button Frame
		Btn_Frame = Frame(Bill_Counter_Frame, bg="white")
		Btn_Frame.place(x=320, y=0)

		self.btn_add_to_cart = Button(Btn_Frame, text="Add To Cart", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_add_to_cart.grid(row=0, column=0)

		self.btn_generate_bill = Button(Btn_Frame, text="Generate Bill", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_generate_bill.grid(row=0, column=1)

		self.btn_save = Button(Btn_Frame, text="Save Bill", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_save.grid(row=0, column=2)

		self.btn_print = Button(Btn_Frame, text="Print", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_print.grid(row=0, column=3)

		self.btn_clear = Button(Btn_Frame, text="Cler", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_clear.grid(row=0, column=4)

		self.btn_exit = Button(Btn_Frame, text="Exit", font=("arial", 15, "bold"), bg="orangered", fg="white", bd=4, height=2, width=15, cursor="hand2")
		self.btn_exit.grid(row=0, column=5)


if __name__ == '__main__':
	root = Tk()
	obj = Bill_App(root)
	root.mainloop()