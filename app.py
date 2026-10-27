
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.set_page_config(
    page_title="WasteWise | Sustainability Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --green: #83d69b;
    --green-dark: #245b42;
    --bg: #0c1411;
    --panel: #141f19;
    --border: #29392f;
    --muted: #9aaca0;
}

.stApp {
    background: var(--bg);
    color: #f3f7f3;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background: #101a14;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    letter-spacing: -0.7px;
}

h1 { font-size: 2.2rem !important; }
h2 { font-size: 1.35rem !important; }
h3 { font-size: 1.05rem !important; }

.eyebrow {
    color: var(--green);
    text-transform: uppercase;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.subtitle {
    color: var(--muted);
    font-size: 0.95rem;
    margin-top: -8px;
    margin-bottom: 24px;
}

.kpi {
    background: linear-gradient(145deg, #19271e, #131d17);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 21px 22px;
    min-height: 145px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.kpi-label {
    color: #a9b9ad;
    font-size: 0.83rem;
    font-weight: 500;
}

.kpi-value {
    color: #f6faf6;
    font-family: 'Manrope', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    margin: 11px 0 4px;
    line-height: 1.2;
}

.kpi-note {
    color: var(--green);
    font-size: 0.77rem;
}

.panel {
    background: #141f19;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 20px 22px;
    margin-bottom: 16px;
}

.hero {
    background: linear-gradient(115deg, #1b3927, #17251c 65%, #182a20);
    border: 1px solid #34583e;
    border-radius: 20px;
    padding: 27px 30px;
    margin: 20px 0 26px;
}

.hero-tag {
    display: inline-block;
    background: #284c34;
    color: #a9edb8;
    border: 1px solid #416d4a;
    border-radius: 30px;
    padding: 5px 11px;
    font-size: 0.74rem;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: 1.65rem;
    font-weight: 800;
    line-height: 1.35;
    margin-bottom: 8px;
}

.hero-copy {
    color: #c1d3c5;
    max-width: 650px;
    line-height: 1.7;
    font-size: 0.91rem;
}

div.stButton > button[kind="primary"] {
    background: var(--green);
    color: #102016;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 43px;
}

div.stButton > button[kind="primary"]:hover {
    background: #a2eab3;
    color: #102016;
}

div[data-testid="stForm"] {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 12px;
}

hr {
    border-color: var(--border);
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- DEMO DATA ----------
# These sample records are for UI preview only.
demo = pd.DataFrame([
    {"Date": "2026-10-20", "Meal": "Breakfast", "Food": "Poha", "Prepared": 18, "Served": 15, "Wasted": 3},
    {"Date": "2026-10-20", "Meal": "Lunch", "Food": "Rice", "Prepared": 30, "Served": 26, "Wasted": 4},
    {"Date": "2026-10-21", "Meal": "Breakfast", "Food": "Paratha", "Prepared": 22, "Served": 19, "Wasted": 3},
    {"Date": "2026-10-21", "Meal": "Lunch", "Food": "Dal", "Prepared": 16, "Served": 14, "Wasted": 2},
    {"Date": "2026-10-22", "Meal": "Dinner", "Food": "Rice", "Prepared": 25, "Served": 21, "Wasted": 4},
    {"Date": "2026-10-23", "Meal": "Lunch", "Food": "Vegetables", "Prepared": 14, "Served": 12, "Wasted": 2},
    {"Date": "2026-10-24", "Meal": "Dinner", "Food": "Roti", "Prepared": 20, "Served": 18, "Wasted": 2},
])

demo["Date"] = pd.to_datetime(demo["Date"])
demo["Waste %"] = (demo["Wasted"] / demo["Prepared"] * 100).round(1)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("##  WasteWise")
    st.caption("FOOD WASTE INTELLIGENCE")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["🏠  Overview", "📝  Add Record", "📊  Analytics", "📋  All Records"],
        label_visibility="visible",
    )

    st.divider()
    st.markdown("### 🌍 Our mission")
    st.caption(
        "Turn everyday food-waste data into smarter preparation "
        "decisions and a more sustainable campus."
    )
    st.divider()
    st.caption("PROJECT STATUS")
    st.markdown("🟢 Dashboard preview")
    st.caption("Version 0.1 · Built with Python")

# ---------- SHARED METRICS ----------
total_prepared = float(demo["Prepared"].sum())
total_wasted = float(demo["Wasted"].sum())
total_served = float(demo["Served"].sum())
waste_pct = total_wasted / total_prepared * 100 if total_prepared else 0
estimated_saved = max(total_prepared - total_wasted, 0)

def kpi(label, value, note, icon):
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-label">{icon} &nbsp; {label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)

def chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#dce8de",
        font_family="DM Sans",
        margin=dict(l=8, r=8, t=25, b=8),
        legend_title_text="",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(
            gridcolor="#29392f",
            zeroline=False,
        ),
    )
    return fig

# ---------- OVERVIEW ----------
if page == "🏠  Overview":
    st.markdown('<div class="eyebrow">SUSTAINABILITY / DASHBOARD</div>', unsafe_allow_html=True)
    st.title("Good evening 👋")
    st.markdown(
        '<div class="subtitle">Here’s your food-waste snapshot. Small changes can make a big difference.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">🌿 MAKE EVERY MEAL COUNT</div>
        <div class="hero-title">Less waste. Better planning.<br>More sustainable meals.</div>
        <div class="hero-copy">
            Monitor food preparation, spot waste patterns, and discover
            opportunities to improve how much food your campus prepares.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Your impact at a glance")
    a, b, c, d = st.columns(4)

    with a:
        kpi("Food prepared", f"{total_prepared:.1f} kg", "Across sample records", "🍲")
    with b:
        kpi("Food wasted", f"{total_wasted:.1f} kg", "Leftover food recorded", "♻️")
    with c:
        kpi("Waste rate", f"{waste_pct:.1f}%", "Waste ÷ prepared × 100", "📉")
    with d:
        kpi("Food served", f"{total_served:.1f} kg", "Recorded as served", "🍽️")

    st.write("")
    left, right = st.columns([1.55, 1])

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 📈 Daily food waste")
        st.caption("Kilograms of leftover food in the sample dataset")
        daily = demo.groupby("Date", as_index=False)["Wasted"].sum()
        fig = px.area(
            daily, x="Date", y="Wasted",
            markers=True,
        )
        fig.update_traces(
            line=dict(color="#83d69b", width=3),
            fillcolor="rgba(131,214,155,0.13)",
            marker=dict(size=7),
        )
        fig.update_yaxes(title="Waste (kg)", rangemode="tozero")
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 🍛 Waste by food item")
        st.caption("Which foods contribute most to waste?")
        food_waste = demo.groupby("Food", as_index=False)["Wasted"].sum().sort_values("Wasted")
        fig = px.bar(
            food_waste, x="Wasted", y="Food",
            orientation="h",
            text="Wasted",
        )
        fig.update_traces(marker_color="#83d69b", textposition="outside")
        fig.update_xaxes(title="Waste (kg)", rangemode="tozero")
        fig.update_yaxes(title="")
        st.plotly_chart(chart_theme(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 💡 Smart insights")
    high_waste = demo.groupby("Food")["Wasted"].sum().idxmax()
    high_waste_amount = demo.groupby("Food")["Wasted"].sum().max()

    x, y = st.columns(2)
    with x:
        st.info(
            f"**Food to investigate:** {high_waste} has the highest total "
            f"recorded waste in this sample ({high_waste_amount:.1f} kg)."
        )
    with y:
        st.success(
            f"**Planning opportunity:** the sample waste rate is "
            f"{waste_pct:.1f}%. Review portions and preparation quantities "
            "before reducing production."
        )

    st.markdown("### 🕘 Recent records")
    recent = demo.sort_values("Date", ascending=False).head(5).copy()
    recent["Date"] = recent["Date"].dt.strftime("%d %b %Y")
    st.dataframe(
        recent[["Date", "Meal", "Food", "Prepared", "Served", "Wasted", "Waste %"]],
        use_container_width=True,
        hide_index=True,
    )

    st.caption("Demo data only — these figures are illustrative, not actual campus measurements.")

# ---------- ADD RECORD ----------
elif page == "📝  Add Record":
    st.markdown('<div class="eyebrow">DATA COLLECTION</div>', unsafe_allow_html=True)
    st.title("Add a food-waste record")
    st.markdown(
        '<div class="subtitle">Record what was prepared, served, and left over.</div>',
        unsafe_allow_html=True,
    )

    with st.form("food_record_form", clear_on_submit=True):
        record_date = st.date_input("Record date", value=date.today())
        meal = st.selectbox("Meal", ["Breakfast", "Lunch", "Dinner", "Snacks"])
        food = st.text_input("Food item", placeholder="e.g. Rice, Dal, Roti")
        st.caption("Enter all quantities in kilograms (kg).")
        c1, c2, c3 = st.columns(3)
        with c1:
            prepared = st.number_input("Prepared (kg)", min_value=0.0, step=0.5)
        with c2:
            served = st.number_input("Served (kg)", min_value=0.0, step=0.5)
        with c3:
            wasted = st.number_input("Wasted (kg)", min_value=0.0, step=0.5)

        submitted = st.form_submit_button("Save record", type="primary", use_container_width=True)

    if submitted:
        if not food.strip():
            st.error("Please enter a food item.")
        elif prepared <= 0:
            st.error("Prepared quantity must be greater than zero.")
        elif served + wasted > prepared + 1e-9:
            st.error("Served + wasted cannot exceed the prepared quantity.")
        else:
            st.success(
                f"Input validated! {food.strip()} — "
                f"{wasted:.1f} kg waste ({wasted / prepared * 100:.1f}%)."
            )
            st.warning(
                "This preview does not save records permanently yet. "
                "SQLite storage is the next development step."
            )

# ---------- ANALYTICS ----------
elif page == "📊  Analytics":
    st.markdown('<div class="eyebrow">DATA EXPLORATION</div>', unsafe_allow_html=True)
    st.title("Food waste analytics")
    st.markdown(
        '<div class="subtitle">Explore the sample dataset and find patterns.</div>',
        unsafe_allow_html=True,
    )

    start = st.date_input("Start date", value=demo["Date"].min().date(), key="start")
    end = st.date_input("End date", value=demo["Date"].max().date(), key="end")

    if start > end:
        st.error("Start date must be before or equal to end date.")
    else:
        filtered = demo[
            (demo["Date"].dt.date >= start) &
            (demo["Date"].dt.date <= end)
        ]

        if filtered.empty:
            st.warning("No sample records found for this date range.")
        else:
            c1, c2, c3 = st.columns(3)
            c1.metric("Prepared", f"{filtered['Prepared'].sum():.1f} kg")
            c2.metric("Wasted", f"{filtered['Wasted'].sum():.1f} kg")
            rate = filtered["Wasted"].sum() / filtered["Prepared"].sum() * 100
            c3.metric("Waste rate", f"{rate:.1f}%")

            meal_waste = filtered.groupby("Meal", as_index=False)["Wasted"].sum()
            fig = px.bar(
                meal_waste, x="Meal", y="Wasted", text="Wasted",
                title="Waste by meal",
            )
            fig.update_traces(marker_color="#83d69b", textposition="outside")
            st.plotly_chart(chart_theme(fig), use_container_width=True)

            st.markdown("### Detailed sample records")
            st.dataframe(filtered, use_container_width=True, hide_index=True)

# ---------- ALL RECORDS ----------
elif page == "📋  All Records":
    st.markdown('<div class="eyebrow">RECORD MANAGEMENT</div>', unsafe_allow_html=True)
    st.title("All food-waste records")
    st.markdown(
        '<div class="subtitle">Review and export the illustrative records.</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(demo, use_container_width=True, hide_index=True)

    csv = demo.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Download sample records as CSV",
        data=csv,
        file_name="wastewise_sample_records.csv",
        mime="text/csv",
        type="primary",
    )

st.divider()
st.caption(" WasteWise · Smart Food Waste Analytics · Built with Streamlit and Python")
