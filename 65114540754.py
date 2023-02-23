import streamlit as st
import BHP
import BMI
from PIL import Image

with st.sidebar:
    Menu = st.selectbox('Menu', ('Introduction👇', 'Body Health Prediction👉', 'BMI Calculate👉', 'BMI charts👉', 'Exercise of Health👉'))

if Menu == 'Introduction👇':
    st.title('✦ Introduce Page 👋🏻')
    st.write('🙋Welcome to my project My name is Udomsap Roeksirisuphakorn 65114540754')
    st.markdown('## 𝗪𝗵𝗮𝘁 𝗶𝘀 𝗯𝗼𝗱𝘆 𝗵𝗲𝗮𝗹𝘁𝗵 𝗽𝗿𝗲𝗱𝗶𝗰𝘁𝗶𝗼𝗻❓')
    st.info('''\n
    🛒 Body health prediction from gender, height, 
    and weight is a common approach used to evaluate an individual's overall 
    health status. The body mass index (BMI) is a widely used method that takes into account an individual's 
    height and weight to determine if they are within a healthy weight range. BMI is calculated by dividing a person's 
    weight in kilograms by their height in meters squared. \n''')

    st.info('''🛒 Gender is also a factor that can impact health status, 
    as men and women tend to have different body compositions. On average, men tend to have a higher percentage 
    of muscle mass and lower percentage of body fat than women. Women, on the other hand, tend to have a higher 
    percentage of body fat and lower muscle mass. \n''')

    st.info('''🛒 It is important to note, however, that BMI is not always an accurate indicator of overall health. Other 
    factors, such as muscle mass, bone density, and body shape, can all impact an individual's health status. 
    In addition, BMI does not take into account other health indicators such as blood pressure, cholesterol 
    levels, and blood sugar levels. \n''')

    st.info('''🛒 Overall, while gender, height, and weight can provide some insight into an individual's health status, 
    it is important to take a comprehensive approach to evaluating health 
    and to consider a variety of factors beyond just these three metrics.''')

if Menu == 'Body Health Prediction👉':
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
if Menu == 'BMI Calculate👉':
    BMI.BI()
if Menu == 'BMI charts👉':
    image = Image.open('BMI.jpg')
    st.image(image)
if Menu == 'Exercise of Health👉':
    st.title('💪🏻การออกกำลังกายเพื่อสุขภาพ')
    st.write('''การออกกำลังกาย เป็นกิจกรรมที่ช่วยสร้างเสริมให้ร่างกายคงไว้ซึ่งสุขภาพและความแข็งแรงของร่างกาย การออกกำลังกาย ช่วย เสริม 
    สร้างความแข็งแรงของกล้ามเนื้อ และระบบไหลเวียนโลหิต รวมทั้งสร้างเสริมทักษะทางกีฬา การออกกำลังกาย อย่างสม่ำเสมอ 
    จะช่วยสร้างเสริมระบบภูมิคุ้มกันและช่วยป้องกันโรคต่างๆ เช่นโรคหัวใจ, โรคระบบไหลเวียนโลหิต, เบาหวาน, และโรคอ้วน 
    นอกจากนี้การออกกำลังกายยังช่วยสร้างเสริมสุขภาพจิตและลดความเครียดได้
    การออกกำลังกาย ไม่ได้หมายถึงการต้องไปแข่งขันกีฬากับผู้อื่น แต่การออกกำลังกายเป็นการแข่งขันกับตัวเอง หลายคนก่อนจะ 
    ออกกำลังกายมักจะอ้างเหตุผลของการไม่ออกกำลังกาย เช่น ไม่มีเวลา ไม่มีสถานที่ ปัญหาเกี่ยวกับสุขภาพ ปัญหาเกี่ยวกับอากาศ 
    ทั้งหมดเป็นข้ออ้างที่จะไม่ออกกำลังกาย แต่ลืมไปว่าการออกกำลังกายอาจจะให้ผลดีมากกว่าสิ่งที่เขาเสียไป
    หลายท่านไม่เคยออกกำลังกายมาก่อนเมื่อเริ่มออกกำลังกายอาจจะทำให้เหนื่อยง่าย วิธีที่ดีที่สุดของการเริ่มต้นออกกำลังกาย คือให้ เริ่มออกกำลังกายจากกิจวัตรประจำวัน เช่น''')
    st.write('✧ ใช้การเดินหรือขี่จักรยานเมื่อไปที่ไม่ไกล')
    st.write('✧ หยุดใช้รถหนึ่งวันแล้วใช้การเดินไปทำงานสำหรับผู้ที่บ้านและที่ทำงานไม่ไกล')
    st.write('✧ ใช้บันไดแทนการขึ้นลิฟต์หรือบันไดเลื่อน')
    st.write('✧ ขี่จักรยานรอบหมู่บ้าน')
    st.write('✧ ทำสวน ล้างรถ ถูบ้าน ขึ้นบันไดหลายขั้น ขุดดินทำสวนนานขึ้น')
    run = Image.open('run.jpg')
    st.image(run)