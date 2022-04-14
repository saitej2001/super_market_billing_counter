from tkinter import *
import math,random
import sys
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Bill Software")
        bg_color = "#123456"
        title = Label(self.root, text="Bill Software", bd=12, bg=bg_color, fg="white", relief=GROOVE,
                      font=("arial", 25, "bold"), pady=10).pack(fill=X)

        # variables
        self.soap = IntVar()
        self.rice = IntVar()
        self.biscuit = IntVar()
        self.shampoo = IntVar()
        self.hairgell = IntVar()
        self.oil = IntVar()
        self.dall = IntVar()
        self.sprit = IntVar()
        self.greentea = IntVar()
        self.sugar = IntVar()
        self.wheat = IntVar()
        self.thumsup = IntVar()
        self.redbull = IntVar()
        self.beer = IntVar()
        self.paperboat = IntVar()

        self.TotalCosmeticsprice = StringVar()
        self.TotalGroceryPrice = StringVar()
        self.Totalcolddrinkprice = StringVar()
        self.totalcoasmetictax = StringVar()
        self.totalgrocerytax = StringVar()
        self.colddrinktax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.Search = StringVar()

        F1 = LabelFrame(self.root, text="Costumer details:", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=100, relwid=1)

        cname_lbl = Label(F1, text="Costumer Name:", relief=GROOVE, font=("arial", 20, "bold"), fg="red",
                          bg=bg_color).grid(row=0, column=3, padx=2, pady=2)
        cname_txt = Entry(F1, width=14, textvariable=self.c_name, font=("arial", 23, "bold"), bd=7).grid(row=0,
                                                                                                         column=5,
                                                                                                         pady=7)

        cphn_lable = Label(F1, text="Cos_Mobile No:", bg=bg_color, fg="red", relief=GROOVE,
                           font=("times new roman", 20, "normal")).grid(row=0, column=7, pady=7, padx=2)
        cphn_txt = Entry(F1, font=("times new roman", 23, "normal"), textvariable=self.c_phone, width=14, bd=7).grid(
            row=0, column=9)

        billno_lable = Label(F1, text="BILL NO:", font=("times new roman", 20, "bold"), fg="red", bg=bg_color,
                             relief=GROOVE).grid(row=0, column=11, padx=2, pady=2)
        billno_txt = Entry(F1, font=("times new roman", 23, "bold"), textvariable=self.Search, width=14, bd=7).grid(
            row=0, column=13)

        search_btn = Button(F1, text="Search", width=14, bd=7, font=("times new roman", 16)).grid(row=0, column=19,
                                                                                                  padx=20)

        # cosmetics
        F2 = LabelFrame(self.root, bd=10, bg=bg_color, relief=GROOVE, text="Cosmetics",
                        font=("times new roman", 15, "bold"), pady=5, fg="gold")
        F2.place(x=5, y=190, width=380, height=350)

        _lbl = Label(F2, text="Bath Soap", font=("times new roman", 20, "normal"), fg="lightgreen", bg=bg_color).grid(
            row=7, column=3)
        bath_txt = Entry(F2, font=("times new roman", 19), textvariable=self.soap, width=7, bd=5).grid(row=7, column=5)

        rice_lable = Label(F2, text="Rice", font=("times new roman", 20, "normal"), fg="lightgreen", bg=bg_color).grid(
            row=9, column=3, pady=15)
        rice_txt = Entry(F2, font=("times new roman", 19), textvariable=self.rice, width=7, bd=5).grid(row=9, column=5)

        bis_lable = Label(F2, text="Biscuit", font=("times new roman", 20, "normal"), fg="lightgreen",
                          bg=bg_color).grid(row=11, column=3, pady=8)
        bis_txt = Entry(F2, font=("times new roman", 19), textvariable=self.biscuit, width=7, bd=5).grid(row=11,
                                                                                                         column=5,
                                                                                                         pady=9)

        shampoo_lable = Label(F2, text="Shampoo", font=("times new roman", 20, "normal"), fg="lightgreen",
                              bg=bg_color).grid(row=13, column=3, pady=8)
        shampoo_txt = Entry(F2, font=("times new roman", 19), textvariable=self.shampoo, width=7, bd=5).grid(row=13,
                                                                                                             column=5,
                                                                                                             pady=9)

        hAIR_lable = Label(F2, text="Hair gell", font=("times new roman", 20, "normal"), fg="lightgreen",
                           bg=bg_color).grid(row=15, column=3, pady=8)
        hAIR_txt = Entry(F2, font=("times new roman", 19), textvariable=self.hairgell, width=7, bd=5).grid(row=15,
                                                                                                           column=5,
                                                                                                           pady=9)

        F3 = LabelFrame(self.root, bd=10, bg=bg_color, relief=GROOVE, text="Grocery",
                        font=("times new roman", 15, "bold"), pady=5, fg="gold")
        F3.place(x=400, y=190, width=380, height=350)

        oil_lbl = Label(F3, text="oil", font=("times new roman", 20, "normal"), fg="lightgreen", bg=bg_color).grid(
            row=7, column=3)
        oil_txt = Entry(F3, font=("times new roman", 19), textvariable=self.oil, width=7, bd=5).grid(row=7, column=5)

        dall_lable = Label(F3, text="Daal", font=("times new roman", 20, "normal"), fg="lightgreen", bg=bg_color).grid(
            row=9, column=3, pady=15)
        dall_txt = Entry(F3, font=("times new roman", 19), textvariable=self.dall, width=7, bd=5).grid(row=9, column=5)

        wheat_lable = Label(F3, text="Wheat", font=("times new roman", 20, "normal"), fg="lightgreen",
                            bg=bg_color).grid(row=11, column=3, pady=8)
        wheat_txt = Entry(F3, font=("times new roman", 19), textvariable=self.wheat, width=7, bd=5).grid(row=11,
                                                                                                         column=5,
                                                                                                         pady=9)

        greentea_lable = Label(F3, text="greentea", font=("times new roman", 20, "normal"), fg="lightgreen",
                               bg=bg_color).grid(row=13, column=3, pady=8)
        greentea_txt = Entry(F3, font=("times new roman", 19), textvariable=self.greentea, width=7, bd=5).grid(row=13,
                                                                                                               column=5,
                                                                                                               pady=9)

        sugar_lable = Label(F3, text="sugar", font=("times new roman", 20, "normal"), fg="lightgreen",
                            bg=bg_color).grid(row=15, column=3, pady=8)
        sugar_txt = Entry(F3, font=("times new roman", 19), textvariable=self.sugar, width=7, bd=5).grid(row=15,
                                                                                                         column=5,
                                                                                                         pady=9)

        # Cool drink
        F4 = LabelFrame(self.root, bd=10, bg=bg_color, relief=GROOVE, text="COOL DRINK",
                        font=("times new roman", 15, "bold"), pady=5, fg="gold")
        F4.place(x=800, y=190, width=380, height=350)

        sprit_lbl = Label(F4, text="Sprit", font=("times new roman", 20, "normal"), fg="lightgreen", bg=bg_color).grid(
            row=7, column=3)
        sprit_txt = Entry(F4, font=("times new roman", 19), textvariable=self.sprit, width=7, bd=5).grid(row=7,
                                                                                                         column=5)

        thumsup_lable = Label(F4, text="Thumsup", font=("times new roman", 20, "normal"), fg="lightgreen",
                              bg=bg_color).grid(row=9, column=3, pady=15)
        thumsup_txt = Entry(F4, font=("times new roman", 19), textvariable=self.thumsup, width=7, bd=5).grid(row=9,
                                                                                                             column=5)

        redbull_lable = Label(F4, text="RedBull", font=("times new roman", 20, "normal"), fg="lightgreen",
                              bg=bg_color).grid(row=11, column=3, pady=8)
        redbull_txt = Entry(F4, font=("times new roman", 19), textvariable=self.redbull, width=7, bd=5).grid(row=11,
                                                                                                             column=5,
                                                                                                             pady=9)

        Beer_lable = Label(F4, text="BEER", font=("times new roman", 20, "normal"), fg="lightgreen",
                           bg=bg_color).grid(row=13, column=3, pady=8)
        Beer_txt = Entry(F4, font=("times new roman", 19), textvariable=self.beer, width=7, bd=5).grid(row=13, column=5,
                                                                                                       pady=9)

        paperboat_lable = Label(F4, text="Paper Boat", font=("times new roman", 20, "normal"), fg="lightgreen",
                                bg=bg_color).grid(row=15, column=3, pady=8)
        paperboat_txt = Entry(F4, font=("times new roman", 19), textvariable=self.paperboat, width=7, bd=5).grid(row=15,
                                                                                                                 column=5,
                                                                                                                 pady=9)

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1190, y=190, width=340, height=350)
        billtitle = Label(F5, text="Bill Area", bg=bg_color, fg="gold", font=("times new roman", 18, "normal"), bd=7,
                          relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        F6 = LabelFrame(self.root, bd=10, bg=bg_color, relief=GROOVE, text="Bill menu",
                        font=("times new roman", 15, "bold"), pady=5, fg="gold")
        F6.place(x=0, y=560, relwid=1, height=220)

        cos_bill_lbl = Label(F6, text=" Total Cosmetics price", fg="gold", bg=bg_color,
                             font=("times new roman", 15, "bold")).grid(row=20, column=3, sticky="w")
        cos_bill_txt = Entry(F6, font=("times new roman", 15, "normal"), textvariable=self.TotalCosmeticsprice,
                             width=20, bd=7, relief=GROOVE).grid(row=20, column=5, padx=15, pady=15)

        gro_bill_lbl = Label(F6, text=" Total Grocery Price", fg="gold", bg=bg_color,
                             font=("times new roman", 15, "bold")).grid(row=23, column=3, pady=12, sticky="w")
        gro_bill_txt = Entry(F6, font=("times new roman", 15, "normal"), textvariable=self.TotalGroceryPrice, width=20,
                             bd=7, relief=GROOVE).grid(row=23, column=5, padx=15)

        cold_bill_lbl = Label(F6, text=" Total Cold drink price", fg="gold", bg=bg_color,
                              font=("times new roman", 15, "bold")).grid(row=25, column=3, pady=12, sticky="w")
        cold_bill_txt = Entry(F6, font=("times new roman", 15, "normal"), textvariable=self.Totalcolddrinkprice,
                              width=20, bd=7, relief=GROOVE).grid(row=25, column=5, padx=15)

        cost_lbl = Label(F6, text="Cosmetic Tax", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(
            row=20, column=8)
        cost_txt = Entry(F6, font=("times new roman", 15, "bold"), textvariable=self.totalcoasmetictax, bd="7",
                         relief=GROOVE, width=20).grid(row=20, column=10, padx=15, pady=10, sticky="w")

        gro_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(
            row=23, column=8)
        gro_txt = Entry(F6, font=("times new roman", 15, "bold"), bd="7", width=20, textvariable=self.totalgrocerytax,
                        relief=GROOVE).grid(row=23, column=10, padx=15, sticky="w")

        cool_lbl = Label(F6, text="Cool drink tax", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(
            row=25, column=8)
        cool_txt = Entry(F6, font=("times new roman", 15, "bold"), bd="7", width=20, textvariable=self.colddrinktax,
                         relief=GROOVE).grid(row=25, column=10, padx=15, pady=1, sticky="w")

        c = Frame(F6, relief=GROOVE, bg=bg_color, padx=20)
        c.place(x=820, width=677, height=180)

        Tot_btn = Button(F6, command=self.total, text="TOTAL", font=("times new roman", 15, "normal"), bd=7, fg="gold",
                         bg="black").grid(row=20, column=20, padx=20, pady=10)
        Tot_btn = Button(F6, text="Generate bill",command=self.bill_area, font=("times new roman", 15, "normal"), bd=7, fg="gold",
                         bg="black").grid(row=20, column=25, padx=20, pady=10)
        Tot_btn = Button(F6, text="Clear", font=("times new roman", 20, "normal"), bd=7, fg="gold", bg="black").grid(
            row=20, column=35, padx=20, pady=10)
        Tot_btn = Button(F6, text="EXIT", font=("times new roman", 15, "normal"), bd=7, fg="gold", bg="black").grid(
            row=20, column=45, padx=20, pady=10)
        Tot_btn = Button(F6, text="Print", font=("times new roman", 15, "normal"), bd=7, fg="gold", bg="black").grid(
            row=20, column=55, padx=20, pady=10)

        t_lab = Label(F6, text="THANK U!!!!!", fg="gold", font=("times new roman", 20, "normal"), bg=bg_color).place(
            x=900, y=100, width=500)
        self.welcome_bill()

    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_r_p=  self.rice.get() * 15
        self.c_b_p = self.biscuit.get() * 12
        self.c_sha_p = self.shampoo.get() * 20
        self.c_hg_p = self.hairgell.get() * 60


        self.total_cosmetic_price = float(
            (self.c_s_p) +
            (self.c_r_p) +
            (self.c_b_p) +
            (self.c_sha_p) +
            (self.c_hg_p)
        )
        self.TotalCosmeticsprice.set("Rs. "+str(round(self.total_cosmetic_price)))

        self.c_o_p = self.oil.get() * 40
        self.c_da_p = self.dall.get() * 12
        self.c_w_p = self.wheat.get() * 12
        self.c_gt_p = self.greentea.get() * 12
        self.c_su_p = self.sugar.get() * 12



        self.total_grocery_price = float(
            (self.c_s_p) +
            (self.c_r_p) +
            (self.c_b_p) +
            (self.c_sha_p) +
            (self.c_hg_p)
        )

        self.TotalGroceryPrice.set("Rs. "+str(round(self.total_grocery_price)))

        self.c_sp_p = self.sprit.get() * 40
        self.c_th_p = self.thumsup.get() * 110
        self.c_be_p = self.beer.get() * 120
        self.c_pa_p = self.paperboat.get() * 12
        self.c_re_p = self.redbull.get() * 12

        self.total_cold_drink_price = float(
            (self.c_sp_p) +
            (self.c_th_p) +
            (self.c_be_p) +
            (self.c_pa_p) +
            (self.c_re_p)
        )


        self.Totalcolddrinkprice.set("Rs. "+str(round(self.total_cold_drink_price)))

        self.c_sp_p = self.sprit.get() * 40
        self.c_th_p = self.thumsup.get() * 120
        self.c_be_p = self.beer.get() * 150
        self.c_pa_p = self.paperboat.get() * 12
        self.c_re_p = self.redbull.get() * 150

        #taxes

        self.c_s_p = self.soap.get() * 0.5
        self.c_r_p = self.rice.get() * 0.9
        self.c_b_p = self.biscuit.get() * 0.3
        self.c_sha_p = self.shampoo.get() * 0.6
        self.c_hg_p = self.hairgell.get() * 5

        self.cosmetic_tax =float(
            (self.c_s_p) +
            (self.c_r_p) +
            (self.c_b_p) +
            (self.c_sha_p) +
            (self.c_hg_p)
        )

        self.totalcoasmetictax.set("Rs. "+str(round(self.cosmetic_tax)))

        self.totalgrocerystax = float(
            (self.oil.get() * 0.2) +
            (self.dall.get() * 0.1) +
            (self.wheat.get() * 0.6) +
            (self.greentea.get() * 6) +
            (self.sugar.get() * 3)

        )

        self.totalgrocerytax.set("Rs. "+str(round(self.totalgrocerystax)))

        self.cod_tax = float(
            (self.sprit.get() * 0.9) +
            (self.thumsup.get() * 1.2) +
            (self.beer.get() * 2) +
            (self.paperboat.get() * 0.1)
        )

        self.colddrinktax.set("Rs. "+str(round(self.cod_tax)))

        self.Total_bill=float(
                              self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price
                              )
        self.Total_saved=str(
            self.cosmetic_tax+
            self.totalgrocerystax+
            self.cod_tax
        )


    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tGanesh Super market")
        self.txtarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCostumer Name:{self.c_name.get()}" )
        self.txtarea.insert(END, f"\nPhone number:{self.c_phone.get()} ")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\t product \t\t Qty \t   Price")
        self.txtarea.insert(END, f"\n=====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Please Enter Costumer Details ")


        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t {self.soap.get()}\t   {self.c_s_p}")
            if self.rice.get()!=0:
                self.txtarea.insert(END, f"\n Rice\t\t {self.rice.get()}\t   {self.c_r_p}")
            if self.biscuit.get()!=0:
                self.txtarea.insert(END, f"\n Biscuit\t\t {self.biscuit.get()}\t   {self.c_b_p}")
            if self.shampoo.get()!=0:
                self.txtarea.insert(END, f"\n Shampoo\t\t {self.shampoo.get()}\t   {self.c_sha_p}")
            if self.oil.get()!=0:
                self.txtarea.insert(END, f"\n oil\t\t {self.oil.get()}\t   {self.c_o_p} ")
            if self.dall.get()!=0:
                self.txtarea.insert(END, f"\n dall\t\t {self.dall.get()}\t   {self.c_da_p} ")
            if self.wheat.get()!=0:
                self.txtarea.insert(END, f"\n wheat\t\t {self.wheat.get()}\t   {self.c_w_p} ")
            if self.greentea.get()!=0:
                self.txtarea.insert(END, f"\n greentea\t\t {self.greentea.get()}\t   {self.c_gt_p} ")
            if self.sugar.get()!=0:
                self.txtarea.insert(END, f"\n sugar\t\t {self.sugar.get()}\t   {self.c_su_p} ")
            if self.sprit.get()!=0:
                self.txtarea.insert(END, f"\n sprit\t\t {self.sprit.get()}\t   {self.c_sp_p} ")
            if self.thumsup.get()!=0:
                self.txtarea.insert(END, f"\n thumsup\t\t {self.thumsup.get()}\t   {self.c_th_p} ")
            if self.beer.get()!=0:
                self.txtarea.insert(END, f"\n beer\t\t {self.beer.get()}\t   {self.c_be_p} ")
            if self.paperboat.get()!=0:
                self.txtarea.insert(END, f"\n paper boat\t\t {self.paperboat.get()}\t   {self.c_pa_p} ")

            self.txtarea.insert(END, f"\n_____________________________________")
            self.txtarea.insert(END,f"\n  Total bill \t\t\tRs:{self.Total_bill}")
            self.txtarea.insert(END, f"\n_____________________________________")
            self.txtarea.insert(END,f"\n ------You have Saved money------")
            self.txtarea.insert(END,f"\n Total Saved \t\t\tRs:{self.Total_saved}")
            self.txtarea.insert(END,f"\n --------Thank you Visit again-------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to print the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("saiteja vs code"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.{self.bill_no.get()},Saved Succesfully")
        else:
            return


root = Tk()
obj = Bill_App(root)
root.mainloop()