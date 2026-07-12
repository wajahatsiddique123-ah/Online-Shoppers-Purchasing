import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Page Settings
st.set_page_config(
    page_title="Online Shoppers Purchase Predictor",
    page_icon="🛒",
    layout="centered"
)

# Title
st.title("🛍️ Online Shoppers Purchase Predictor")
st.write("Predict whether a customer is likely to purchase a product.")

st.divider()

# ==========================
# User Inputs
# ==========================

administrative = st.number_input("Administrative Pages", min_value=0, value=2)

administrative_duration = st.number_input(
    "Administrative Duration", min_value=0.0, value=20.0
)

informational = st.number_input("Informational Pages", min_value=0, value=1)

informational_duration = st.number_input(
    "Informational Duration", min_value=0.0, value=5.0
)

product_related = st.number_input(
    "Product Related Pages", min_value=0, value=50
)

product_related_duration = st.number_input(
    "Product Related Duration", min_value=0.0, value=1000.0
)

bounce_rates = st.number_input(
    "Bounce Rate", min_value=0.0, max_value=1.0, value=0.02
)

exit_rates = st.number_input(
    "Exit Rate", min_value=0.0, max_value=1.0, value=0.05
)

page_values = st.number_input(
    "Page Value", min_value=0.0, value=0.0
)

special_day = st.slider(
    "Special Day",
    0.0,
    1.0,
    0.0
)

month = st.selectbox(
    "Month",
    ["Feb","Mar","May","June","Jul","Aug","Sep","Oct","Nov","Dec"]
)

operating_system = st.selectbox(
    "Operating System",
    [1,2,3,4,5,6,7,8]
)

browser = st.selectbox(
    "Browser",
    list(range(1,14))
)

region = st.selectbox(
    "Region",
    list(range(1,10))
)

traffic_type = st.selectbox(
    "Traffic Type",
    list(range(1,21))
)

visitor_type = st.selectbox(
    "Visitor Type",
    ["New_Visitor","Returning_Visitor","Other"]
)

weekend = st.selectbox(
    "Weekend",
    ["No","Yes"]
)

# ==========================
# Encoding
# ==========================

month_map = {
    "Feb":0,
    "Mar":1,
    "May":2,
    "June":3,
    "Jul":4,
    "Aug":5,
    "Sep":6,
    "Oct":7,
    "Nov":8,
    "Dec":9
}

visitor_map = {
    "New_Visitor":0,
    "Returning_Visitor":1,
    "Other":2
}

weekend_map = {
    "No":0,
    "Yes":1
}

input_data = pd.DataFrame({
    "Administrative":[administrative],
    "Administrative_Duration":[administrative_duration],
    "Informational":[informational],
    "Informational_Duration":[informational_duration],
    "ProductRelated":[product_related],
    "ProductRelated_Duration":[product_related_duration],
    "BounceRates":[bounce_rates],
    "ExitRates":[exit_rates],
    "PageValues":[page_values],
    "SpecialDay":[special_day],
    "Month":[month_map[month]],
    "OperatingSystems":[operating_system],
    "Browser":[browser],
    "Region":[region],
    "TrafficType":[traffic_type],
    "VisitorType":[visitor_map[visitor_type]],
    "Weekend":[weekend_map[weekend]]
})

# ==========================
# Prediction
# ==========================

if st.button("Predict Purchase"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Customer is likely to make a purchase.")
        st.balloons()
    else:
        st.error("❌ Customer is not likely to make a purchase.")

st.divider()

st.caption("Developed by Wajahat Ahmed Siddiqui")
