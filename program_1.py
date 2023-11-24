# Program 1
#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output

import tkinter as tk
from tkinter import simpledialog
from PIL import ImageTk, Image
import pyttsx3

def start_purchase():
    apples = simpledialog.askinteger("Apples", "How many apples do you want to buy?")
    purchase_apples = apples*20

    oranges = simpledialog.askinteger("Oranges", "How many oranges do you want to buy?")
    purchase_oranges = oranges*25

    purchase_total = purchase_oranges + purchase_apples

    def purchase_buy():

        purchase_confirm = tk.Toplevel(result)
        purchase_confirm.title("Purchase Complete")
        purchase_confirm.geometry("700x500")
        purchase_confirm.resizable(False,False)

        bg_img = Image.open("images_prog1/market_bgi.jpg")
        resized = bg_img.resize((700,500))
        new_bg_img = ImageTk.PhotoImage(resized)
        tk.Label(purchase_confirm, image = new_bg_img).place(relx=0/700,rely=0/500)

        message = tk.Label(purchase_confirm, text ="Thank you for choosing \n Uncle Buck's Farm Fresh \n Apple and Orange Fruits!")
        message.config(font = ('Segoe Print', 25), bg= '#d4effa')
        message.pack()

        buy_button = tk.Button(purchase_confirm, text = "  OK  ", command = root.destroy)
        buy_button.config(font = ('Segoe Print', 15,'bold'), bg = '#d4effa')
        buy_button.pack(padx=10, pady=20)

        speech2 = pyttsx3.init()
        speech2.say(f"Thank you for choosing Uncle Buck's Farm Fresh Apple and Orange Fruits!")
        speech2.runAndWait()

        purchase_confirm.mainloop()

    result = tk.Toplevel(root)
    result.title("Selling Fruits")
    result.geometry("700x500")
    root.resizable(False,False)

    bg_img = Image.open("images_prog1/market_bgi.jpg")
    resized = bg_img.resize((700,500))
    new_bg_img = ImageTk.PhotoImage(resized)
    tk.Label(result, image = new_bg_img).place(relx=0/700,rely=0/500)

    apple_payment = f"It costs ₱{purchase_apples} for the apples"
    pay_for_apples = tk.Label(result, text = apple_payment)
    pay_for_apples.config(font = ('Segoe Print', 20), bg= '#d4effa')
    pay_for_apples.pack()

    orange_payment = f" and ₱{purchase_oranges} for the orange."
    pay_for_orange = tk.Label(result, text = orange_payment)
    pay_for_orange.config(font = ('Segoe Print', 20), bg= '#d4effa')
    pay_for_orange.pack()

    total_payment = f"With a total of ₱{purchase_total} needed to pay."
    total_payment = tk.Label(result, text = total_payment)
    total_payment.config(font = ('Segoe Print', 20), bg= '#d4effa')
    total_payment.pack()

    confirm_payment = tk.Label(result, text = "Are you going to buy it?")
    confirm_payment.config(font = ('Segoe Print',20), bg= '#d4effa')
    confirm_payment.pack()

    buy_button = tk.Button(result, text = "  BUY  ", command = purchase_buy)
    buy_button.config(font = ('Segoe Print', 12,'bold'), bg = '#d4effa')
    buy_button.pack(padx=10, pady=20)

    cancel_button = tk.Button(result, text = "CANCEL", command= result.destroy)
    cancel_button.config(font = ('Segoe Print', 12,'bold'), bg = '#d4effa')
    cancel_button.pack(padx=10, pady=20)

    speech = pyttsx3.init()
    speech.say(f"Hello! My Dear Customer! It costs {purchase_apples} pesos for the apples and and {purchase_oranges} for the orange. With a total of {purchase_total} pesos needed to pay. Are you going to buy it?")
    speech.runAndWait()

    result.mainloop()

root = tk.Tk()
root.geometry("900x700")
root.resizable(False,False)
root.title("Uncle Bucks Fresh Fruits!")

bg_img = Image.open("images_prog1/market_bgi.jpg")
resized = bg_img.resize((900,700))
new_bg_img = ImageTk.PhotoImage(resized)
tk.Label(root, image = new_bg_img).place(relx=0/900,rely=0/700)

home_label = tk.Label(root, text = "Welcome to Uncle Buck's Farm ! ")
home_label.config(font = ('Segoe Print', 30,'bold'), bg= '#d4effa')
home_label.pack()

home_label2 = tk.Label(root, text = "Fresh Apple and Orange Fruits that \n You can choose!")
home_label2.config(font = ('Segoe Print', 20), bg= '#d4effa')
home_label2.pack()

start_btn = tk.Button(root, text= " Buy Now ", command= start_purchase)
start_btn.config(font = ('Segoe Print', 15,'bold'), bg = '#d4effa')
start_btn.pack(padx=10, pady=20)

close_button = tk.Button(root, text = "No thanks!", command=root.quit)
close_button.config(font = ('Segoe Print', 15,'bold'), bg = '#d4effa')
close_button.pack(padx=10, pady=20)

root.mainloop()