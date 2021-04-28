import streamlit as st
import scrapin as n
t = n.l
a="tomate"
recip = {}
def get_r(a):
    name=[]
    for i in t:
        if(i["ingredient"] == "ingredient"):
            ingreName=i["value"]
            for j in ingreName:
                if j == a:
                    name.append(i["key"]=='title')
                    name.append(ingreName)
                    return name


def main():
    st.title("Welcom to ELIMINAT DEIT")
    menu = ["Home", "Allergy food"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "home":
        st.subheader("Home")
    elif choice == "Allergy food":
        st.subheader("We will hepl you chose a menu that does not includ Allergic food reaction")
        name = st.sidebar.text_input('food')
        if st.sidebar.button("search"):
            st.subheader(get_r("{}".format(name)))

if __name__ == '__main__':
    main()