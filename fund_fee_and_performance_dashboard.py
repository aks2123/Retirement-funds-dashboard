import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fund Fees & Performance", page_icon="📊", layout="wide")

funds = pd.DataFrame([
    {"Fund": "Fidelity Blue Chip Growth Fund", "Ticker": "FBGRX", "Asset Class": "U.S. equity", "Style": "Large-Cap Growth", "Approach": "Actively managed blue-chip growth stocks.", "Net Expense Ratio": 0.0061, "Gross / Operating Expense": 0.0061, "Waiver": "None shown", "Fee Date": "Sep. 29, 2025", "YTD": None, "1 Year": 19.91, "3 Year": 37.62, "5 Year": 14.50, "10 Year": 19.53, "Since Inception": 13.39, "As Of": "Dec. 31, 2025"},
    {"Fund": "MFS Mid Cap Value R6", "Ticker": "MVCKX", "Asset Class": "U.S. equity", "Style": "Mid-Cap Value", "Approach": "Actively managed medium-sized value stocks.", "Net Expense Ratio": 0.0061, "Gross / Operating Expense": 0.0062, "Waiver": "0.01% contractual management-fee waiver through Jan. 31, 2027", "Fee Date": "Jan. 28, 2026", "YTD": 13.02, "1 Year": 19.57, "3 Year": 13.47, "5 Year": 9.27, "10 Year": 10.86, "Since Inception": 11.06, "As Of": "Jun. 30, 2026"},
    {"Fund": "Dodge & Cox Stock X", "Ticker": "DOXGX", "Asset Class": "U.S. equity", "Style": "Large Value", "Approach": "Actively managed diversified value-oriented equities.", "Net Expense Ratio": 0.0041, "Gross / Operating Expense": 0.0046, "Waiver": "0.05% contractual expense-ratio waiver through Apr. 30, 2029", "Fee Date": "May 1, 2026", "YTD": 3.86, "1 Year": 9.86, "3 Year": 14.10, "5 Year": None, "10 Year": None, "Since Inception": 11.39, "As Of": "Jun. 30, 2026"},
    {"Fund": "Vanguard Institutional Index I", "Ticker": "VINIX", "Asset Class": "U.S. equity", "Style": "Large Blend / S&P 500 Index", "Approach": "Index fund designed to track the S&P 500.", "Net Expense Ratio": 0.0004, "Gross / Operating Expense": 0.0004, "Waiver": "None shown", "Fee Date": "Apr. 28, 2026", "YTD": 10.19, "1 Year": 22.28, "3 Year": 20.57, "5 Year": 13.36, "10 Year": 15.47, "Since Inception": 11.04, "As Of": "Jun. 30, 2026"},
    {"Fund": "BrandywineGLOBAL High Yield IS", "Ticker": "BGHSX", "Asset Class": "Taxable bond", "Style": "High Yield Bond", "Approach": "Actively managed below-investment-grade corporate bonds.", "Net Expense Ratio": 0.0054, "Gross / Operating Expense": 0.0055, "Waiver": "0.01% contractual expense-ratio waiver through Dec. 31, 2027", "Fee Date": "May 1, 2026", "YTD": 1.04, "1 Year": 4.38, "3 Year": 8.35, "5 Year": 4.40, "10 Year": 7.36, "Since Inception": 7.70, "As Of": "Jun. 30, 2026"},
    {"Fund": "Vanguard Total Bond Market Index Adm", "Ticker": "VBTLX", "Asset Class": "Taxable bond", "Style": "Intermediate Core Bond", "Approach": "Index fund tracking broad U.S. investment-grade taxable bonds.", "Net Expense Ratio": 0.0004, "Gross / Operating Expense": 0.0004, "Waiver": "None shown", "Fee Date": "Apr. 28, 2026", "YTD": 0.74, "1 Year": 3.70, "3 Year": 4.16, "5 Year": 0.07, "10 Year": 1.50, "Since Inception": 3.35, "As Of": "Jun. 30, 2026"},
    {"Fund": "Vanguard Total International Bond Index Adm", "Ticker": "VTABX", "Asset Class": "Taxable bond", "Style": "Global Bond — USD Hedged", "Approach": "Index fund tracking investment-grade non-U.S. bonds with currency hedging.", "Net Expense Ratio": 0.0010, "Gross / Operating Expense": 0.0010, "Waiver": "None shown", "Fee Date": "Feb. 27, 2026", "YTD": 1.24, "1 Year": 2.37, "3 Year": 4.28, "5 Year": 0.45, "10 Year": 1.63, "Since Inception": 2.43, "As Of": "Jun. 30, 2026"},
    {"Fund": "iShares MSCI Total International Index K", "Ticker": "BDOKX", "Asset Class": "International equity", "Style": "Foreign Large Blend", "Approach": "Index fund tracking developed and emerging-market stocks outside the U.S.", "Net Expense Ratio": 0.0009, "Gross / Operating Expense": 0.0009, "Waiver": "None shown", "Fee Date": "Apr. 30, 2026", "YTD": 14.75, "1 Year": 28.27, "3 Year": 18.94, "5 Year": 8.78, "10 Year": 9.87, "Since Inception": 6.46, "As Of": "Jun. 30, 2026"},
    {"Fund": "PGIM Total Return Bond R6", "Ticker": "PTRQX", "Asset Class": "Taxable bond", "Style": "Total Return Bond", "Approach": "Fund profile supplied, but readable fee and performance data were not available in the uploaded OCR extract.", "Net Expense Ratio": None, "Gross / Operating Expense": None, "Waiver": "Verify in the current prospectus", "Fee Date": "Not available from extract", "YTD": None, "1 Year": None, "3 Year": None, "5 Year": None, "10 Year": None, "Since Inception": None, "As Of": "Not available"},
    {"Fund": "Vanguard Inflation-Protected Securities Adm", "Ticker": "VAIPX", "Asset Class": "Taxable bond", "Style": "Inflation-Protected Bond", "Approach": "Actively managed inflation-indexed bonds, primarily U.S. TIPS.", "Net Expense Ratio": 0.0010, "Gross / Operating Expense": 0.0010, "Waiver": "None shown", "Fee Date": "Apr. 28, 2026", "YTD": 1.22, "1 Year": 3.42, "3 Year": 3.94, "5 Year": 0.93, "10 Year": 2.46, "Since Inception": 3.32, "As Of": "Jun. 30, 2026"},
    {"Fund": "American Funds New World R-6", "Ticker": "RNWGX", "Asset Class": "International equity", "Style": "Diversified Emerging Markets", "Approach": "Actively managed equities and debt with developing-market exposure.", "Net Expense Ratio": 0.0057, "Gross / Operating Expense": 0.0057, "Waiver": "None shown", "Fee Date": "Jan. 1, 2026", "YTD": 16.64, "1 Year": 29.73, "3 Year": 18.51, "5 Year": 6.82, "10 Year": 11.36, "Since Inception": 10.09, "As Of": "Jun. 30, 2026"},
    {"Fund": "Cohen & Steers Global Realty I", "Ticker": "CSSPX", "Asset Class": "Real assets / equity", "Style": "Global Real Estate", "Approach": "Actively managed global REIT and real-estate equity securities.", "Net Expense Ratio": 0.0090, "Gross / Operating Expense": 0.0093, "Waiver": "0.03% contractual expense-ratio waiver through Jun. 30, 2027", "Fee Date": "May 1, 2026", "YTD": 9.15, "1 Year": 11.95, "3 Year": 9.31, "5 Year": 1.96, "10 Year": 5.14, "Since Inception": 7.47, "As Of": "Jun. 30, 2026"},
    {"Fund": "EUPAC Fund Growth Class R-6", "Ticker": "RERGX", "Asset Class": "International equity", "Style": "Foreign Large Growth", "Approach": "Actively managed developed- and emerging-market growth equities.", "Net Expense Ratio": 0.0047, "Gross / Operating Expense": 0.0047, "Waiver": "Not specified in supplied fact sheet", "Fee Date": "Jun. 30, 2026", "YTD": 14.53, "1 Year": 11.28, "3 Year": 23.73, "5 Year": 16.00, "10 Year": 5.51, "Since Inception": 9.91, "As Of": "Jun. 30, 2026"},
    {"Fund": "Invesco Discovery R6", "Ticker": "ODIIX", "Asset Class": "U.S. equity", "Style": "Small Growth", "Approach": "Actively managed small-company growth stocks.", "Net Expense Ratio": 0.0065, "Gross / Operating Expense": 0.0065, "Waiver": "None shown", "Fee Date": "Dec. 19, 2025", "YTD": 39.09, "1 Year": 57.71, "3 Year": 27.42, "5 Year": 11.40, "10 Year": 17.63, "Since Inception": 15.84, "As Of": "Jun. 30, 2026"},
    {"Fund": "Vanguard Small-Cap Index Admiral", "Ticker": "VSMAX", "Asset Class": "U.S. equity", "Style": "Small Blend", "Approach": "Index fund tracking the CRSP U.S. Small Cap Index.", "Net Expense Ratio": 0.0005, "Gross / Operating Expense": 0.0005, "Waiver": "None shown", "Fee Date": "Apr. 28, 2026", "YTD": 18.24, "1 Year": 29.48, "3 Year": 16.72, "5 Year": 7.68, "10 Year": 11.74, "Since Inception": 9.74, "As Of": "Jun. 30, 2026"},
    {"Fund": "Janus Henderson Enterprise T", "Ticker": "JAENX", "Asset Class": "U.S. equity", "Style": "Mid-Cap Growth", "Approach": "Actively managed growth-oriented, primarily mid-cap stocks.", "Net Expense Ratio": 0.0091, "Gross / Operating Expense": 0.0091, "Waiver": "None shown", "Fee Date": "Jan. 28, 2026", "YTD": 9.22, "1 Year": 13.86, "3 Year": 12.15, "5 Year": 7.36, "10 Year": 12.91, "Since Inception": 11.22, "As Of": "Jun. 30, 2026"},
    {"Fund": "Vanguard Mid-Cap Index Admiral", "Ticker": "VIMAX", "Asset Class": "U.S. equity", "Style": "Mid-Cap Blend", "Approach": "Index fund tracking the CRSP U.S. Mid Cap Index.", "Net Expense Ratio": 0.0005, "Gross / Operating Expense": 0.0005, "Waiver": "None shown", "Fee Date": "Apr. 28, 2026", "YTD": 11.84, "1 Year": 16.75, "3 Year": 15.32, "5 Year": 7.94, "10 Year": 11.77, "Since Inception": 10.41, "As Of": "Jun. 30, 2026"},
    {"Fund": "Fidelity Advisor Small Cap Value I", "Ticker": "FCVIX", "Asset Class": "U.S. equity", "Style": "Small Value", "Approach": "Actively managed small-cap value stocks.", "Net Expense Ratio": 0.0095, "Gross / Operating Expense": 0.0095, "Waiver": "None shown", "Fee Date": "Sep. 29, 2025", "YTD": 28.70, "1 Year": 41.16, "3 Year": 19.28, "5 Year": 10.76, "10 Year": 12.26, "Since Inception": 11.32, "As Of": "Jun. 30, 2026"},
])

