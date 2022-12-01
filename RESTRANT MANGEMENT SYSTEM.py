from tkinter import*
from tkinter import ttk
from tkinter.font import Font
import mysql.connector as mc
from  tkinter import messagebox
import random
import time
from PIL import Image,ImageTk
import sqlite3


root=Tk()
root.geometry("1350x800")
root.config(bg="#FFE5B4")
root.title("Restaurant ")

############################################
def About_win():
    new_win=Toplevel(root)
    new_win.geometry('1350x800')
    new_win.config(bg="#FFE5B4")
    new_win.title("about")
    l1=Label(new_win,text="About...........................",font=("times",50),bg="#FFE5B4").place(x=10,y=100)
    l2=Label(new_win,text="Yummy Restaurant designed featuring a menu that changes daily with a focus on \nseasonal and local cusine.\nHere we concentrate on hygeinic and healthy food with less fat content.\nFOOD IS CULTURE,HABIT,CRAVING AND IDENTITY'.\n'FOOD MAY BE ESSENTIAL AS FUEL FOR THE BODY'.\n'BUT HEALTHY FOOD IS FUEL FOR THE SOUL'.\nPull up a chair.Take a taste.\n 'Come join us.Life is so endlessly delicious'.\nVisit Yummy restarunt will diffently get best experince.",font=60,bg="#FFE5B4").place(x=10,y=300)

    i=Image.open(r"C:/Users/Yamini/Pictures/crowne-plaza-jeddah-5499645385-2x1.jpg")
    i=i.resize((1000,800))
    new_win.photoi=ImageTk.PhotoImage(i)

    lbli=Label(new_win, image=new_win.photoi,bd=2,relief=RIDGE)
    lbli.place(x=800,y=0,width=1000,height=800)

    new_win.mainloop()
#######################################################################################    
def glary_win():  
    glary_win= Toplevel(root)
    glary_win.geometry("1350x800")
    glary_win.title("Gallery")
    glary_win.config(bg="#FFE5B4")
    l1=Label(glary_win,text="Gallery...........................",font=("times",30),bg="#FFE5B4").place(x=10,y=10)
    
    
    i=Image.open(r"C:\Users\Yamini\Pictures\cake.webp")
    i=i.resize((200,200))
    glary_win.photoi=ImageTk.PhotoImage(i)

    lbli=Label(glary_win,image=glary_win.photoi,bd=2,relief=RIDGE)
    lbli.place(x=30,y=80,width=200,height=200)

    i1=Image.open(r"C:\Users\Yamini\Pictures\maxresdefault.jpg")
    i1=i1.resize((200,200))
    glary_win.photoi1=ImageTk.PhotoImage(i1)
    
    lbli1=Label(glary_win,image=glary_win.photoi1,bd=2,relief=RIDGE)
    lbli1.place(x=30,y=400,width=200,height=200) 
    
    i2=Image.open(r"C:\Users\Yamini\Pictures\mil.jpg")
    i2=i2.resize((200,200))
    glary_win.photoi2=ImageTk.PhotoImage(i2)

    lbli2=Label(glary_win,image=glary_win.photoi2,bd=2,relief=RIDGE)
    lbli2.place(x=500,y=80,width=200,height=200)
    
    i3=Image.open(r"C:\Users\Yamini\Pictures\frit.jpg")
    i3=i3.resize((200,200))
    glary_win.photoi3=ImageTk.PhotoImage(i3)

    lbli=Label(glary_win,image=glary_win.photoi3,bd=2,relief=RIDGE)
    lbli.place(x=500,y=400,width=200,height=200)

    i4=Image.open(r"C:\Users\Yamini\Pictures\ca.jpg")
    i4=i4.resize((200,200))
    glary_win.photoi4=ImageTk.PhotoImage(i4)

    lbli4=Label(glary_win,image=glary_win.photoi4,bd=2,relief=RIDGE)
    lbli4.place(x=900,y=80,width=200,height=200)
    
    i5=Image.open(r"C:\Users\Yamini\Pictures\vv.jpg")
    i5=i5.resize((200,200))
    glary_win.photoi5=ImageTk.PhotoImage(i5)

    lbli5=Label(glary_win,image=glary_win.photoi5,bd=2,relief=RIDGE)
    lbli5.place(x=900,y=400,width=200,height=200)




    glary_win.mainloop()
    

    


