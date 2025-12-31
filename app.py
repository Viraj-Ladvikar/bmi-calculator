import streamlit as st 


# This "set_page_config" is use to set Browser tab title, Icons, layout of page 
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="wide" # → full width layout
)

# st.title --> Purpose: Main page title (BIGGEST text)
st.title("⚖️BMI Calculator") # Streamlit does NOT provide a built-in way to center st.title().

# st.markdown(
#     "<h1 style='text-align:center'>⚖️BMI Calculator</h1>",
#     unsafe_allow_html=True
# )


st.html("<p>This app calculates your <b>Body Mass Index (BMI)</b></p>")

# Initialize session state
if "height" not in st.session_state:
    st.session_state.height = 0.0

if "weight" not in st.session_state:
    st.session_state.weight = 0.0
user_height = st.number_input("Enter your height in cm",min_value=0.0,key="height",placeholder="height in cm")

user_weight = st.number_input("Enter your weight in kg",min_value=0.0,key="weight",placeholder="weight in kg")


with st.container(horizontal=True):
    calculate = st.button("Calculate",type="primary")
    reset = st.button("reset",type="secondary")
    
if calculate:
    if user_weight and user_height:
        
            
            height_m = user_height/100
            user_bmi =   bmi = user_weight / (height_m ** 2)


            st.subheader(f"Your BMI is : {user_bmi}")

            if user_bmi <18.5:
                st.warning("You are underweight 🥦")
            elif 18.5 <= user_bmi < 24.9:
                st.success("You have normal weight ✅") 
            elif 25<= user_bmi < 29.9:
                st.warning("You are overweight ⚠️")
            else:
                st.error("You are obese 🚨")
    else:
            st.badge("Enter vaild height and weight",color='red')

if reset:
    st.session_state.height = 0.0
    st.session_state.weight = 0.0
    