performance_columns = ["YTD", "1 Year", "3 Year", "5 Year", "10 Year", "Since Inception"]

st.title("Fund Fees & Performance Dashboard")
st.caption("Fund data come from the user-supplied profile sheets and fact sheet. The performance page reports total returns as stated in those documents.")
st.warning("Past performance does not guarantee future results. Funds have different asset classes, risks, benchmarks, inception dates, and measurement periods, so direct ranking across all funds is not an apples-to-apples comparison.")

page = st.sidebar.radio("Navigate", ["Fees & Expenses", "Performance Comparison"])
asset_classes = ["All"] + sorted(funds["Asset Class"].unique().tolist())
selected_asset_class = st.sidebar.selectbox("Filter by asset class", asset_classes)
filtered = funds if selected_asset_class == "All" else funds[funds["Asset Class"] == selected_asset_class]

if page == "Fees & Expenses":
    st.header("Fees & Expenses")
    st.info("Expense ratios are annual operating costs deducted from fund assets. They are not usually billed as a separate charge. This dashboard is educational only and is not investment advice.")

    table = filtered[["Fund", "Ticker", "Asset Class", "Style", "Net Expense Ratio", "Gross / Operating Expense", "Waiver", "Fee Date"]].copy()
    table["Net Expense Ratio"] = table["Net Expense Ratio"].map(lambda x: f"{x:.2%}" if pd.notna(x) else "Not available")
    table["Gross / Operating Expense"] = table["Gross / Operating Expense"].map(lambda x: f"{x:.2%}" if pd.notna(x) else "Not available")
    st.dataframe(table, use_container_width=True, hide_index=True)
    st.caption("All readable fund sheets show no maximum sales charge, 12b-1 fee, or redemption fee. PTRQX is excluded from that statement because its fee section was not available in the extracted document text.")

    st.subheader("Fund introductions")
    for _, fund in filtered.iterrows():
        with st.expander(f"{fund['Fund']} ({fund['Ticker']})"):
            st.write(f"**Asset class:** {fund['Asset Class']}")
            st.write(f"**Investment style:** {fund['Style']}")
            st.write(f"**Basic approach:** {fund['Approach']}")
            net = f"{fund['Net Expense Ratio']:.2%}" if pd.notna(fund['Net Expense Ratio']) else "Not available"
            gross = f"{fund['Gross / Operating Expense']:.2%}" if pd.notna(fund['Gross / Operating Expense']) else "Not available"
            st.write(f"**Net expense ratio:** {net}")
            st.write(f"**Gross / total annual operating expense:** {gross}")
            st.write(f"**Waiver information:** {fund['Waiver']}")
            st.write(f"**Reported fee date:** {fund['Fee Date']}")

    st.subheader("Net expense ratio comparison")
    chart_data = filtered.dropna(subset=["Net Expense Ratio"]).set_index("Ticker")[["Net Expense Ratio"]] * 100
    st.bar_chart(chart_data)
    st.caption("Net expense ratio, expressed as a percentage. PTRQX is omitted because its fee data were unavailable from the uploaded extract.")

    st.subheader("Estimated annual fund expenses")
    investment = st.number_input("Investment amount ($)", min_value=0.0, value=10000.0, step=1000.0, format="%.2f")
    costs = filtered[["Fund", "Ticker", "Net Expense Ratio"]].copy()
    costs["Estimated Annual Cost"] = investment * costs["Net Expense Ratio"]
    costs["Net Expense Ratio"] = costs["Net Expense Ratio"].map(lambda x: f"{x:.2%}" if pd.notna(x) else "Not available")
    costs["Estimated Annual Cost"] = costs["Estimated Annual Cost"].map(lambda x: f"${x:,.2f}" if pd.notna(x) else "Not available")
    st.dataframe(costs, use_container_width=True, hide_index=True)

