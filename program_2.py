# Program 2
# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output

import customtkinter
from tkinter import *
from tkinter import simpledialog
from PIL import ImageTk, Image

def buy_fruits():
    def result_purchase():
        if(check_var.get() == 1):
            amount_apples = simpledialog.askinteger("Apples", "At what price do you want to buy the apples?", parent=store_window)
            apples_price = amount_apples
            
            amount_money = simpledialog.askinteger("Money", "How much money do you have?", parent=store_window)
            available_money = amount_money

            max_apples = available_money // apples_price
            remaining_money = available_money % apples_price

            result_name = customtkinter.CTkLabel(reciept_frame, text=f"   Name: {name_entry.get()}")
            result_name.configure(font = font3, text_color='#FFFFFF', bg_color = '#808080')
            result_name.place(relx=0/600, rely=90/700)

            result_price = customtkinter.CTkLabel(reciept_frame, text=f"   Price per piece: ₱{apples_price}")
            result_price.configure(font = font3, text_color='#FFFFFF', bg_color = '#808080')
            result_price.place(relx=0/600, rely= 130/700)

            result_total = customtkinter.CTkLabel(reciept_frame, text=f"   Total Apples: {max_apples}")
            result_total.configure(font = font3, text_color='#FFFFFF', bg_color = '#808080')
            result_total.place(relx=0/600, rely=170/700)

            result_money = customtkinter.CTkLabel(reciept_frame, text=f"   Money Recieved: ₱{available_money}")
            result_money.configure(font = font3, text_color='#FFFFFF', bg_color = '#808080')
            result_money.place(relx=0/600, rely= 220/700)

            result_change = customtkinter.CTkLabel(reciept_frame, text=f"   Change: ₱{remaining_money}")
            result_change.configure(font = font3, text_color='#FFFFFF', bg_color = '#808080')
            result_change.place(relx=0/600, rely= 260/700)
            
            reciept_label = customtkinter.CTkLabel(reciept_frame, text = "________________________________")
            reciept_label.configure(font = ('Ink Free', 15, 'bold'), text_color='#FFFFFF', bg_color = '#808080')
            reciept_label.place(relx=20/600, rely= 300/700)

            result_message = customtkinter.CTkLabel(reciept_frame, text=f" Thank you for buying fruits at \n Jhude's Goods Fresh Fruits! \n Till next time!")
            result_message.configure(font = ('Ink Free', 15, 'bold'), text_color='#FFFFFF', bg_color = '#808080')
            result_message.place(relx=30/600, rely= 330/700)

        else:
            return 
        
    store_window = customtkinter.CTkToplevel()
    store_window.attributes('-topmost', 'true')
    store_window.title("Jhude's Goods")
    store_window.geometry("1000x400")
    store_window.config(bg = '#161F6D')
    store_window.resizable(False,False)

    font1 = ('Papyrus', 30, 'bold')
    font2 = ('Century Gothic', 25, 'bold')
    font3 = ('Kristen ITC', 15, 'bold')

    menu_label = customtkinter.CTkLabel(store_window, text = "Jhude's Goods Fresh Fruits")
    menu_label.configure(font = font1, text_color='#FFFFFF', bg_color = '#161F6D')
    menu_label.place(relx=150/1000, rely=5/400)

    reciept_frame = customtkinter.CTkFrame(store_window, width = 680, height = 700, fg_color='#808080')
    reciept_frame.place(relx=700/1000,rely=0/400)

    reciept_label = customtkinter.CTkLabel(reciept_frame, text = "Jhude's Goods Receipt")
    reciept_label.configure(font = ('Ink Free', 25, 'bold'), text_color='#FFFFFF', bg_color = '#808080')
    reciept_label.place(relx=20/600, rely= 20/700)
    
    reciept_label = customtkinter.CTkLabel(reciept_frame, text = "________________________________")
    reciept_label.configure(font = ('Ink Free', 15, 'bold'), text_color='#FFFFFF', bg_color = '#808080')
    reciept_label.place(relx=20/600, rely= 47/700)
    
    img1 = Image.open("images_prog2/apple_clear.png")
    resized_img = img1.resize((100,100))
    new_img1 = ImageTk.PhotoImage(resized_img)
    img_label1 = customtkinter.CTkLabel(store_window, image = new_img1, text = "Apple Promo \n Sale!!!")
    img_label1.configure(font = font2, text_color = '#FFFFFF', fg_color='#090b17', width = 200, height = 200, corner_radius = 20, compound = TOP, anchor=N)
    img_label1.place(relx=20/1000, rely=70/400)

    img2 = Image.open("images_prog2/orange.png")
    resized_img2 = img2.resize((100,100))
    new_img2 = ImageTk.PhotoImage(resized_img2)
    img_label2 = customtkinter.CTkLabel(store_window, image = new_img2, text = "SOLD OUT!!! \n No more stocks")
    img_label2.configure(font = font2, text_color = 'red', fg_color='#090b17', width = 200, height = 200, corner_radius = 20, compound = TOP, anchor=N)
    img_label2.place(relx=229/1000, rely=70/400)

    img2 = Image.open("images_prog2/strawberry.png")
    resized_img2 = img2.resize((100,100))
    new_img2 = ImageTk.PhotoImage(resized_img2)
    img_label2 = customtkinter.CTkLabel(store_window, image = new_img2, text = "SOLD OUT!!! \n No more stocks")
    img_label2.configure(font = font2, text_color = 'red', fg_color='#090b17', width = 200, height = 200, corner_radius = 20, compound = TOP, anchor=N)
    img_label2.place(relx=460/1000, rely=70/400)

    name_entry = customtkinter.CTkEntry(store_window)
    name_entry.configure(font = font2, text_color = '#000000', fg_color='#FFFFFF', border_color = '#FFFFFF', width = 350)
    name_entry.place(relx=280/1000, rely=280/400)

    name_label = customtkinter.CTkLabel(store_window, text = "Customer's Name:")
    name_label.configure(font = font2, text_color = '#FFFFFF', fg_color='#161F6D', width = 200)
    name_label.place(relx=50/1000, rely=284/400)

    check_var = customtkinter.IntVar()
    check_apple = customtkinter.CTkCheckBox(store_window, text="Buy", variable=check_var, onvalue = '1', offvalue = '0')
    check_apple.place(relx=50/1000, rely=220/400)

    buy_button = customtkinter.CTkButton(store_window, text = "    BUY    ", command = result_purchase)
    buy_button.configure(font = font2, fg_color = 'green', hover_color ='light green', corner_radius=20, cursor='hand2')
    buy_button.place(relx=200/1000, rely=350/400)

    exit_button = customtkinter.CTkButton(store_window, text= "Exit", command= store_window.destroy)
    exit_button.configure (font = font2, fg_color = 'red', hover_color ='dark red', corner_radius=20, cursor='hand2')
    exit_button.place(relx=450/1000, rely=350/400)

    store_window.mainloop()

