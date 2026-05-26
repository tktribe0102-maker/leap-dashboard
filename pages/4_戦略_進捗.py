import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="戦略・進捗", page_icon="📊", layout="wide")

st.title("📊 戦略・進捗管理")
st.caption("短期戦略（2026年）の進捗状況")

today = date.today()

st.divider()

# Step 1
st.subheader("🔵 Step 1｜スキル構築期")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("**期間:** 〜2026年6月30日")
    st.write("**目標:** Claudeを使った業務効率化スキルを実践レベルまで習得する")
    st.progress(10, text="進捗 10%")

    st.write("**アクションチェックリスト**")
    checks = {
        "プロンプト設計の基本パターンを習得する": False,
        "文書生成（議事録・報告書・メール）を試す": False,
        "Leap社内業務にClaudeを活用する": False,
        "ランサーズのアカウント開設・プロフィール整備": True,
        "サービスの出品": True,
    }
    for task, done in checks.items():
        if done:
            st.write(f"✅ {task}")
        else:
            st.write(f"⬜ {task}")

with col2:
    deadline = date(2026, 6, 30)
    days_left = (deadline - today).days
    st.metric("残り日数", f"{days_left}日", delta="〜6月末")

st.divider()

# Step 2
st.subheader("🟡 Step 2｜実績構築期")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("**期間:** 〜2026年9月30日")
    st.write("**目標:** ランサーズで継続的に受注・納品できる状態をつくる")
    st.progress(0, text="未着手")

    st.write("**目標KPI**")
    st.write("- 月次受注件数: 2〜3件以上")
    st.write("- レビュー評価: ★4.0以上を維持")
    st.write("- 累計受注数: 10件以上")

with col2:
    deadline2 = date(2026, 9, 30)
    days_left2 = (deadline2 - today).days
    st.metric("残り日数", f"{days_left2}日", delta="〜9月末")

st.divider()

# Step 3
st.subheader("🟢 Step 3｜展開期")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("**期間:** 〜2026年12月31日")
    st.write("**目標:** 実績をもとに知り合いの経営者・地元企業へアプローチ開始")
    st.progress(0, text="未着手")

    st.write("**アクション（予定）**")
    st.write("- 実績・事例をまとめた提案資料を作成する")
    st.write("- 知り合いの経営者へのアプローチ開始")
    st.write("- 地元（茨城・土浦）企業へのアプローチ")
    st.write("- ランサーズの単価を引き上げる")

with col2:
    deadline3 = date(2026, 12, 31)
    days_left3 = (deadline3 - today).days
    st.metric("残り日数", f"{days_left3}日", delta="〜12月末")

st.divider()

# 全体タイムライン
st.subheader("📅 全体タイムライン")
st.markdown("""
```
5月  ████ 会社設立・基盤構築・ランサーズ出品
6月  ████ スキル構築完了
7月  ░░░░ 実績構築開始
8月  ░░░░ ランサーズ受注サイクルを回す
9月  ░░░░ 実績構築完了
10月 ░░░░ 展開開始
11月 ░░░░ 知り合い・地元企業へのアプローチ
12月 ░░░░ 2027年戦略策定
```
""")
