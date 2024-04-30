import streamlit as st

def main():
    st.set_page_config(
        page_title="Thoughtful Homework",
        page_icon="🤡")
    
    width = st.number_input("Width")
    height = st.number_input("Height")
    length = st.number_input("Length")
    mass = st.number_input("Mass")
    submit = st.button("Submit")

    if submit:
        st.header(sort(width, height, length, mass))
    
def sort(width, height, length, mass):
  bulky = width >= 150 or height >= 150 or length >= 150 or (width * height * length) >= 1000000
  heavy = mass >= 20
  if bulky and heavy:
    return "REJECTED"
  elif bulky or heavy:
    return "SPECIAL"
  else:
    return "STANDARD"

if __name__ == "__main__":
    main()