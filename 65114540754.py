import streamlit as st
import BHP
import BMI
from PIL import Image

with st.sidebar:
    Menu = st.selectbox('Menu', ('Introduction๐', 'Body Health Prediction๐', 'BMI Calculate๐', 'BMI charts๐', 'Exercise of Health๐'))

if Menu == 'Introduction๐':
    st.title('โฆ Introduce Page ๐๐ป')
    st.write('๐Welcome to my project My name is Udomsap Roeksirisuphakorn 65114540754')
    st.markdown('## ๐ช๐ต๐ฎ๐ ๐ถ๐ ๐ฏ๐ผ๐ฑ๐ ๐ต๐ฒ๐ฎ๐น๐๐ต ๐ฝ๐ฟ๐ฒ๐ฑ๐ถ๐ฐ๐๐ถ๐ผ๐ปโ')
    st.info('''\n
    ๐ Body health prediction from gender, height, 
    and weight is a common approach used to evaluate an individual's overall 
    health status. The body mass index (BMI) is a widely used method that takes into account an individual's 
    height and weight to determine if they are within a healthy weight range. BMI is calculated by dividing a person's 
    weight in kilograms by their height in meters squared. \n''')

    st.info('''๐ Gender is also a factor that can impact health status, 
    as men and women tend to have different body compositions. On average, men tend to have a higher percentage 
    of muscle mass and lower percentage of body fat than women. Women, on the other hand, tend to have a higher 
    percentage of body fat and lower muscle mass. \n''')

    st.info('''๐ It is important to note, however, that BMI is not always an accurate indicator of overall health. Other 
    factors, such as muscle mass, bone density, and body shape, can all impact an individual's health status. 
    In addition, BMI does not take into account other health indicators such as blood pressure, cholesterol 
    levels, and blood sugar levels. \n''')

    st.info('''๐ Overall, while gender, height, and weight can provide some insight into an individual's health status, 
    it is important to take a comprehensive approach to evaluating health 
    and to consider a variety of factors beyond just these three metrics.''')

if Menu == 'Body Health Prediction๐':
    st.markdown(
        f"""
           <style>
           .stApp {{
               background-image: url("https://i.pinimg.com/564x/78/21/d8/7821d8e4364a288fd622e31388d6744e.jpg");
               background-attachment: fixed;
               background-size: cover;
               /* opacity: 0.3; */
           }}
           </style>
           """,
        unsafe_allow_html=True
    )
    BHP.BP()
if Menu == 'BMI Calculate๐':
    BMI.BI()
if Menu == 'BMI charts๐':
    image = Image.open('BMI.jpg')
    st.image(image)
