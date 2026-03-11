import streamlit as st
from agent import generate_diet_plan
from tools import calculate_bmi, calorie_estimator

st.title("🥗 AI Diet Planner")

age = st.number_input("Age")
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
goal = st.selectbox("Goal", ["Weight Loss","Muscle Gain","Maintenance"])
diet = st.selectbox("Diet Type", ["Vegetarian","Vegan","Keto","Non-Vegetarian"])

if st.button("Generate Diet Plan"):

    bmi = calculate_bmi(weight, height)
    calories = calorie_estimator(weight, height, age)

    user_data = f"""
    Age: {age}
    Weight: {weight}
    Height: {height}
    Goal: {goal}
    Diet: {diet}
    BMI: {bmi}
    Estimated Calories: {calories}
    """

    result = generate_diet_plan(user_data)

    st.subheader("Your BMI")
    st.write(bmi)

    st.subheader("Estimated Calories")
    st.write(calories)

    st.subheader("AI Diet Plan")
    st.write(result)
