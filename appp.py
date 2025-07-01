import streamlit as st
from prediction import load_model_and_preprocessor, make_prediction

def main():
    st.title("Student Performance Prediction")

    # Load models and preprocessor once when app starts
    model, preprocessor = load_model_and_preprocessor()

    # Input form for user
    gender = st.selectbox("Gender", ["female", "male"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_education = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", "associate's degree",
        "bachelor's degree", "master's degree"])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation = st.selectbox("Test Preparation Course", ["none", "completed"])
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)

    if st.button("Predict Math Score"):
        # Prepare input data dictionary
        input_data = {
            "gender": gender,
            "race_ethnicity": race_ethnicity,
            "parental_level_of_education": parental_education,
            "lunch": lunch,
            "test_preparation_course": test_preparation,
            "writing_score": writing_score,
            "reading_score": reading_score,
        }

        prediction = make_prediction(model, preprocessor, input_data)
        st.success(f"Predicted Math Score: {prediction:.2f}")

if __name__ == "__main__":
    main()
 