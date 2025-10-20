# pages/2_Employee_Registration_(Phase_2).py
import streamlit as st
from datetime import date
import pandas as pd
from src.preloaded import DEPARTMENTS
from src.registration import (
    registration_form_structure,
    render_fields,
    validate_required,
)

st.title("Employee Registration")


@st.dialog("Registration")
def open_registration_dialog(dept: str):
    st.write(f"**Department:** {dept}")

    fields = registration_form_structure(dept)

    with st.form("employee_registration_form"):  # form key distinct from session key
        values = render_fields(fields, key_prefix=f"reg_{dept.lower()}")
        submitted = st.form_submit_button("Submit")

    if submitted:
        missing = validate_required(fields, values)
        if missing:
            st.error("Please fill required fields: " + ", ".join(missing))
            return

        data = {"department": dept, **values}
        # Persist safely (session key different from form key)
        st.session_state["employee_registration_data"] = data
        st.success("Employee registered.")
        st.rerun()

# --- Page body ---
with st.container():
    dept = st.selectbox("Department", DEPARTMENTS, index=None, placeholder="Choose a department…")

    if dept and st.button("Open registration"):
        open_registration_dialog(dept)

    if st.session_state.get("employee_registration_data"):
        st.divider()
        st.subheader("Last registration (session)")
        st.json(st.session_state["employee_registration_data"])
