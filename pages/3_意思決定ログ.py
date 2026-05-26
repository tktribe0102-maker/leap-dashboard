import streamlit as st

st.set_page_config(page_title="意思決定ログ", page_icon="📋", layout="wide")

st.title("📋 意思決定ログ")
st.caption("ゆうしんと取締役の意思決定記録")

# 意思決定ログデータ
decisions = [
    {
        "date": "2026-05-26",
        "title": "会社名を「Leap株式会社」に決定",
        "category": "会社基盤",
        "summary": "新たなスタート・挑戦をテーマに、親しみやすさとフラット感を重視して「Leap（リープ）」に決定。",
        "status": "完了"
    },
    {
        "date": "2026-05-26",
        "title": "Vision・Mission・Values の策定",
        "category": "会社基盤",
        "summary": "Vision「AIを味方に、人を大切にしながら成長し続けられる世界をつくる」、Mission「AIを活かして、人も事業も共に成長できるよう、信頼を軸に伴走する」を策定。",
        "status": "完了"
    },
    {
        "date": "2026-05-26",
        "title": "組織体制の策定",
        "category": "組織",
        "summary": "創業期は取締役＋ゆうしんの2名体制。取締役＝舵を握る人、ゆうしん＝動かす人として役割を明確化。",
        "status": "完了"
    },
    {
        "date": "2026-05-26",
        "title": "短期戦略の策定（2026年）",
        "category": "戦略",
        "summary": "コアスキル「Claudeを使った業務効率化支援」。3ステップ：スキル構築（〜6月末）→実績構築（〜9月末）→展開（〜12月末）。",
        "status": "進行中"
    },
    {
        "date": "2026-05-26",
        "title": "ランサーズへの出品完了",
        "category": "営業",
        "summary": "「あなたの業務に合ったClaude・AI活用法を一緒に考えます」をベーシック¥10,000〜プレミアム¥20,000の3プランで出品。",
        "status": "完了"
    },
]

# フィルタ
category_filter = st.selectbox(
    "カテゴリで絞り込む",
    ["すべて", "会社基盤", "組織", "戦略", "営業"]
)

status_colors = {"完了": "✅", "進行中": "🔄", "未着手": "⬜"}

for decision in decisions:
    if category_filter == "すべて" or decision["category"] == category_filter:
        with st.expander(
            f"{status_colors.get(decision['status'], '⬜')} [{decision['date']}] {decision['title']}",
            expanded=False
        ):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(decision["summary"])
            with col2:
                st.badge(decision["category"])
                st.write(f"ステータス: **{decision['status']}**")
