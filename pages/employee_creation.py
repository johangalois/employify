import streamlit as st
from common_ui import inject_sticky_footer_css, header, footer

st.set_page_config(page_title="Static Footer at Page End", layout="wide")

st.sidebar.header("Sidebar")
st.sidebar.write("Filters & controls go here.")

inject_sticky_footer_css()

header(
    title="my-org / my-repo",
    subtitle="analytics",
    # logo_url="https://your.cdn/logo.svg",
    nav_items=[("Code", "#"), ("Issues", "#"), ("Pull requests", "#"), ("Actions", "#")],
    right_html="<span style='opacity:.7;font-size:.9rem;'>v1.4.0</span>",
)

# Try both a short page and a long page to see behavior.
st.write("On short pages, the footer sits at the bottom of the viewport. On long pages, it's below all content.")
for i in range(6):
    st.write(f"Row {i+1}")

footer("© 2025 My Org", links={"Status":"#", "Docs":"#", "Privacy":"#", "Contact":"mailto:hello@example.com"})
