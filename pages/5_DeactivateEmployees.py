import streamlit as st

st.title("Deactivate Employee")

st.markdown("Use this form to deactivate an employee from the system.")

# Dictionary
team_options = {
    "Customer Support": ["AMER", "EMEA", "APAC"],
    "Experience": ["Disputes", "Refunds", "NPS"],
    "Quality": ["Quality"]
}
#department dropdown
department = st.selectbox(
    "Department",
    ["--"] + list(team_options.keys()),
    index=0,
    key="department"
)

# according to department, show team options
if department != "--":
    team = st.selectbox(
        "Team",
        ["--"] + team_options[department],
        index=0,
        key="team"
    )
else:
    team = st.selectbox(
        "Team",
        ["--"],
        index=0,
        key="team"
    )

# Form to deactivate employee
with st.form("deactivate_form"):
    manager = st.text_input("Manager Name")
    email = st.text_input("Employee Email")

    submitted = st.form_submit_button("Set as inactive")

    if submitted:
        if email.strip() == "" or department == "--" or team == "--":
            st.error("Please complete all required fields before deactivating.")
        else:
            st.success(f"Employee with email **{email}** has been set as inactive ✅")