import streamlit as st

# Store balance in session
if "balance" not in st.session_state:
    st.session_state.balance = 0

st.title("🏦 Bank Account Simulator")

option = st.selectbox("Choose Action", ["Deposit", "Withdraw", "Check Balance"])

if option == "Deposit":
    amount = st.number_input("Enter amount", min_value=0)
    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"Deposited ₹{amount}")

elif option == "Withdraw":
    amount = st.number_input("Enter amount", min_value=0)
    if st.button("Withdraw"):
        if amount > st.session_state.balance:
            st.error("Insufficient balance")
        else:
            st.session_state.balance -= amount
            st.success(f"Withdrawn ₹{amount}")

elif option == "Check Balance":
    st.info(f"Current Balance: ₹{st.session_state.balance}")