###############################################################################

def menu_win():
    men_win=Toplevel(root)
    men_win.geometry('1550x1000')
    men_win.config(bg="black")
    men_win.title("Restaurant Home Page")
    l1=Label(men_win,text="                                                             Menu                                                                      ",font=("times",25),bg="black",fg="white").place(x=600,y=0,width=200)
    l2=Label(men_win,text="    Veg Starter ",font=("times",15),bg="red",fg="white").place(x=10,y=50)
    l3=Label(men_win,text="Chilli Pototo             40 ",font=("times",13),bg="black",fg="white").place(x=10,y=100)
    l4=Label(men_win,text="Massroom Chilli       50",font=("times",13),bg="black",fg="white").place(x=10,y=150)
    l5=Label(men_win,text="Baby Corn Chilli       50 ",font=("times",13),bg="black",fg="white").place(x=10,y=200)
    l6=Label(men_win,text="French Fries            60",font=("times",13),bg="black",fg="white").place(x=10,y=250)
    l7=Label(men_win,text="Gobi 65                    50",font=("times",13),bg="black",fg="white").place(x=10,y=300)

    l8=Label(men_win,text="      Veg Soup    ",font=("times",15),bg="red",fg="white").place(x=10,y=350)
    l9=Label(men_win,text="Tomoto Soup           60",font=("times",13),bg="black",fg="white").place(x=10,y=400)
    l11=Label(men_win,text="Veg Sweet Corn     70",font=("times",13),bg="black",fg="white").place(x=10,y=450)
    l12=Label(men_win,text="Masroom Soup      60",font=("times",13),bg="black",fg="white").place(x=10,y=500)

    l13=Label(men_win,text="    Non-Veg Soup    ",font=("times",15),bg="red",fg="white").place(x=10,y=550)
    l14=Label(men_win,text="Chicken Soup         120  ",font=("times",13),bg="black",fg="white").place(x=10,y=600)
    l15=Label(men_win,text="Matton Soup           160",font=("times",13),bg="black",fg="white").place(x=10,y=650)
    l16=Label(men_win,text="Chicken Hot&Sour   80     ",font=("times",13),bg="black",fg="white").place(x=10,y=700)

    l2=Label(men_win,text="    Main Veg Dishes        ",font=("times",15),bg="red",fg="white").place(x=600,y=50)
    l3=Label(men_win,text="Dal Fry                          150 ",font=("times",13),bg="black",fg="white").place(x=600,y=100)
    l4=Label(men_win,text="Masrrom Biryani           130",font=("times",13),bg="black",fg="white").place(x=600,y=150)
    l5=Label(men_win,text="Panner Rice                  140",font=("times",13),bg="black",fg="white").place(x=600,y=200)

    l2=Label(men_win,text="   Main Non-Veg Dishes    ",font=("times",15),bg="red",fg="white").place(x=600,y=250)
    l3=Label(men_win,text="Chicken Biryani             250 ",font=("times",13),bg="black",fg="white").place(x=600,y=300)
    l4=Label(men_win,text="Motton Biryani              350",font=("times",13),bg="black",fg="white").place(x=600,y=350)
   
    l2=Label(men_win,text="     Drinks                  ",font=("times",15),bg="red",fg="white").place(x=600,y=400)
    l3=Label(men_win,text="Soda Water                    30",font=("times",13),bg="black",fg="white").place(x=600,y=450)
    l4=Label(men_win,text="Fresh Juice                    60",font=("times",13),bg="black",fg="white").place(x=600,y=500)
    l5=Label(men_win,text="Organic Tea&Coffece    30",font=("times",13),bg="black",fg="white").place(x=600,y=550)
    l2=Label(men_win,text=" Milk Shakes                  45",font=("times",13),bg="black",fg="white").place(x=600,y=600)
    l3=Label(men_win,text="Soda Water                   25",font=("times",13),bg="black",fg="white").place(x=600,y=650)
    l4=Label(men_win,text="Fresh Juice                   35",font=("times",13),bg="black",fg="white").place(x=600,y=700)
  

    l2=Label(men_win,text="      Ice Creames    ",font=("times",15),bg="red",fg="white").place(x=1200,y=50)
    l3=Label(men_win,text="Vinilla                       100",font=("times",13),bg="black",fg="white").place(x=1200,y=100)
    l4=Label(men_win,text="Stoberry                   150",font=("times",13),bg="black",fg="white").place(x=1200,y=150)
    l5=Label(men_win,text="pista cream              140 ",font=("times",13),bg="black",fg="white").place(x=1200,y=200)


    l2=Label(men_win,text="      Cakes   ",font=("times",15),bg="red",fg="white").place(x=1200,y=250)
    l3=Label(men_win,text=" Red Velvet Cake        200",font=("times",13),bg="black",fg="white").place(x=1200,y=300)
    l4=Label(men_win,text="Rasamalai                   180",font=("times",13),bg="black",fg="white").place(x=1200,y=350)
    l5=Label(men_win,text="Stoberry                     200",font=("times",13),bg="black",fg="white").place(x=1200,y=400)


    men_win.mainloop()
