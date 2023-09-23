import pymongo
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_data_from_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["snack_survey"]
    collection = db["responses"]

    data = list(collection.find({}))
    client.close()

    return data

def analyze_and_visualize_data():
    data = get_data_from_mongodb()

    df = pd.DataFrame(data)

    palette = sns.color_palette("pastel")

    age = df["Age"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(age, labels=age.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Age Distribution")
    plt.axis('equal')  

    snack_shopping = df["Where do you usually buy snacks"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(snack_shopping, labels=snack_shopping.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Where do people usually buy snacks from")
    plt.axis('equal') 

    snack_brand = df["Go to snack brand"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(snack_brand, labels=snack_brand.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Go to snack brand")
    plt.axis('equal') 

    last_purchase = df["Last purchase from which brand"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(last_purchase, labels=last_purchase.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Last purchase from which brand")
    plt.axis('equal') 

    price_consider = df["Price consideration when buying snacks"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(price_consider, labels=price_consider.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Price consideration when buying snacks")
    plt.axis('equal')

    willing_to_pay_more_for_healthy = df["Willingness to pay more for healthier snacks"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(willing_to_pay_more_for_healthy, labels=willing_to_pay_more_for_healthy.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Dirtribution of people's willingness to pay more for healthier snacks")
    plt.axis('equal')

    nutrition_labels = df["Attention to nutritional labels"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(nutrition_labels, labels=nutrition_labels.index, autopct='%.0f%%', startangle=140, colors=palette)
    plt.title("Attention to nutritional labels")
    plt.axis('equal')

    plt.show()

analyze_and_visualize_data()
