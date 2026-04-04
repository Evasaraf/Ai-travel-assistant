import streamlit as st
from groq import Groq

# 🔑 Setup Groq
client = Groq(api_key="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")

st.title("✈️ AI Travel Assistant")

# Inputs
destination = st.text_input("Enter Destination")
days = st.slider("Number of Days", 1, 10)
budget = st.number_input("Total Budget (₹)", min_value=1000)
people = st.number_input("Number of People", min_value=1)

# Generate Plan
if st.button("Generate Plan"):

    if destination == "":
        st.warning("Enter destination")
    else:
        with st.spinner("Generating..."):

            prompt = f"""
            Create a detailed travel plan for {destination}.

            Include:
            - Day-wise itinerary for {days} days
            - Famous places
            - Must-visit spots
            - Food and eateries
            - Best time to visit

            Budget: {budget}
            People: {people}
            """

            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response.choices[0].message.content)

# ---------------- SCAM DETECTOR ---------------- #
st.subheader("🚨 Scam Detector")

deal = st.text_area("Paste deal")

if st.button("Check Scam"):

    if deal:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{
                "role": "user",
                "content": f"Check if this is a scam and explain: {deal}"
            }]
        )

        st.write(response.choices[0].message.content)

# ---------------- CHAT ---------------- #
st.subheader("💬 Ask AI")

query = st.text_input("Ask something")

if st.button("Ask"):

    if query:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": query}]
        )

        st.write(response.choices[0].message.content)