main_window = customtkinter.CTk()
main_window.title("Jhude's Goods")
main_window.geometry("1000x600")
main_window.resizable(False,False)

bg_img = Image.open("images_prog2/market_bg3.jpg")
resized = bg_img.resize((1300,800))
new_bg_img = ImageTk.PhotoImage(resized)
bg_img_label = Label(main_window, image = new_bg_img).place(x=0,y=0)

market_name = customtkinter.CTkLabel(main_window, text= "Jhude's Goods Fresh Fruits")
market_name.configure(font = ('Papyrus', 45, 'bold'), text_color = '#000000' , fg_color = '#d4effa')
market_name.pack()

market_name2 = customtkinter.CTkLabel(main_window, text=" Farm Fresh Apples and Many more!")
market_name2.configure(font = ('Papyrus', 30, 'bold'), text_color = '#000000' , fg_color = '#d4effa')
market_name2.pack()

buy_button = customtkinter.CTkButton(main_window, text = "    BUY    ", command = buy_fruits)
buy_button.configure(font = ('Segoe Print', 30,'bold'), bg_color = '#d4effa')
buy_button.place(relx=300/1000, rely=340/600)

close_button = customtkinter.CTkButton(main_window, text = "No Thanks!", command=main_window.quit)
close_button.configure(font = ('Segoe Print', 30,'bold'), bg_color = '#d4effa')
close_button.place(relx=570/1000, rely=340/600)

main_window.mainloop()