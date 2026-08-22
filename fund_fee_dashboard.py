import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fund Fees Overview", page_icon="📊", layout="wide")

funds = pd.DataFrame(
    [
        {
            "Fund": "Fidelity Blue Chip Growth Fund",
            "Ticker": "FBGRX",
            "Style": "Large-Cap Growth",
            "Approach": "Actively managed growth-stock fund focused on blue-chip companies.",
            "Net Expense Ratio": 0.0061,
            "Gross / Operating Expense": 0.0061,
            "Waiver": "None shown",
            "Fee Date": "Sep. 29, 2025",
        },
        {
            "Fund": "MFS Mid Cap Value R6",
            "Ticker": "MVCKX",
            "Style": "Mid-Cap Value",
            "Approach": "Actively managed fund investing primarily in medium-sized value-oriented companies.",
            "Net Expense Ratio": 0.0061,
            "Gross / Operating Expense": 0.0062,
            "Waiver": "0.01% contractual management-fee waiver through Jan. 31, 2027",
            "Fee Date": "Jan. 28, 2026",
        },
        {
            "Fund": "Dodge & Cox Stock X",
            "Ticker": "DOXGX",
            "Style": "Large Value",
            "Approach": "Actively managed diversified equity fund seeking long-term growth and income.",
            "Net Expense Ratio": 0.0041,
            "Gross / Operating Expense": 0.0046,
            "Waiver": "0.05% contractual expense-ratio waiver through Apr. 30, 2029",
            "Fee Date": "May 1, 2026",
        },
        {
            "Fund": "Vanguard Institutional Index I",
            "Ticker": "VINIX",
            "Style": "Large Blend / S&P 500 Index",
            "Approach": "Index fund designed to track the S&P 500 through broad exposure to large U.S. companies.",
            "Net Expense Ratio": 0.0004,
            "Gross / Operating Expense": 0.0004,
            "Waiver": "None shown",
            "Fee Date": "Apr. 28, 2026",
        },
    ]
)

st.title("Fund Introduction & Fee Comparison")
st.caption("A basic overview of four funds and the ongoing expenses reported in their fund materials.")

st.info(
    "Expense ratios are annual operating expenses deducted from fund assets. "
    "They are not typically billed as a separate charge. This dashboard is educational, not investment advice."
)

st.subheader("Funds at a glance")
for _, fund in funds.iterrows():
    with st.expander(f"{fund['Fund']} ({fund['Ticker']})", expanded=False):
        st.write(f"**Investment style:** {fund['Style']}")
        st.write(f"**Basic approach:** {fund['Approach']}")
        st.write(f"**Net expense ratio:** {fund['Net Expense Ratio']:.2%}")
        st.write(f"**Total annual operating expense:** {fund['Gross / Operating Expense']:.2%}")
        st.write(f"**Waiver information:** {fund['Waiver']}")
        st.write(f"**Reported fee date:** {fund['Fee Date']}")
        st.write("**Sales charge / 12b-1 fee / redemption fee:** None shown in the supplied fund sheets.")

st.subheader("Fee comparison")
comparison = funds[["Fund", "Ticker", "Style", "Net Expense Ratio", "Gross / Operating Expense"]].copy()
comparison["Net Expense Ratio"] = comparison["Net Expense Ratio"].map("{:.2%}".format)
comparison["Gross / Operating Expense"] = comparison["Gross / Operating Expense"].map("{:.2%}".format)
st.dataframe(comparison, use_container_width=True, hide_index=True)

chart_data = funds.set_index("Ticker")[["Net Expense Ratio"]] * 100
st.bar_chart(chart_data)
st.caption("Net expense ratio, expressed as a percentage.")

st.subheader("Estimated annual fund expenses")
investment = st.number_input(
    "Investment amount ($)", min_value=0.0, value=10000.0, step=1000.0, format="%.2f"
)

costs = funds[["Fund", "Ticker", "Net Expense Ratio"]].copy()
costs["Estimated Annual Cost"] = investment * costs["Net Expense Ratio"]
costs["Net Expense Ratio"] = costs["Net Expense Ratio"].map("{:.2%}".format)
costs["Estimated Annual Cost"] = costs["Estimated Annual Cost"].map("${:,.2f}".format)
st.dataframe(costs, use_container_width=True, hide_index=True)

lowest = funds.loc[funds["Net Expense Ratio"].idxmin()]
st.success(
    f"Lowest reported net expense ratio: {lowest['Fund']} ({lowest['Ticker']}) at "
    f"{lowest['Net Expense Ratio']:.2%}."
)

st.subheader("How to interpret the fees")
st.markdown(
    """
- A **net expense ratio** reflects the ongoing annual expenses currently charged to fund assets.
- A **waiver** can temporarily reduce expenses; the net expense ratio may increase if the waiver expires and is not renewed.
- The calculation above is a simple one-year illustration. Actual costs vary with your account balance and the fund's changing expenses.
- Fund-level expenses do not necessarily include retirement-plan administrative fees, account fees, or brokerage transaction costs that may apply in your specific account.
"""
)

st.caption("Source: fund profiles supplied by the user. Verify current fees in the latest prospectus before investing.")
