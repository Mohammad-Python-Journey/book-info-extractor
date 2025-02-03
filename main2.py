import validation2
import scraper


def show_instruction():
    instructions = """
***************************************User guide for the script***************************************
**********************this script is designed for web scrapping of book websites***********************
1. First, enter the desired website address. (e.g www.example.com)
2. The script will display a list of book categories.
3. By selecting a category number, you will see the list of its books.
4. By selecting book number one, a summary and complete information about it will be displayed.
5. There is an option to download or pay for the selected book.
6. To return to the previous stage, enter the number 0.
*******************************************************************************************************
"""
    print(instructions)


show_instruction()

# دریافت و ذخیره URL معتبر
url = validation2.get_website_url()

# دریافت دسته‌بندی‌ها از صفحه اصلی
category_dict = scraper.fetch_categories(url)

if category_dict:
    # انتخاب دسته‌بندی از کاربر
    category_choice = int(input("\nEnter the category number to explore: "))

    if category_choice in category_dict:
        # استخراج لینک دسته‌بندی
        category_url = category_dict[category_choice][1]
        full_url = url + category_url

        # اسکرپ کردن کتاب‌های موجود در دسته‌بندی
        scraper.scrape_books_from_category(full_url)
    else:
        print("Invalid choice.")
