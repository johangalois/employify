import streamlit as st
from datetime import date
from src.preloaded import (DEPARTMENTS, ROLES)

def base_form_structure():
    
    return [
        {"name": "first_name", "label": "First Name", "type": "text", "required": True},
        {"name": "last_name", "label": "Last Name", "type": "text", "required": True },
        {"name": "email","label": "Email", "type": "text", "required": True},
        {"name": "role", "label":"Role", "type": "select", "required": True, "options": ROLES},
        {"name": "effective_date","label":"Effective date", "type": "date",  "default": date.today()}
    ]

def extra_fields_cs_support():
    
    return [
        {"name": "role_iso", "label": "Role Code", "type": "select", "options": ["CD", "ADV", "SP", "SPN", "N"]},
        {"name": "language", "label": "Language", "type": "select", "options": ["SP", "ENG", "FR", "IT", "MUL"]},
        {"name": "a_type", "label": "Type", "type": "select", "options": ["R", "F"]}
    ]


def extra_fields_customer_exp():
    
    return []


def extra_fields_qa():
    
    return []


def extra_fields_sales():
    
    return []



def department_fields(dept: str):
    d = (dept or "").strip().lower()
    if d in ("cs support"):
        return extra_fields_cs_support()
    if d in ("qa"):
        return extra_fields_qa()
    if d in ("customer experience"):
        return extra_fields_customer_exp()
    if d in ("sales"):
        return extra_fields_sales()
    return []  # fallback


def registration_form_structure(dept: str):
    """
        Returns the base fields + the extra fields.
    """

    return base_form_structure() + department_fields(dept)



def render_fields(fields, *, key_prefix ="ref"):
    
    values = {}
    for f in fields:
        name = f["name"]
        label = f.get("label", name)
        ftype = f.get("type", "text")
        k = f"{key_prefix}_{name}"

        if ftype == "text":
            values[name] = st.text_input(label, value=f.get("default", ""), key=k)
        elif ftype == "number":
            values[name] = st.number_input(
                label,
                value=f.get("default", 0),
                min_value=f.get("min_value", None),
                max_value=f.get("max_value", None),
                step=f.get("step", None),
                key=k,
            )
        elif ftype == "date":
            values[name] = st.date_input(label, value=f.get("default"), key=k)
        elif ftype == "select":
            opts = f.get("options", [])
            values[name] = st.selectbox(label, opts, index=0 if opts else None, key=k)
        elif ftype == "multiselect":
            opts = f.get("options", [])
            values[name] = st.multiselect(label, opts, default=f.get("default", []), key=k)
        elif ftype == "checkbox":
            values[name] = st.checkbox(label, value=f.get("default", False), key=k)
        else:
            values[name] = st.text_input(label, value=f.get("default", ""), key=k)

    return values


def validate_required(fields, values):
    missing = [
        f.get("label", f["name"])
        for f in fields
        if f.get("required") and not values.get(f["name"])
    ]
    return missing