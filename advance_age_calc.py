import streamlit as st
from datetime import date
from calendar import monthrange

def welcome_page():
    st.title(":blue[Welcome to Age Calculator App!]",width='content')
    # st.title("_Streamlit_ is :blue[cool] :sunglasses:")
    st.subheader("Your friendly tool to calculate age and more.")
    st.image(r"cute_monkey.png", width=200)
    
    st.write("This app is designed to help you calculate your age based on your birth year.")
    dob = st.date_input("Select your birth date:",
                        min_value=date(1900, 1, 1),max_value=date(2100, 12, 31))
    if dob:
        try:
            today = date.today()
            years = today.year - dob.year
            months = today.month - dob.month
            days = today.day - dob.day

            if days < 0:
                months -= 1
                # Get days in previous month
                prev_month = today.month - 1 or 12
                prev_year = today.year if today.month > 1 else today.year - 1
                
                days += monthrange(prev_year, prev_month)[1]

            if months < 0:
                years -= 1
                months += 12

            st.write(f"You are {years} years, {months} months, and {days} days old!")





            # today = date.today()
            # age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            # st.write(f"You are {age} years old!")
            st.success("This is a success message!")
        except Exception as e: 
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please select your birth date to calculate your age.")
        

    
    


if __name__ == "__main__":
    welcome_page()