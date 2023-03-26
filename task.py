import time
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
import os
from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem

browser = Selenium()

def configure():
    load_dotenv()

def login_to_web_page():
    browser.open_available_browser("https://acme-test.uipath.com/login")
    browser.input_text("xpath://div//input[@id='email']", f"{os.getenv('ACME_LOGIN')}")
    browser.input_text("xpath://div//input[@id='password']", f"{os.getenv('ACME_PASSWORD')}")
    browser.click_button("xpath://div//button[@type='submit']")
    time.sleep(5)

def download_monthly_report():
    browser.click_button("xpath://div//button[@class='btn btn-default btn-lg dropdown-toggle']")
    browser.click_button("xpath://div[@class='dropdown']//a[@href='https://acme-test.uipath.com/reports/download']")
    browser.input_text("xpath://div[@class='control-group form-group']//input", "TaxID27461")

    select_element = browser.find_element("xpath://div[@class='control-group form-group']//select[@id='reportMonth']")
    time.sleep(3)

def redirect_to_work_items():
    browser.click_button("xpath://div//button[@class='btn btn-default btn-lg']")
    time.sleep(3)

def send_mail():
    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    email_from = f"{os.getenv('GMAIL_MAIL')}"
    email_to = f"{os.getenv('GMAIL_MAIL')}"
    pswd = f"{os.getenv('GOOGLE_APP_CREDENTIAL')}"
    message = "RPAHashBot"

    simple_email_context = ssl.create_default_context()

    try:
        print("Conecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        print("Connected to server :) ")

        print(f"Sending email to {email_to}")
        TIE_server.sendmail(email_from, email_to, message)
        print(f"Email send successfully to {email_to}")
    except Exception as e:
        print(e)
    finally:
        TIE_server.quit

def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
