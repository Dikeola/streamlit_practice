import streamlit as st

def main():
  st.title("Interactive Pizza Customizer")
  size = st.radio("What Size?",["Small", "Medium", "Large"])
  toppings = st.multiselect("What toppings?",["Pepperoni", "Mushrooms", "Onions", "Peppers", "Olives", "Extra Cheese"])
  crust = st.selectbox("What crust?",["Thin Crust", "Thick Crust", "Stuffed Crust"])
  extra = st.checkbox("Add garlic dip?", ["Yes", "No"])

  if st.button("Display Order"):
    st.write(f"You ordered a {size} pizza on {crust} Crust.")
    st.write(f"Toppings: {toppings}")
    st.write("Garlic Dip included: {extra}.")
if __name__ == "__main__":
  main()