################################################################################
###############################################################################

def ord_win():
    ord_win = Toplevel(root)
    ord_win.geometry("1700x800")
    ord_win.title("place order")
    ord_win.config(bg="blue")


    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

    # variables
    orderno = StringVar()
    roti = StringVar()
    biryani= StringVar()
    pista = StringVar()
    cakes= StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        # fetching the values from entry box
        order = (orderno.get())
        ro = float(roti.get())
        bi = float(biryani.get())
        pi = float(pista.get())
        ca = float(cakes.get())

        # computing the cost of items

        costro =ro* 240
        costbi = bi* 125
        costpi = pi * 80
        costca = ca * 60

        # computing the charges
        costofmeal = (costro + costbi + costpi + costca)
        ptax = ((costro+ costbi + costpi + costca) * 0.18)
        sub = (costro + costbi + costpi + costca)
        ser = ((costro + costbi + costpi + costca) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        # Displaying the values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    # defining reset function
    def reset():
        orderno.set("")
        roti.set("")
        biyani.set("")
        pista.set("")
        cakes.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    # defining exit function
    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(ord_win, bg="pink", width=1600, height=50)
    topframe.pack(side=TOP)

    # Leftframe
    leftframe = Frame(ord_win, width=900, height=700,bg='red')
    leftframe.pack(side=LEFT)

    # rightframe
    rightframe = Frame(ord_win, width=400, height=700,bg='red')
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",fg="black",rowheight=40,fieldbackground="orange")
    style.map('Treeview', background=[('selected', 'lightpink')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "ro", "bi", "pi", "ca", "ct", "sb", "tax", "sr", "tot")

    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("ro", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bi", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("pi", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("ca", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("ro", text="Roti", anchor=CENTER)
    my_tree.heading("bi", text="Biryani", anchor=CENTER)
    my_tree.heading("pi", text="Pista", anchor=CENTER)
    my_tree.heading("ca", text="Cakes", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    # defining add function to add record
    def add():
        Database()
        # getting  data
        orders = orderno.get()
        roti = roti.get()
        biryani = biryani.get()
        pista = pista.get()
        cake= drinks.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        services = service.get()
        totals = total.get()
        if orders == "" or pizzas == "" or burgers == "" or ices == "" or drinkss == "" or costs == "" or subtotals == "" or taxs == "" or services == "" or totals == "":
            messagebox.showinfo("Warning", "Please fill the empty field!")
        else:
            connectn.execute( 'INSERT INTO Restaurantrecords (ordno, ro, bi, pi ,ca ,ct ,sb ,tax, sr, tot) VALUES , (orders, roti, biyani, pista, cakes, costs, subtotals, taxs, services, totals)');
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        connectn.close()

    # defining function to access data from sqlite datrabase
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()

    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(topframe, font=('Calibri', 25, 'bold'), text="Food Orders", fg="red", anchor=W)
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(topframe, font=('Calibri', 15,), text=localtime, fg="black", anchor=W)
    main_lbl.grid(row=1, column=0)

    ### Labels
    # items
    ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black", bd=5, anchor=W,bg='pink').grid(row=1, column=0)
    ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=orderno).grid(row=1, column=1)
    
    rolbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Roti", fg="black", bd=5, anchor=W).grid(row=2 ,column=0)
    rotxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=roti).grid(row=2, column=1)
    
    birlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Biryani", fg="black", bd=5, anchor=W).grid(row=3,column=0)
    birtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=biryani).grid(row=3, column=1)

   
    pislbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="pista", fg="black", bd=5, anchor=W).grid(row=4,column=0)
    pistxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=pista).grid(row=4, column=1)
   
    calbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="cakes", fg="black", bd=5, anchor=W).grid(row=5,column=0)
    catxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=cakes).grid(row=5, column=1)
    
    costlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", bd=5, anchor=W).grid(row=6, column=0)
    costtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=cost).grid(row=6, column=1)
    # subtotal
    sublbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Subtotal", bd=5, anchor=W).grid(row=7, column=0)
    subtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=subtotal).grid(row=7, column=1)
    # tax
    taxlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Tax", bd=5, anchor=W).grid(row=8, column=0)
    taxtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=tax).grid(row=8, column=1)
    # service
    servicelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Service", bd=5, anchor=W).grid(row=9,column=0)
    servicetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=service).grid(row=9, column=1)
    # total
    totallbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Total", bd=5, anchor=W).grid(row=10, column=0)
    totaltxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=total).grid(row=10, column=1)
    # ---button--


    totbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Total", bg="Lightgrey", fg="black", bd=3, padx=5, pady=5,width=6, command=tottal).grid(row=6, column=3)

    resetbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=3, padx=5,pady=5, width=6, command=reset).grid(row=4, column=3)

    exitbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Exit The System", bg="lightgrey", fg="black", bd=3, padx=5,pady=5, width=12, command=exit).grid(row=6, column=2)

    addbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Add", bg="lightgrey", fg="black", bd=3, padx=5, pady=5,width=6, command=add).grid(row=2, column=3)

    deletebtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Delete Record", bg="lightgrey", fg="black", bd=3,padx=5, pady=5, width=12, command=Delete).grid(row=4, column=2)

    ########################### feedback form ################################

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Submit Feedback form")
        feed.config(bg='red')
        # database #
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
        # variables
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # submit function####################################################################
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Restaurant.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # cancel button##############################################################
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("times", 15, "bold"), text="Thanks for Visiting!", fg="black",).pack(side=TOP)
        lbl2 = Label(feed, font=("times", 15), text="We're glad you chose us ! Please tell us how it was!",fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('times', 15), text="Name:-", fg="grey", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('times', 15), bd=6, insertwidth=2, bg="white", justify='right', textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('times', 15), text="Email:-", fg="grey", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('times', 15), bd=6, insertwidth=2, bg="white", justify='right', textvariable=email).place(x=285, y=185)
        ###checkbutton###################
        ratelbl = Label(feed, font=('times', 15), text="How would you rate us?", fg="grey", bd=10, anchor=W).place( x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('times', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('times', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('times', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('times', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        # comments"
        commentslbl = Label(feed, font=('times', 15), text="Comments", fg="grey", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("times", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(x=145, y=430)
        cancel = Button(feed, font=("times", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(x=245, y=430)
        feed.mainloop()

    # Feedbackbutton
    feedbtn = Button(leftframe, font=('times', 16, 'bold'), text="Feedback Form", fg="black", bg="lightgrey", bd=3, padx=10, pady=10, width=10, command=feedbackk).grid(row=8, column=2, columnspan=1)

    ##################### Menu card ################################
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x300")
        lblinfo = Label(root, font=("calibri", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(root, font=("Calibri", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblpizza = Label(roott, font=("Calibri", 20, "bold"), text="roti", fg="Blue", bd=10)
        lblpizza.grid(row=1, column=0)
        lblpricep = Label(roott, font=("Calibri", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpricep.grid(row=1, column=3)
        lblburger = Label(roott, font=("Calibri", 20, "bold"), text="biryani", fg="Blue", bd=10)
        lblburger.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Calibri", 20, "bold"), text="155/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lblicecream = Label(roott, font=("Calibri", 20, "bold"), text="pista", fg="Blue", bd=10)
        lblicecream.grid(row=4, column=0)
        lblpricei = Label(roott, font=("Calibri", 20, "bold"), text="80/-", fg="blue", bd=10)
        lblpricei.grid(row=4, column=3)
        lbldrinks = Label(roott, font=("Calibri", 20, "bold"), text="cakes", fg="Blue", bd=10)
        lbldrinks.grid(row=5, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpriced.grid(row=5, column=3)
        roott.mainloop()
    # menubutton
    menubtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Menu Card", bg="lightgrey", fg="black", bd=3, padx=6,pady=6, width=12, command=menu).grid(row=2, column=2)

    ord_win.mainloop()


    
##########################################################################################

t1=Label(root,text="Yummy Restaurant",font=("times",25,"bold"),bg="black",fg="gold",anchor="center",padx=10)
t1.place(x=0,y=0,relwidth=1,height=70)

clck=Label(root,text=" Welcom To My Yummy Restarunt                                 Mon-Sat:11AM-11PM",font=("times",15,"bold"),bg="orange",fg="black")
clck.place(x=0,y=70,relwidth=1,height=40)


f1=Frame(root,bd=4,relief=RIDGE)
f1.place(x=0,y=110,width=230,height=40)

m1=Frame(root,bd=2,relief=RIDGE,bg="black")
m1.place(x=0,y=310,width=230,height=550)

b2=Frame(m1,bd=4,relief=RIDGE)
b2.place(x=0,y=38,width=230)

t2=Label(m1,text="Home ", font=("times",15,"bold"),bg="black",fg="gold",bd=2)
t2.place(x=0,y=0,width=230)


b3=Button(b2, text="About",width="20",font=("times",15,"bold"),bg="black",fg="gold",bd=4,command=About_win)
b3.grid(row=1,column=0)

b4=Button(b2, text="Menu",width="20",font=("times",15,"bold"),bg="black",fg="gold",bd=4,command=menu_win)
b4.grid(row=2,column=0)

b5=Button(b2, text="Place Order",width="20",font=("times",15,"bold"),bg="black",fg="gold",bd=4,comman=ord_win)
b5.grid(row=3,column=0)

b7=Button(b2, text="Gallery",width="20",font=("times",15,"bold"),bg="black",fg="gold",bd=4,command=glary_win)
b7.grid(row=5,column=0)

i1=Image.open(r"C:/Users/Yamini/Pictures/cake.webp")
i1=i1.resize((230,200))
root.photoi1=ImageTk.PhotoImage(i1)

lbli1=Label(root, image=root.photoi1,bd=2,relief=RIDGE)
lbli1.place(x=0,y=110,width=230,height=200)

i2=Image.open(r"C:/Users/Yamini/Pictures/plates.jpg")
i2=i2.resize((1350,750))     
root.photoi2=ImageTk.PhotoImage(i2)

lbli2=Label(root, image=root.photoi2,bd=2,relief=RIDGE)
lbli2.place(x=230,y=110,width=1350,height=750)


i3=Image.open(r"C:\Users\Yamini\Pictures\photo.jpg")
i3=i3.resize((230,200))
root.photoi3=ImageTk.PhotoImage(i3)

lbli3=Label(root,image=root.photoi3,bd=2)
lbli3.place(x=0,y=520,width=230,height=206)
                         
footer=Label(root,text="Restaurant Management System | Developed by YAMINI.L\n For Any Enquires Contact:6304401242",font=("times",15,"bold"),bg="black",fg="gold")
footer.place(x=0,y=753,relwidth=1)



root.mainloop()
 
 
