import tkinter as tk
from tkinter import ttk
import pymongo
import smtplib
from email.mime.text import MIMEText
import string
import random

ref_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["snack_survey"]
col = db["Referral code"]


def send_email(rec_email):
    from_email = 'testforhackathon.techv@gmail.com'
    to_email = rec_email
    subject = 'Your Exclusive Mondelez Offer!'
    message = f"""We hope this message finds you well. 
As a valued customer, we are delighted to offer you an exclusive deal from Mondelez!

Cashback Code: MON20EXCLSV
Use the Cashback code on any brand's website (associated with Mondelez) and get an instant cashback of upto 20%!

But that's not all! We have a special referral program just for you. Share your unique referral code below with your friends and family, and gather as many people you can to share your referral code with. The person with the maximum referrals will receive a fantastic hamper prize from Mondelez!
Your unique code-{ref_code}

Don't miss out on this opportunity to enjoy more of your favorite snacks at an amazing price. Share the joy of snacking with your loved ones today!

Thank you for being a part of the Mondelez family. We appreciate your loyalty.

Best regards,
Mondelez Snacks Inc.

"""

    msg = MIMEText(message)
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, 'ymsj kwfd blpv lbem')
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed. Error: {str(e)}")

    col.insert_one({"ref_code":ref_code,"email": rec_email})

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = age_var.get()
    gender = gender_var.get()
    location = location_var.get()
    snack_frequency = snack_frequency_var.get()
    snack_source = snack_source_var.get()
    snack_brands =  snack_brand_var.get()
    last_purchase_brand = last_purchase_brand_var.get()
    budget = budget_var.get()
    price_consideration = price_consideration_var.get()
    pay_more_healthier = pay_more_healthier_var.get()
    nutritional_labels = nutritional_labels_var.get()
    referral_code=entry_referral_code.get()

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["snack_survey"]
    collection = db["responses"]

    response_data = {
        "Name": name,
        "Email": email,
        "Age": age,
        "Gender": gender,
        "Location": location,
        "How often do you eat snacks": snack_frequency,
        "Where do you usually buy snacks": snack_source,
        "Go to snack brand": snack_brands,
        "Last purchase from which brand": last_purchase_brand,
        "Budget for snacks": budget,
        "Price consideration when buying snacks": price_consideration,
        "Willingness to pay more for healthier snacks": pay_more_healthier,
        "Attention to nutritional labels": nutritional_labels,
        "Referral code": referral_code
    }

    collection.insert_one(response_data)
    client.close()

    print("Form submitted successfully and data stored in MongoDB.")

    app.destroy()

    send_email(email)

app = tk.Tk()
app.title("Snack Survey")

label_name = ttk.Label(app, text="1. Name:")
label_name.grid(row=0, column=0)
entry_name = ttk.Entry(app)
entry_name.grid(row=0, column=1)

label_email = ttk.Label(app, text="2. Email address:")
label_email.grid(row=1, column=0)
entry_email = ttk.Entry(app)
entry_email.grid(row=1, column=1)

label_age = ttk.Label(app, text="3. Age:")
label_age.grid(row=2, column=0)
age_var = tk.StringVar()
age_var.set("Select Option")
age_options = ["Select Option", "8-14", "15-20", "21-26", "27+"]
age_menu = ttk.OptionMenu(app, age_var, *age_options)
age_menu.grid(row=2, column=1)

label_gender = ttk.Label(app, text="4. Gender:")
label_gender.grid(row=3, column=0)
gender_var = tk.StringVar()
gender_var.set("Select Option")
gender_options = ["Select Option", "Male", "Female", "Other"]
gender_menu = ttk.OptionMenu(app, gender_var, *gender_options)
gender_menu.grid(row=3, column=1)

