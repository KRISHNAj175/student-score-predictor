
import streamlit as st
import pandas as pd
import joblib

# ---------- Page configuration ----------
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------- Load model ----------
@st.cache_resource
def load_model():
    return joblib.load("student_model.pkl")

model = load_model()

# ---------- Header ----------
st.title("🎓 Student Score Predictor")
st.markdown(
    "### Predict academic performance using machine learning"
)
st.caption(
    "Enter the student's details to estimate their final exam score."
)

st.divider()

# ---------- Sidebar inputs ----------
st.sidebar.header("📝 Student Details")
st.sidebar.write("Adjust the values below.")

study_hours = st.sidebar.slider(
    "Study Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=5.0,
    step=0.5
)

attendance = st.sidebar.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=85
)

previous_score = st.sidebar.slider(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=75
)

assignment_score = st.sidebar.slider(
    "Assignment Score",
    min_value=0,
    max_value=100,
    value=80
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)

predict_button = st.sidebar.button(
    "Predict Final Score",
    type="primary",
    use_container_width=True
)

# ---------- Main dashboard ----------
left, right = st.columns([2, 1])

with left:
    st.subheader("Performance Overview")
    st.write(
        "Your prediction is based on the five student "
        "features entered in the sidebar."
    )

    if predict_button:
        new_student = pd.DataFrame({
            "study_hours": [study_hours],
            "attendance": [attendance],
            "previous_score": [previous_score],
            "assignment_score": [assignment_score],
            "sleep_hours": [sleep_hours]
        })

        prediction = float(model.predict(new_student)[0])

        # Keep display within the expected score range
        display_score = max(0, min(100, prediction))

        st.metric(
            label="Predicted Final Score",
            value=f"{display_score:.2f} / 100"
        )

        st.progress(display_score / 100)

        if display_score >= 75:
            st.success("The model predicts a high score.")
        elif display_score >= 50:
            st.info("The model predicts a moderate score.")
        else:
            st.warning(
                "The model predicts a lower score. "
                "Use this estimate as a starting point for review."
            )

        st.caption(
            "This is a model estimate, not a guaranteed exam result."
        )
    else:
        st.info(
            "Choose the student details in the sidebar, "
            "then click **Predict Final Score**."
        )

with right:
    st.subheader("Student Profile")

    st.write(f"📚 **Study:** {study_hours} hours/day")
    st.write(f"📅 **Attendance:** {attendance}%")
    st.write(f"📝 **Previous score:** {previous_score}/100")
    st.write(f"✍️ **Assignment:** {assignment_score}/100")
    st.write(f"😴 **Sleep:** {sleep_hours} hours/day")

st.divider()

st.caption(
    "Student Score Predictor | Built with Python, "
    "Scikit-learn and Streamlit"
)
