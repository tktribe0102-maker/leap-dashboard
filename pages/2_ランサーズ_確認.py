import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

st.set_page_config(page_title="ランサーズ確認", page_icon="📬", layout="wide")

st.title("📬 ランサーズ サービス確認")
st.caption("サービスページの状態をチェックします")

LANCERS_URL = "https://www.lancers.jp/menu/detail/1328558"

st.info(f"📌 サービスURL: {LANCERS_URL}")

col1, col2 = st.columns([2, 1])

with col1:
    if st.button("🔄 今すぐ確認する", type="primary"):
        with st.spinner("ランサーズを確認中..."):
            try:
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(LANCERS_URL, headers=headers, timeout=10)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")

                    st.success(f"✅ ページ正常に表示されています（{datetime.now().strftime('%H:%M')}確認）")

                    # タイトル確認
                    title = soup.find("title")
                    if title:
                        st.write(f"**ページタイトル:** {title.text.strip()}")

                    # レビュー情報を探す
                    review_section = soup.find_all(class_=lambda x: x and "review" in x.lower())
                    if review_section:
                        st.write("**レビュー情報:**")
                        for r in review_section[:3]:
                            st.write(r.text.strip()[:100])
                    else:
                        st.write("📊 **レビュー:** まだレビューはありません（初受注を目指しましょう！）")

                else:
                    st.error(f"❌ ページの取得に失敗しました（ステータス: {response.status_code}）")

            except Exception as e:
                st.error(f"❌ エラーが発生しました: {str(e)}")

with col2:
    st.subheader("📨 受信ボックス")
    st.warning("メッセージの確認はランサーズアプリで行ってください")
    st.link_button("ランサーズ受信ボックスへ", "https://www.lancers.jp/message")
    st.link_button("サービスページへ", LANCERS_URL)

st.divider()

# サービス情報サマリー
st.subheader("📦 出品中のサービス")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="ベーシック", value="¥10,000", delta="納期3日")

with col2:
    st.metric(label="スタンダード", value="¥15,000", delta="納期5日")

with col3:
    st.metric(label="プレミアム", value="¥20,000", delta="納期7日")
