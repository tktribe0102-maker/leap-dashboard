import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="ランサーズ レポート", page_icon="🔍", layout="wide")
st.title("🔍 ランサーズ案件チェックレポート")
st.caption("ゆうしんが自動チェックした案件レポート（毎日 朝8時・昼12時・夜21時）")

REPO = "tktribe0102-maker/leap-dashboard"
API_URL = f"https://api.github.com/repos/{REPO}/contents/reports"
RAW_URL = f"https://raw.githubusercontent.com/{REPO}/main/reports"

@st.cache_data(ttl=300)
def get_report_list():
    try:
        res = requests.get(API_URL, timeout=10)
        if res.status_code == 200:
            files = res.json()
            return sorted([f["name"] for f in files if f["name"].endswith(".md") and f["name"] != "README.md"], reverse=True)
    except:
        pass
    return []

@st.cache_data(ttl=300)
def get_report_content(filename):
    try:
        res = requests.get(f"{RAW_URL}/{filename}", timeout=10)
        if res.status_code == 200:
            return res.text
    except:
        pass
    return None

reports = get_report_list()

if not reports:
    st.info("📭 まだレポートがありません。ゆうしんが毎日 朝8時・昼12時・夜21時 に自動チェックします。")
    st.caption("今夜21時に最初のレポートが届きます！")
else:
    col1, col2 = st.columns([3, 1])
    with col1:
        selected = st.selectbox(
            "レポートを選択",
            reports,
            format_func=lambda x: x.replace("_lancers-check.md", "").replace("_", " ")
        )
    with col2:
        if st.button("🔄 更新"):
            st.cache_data.clear()
            st.rerun()

    if selected:
        content = get_report_content(selected)
        if content:
            st.divider()
            st.markdown(content)
        else:
            st.error("レポートの読み込みに失敗しました")