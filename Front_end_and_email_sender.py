#Importing all the libraries 
# This for building the front end for user interaction 
import streamlit as st
import pandas as pd
#datetime and scheduler were used to run a function everyday on a given particular time
# import schedule
import datetime as dt
#To send an email to the user with todays dashboard as a png image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import smtplib
#For reading image files 
from PIL import Image
import os


#Taking user name from the user
# user_name = st.text_input('Enter you Name')

#Title for the web app 
st.markdown("<h1 style='text-align: center; color: white;'>GRAPHICS CARD PICKER</h1>", unsafe_allow_html=True)

st.markdown('#')

#Title of the table
st.subheader('Table generator based on price')

df = pd.read_excel('cleaned_data.xlsx')

max_price = df['Price'].max()



#Displaying the image with the user interaction
with st.expander("Click to expand"):
    user_price = st.slider(label = 'Slide to increase/decrease the price and get all graphic cards below/equal to the price provided',max_value= int(max_price),step = 5000, value = 10000)
    return_table = df.loc[df['Price']<=user_price]
    st.table(return_table)

st.markdown('#')

#Title for the report generator
st.subheader('Report Generator')

#To display the dashboard to the user 

if st.button(label = 'Press the button to get a report online'):
   with st.spinner('Wait for it...'): 
        image_output = Image.open('report.png')
        st.image(image_output)
        st.write('"Here are todays report on the graphic cards"')

#Part of the code to send and email to the user

st.markdown('#')

st.subheader('Subscribe to get the reports automatically sent to you everyday!')

user_email = st.text_input('Enter your Email')

#Button to intiate the email to the user
if st.button(label = 'Press the button to get a report to your email '):
    with st.spinner('Wait for it...'):
# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
        email_user = user_email
        my_secret2 = email_user
        fromaddr = 'trustthetechie@gmail.com'
        toaddr = my_secret2

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Subject of the Mail"

        # string to store the body of the mail
        body = "Body_of_the_mail"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = 'report.png'
        attachment = Image.open('report.png')

        # instance of MIMEBase and named as p
        # p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        # p.set_payload((attachment).read())

        # encode into base64
        # encoders.encode_base64(p)

        # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        with open('report.png', 'rb') as f:
            img_data = f.read()

        image = MIMEImage(img_data, name=os.path.basename('report.png'))

        msg.attach(image)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, 'pass@ord')

        # # Converts the Multipart msg into a string
        text = msg.as_string()
        

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()
        with st.spinner('Wait for it...'):

         st.success('Email has been sent to you!')

