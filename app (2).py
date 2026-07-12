import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Online Shoppers Purchase Intention Predictor",
    page_icon="🛒",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -----------------------------
# Title
# -----------------------------
st.title("🛍️ Online Shoppers Purchase Intention")
st.write(
    "Predict whether an online shopper will generate **Revenue** based on browsing behaviour."
)

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

Administrative = st.number_input("Administrative", 0, 30, 2)

Administrative_Duration = st.number_input(
    "Administrative Duration", 0.0, 500.0, 20.0
)

Informational = st.number_input("Informational", 0, 30, 0)

Informational_Duration = st.number_input(
    "Informational Duration", 0.0, 500.0, 0.0
)

ProductRelated = st.number_input(
    "Product Related Pages", 0, 800, 50
)

ProductRelated_Duration = st.number_input(
    "Product Related Duration", 0.0, 5000.0, 1000.0
)

BounceRates = st.number_input(
    "Bounce Rate",
    0.0,
    1.0,
    0.02,
    format="%.4f"
)

ExitRates = st.number_input(
    "Exit Rate",
    0.0,
    1.0,
    0.05,
    format="%.4f"
)

PageValues = st.number_input(
    "Page Value",
    0.0,
    500.0,
    0.0
)

SpecialDay = st.slider(
    "Special Day",
    0.0,
    1.0,
    0.0
)

Month = st.selectbox(
    "Month",
    [
        "Feb","Mar","May","June",
        "Jul","Aug","Sep","Oct",
        "Nov","Dec"
    ]
)

OperatingSystems = st.selectbox(
    "Operating System",
    [1,2,3,4,5,6,7,8]
)

Browser = st.selectbox(
    "Browser",
    [1,2,3,4,5,6,7,8,9,10,11,12,13]
)

Region = st.selectbox(
    "Region",
    [1,2,3,4,5,6,7,8,9]
)

TrafficType = st.selectbox(
    "Traffic Type",
    list(range(1,21))
)

VisitorType = st.selectbox(
    "Visitor Type",
    [
        "Returning_Visitor",
        "New_Visitor",
        "Other"
    ]
)

Weekend = st.selectbox(
    "Weekend",
    ["False","True"]
)

# -----------------------------
# Encoding
# -----------------------------

month_dict = {
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

visitor_dict = {
    "New_Visitor":0,
    "Other":1,
    "Returning_Visitor":2
}

weekend_dict = {
    "False":0,
    "True":1
}

data = pd.DataFrame({
    "Administrative":[Administrative],
    "Administrative_Duration":[Administrative_Duration],
    "Informational":[Informational],
    "Informational_Duration":[Informational_Duration],
    "ProductRelated":[ProductRelated],
    "ProductRelated_Duration":[ProductRelated_Duration],
    "BounceRates":[BounceRates],
    "ExitRates":[ExitRates],
    "PageValues":[PageValues],
    "SpecialDay":[SpecialDay],
    "Month":[month_dict[Month]],
    "OperatingSystems":[OperatingSystems],
    "Browser":[Browser],
    "Region":[Region],
    "TrafficType":[TrafficType],
    "VisitorType":[visitor_dict[VisitorType]],
    "Weekend":[weekend_dict[Weekend]]
})

scaled = scaler.transform(data)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔍 Predict"):

    prediction = model.predict(scaled)[0]

    if prediction == 1:
        st.success("✅ Customer is likely to Purchase (Revenue = TRUE)")
        st.balloons()

    else:
        st.error("❌ Customer is NOT likely to Purchase (Revenue = FALSE)")

st.markdown("---")
st.caption("Developed by Wajahat Ahmed Siddiqui")
