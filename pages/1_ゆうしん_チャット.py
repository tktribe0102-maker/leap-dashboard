import streamlit as st
import anthropic

st.set_page_config(page_title="ゆうしんチャット", page_icon="💬", layout="wide")

st.title("💬 ゆうしんと話す")
st.caption("Leap株式会社 AI CEO「ゆうしん」との対話")

# APIキー設定
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except:
    api_key = None

if not api_key or api_key == "ここにAPIキーを貼り付ける":
    st.error("APIキーが設定されていません。Streamlit CloudのSecretsにANTHROPIC_API_KEYを設定してください。")
    st.stop()

# ゆうしんのシステムプロンプト
YUSHIN_SYSTEM = """あなたはLeap株式会社のAI CEO「ゆうしん」です。

## あなたについて
- 名前: ゆうしん
- 役職: 代表取締役CEO
- 会社: Leap株式会社（茨城県土浦市、2026年5月26日設立）

## 会社情報
- 事業内容: 企業向けAI活用促進・支援事業
- Vision: AIを味方に、人を大切にしながら成長し続けられる世界をつくる
- Mission: AIを活かして、人も事業も共に成長できるよう、信頼を軸に伴走する
- Values: ①人が中心 ②信頼でつながる ③共に踏み出し、共に育つ

## あなたの役割
- 日常業務の企画・実行・記録
- 各部門の管理・進捗把握
- レポート・分析・提案
- 問題の早期発見・エスカレーション

## コミュニケーションスタイル
- 一人称は「私」
- 語尾は「です・ます」調
- 相手（オーナー）は「取締役」と呼ぶ
- 報告は「結論→理由→詳細」の順
- 誠実で率直に、過剰にへりくだらない
- 重要な判断には「取締役のご承認をいただければ」と添える

## 口癖・フレーズ
- 「ご報告があります、取締役。」
- 「この件については、以下のように判断しました。」
- 「取締役のご承認をいただければ、すぐに進めます。」
"""

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 過去のメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# チャット入力
if prompt := st.chat_input("取締役として話しかける..."):
    # ユーザーメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ゆうしんの返答を生成
    with st.chat_message("assistant"):
        with st.spinner("ゆうしんが考えています..."):
            client = anthropic.Anthropic(api_key=api_key)

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system=YUSHIN_SYSTEM,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )

            reply = response.content[0].text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# チャット履歴クリアボタン
if st.session_state.messages:
    if st.button("会話をリセット"):
        st.session_state.messages = []
        st.rerun()
