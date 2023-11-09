import streamlit as st
import pandas as pd
from datetime import time
import time as ts

st.markdown("""
<style>
    .st-emotion-cache-6q9sum, .ef3psqc4, .st-emotion-cache-cio0dv, .ea3mdgi1, .st-emotion-cache-1avcm0n, .ezrtsby2{
            visibility: hidden;
    }
            
    .title_text {
            text-align: center;
    }
</style>

""", unsafe_allow_html = True)

st.markdown('<h1 class="title_text">User Registration Form</h1>', unsafe_allow_html=True)

# #first method to create form - use form object to access everything inside
# form = st.form('Form 1')
# form.text_input('First Name')
# form.form_submit_button('Submit')

#2nd method - use 'with' key word make it function like
with st.form('Form 2', clear_on_submit=False):
   #Use 'column' widget
   col1, col2, col3 = st.columns(3)
   f_name = col1.text_input('Firstname')
   m_name = col2.text_input('Middlename')
   l_name = col3.text_input('Lastname')

   email = st.text_input('Email')
   u_pass = st.text_input('Password')
   c_pass = st.text_input('Confirm Password')

   day, month, year = st.columns(3)
   d = day.text_input('Day')
   m = month.text_input('Month')
   y = year.text_input('Year')
   s_state = st.form_submit_button('Submit')


   if s_state:
      if f_name == '' and l_name == '':
         st.warning('Please fill all the inputs')
      elif u_pass != c_pass:
         st.warning('Please confirm the password')
      else:
         st.success('Form Submitted Successfully')
         st.divider()
         st.write('> ## REGISTRATION DATA')
         if m_name == '':
            st.write('Name: ', f_name , ' ', l_name)
         else:
            st.write('Name: ', f_name , ' ',m_name, ' ', l_name) 
         st.write("Email: ", email)
         st.write("Password: ", u_pass)
         st.write('Birth Data: ', d,'-', m,'-',y)