label_location = ttk.Label(app, text="5. Location (State):")
label_location.grid(row=4, column=0)
location_var = tk.StringVar()
location_var.set("Select Option")
location_options = ["Select Option", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
location_menu = ttk.OptionMenu(app, location_var, *location_options)
location_menu.grid(row=4, column=1)

label_snack_frequency = ttk.Label(app, text="6. How often do you eat snacks in a day:")
label_snack_frequency.grid(row=5, column=0)
snack_frequency_var = tk.StringVar()
snack_frequency_var.set("Select Option")
snack_frequency_options = ["Select Option", "Once a day", "2-3 times", "Few times a week", "Few times a month", "Rarely"]
snack_frequency_menu = ttk.OptionMenu(app, snack_frequency_var, *snack_frequency_options)
snack_frequency_menu.grid(row=5, column=1)

label_snack_source = ttk.Label(app, text="7. Where do you usually buy snacks from:")
label_snack_source.grid(row=6, column=0)
snack_source_var = tk.StringVar()
snack_source_var.set("Select Option")
snack_source_options = ["Select Option", "Online", "Local shop", "Big retail store"]
snack_source_menu = ttk.OptionMenu(app, snack_source_var, *snack_source_options)
snack_source_menu.grid(row=6, column=1)

label_snack_brand = ttk.Label(app, text="8.Go to snack brand:")
label_snack_brand.grid(row=7, column=0)
snack_brand_var = tk.StringVar()
snack_brand_var.set("Select Option")
snack_brand_options = ["Select Option", "Cadbury", "Tang", "Perk", "Halls", "5 Star", "BournVita", "Dairy Milk", "Oreo", "Toblerone"]
snack_brand_menu = ttk.OptionMenu(app, snack_brand_var, *snack_brand_options)
snack_brand_menu.grid(row=7, column=1)

label_last_purchase_brand = ttk.Label(app, text="9. Last purchase from which brand:")
label_last_purchase_brand.grid(row=8, column=0)
last_purchase_brand_var = tk.StringVar()
last_purchase_brand_var.set("Select Option")
last_purchase_brand_options = ["Select Option", "Cadbury", "Tang", "Halls", "5 Star", "BournVita", "Dairy Milk", "Oreo", "Tobleron"]
last_purchase_brand_menu = ttk.OptionMenu(app, last_purchase_brand_var, *last_purchase_brand_options)
last_purchase_brand_menu.grid(row=8, column=1)

label_budget = ttk.Label(app, text="10. When it comes to buying snacks, do you typically have a monthly budget in mind?")
label_budget.grid(row=9, column=0)
budget_var = tk.StringVar()
budget_var.set("Select Option")
budget_options = ["Select Option", "Yes, I have a specific budget", "I have a rough idea but don't stick to it", "No, I don't budget for snacks"]
budget_menu = ttk.OptionMenu(app, budget_var, *budget_options)
budget_menu.grid(row=9, column=1)

label_price_consideration = ttk.Label(app, text="11. How often do you consider the price when buying snacks?")
label_price_consideration.grid(row=10, column=0)
price_consideration_var = tk.StringVar()
price_consideration_var.set("Select Option")
price_consideration_options = ["Select Option", "Always", "Most of the times", "Occasionally", "Rarely", "Never"]
price_consideration_menu = ttk.OptionMenu(app, price_consideration_var, *price_consideration_options)
price_consideration_menu.grid(row=10, column=1)

label_pay_more_healthier = ttk.Label(app, text="12. Would you be willing to pay more for healthier snack options?")
label_pay_more_healthier.grid(row=11, column=0)
pay_more_healthier_var = tk.StringVar()
pay_more_healthier_var.set("Select Option")
pay_more_healthier_options = ["Select Option", "Yes, I prioritize health over price", "Maybe, depending on the snack", "No, I feel it's okay to enjoy your favorite snack in moderation"]
pay_more_healthier_menu = ttk.OptionMenu(app, pay_more_healthier_var, *pay_more_healthier_options)
pay_more_healthier_menu.grid(row=11, column=1)

label_nutritional_labels = ttk.Label(app, text="13. Do you pay attention to the nutritional labels on snack packaging?")
label_nutritional_labels.grid(row=12, column=0)
nutritional_labels_var = tk.StringVar()
nutritional_labels_var.set("Select Option")
nutritional_labels_options = ["Select Option", "Always", "Most of the times", "Occasionally", "Rarely", "Never"]
nutritional_labels_menu = ttk.OptionMenu(app, nutritional_labels_var, *nutritional_labels_options)
nutritional_labels_menu.grid(row=12, column=1)

label_referral_code = ttk.Label(app, text="14. Enter the referral code:")
label_referral_code.grid(row=14, column=0)
entry_referral_code = ttk.Entry(app)
entry_referral_code.grid(row=14, column=1)

label_post_pic = ttk.Label(app, text="Dont' forget to share a photo of yourself enjoying your favorite snack on your social media, tag Mondelez, use the hashtag #myfavsnacc,\n and get a chance to be featured on Mondelez's official social media profiles.")
label_post_pic.grid(row=15, column=0)

label_cashback = ttk.Label(app, text="Cashback code will be sent to your email id that can be redeemed on all websites associated with Mondelez")
label_cashback.grid(row=16, column=0)

submit_button = ttk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=50, columnspan=2)

app.mainloop()



