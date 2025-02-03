import re

validated_url = None  # متغیر سراسری برای ذخیره URL


def get_website_url():
    global validated_url  # استفاده از متغیر سراسری

    if validated_url:  # اگر قبلاً مقداردهی شده باشد، همان مقدار را برگردان
        return validated_url

    while validated_url is None:  # فقط وقتی مقدار ندارد، حلقه اجرا شود
        url = input("Please enter your desired URL (example.com): ").strip()
        print(f"Checking website: {url}")

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # افزودن `http://` در صورت نیاز

        pattern = r"^https?://[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(\S*)$"
        if re.fullmatch(pattern, url):
            validated_url = url  # ذخیره مقدار معتبر
            print(f"{validated_url}: Your URL is valid.")
            return validated_url  # خروج از تابع پس از دریافت URL معتبر

        print("Your URL is invalid. Please try again.")
