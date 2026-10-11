import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_smartphones():
    # داتا افتراضية بتمثل عملية سحب البيانات (Web Scraping) لسوق الموبايلات
    data = [
        {"Phone Name": "Samsung Galaxy S24", "Brand": "Samsung", "Price (EGP)": 45000, "Rating": 4.8, "Storage (GB)": 256},
        {"Phone Name": "iPhone 15 Pro", "Brand": "Apple", "Price (EGP)": 60000, "Rating": 4.9, "Storage (GB)": 128},
        {"Phone Name": "Xiaomi Redmi Note 13", "Brand": "Xiaomi", "Price (EGP)": 11000, "Rating": 4.3, "Storage (GB)": 256},
        {"Phone Name": "Oppo Reno 11", "Brand": "Oppo", "Price (EGP)": 18000, "Rating": 4.4, "Storage (GB)": 256},
        {"Phone Name": "Realme 11", "Brand": "Realme", "Price (EGP)": 12500, "Rating": 4.2, "Storage (GB)": 128},
        {"Phone Name": "Samsung Galaxy A55", "Brand": "Samsung", "Price (EGP)": 21000, "Rating": 4.6, "Storage (GB)": 256},
        {"Phone Name": "iPhone 14", "Brand": "Apple", "Price (EGP)": 42000, "Rating": 4.7, "Storage (GB)": 128},
        {"Phone Name": "Xiaomi Poco X6", "Brand": "Xiaomi", "Price (EGP)": 15000, "Rating": 4.5, "Storage (GB)": 256},
    ]

    df = pd.DataFrame(data)
    # حفظ البيانات في ملف csv هيظهر لوحده في المجلد بعد التشغيل
    df.to_csv("smartphones.csv", index=False, encoding="utf-8-sig")
    print("تم سحب البيانات بنجاح وحفظها في smartphones.csv")

if __name__ == "__main__":
    scrape_smartphones()