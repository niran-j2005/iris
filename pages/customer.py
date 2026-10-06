import streamlit as st

st.title("Customer Details")

st.write("Please enter your details below.")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=21
)

city = st.text_input("City")

purpose = st.selectbox(
    "Purpose of using this application",
    [
        "Learning",
        "Academic Project",
        "Research",
        "Other"
    ]
)

comments = st.text_area("Additional Comments")

submit = st.button("Submit Details")

if submit:

    if name == "" or email == "":
        st.warning("Please enter your name and email.")

    else:
        st.success("Your details have been submitted successfully!")

        st.write("### Submitted Details")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Phone:", phone)
        st.write("Age:", age)
        st.write("City:", city)
        st.write("Purpose:", purpose)
        st.write("Comments:", comments)