if Menu == 'Exercise of Health๐':
    st.title('๐ช๐ปเธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเนเธเธทเนเธญเธชเธธเธเธ?เธฒเธ')
    st.write('''เธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เนเธเนเธเธเธดเธเธเธฃเธฃเธกเธเธตเนเธเนเธงเธขเธชเธฃเนเธฒเธเนเธชเธฃเธดเธกเนเธซเนเธฃเนเธฒเธเธเธฒเธขเธเธเนเธงเนเธเธถเนเธเธชเธธเธเธ?เธฒเธเนเธฅเธฐเธเธงเธฒเธกเนเธเนเธเนเธฃเธเธเธญเธเธฃเนเธฒเธเธเธฒเธข เธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เธเนเธงเธข เนเธชเธฃเธดเธก 
    เธชเธฃเนเธฒเธเธเธงเธฒเธกเนเธเนเธเนเธฃเธเธเธญเธเธเธฅเนเธฒเธกเนเธเธทเนเธญ เนเธฅเธฐเธฃเธฐเธเธเนเธซเธฅเนเธงเธตเธขเธเนเธฅเธซเธดเธ เธฃเธงเธกเธเธฑเนเธเธชเธฃเนเธฒเธเนเธชเธฃเธดเธกเธเธฑเธเธฉเธฐเธเธฒเธเธเธตเธฌเธฒ เธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เธญเธขเนเธฒเธเธชเธกเนเธณเนเธชเธกเธญ 
    เธเธฐเธเนเธงเธขเธชเธฃเนเธฒเธเนเธชเธฃเธดเธกเธฃเธฐเธเธเธ?เธนเธกเธดเธเธธเนเธกเธเธฑเธเนเธฅเธฐเธเนเธงเธขเธเนเธญเธเธเธฑเธเนเธฃเธเธเนเธฒเธเน เนเธเนเธเนเธฃเธเธซเธฑเธงเนเธ, เนเธฃเธเธฃเธฐเธเธเนเธซเธฅเนเธงเธตเธขเธเนเธฅเธซเธดเธ, เนเธเธฒเธซเธงเธฒเธ, เนเธฅเธฐเนเธฃเธเธญเนเธงเธ 
    เธเธญเธเธเธฒเธเธเธตเนเธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธขเธฑเธเธเนเธงเธขเธชเธฃเนเธฒเธเนเธชเธฃเธดเธกเธชเธธเธเธ?เธฒเธเธเธดเธเนเธฅเธฐเธฅเธเธเธงเธฒเธกเนเธเธฃเธตเธขเธเนเธเน
    เธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เนเธกเนเนเธเนเธซเธกเธฒเธขเธเธถเธเธเธฒเธฃเธเนเธญเธเนเธเนเธเนเธเธเธฑเธเธเธตเธฌเธฒเธเธฑเธเธเธนเนเธญเธทเนเธ เนเธเนเธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเนเธเนเธเธเธฒเธฃเนเธเนเธเธเธฑเธเธเธฑเธเธเธฑเธงเนเธญเธ เธซเธฅเธฒเธขเธเธเธเนเธญเธเธเธฐ 
    เธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธกเธฑเธเธเธฐเธญเนเธฒเธเนเธซเธเธธเธเธฅเธเธญเธเธเธฒเธฃเนเธกเนเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เนเธเนเธ เนเธกเนเธกเธตเนเธงเธฅเธฒ เนเธกเนเธกเธตเธชเธเธฒเธเธเธตเน เธเธฑเธเธซเธฒเนเธเธตเนเธขเธงเธเธฑเธเธชเธธเธเธ?เธฒเธ เธเธฑเธเธซเธฒเนเธเธตเนเธขเธงเธเธฑเธเธญเธฒเธเธฒเธจ 
    เธเธฑเนเธเธซเธกเธเนเธเนเธเธเนเธญเธญเนเธฒเธเธเธตเนเธเธฐเนเธกเนเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เนเธเนเธฅเธทเธกเนเธเธงเนเธฒเธเธฒเธฃเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธญเธฒเธเธเธฐเนเธซเนเธเธฅเธเธตเธกเธฒเธเธเธงเนเธฒเธชเธดเนเธเธเธตเนเนเธเธฒเนเธชเธตเธขเนเธ
    เธซเธฅเธฒเธขเธเนเธฒเธเนเธกเนเนเธเธขเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธกเธฒเธเนเธญเธเนเธกเธทเนเธญเนเธฃเธดเนเธกเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธญเธฒเธเธเธฐเธเธณเนเธซเนเนเธซเธเธทเนเธญเธขเธเนเธฒเธข เธงเธดเธเธตเธเธตเนเธเธตเธเธตเนเธชเธธเธเธเธญเธเธเธฒเธฃเนเธฃเธดเนเธกเธเนเธเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธข เธเธทเธญเนเธซเน เนเธฃเธดเนเธกเธญเธญเธเธเธณเธฅเธฑเธเธเธฒเธขเธเธฒเธเธเธดเธเธงเธฑเธเธฃเธเธฃเธฐเธเธณเธงเธฑเธ เนเธเนเธ''')
    st.write('โง เนเธเนเธเธฒเธฃเนเธเธดเธเธซเธฃเธทเธญเธเธตเนเธเธฑเธเธฃเธขเธฒเธเนเธกเธทเนเธญเนเธเธเธตเนเนเธกเนเนเธเธฅ')
    st.write('โง เธซเธขเธธเธเนเธเนเธฃเธเธซเธเธถเนเธเธงเธฑเธเนเธฅเนเธงเนเธเนเธเธฒเธฃเนเธเธดเธเนเธเธเธณเธเธฒเธเธชเธณเธซเธฃเธฑเธเธเธนเนเธเธตเนเธเนเธฒเธเนเธฅเธฐเธเธตเนเธเธณเธเธฒเธเนเธกเนเนเธเธฅ')
    st.write('โง เนเธเนเธเธฑเธเนเธเนเธเธเธเธฒเธฃเธเธถเนเธเธฅเธดเธเธเนเธซเธฃเธทเธญเธเธฑเธเนเธเนเธฅเธทเนเธญเธ')
    st.write('โง เธเธตเนเธเธฑเธเธฃเธขเธฒเธเธฃเธญเธเธซเธกเธนเนเธเนเธฒเธ')
    st.write('โง เธเธณเธชเธงเธ เธฅเนเธฒเธเธฃเธ เธเธนเธเนเธฒเธ เธเธถเนเธเธเธฑเธเนเธเธซเธฅเธฒเธขเธเธฑเนเธ เธเธธเธเธเธดเธเธเธณเธชเธงเธเธเธฒเธเธเธถเนเธ')
    run = Image.open('run.jpg')
    st.image(run)