else:
    st.header("Performance Comparison")
    st.write("Returns are total returns from the supplied fund documents. Periods longer than one year are annualized where the source reports them that way. FBGRX performance is dated Dec. 31, 2025; the other readable profiles are dated Jun. 30, 2026.")

    selected_period = st.selectbox("Select return period", performance_columns, index=2)
    available = filtered.dropna(subset=[selected_period]).copy()
    available["Return"] = available[selected_period]
    available = available.sort_values("Return", ascending=False)

    st.subheader(f"{selected_period} total-return ranking")
    ranking = available[["Fund", "Ticker", "Asset Class", "Style", "Return", "As Of"]].copy()
    ranking["Return"] = ranking["Return"].map("{:.2f}%".format)
    st.dataframe(ranking, use_container_width=True, hide_index=True)

    chart = available.set_index("Ticker")[["Return"]]
    st.bar_chart(chart)

    st.subheader("Multi-period comparison")
    selected_tickers = st.multiselect(
        "Select funds to compare",
        options=available["Ticker"].tolist(),
        default=available["Ticker"].tolist()[: min(6, len(available))],
    )
    selected_funds = filtered[filtered["Ticker"].isin(selected_tickers)].copy()
    multi_period = selected_funds[["Fund", "Ticker", "Asset Class", "Style", "As Of"] + performance_columns].copy()
    display_periods = [column for column in performance_columns if multi_period[column].notna().any()]
    for column in display_periods:
        multi_period[column] = multi_period[column].map(lambda x: f"{x:.2f}%" if pd.notna(x) else "—")
    st.dataframe(multi_period, use_container_width=True, hide_index=True)

    if selected_tickers:
        chart_period = st.selectbox("Chart a comparison period", performance_columns, index=2, key="multi_period_chart")
        selected_chart = selected_funds.dropna(subset=[chart_period]).set_index("Ticker")[[chart_period]]
        st.bar_chart(selected_chart)

    st.subheader("Return versus expense ratio")
    scatter = filtered.dropna(subset=[selected_period, "Net Expense Ratio"])[["Ticker", "Fund", selected_period, "Net Expense Ratio"]].copy()
    scatter = scatter.rename(columns={selected_period: "Return", "Net Expense Ratio": "Expense Ratio"})
    st.scatter_chart(scatter, x="Expense Ratio", y="Return", color=None, size=None)
    st.caption("Use this as a descriptive view only. A return figure from one period does not establish whether a fund is better or worse, and the compared funds pursue materially different strategies.")

    with st.expander("Performance data notes"):
        st.markdown("""
- Returns may not be directly comparable across different categories, such as stocks, bonds, emerging markets, and global real estate.
- Fund returns are generally shown after the fund's expenses, while benchmarks do not bear fund expenses.
- The fund sheets use different reporting dates for FBGRX versus the other funds.
- PTRQX is included in the dashboard but excluded from performance analysis because the uploaded OCR extract did not contain readable return data.
- Review each fund's current prospectus and compare it with its appropriate benchmark and peer group before making a decision.
""")

st.caption("Sources: user-supplied fund profiles and fact sheet. Review each fund's current prospectus before investing.")
