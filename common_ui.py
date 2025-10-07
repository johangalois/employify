# common_ui.py
from typing import Iterable, Optional, Tuple, Dict
import streamlit as st

def inject_sticky_footer_css() -> None:
    """
    Layout:
      - Main Streamlit block-container becomes a flex column with min-height:100vh
      - Header is sticky (optional; remove 'position:sticky' if you want it normal)
      - Footer is static and pushed to the bottom via margin-top:auto
      - No white bars in dark mode (transparent backgrounds + subtle borders)
    """
    st.markdown("""
<style>
  :root{
    --header-h: 56px;
    --pad-x: 16px;
    --gh-border: rgba(140,149,159,.24); /* subtle, theme-friendly */
  }

  /* Make page a flex column so footer can sit at bottom on short pages */
  [data-testid="stAppViewContainer"] .main .block-container{
    display: flex !important;
    flex-direction: column;
    min-height: 100vh;
    padding-top: calc(var(--header-h) + 12px) !important; /* space for sticky header */
    padding-bottom: 12px !important;
    gap: 0.75rem;
  }

  /* ===== Header (sticky) ===== */
  .app-header{
    position: sticky; top: 0; left: 0; right: 0;
    z-index: 100;
    background: transparent;
    border-bottom: 1px solid var(--gh-border);
    min-height: var(--header-h);
    display: flex; align-items: center;
    padding: 8px var(--pad-x);
  }
  .app-header-inner{
    width: 100%;
    display: grid;
    grid-template-columns: auto 1fr auto; /* logo | title+nav | right */
    gap: 12px; align-items: center;
  }
  .app-logo img{ height:24px; display:block; }
  .app-title{ font-weight:600; font-size:1rem; margin:0; }
  .app-subtitle{ opacity:.7; font-size:.9rem; margin-left:8px; }
  .app-nav{ display:inline-flex; gap:16px; flex-wrap:wrap; font-size:.95rem; }
  .app-nav a{ text-decoration:none; }
  .app-right{ display:inline-flex; gap:10px; align-items:center; }

  /* ===== Footer (STATIC, bottom via flex) ===== */
  .app-footer{
    margin-top: auto;                /* <-- pushes footer to bottom on short pages */
    background: transparent;
    border-top: 1px solid var(--gh-border);
    padding: 12px var(--pad-x);
    font-size: .95rem;
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
  }
  .app-footer a{ text-decoration:none; }
  .app-footer .divider{ opacity:.55; padding: 0 8px; }

  /* Hide Streamlit's default footer */
  footer { visibility: hidden; }

  /* Responsiveness */
  @media (max-width: 800px){
    :root{ --header-h: 52px; --pad-x: 12px; }
    .app-subtitle{ display:none; }
    .app-header-inner{ grid-template-columns: auto 1fr; }
    .app-right{ display:none; }
  }
</style>
    """, unsafe_allow_html=True)

def header(
    title: str,
    subtitle: str = "",
    *,
    logo_url: str = "",
    nav_items: Optional[Iterable[Tuple[str, str]]] = None,
    right_html: str = "",
) -> None:
    """Render a slim, GitHub-ish header (sticky)."""
    if nav_items is None:
        nav_items = []
    nav_html = "".join(f"<a href='{href}' target='_self'>{label}</a>" for label, href in nav_items)

    html = f"""
<div class="app-header">
  <div class="app-header-inner">
    <div class="app-logo">{f"<img src='{logo_url}' alt='logo'/>" if logo_url else ""}</div>
    <div>
      <span class="app-title">{title}</span>
      {f"<span class='app-subtitle'> — {subtitle}</span>" if subtitle else ""}
      <div class="app-nav">{nav_html}</div>
    </div>
    <div class="app-right">{right_html or ""}</div>
  </div>
</div>
"""
    st.markdown(html, unsafe_allow_html=True)

def footer(left_text: str, links: Optional[Dict[str, str]] = None) -> None:
    """Render a static footer that stays at the end of the page (not fixed)."""
    parts = []
    if links:
        for i, (name, url) in enumerate(links.items()):
            if i: parts.append("<span class='divider'>|</span>")
            parts.append(f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{name}</a>")
    link_html = (" " + "".join(parts)) if parts else ""
    st.markdown(f"<div class='app-footer'><span>{left_text}</span>{link_html}</div>", unsafe_allow_html=True)
