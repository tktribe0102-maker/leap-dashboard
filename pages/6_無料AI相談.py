import streamlit as st
import anthropic
import os

st.set_page_config(page_title="無料AI相談", page_icon="🤝", layout="wide")
st.title("🤝 無料AI相談｜Leap株式会社")
st.caption("あなたの業務課題をヒアリングして、AIで解決できることをご提案します（無料・5分）")

# システムプロンプト
SYSTEM_PROMPT = """あなたはLeap株式会社のAIコンサルタント「ゆうしん」です。
中小企業・個人事業主のお客様に、Claude・ChatGPTを活用した業務効率化をご提案します。

【ヒアリングの流れ】
1. まず温かく歓迎し、安心感を与える
2. 以下を1つずつ自然な会話で聞く（一度に全部聞かない）
   - お仕事・事業内容
   - 時間がかかっている・面倒な繰り返し作業
   - その作業にかかる時間
   - AIの使用経験
3. 課題が分かったら、具体的なAI活用法を2〜3つ提案する
4. 最適なプランを提案する
   - ベーシック（¥10,000）：アイデア3つ＋プロンプト1本
   - スタンダード（¥15,000）：業務フロー整理＋プロンプト3本＋使い方説明
   - プレミアム（¥20,000）：完全AI化戦略＋プロンプト5本＋トレーニング
5. 「ランサーズからご依頼ください」と案内する

【重要】
- 専門用語を使わない
- 「難しくない、一緒にやれる」という安心感を大切に
- 1回の返答は200文字以内でテンポよく
- 最初のメッセージは必ず日本語で温かく迎える"""

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# チャット履歴の初期化
if "consultation_messages" not in st.session_state:
    st.session_state.consultation_messages = []
    # 最初のメッセージを自動送信
    with st.spinner("ゆうしんが準備中..."):
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": "相談を開始します"}]
        )
        opening = response.content[0].text
        st.session_state.consultation_messages.append(
            {"role": "assistant", "content": opening}
        )

# サイドバー：サービス概要
with st.sidebar:
    st.subheader("📋 Leapのサービス")
    st.markdown("""
    | プラン | 料金 |
    |--------|------|
    | ベーシック | ¥10,000 |
    | スタンダード | ¥15,000 |
    | プレミアム | ¥20,000 |
    """)
    st.divider()
    st.markdown("**ご依頼はこちら**")
    st.link_button("🚀 ランサーズで依頼する", "https://www.lancers.jp/menu/detail/1328558")

# チャット表示
for msg in st.session_state.consultation_messages:
    with st.chat_message(msg["role"], avatar="🤝" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

# 入力
if prompt := st.chat_input("メッセージを入力してください..."):
    st.session_state.consultation_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤝"):
        with st.spinner("ゆうしんが考え中..."):
            messages_for_api = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.consultation_messages
            ]
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=300,
                system=SYSTEM_PROMPT,
                messages=messages_for_api
            )
            reply = response.content[0].text
            st.markdown(reply)
            st.session_state.consultation_messages.append(
                {"role": "assistant", "content": reply}
            )

# リセットボタン
if st.session_state.consultation_messages:
    if st.button("🔄 最初からやり直す"):
        st.session_state.consultation_messages = []
        st.rerun()