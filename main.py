from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Bill_App:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1800x900+0+0")
		self.root.title("Billing Software")

		# Product Categories List
		self.Category 			= ["Select Options", "Clothing", "LifeStyle", "Mobiles"]
		self.SubCatClothing 	= ["Pant", "T-Shirt", "Shirt"]
		
		self.pant 				= ["Levis", "Mufti", "Spykar"]
		self.price_levis  = 5000
		self.price_mufti  = 7000
		self.price_spykar = 8000

		self.pant 				= ["Polo", "Roadster", "Jack&Jones"]
		self.price_polo      = 1500
		self.price_roadster  = 1800
		self.price_jackjones = 1700

		self.pant 				= ["Peter England", "Louis Phillipe", "Park Avenue"]
		self.price_peter  = 2100
		self.price_louis  = 2700
		self.price_park   = 1470
		
		self.SubCatLifeStyle 	= ["Bath Soap", "Face Cream", "Hair Oil"]
		self.Bath_soap 			= ["LifeBuy", "Lux", "Santoor", "Pearl"]
		self.price_life  	= 20
		self.price_lux  	= 20
		self.price_santoor  = 20
		self.price_garnier  = 30

		self.Bath_soap 			= ["Fair&Lovely", "Ponds", "Olay", "Garnier"]
		self.price_fair  	= 20
		self.price_ponds  	= 20
		self.price_olay     = 20
		self.price_pearl    = 30

		self.Bath_soap 			= ["Parachute", "Jashmin", "Bajaj"]
		self.price_para  	= 25
		self.price_jashmin  = 22
		self.price_bajaj    = 30

		self.SubCatMobiles 		= ["Iphone", "Sumsung", "Xiome", "RealMe", "One"]
		self.Bath_soap 			= ["Iphone_X", "Iphone_11", "Iphone_12"]
		self.price_ix  	        = 40000
		self.price_i11          = 60000
		self.price_i12          = 85000

		self.Bath_soap 	   = ["Sumsung M16", "Sumsung 12", "Sumsung 21"]
		self.price_sm16    = 16000
		self.price_sm12    = 12000
		self.price_sm21    = 18000

		self.Xiome 			= ["Red11", "Redme-12", "RedmePro"]
		self.price_r11  	= 11000
		self.price_r12      = 12000
		self.price_rpro     = 9000

		self.RealMe 		= ["RealMe 12", "RealMe 13", "Realme Pro"]
		self.price_rel12  	= 25000
		self.price_rel13    = 22000
		self.price_relpro   = 30000

		self.OnePlus 		= ["OnePlus1", "OnePlus2", "OnePlus3"]
		self.price_one1  	= 45000
		self.price_one2     = 60000
		self.price_one3     = 45800

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

		self.Combo_Category = ttk.Combobox(Product_Frame, font=("times new roman", 10, "bold"), width=24, state="readonly", value=self.Category)
		self.Combo_Category.current(0)
		self.Combo_Category.grid(row=0, column=1, stick=W, padx=5, pady=2)
		self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

		self.lbl_SubCategory = Label(Product_Frame, font=("times new roman", 12, "bold"), bg="white", text="Sub Category", bd=4)
		self.lbl_SubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.Combo_SubCategory = ttk.Combobox(Product_Frame, value=[""], font=("times new roman", 10, "bold"), width=24, state="readonly")
		self.Combo_SubCategory.grid(row=1, column=1, stick=W, padx=5, pady=2)
		self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.Product_add)

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

		# Image LabelFrame
		Image_Frame = Frame(Main_Frame, bd=10)
		Image_Frame.place(x=10, y=150, width=1290, height=455)

		image_1 = Image.open("images/image(3).jpg")
		image_1 = image_1.resize((640, 440), Image.ANTIALIAS)
		self.photoimage_1 = ImageTk.PhotoImage(image_1)

		lbl_image_1 = Label(Image_Frame, image=self.photoimage_1)
		lbl_image_1.place(x=0, y=0, width=640, height=440)

		image_2 = Image.open("images/image(4).jpg")
		image_2 = image_2.resize((640, 440), Image.ANTIALIAS)
		self.photoimage_2 = ImageTk.PhotoImage(image_2)

		lbl_image_2 = Label(Image_Frame, image=self.photoimage_2)
		lbl_image_2.place(x=642, y=0, width=630, height=440)

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
		Bill_Frame.place(x=1370, y=55, width=480, height=550)

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

		self.entry_subTotal = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=70)
		self.entry_subTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

		self.lbl_tax = Label(Bill_Counter_Frame, font=("times new roman", 12, "bold"), bg="white", text="Gov Tax", bd=4)
		self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

		self.txt_tax = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=70)
		self.txt_tax.grid(row=1, column=1, stick=W, padx=5, pady=2)

		self.lbl_amountTotal = Label(Bill_Counter_Frame, font=("times new roman", 12, "bold"), bg="white", text="Total", bd=4)
		self.lbl_amountTotal.grid(row=2, column=0, stick=W, padx=5, pady=2)

		self.txt_amountTotal = ttk.Entry(Bill_Counter_Frame, font=("times new roman", 10, "bold"), width=70)
		self.txt_amountTotal.grid(row=2, column=1, stick=W, padx=5, pady=2)

		# Button Frame
		Btn_Frame = Frame(Bill_Counter_Frame, bg="white")
		Btn_Frame.place(x=620, y=1)

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

	def Categories(self, event=""):
		if self.Combo_Category.get() == "Clothing":
			self.Combo_SubCategory.config(value=self.SubCatClothing)
			self.Combo_SubCategory.current(0)

		if self.Combo_Category.get() == "LifeStyle":
			self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
			self.Combo_SubCategory.current(0)

		if self.Combo_Category.get() == "Mobiles":
			self.Combo_SubCategory.config(value=self.SubCatMobiles)
			self.Combo_SubCategory.current(0)

	def Product_add(self, event=""):
		if self.Combo_SubCategory.get() == "Pant":
			self.Combo_Product.config(value=self.pant)
			self.Combo_Product.current(0)


if __name__ == '__main__':
	root = Tk()
	obj = Bill_App(root)
	root.mainloop()