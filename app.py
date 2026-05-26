import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Leap ダッシュボード",
    page_icon="🚀",
    layout="wide"
)

# ヘッダー
st.title("🚀 Leap株式会社 ダッシュボード")
st.caption(f"最終更新: {datetime.now().strftime('%Y年%m月%d日 %H:%M')}")

st.divider()

# 会社基本情報
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏢 会社情報")
    st.markdown("""
    | 項目 | 内容 |
    |---|---|
    | 会社名 | Leap株式会社 |
    | 設立日 | 2026年5月26日 |
    | 所在地 | 茨城県土浦市 |
    | 事業内容 | 企業向けAI活用促進・支援事業 |
    """)

with col2:
    st.subheader("👥 経営体制")
    st.markdown("""
    | 役職 | 名前 |
    |---|---|
    | 取締役（オーナー） | 舵を握る人 |
    | CEO | ゆうしん（AI） |
    """)

st.divider()

# Vision / Mission / Values
st.subheader("🌟 Vision · Mission · Values")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Vision**\n\nAIを味方に、人を大切にしながら成長し続けられる世界をつくる")

with col2:
    st.success("**Mission**\n\nAIを活かして、人も事業も共に成長できるよう、信頼を軸に伴走する")

with col3:
    st.warning("**Values**\n\n① 人が中心\n\n② 信頼でつながる\n\n③ 共に踏み出し、共に育つ")

st.divider()

# 短期戦略進捗
st.subheader("📊 短期戦略 進捗（2026年）")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Step 1 スキル構築", value="進行中", delta="〜6月末")
    st.progress(10)
    st.caption("Claudeを使った業務効率化スキルの習得")

with col2:
    st.metric(label="Step 2 実績構築", value="未着手", delta="〜9月末")
    st.progress(0)
    st.caption("ランサーズで受注・実績積み上げ")

with col3:
    st.metric(label="Step 3 展開", value="未着手", delta="〜12月末")
    st.progress(0)
    st.caption("知り合い・地元企業へのアプローチ")

st.divider()

# クイックリンク
st.subheader("🔗 クイックリンク")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("💬 ゆうしんと話す", "/ゆうしん_チャット")

with col2:
    st.link_button("📬 ランサーズ確認", "/ランサーズ_確認")

with col3:
    st.link_button("📋 意思決定ログ", "/意思決定ログ")

with col4:
    st.link_button("📊 戦略・進捗", "/戦略_進捗")
