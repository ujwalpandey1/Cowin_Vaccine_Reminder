import requests
import time
import streamlit as st


st.title('Cowin Vaccine Reminder')


pincode=st.text_input("Pincode")
options=["COVISHIELD","COVAXIN"]
vaccinetype=st.selectbox("Vaccine", options, index=0)
date=st.text_input("Date (DD-MM-YYYY)")
numbers=st.text_input("Mobile Number")


url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode, date)
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

if st.button('Get Notification'):
    st.write("Please Do Not Close the Application")
    def findslot():
        counter = 0;
        result = requests.get(url, headers=headers)
        resultjson = result.json()
        data = resultjson["sessions"]
        for i in data:
            if ((i["available_capacity"] > 0) & (i["fee_type"] == "Free") & (i["vaccine"] == vaccinetype)):
                cname = i["name"]
                message = 'Vaccine is Available in your Area at {}'.format(cname)
                url1 = 'https://www.fast2sms.com/dev/bulkV2?authorization=iEGVSqureht7ttAlqRy9p09TuenflACJaA0f6yDKj0DXNb8SnLW9l0uz1rib&route=q&message={}&language=english&flash=1&numbers={}'.format(
                    message, numbers)
                response = requests.get(url=url1)

                counter = counter + 1;
                return True
        if (counter == 0):
            return False


    while (findslot() != True):
        time.sleep(5)
        findslot()
