import smtplib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail info

SENDER_EMAIL=""
SENDER_PASSWORD=""


service = Service(executable_path=r'C:\Users\user\chromedriver-win64\chromedriver-win64\chromedriver.exe')  


def send_email(name, link):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL
    msg['Subject'] = "დაიდო ახალი"

    # Body of the email
    body = f"დაიდო ახალი!!!!!! {name}.\nCheck the details here: {link}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        
        # Login using Gmail credentials
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Send the email
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())

def new_program():
    driver = webdriver.Chrome(service=service)
    driver.get("https://btu.edu.ge/stsavla/gatsvlithi-programebi/")

    time.sleep(5) 

    date_element = driver.find_element(By.CSS_SELECTOR, "span.elementor-post-date")
    title_element = driver.find_element(By.CSS_SELECTOR, "h3.elementor-post__title a")


    date_text=date_element.text.strip()
    date_day=int(date_text.split(" ")[1].replace(',', ''))  # day number ( "10" from "ოქტომბერი 10, 2024")

    if date_day > 10:
         # Extract the program link
        program_link = title_element.get_attribute("href") 
        program_name = title_element.text.strip() 

        send_email(program_name,program_link)

    driver.quit()




if __name__ == "__main__":
    new_program()