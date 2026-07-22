import streamlit as st
import pandas as pd

# -------------------------------
# Load Data
# -------------------------------
career = pd.read_csv("career_roles.csv")
resources = pd.read_csv("learning_resources.csv")

career["required_skill"] = career["required_skill"].str.lower().str.strip()
resources["skill"] = resources["skill"].str.lower().str.strip()

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="SKILLUP by Aditya",
    page_icon="🚀",
    layout="wide"
)

st.title(" SKILLUP by Aditya ")
st.write("Enter your current skills and get career recommendations.")

# -------------------------------
# User Input
# -------------------------------
skills = st.text_input(
    "Enter Skills (Comma Separated)",
    placeholder="Python, SQL"
)

# -------------------------------
# Recommendation
# -------------------------------
if st.button("Recommend Career"):

    if skills == "":
        st.warning("Please enter your skills.")
        st.stop()

    user_skills = [
        s.strip().lower()
        for s in skills.split(",")
    ]

    recommended_roles = []

    for role in career["role"].unique():

        req = career[
            career["role"] == role
        ]["required_skill"].tolist()

        matched = len(set(user_skills) & set(req))

        score = matched / len(req)

        if matched > 0:

            recommended_roles.append(
                (role, score, req)
            )

    recommended_roles.sort(
        key=lambda x: x[1],
        reverse=True
    )

    if len(recommended_roles) == 0:
        st.error("No matching career found.")
        st.stop()

    st.subheader("🎯 Recommended Careers")

    for role, score, req in recommended_roles:

        st.success(f"{role}")

        st.progress(score)

        st.write(f"**Match Score : {round(score*100,2)} %**")

        missing = list(
            set(req) - set(user_skills)
        )

        st.write("### Missing Skills")

        for skill in missing:

            st.write("❌", skill)

        st.write("### Learning Resources")

        rec = resources[
            resources["skill"] == skill.lower()
        ]

        if len(rec) == 0:

            st.info("No Resource Available")

        else:

            for _, row in rec.iterrows():

                st.write(
                    f"📚 **{row['platform']}**  \n"
                    f"{row['resource']}  \n"
                    f"Difficulty : {row['difficulty']}"
                )

        st.divider()
