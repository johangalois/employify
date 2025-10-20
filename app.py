import pandas as pd
import matplotlib.pyplot as plt
from common_ui import nav_pages,inject_sticky_footer_css, header, footer
import streamlit as st

#notas por aquí

header(
    title="Home",
    subtitle="Clients Data",
    # logo_url="",
    # nav_items=[("Code", "#"), ("Issues", "#"), ("Pull requests", "#"), ("Actions", "#")],
    right_html="<span style='opacity:.7;font-size:.9rem;'>v0.0.1</span>",
)

st.set_page_config(page_title= 'Holafly Admin', layout = 'wide')

pg = nav_pages()
pg.run()

inject_sticky_footer_css()


footer("© 2025 My Org", links={"Status":"#", "Docs":"#", "Privacy":"#", "Contact":"mailto:hello@example.com"})
