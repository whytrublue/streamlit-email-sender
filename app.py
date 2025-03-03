import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.title("Bulk Gmail Sender")

gmail_user = st.text_input("Your Gmail Address")
gmail_password = st.text_input("App Password", type="password")
to_email = st.text_input("Recipient Email")
subject = st.text_input("Subject")
message = st.text_area("Email Body")

if st.button("Send Email"):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = to_email

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()

        st.success("Email Sent Successfully!")
    except Exception as e:
        st.error(f"Error: {e}")
