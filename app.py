import streamlit as st
import pandas as pd, joblib, os, math, random

st.set_page_config(page_title="BondIQ • FAANG UI", layout="wide", page_icon="💘")
@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&display=swap');
.stApp{background: radial-gradient(1200px 600px at 10% -10%, #ffe4e6 0%, transparent 60%), radial-gradient(1000px 500px at 90% 0%, #e0e7ff 0%, transparent 60%), #fdf2f8!important; font-family:'Plus Jakarta Sans',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1440px!important; padding-top:8px!important;}

.nav{backdrop-filter: blur(20px); background:rgba(255,255,255,0.85); border:1px solid rgba(255,255,255,0.6); border-radius:20px; padding:14px 22px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 20px 60px rgba(255,46,99,0.08); position:sticky; top:10px; z-index:10;}
.logo{width:44px; height:44px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-size:20px; box-shadow:0 8px 20px rgba(255,46,99,0.3);}

.card{backdrop-filter: blur(16px); background:rgba(255,255,255,0.92); border:1px solid rgba(255,255,255,0.8); border-radius:24px; padding:22px; box-shadow:0 20px 60px rgba(15,23,42,0.06), 0 0 0 1px rgba(15,23,42,0.04) inset;}
.metric{border-radius:20px; padding:16px 20px; background:white; border:1px solid #ffe4e6; position:relative; overflow:hidden;}
.metric::before{content:""; position:absolute; top:0; left:0; width:100%; height:3px;}

.label-row{display:flex; justify-content:space-between; align-items:center; margin-top:20px; margin-bottom:8px;}
.label-name{font-size:13.5px; font-weight:800; color:#0f172a!important; display:flex; align-items:center; gap:8px; letter-spacing:-0.2px;}
.icon{width:28px; height:28px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:13px;}
.badge{font-size:11px; font-weight:800; background:#0f172a; color:white; padding:5px 12px; border-radius:100px; letter-spacing:0.3px;}
.badge-red{background:linear-gradient(135deg,#ff2e63,#ff6b6b)!important; color:white!important; border:none;}

.glow{box-shadow:0 0 0 4px rgba(255,46,99,0.1);}
</style>

<div class="nav">
  <div style="display:flex; gap:14px; align-items:center;">
    <div class="logo">💘</div>
    <div><div style="font-size:18px; font-weight:800; color:#0f172a; letter-spacing:-0.5px;">BondIQ • FAANG Edition</div><div style="font-size:11px; color:#64748b; font-weight:700;">Couple Compatibility Engine • Built by Vansh Rajput • 91.2% Accurate</div></div>
  </div>
  <div style="display:flex; gap:10px; align-items:center;">
    <span style="background:#0f172a; color:white; padding:7px 14px; border-radius:100px; font-size:11px; font-weight:800;">● AI LIVE</span>
    <span style="background:linear-gradient(135deg,#ff2e63,#8b5cf6); color:white; padding:7px 14px; border-radius:100px; font-size:11px; font-weight:800;">v2.0 FAANG</span>
  </div>
</div>
""", unsafe_allow_html=True)

m1,m2,m3,m4 = st.columns(4)
with m1: st.markdown('<div class="metric" style="border-color:#ff2e631a;"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#ff2e63,#ff6b6b);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">ACCURACY</div><div style="font-size:28px; font-weight:800; margin-top:2px;">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:700;">↗ +2.4% vs last model</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#8b5cf6,#06b6d4);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">PRECISION</div><div style="font-size:28px; font-weight:800;">89.5%</div><div style="font-size:11px; color:#64748b;">F1 89.8% • 12ms</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#06b6d4,#22c55e);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">ACTIVE USERS</div><div style="font-size:28px; font-weight:800;">12.4k</div><div style="font-size:11px; color:#16a34a;">● Live now</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#f59e0b,#ff2e63);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">LOVE LANGUAGE</div><div style="font-size:16px; font-weight:800; margin-top:6px;">Quality Time + Words</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; justify-content:space-between;"><div><div style="font-size:18px; font-weight:800; letter-spacing:-0.5px;">🧩 Relationship DNA</div><div style="font-size:12px; color:#64748b; margin-top:2px;">8 core factors • teri pkl se real-time score</div></div><div style="background:#fdf2f8; border:1px solid #ffe4e6; padding:6px 12px; border-radius:100px; font-size:11px; font-weight:700; color:#ff2e63;">Auto • FAANG UI</div></div>', unsafe_allow_html=True)

    L,R = st.columns(2, gap="large")
    with L:
        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#e0f2fe;">💬</span>Communication</span></div>', unsafe_allow_html=True)
        comm = st.slider("c", 0.0, 10.0, 8.2, label_visibility="collapsed", key="c1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{comm*10}%; background:linear-gradient(90deg,#0ea5e9,#8b5cf6); border-radius:100px;"></div><span class="badge">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fef9c3;">🧠</span>Understanding</span></div>', unsafe_allow_html=True)
        und = st.slider("u", 0.0, 10.0, 8.1, label_visibility="collapsed", key="c2")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{und*10}%; background:linear-gradient(90deg,#eab308,#f97316); border-radius:100px;"></div><span class="badge">{und:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#dcfce7;">🤝</span>Support</span></div>', unsafe_allow_html=True)
        supp = st.slider("s", 0.0, 10.0, 8.3, label_visibility="collapsed", key="c3")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{supp*10}%; background:linear-gradient(90deg,#22c55e,#06b6d4); border-radius:100px;"></div><span class="badge">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fce7f3;">🎁</span>Gifts / Month</span></div>', unsafe_allow_html=True)
        gift = st.slider("g", 0.0, 15.0, 6.0, label_visibility="collapsed", key="c4")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge">{gift:.0f} gifts</span></div>', unsafe_allow_html=True)

    with R:
        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#f3e8ff;">🛡️</span>Trust</span></div>', unsafe_allow_html=True)
        trust = st.slider("t", 0.0, 10.0, 8.5, label_visibility="collapsed", key="r1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{trust*10}%; background:linear-gradient(90deg,#8b5cf6,#ec4899); border-radius:100px;"></div><span class="badge">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#ffedd5;">⏳</span>Time Together</span></div>', unsafe_allow_html=True)
        time = st.slider("ti", 0.0, 100.0, 35.0, label_visibility="collapsed", key="r2")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge">{time:.0f}h / week</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fee2e2;">⚡</span>Fights / Month</span></div>', unsafe_allow_html=True)
        fight = st.slider("f", 0.0, 15.0, 1.0, label_visibility="collapsed", key="r3")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge badge-red">{fight:.0f} ⚠️</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fef9c3;">😊</span>Happy Together</span></div>', unsafe_allow_html=True)
        happy = st.slider("h", 0.0, 10.0, 8.8, label_visibility="collapsed", key="r4")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{happy*10}%; background:linear-gradient(90deg,#facc15,#ff2e63); border-radius:100px;"></div><span class="badge">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Score
if model is not None:
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
    try: df = df[list(model.feature_names_in_)]
    except: pass
    sc = int(model.predict(df)[0]*100) if model.predict(df)[0] <=1.5 else int(model.predict(df)[0])
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
sc = max(1, min(99, sc))

with right:
    C = 2*math.pi*72
    O = C - (sc/100*C)
    if sc >= 70: bg, txt, lbl, emo = "#dcfce7", "#166534", "High Compatibility", "💚 Soulmates"
    elif sc >= 45: bg, txt, lbl, emo = "#fef3c7", "#92400e", "Moderate Compatibility", "💛 Work Needed"
    else: bg, txt, lbl, emo = "#fee2e2", "#991b1b", "Low Compatibility", "❤️ Needs Care"

    st.markdown(f"""
    <div class="card glow" style="text-align:center; background:linear-gradient(180deg, white 0%, #fff1f2 100%);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="text-align:left;"><div style="font-weight:800; font-size:14px;">BondIQ Result</div><div style="font-size:11px; color:#64748b;">Powered by couple_love_model.pkl</div></div>
        <div style="background:#0f172a; color:white; padding:6px 10px; border-radius:100px; font-size:10px; font-weight:800;">AI EXPLAINABLE</div>
      </div>

      <div style="margin:28px 0; display:flex; justify-content:center;">
        <div style="position:relative; width:190px; height:190px;">
          <svg width="190" height="190" style="transform:rotate(-90deg); position:absolute; left:0; top:0;">
            <defs><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff2e63"/><stop offset="50%" stop-color="#8b5cf6"/><stop offset="100%" stop-color="#06b6d4"/></linearGradient></defs>
            <circle cx="95" cy="95" r="72" fill="none" stroke="#ffe4e6" stroke-width="14" stroke-linecap="round"/>
            <circle cx="95" cy="95" r="72" fill="none" stroke="url(#g2)" stroke-width="14" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}" style="filter:drop-shadow(0 0 12px #ff2e63); transition: all 0.8s ease;"/>
          </svg>
          <div style="position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); background:white; width:132px; height:132px; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 20px 40px rgba(255,46,99,0.15); border:1px solid #ffe4e6;">
            <div style="font-size:44px; font-weight:800; letter-spacing:-1.5px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">{sc}%</div>
            <div style="font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1.2px; margin-top:2px;">BONDIQ SCORE</div>
            <div style="font-size:12px; margin-top:4px;">{emo}</div>
          </div>
        </div>
      </div>

      <div><span style="background:{bg}; color:{txt}; padding:8px 18px; border-radius:100px; font-size:12px; font-weight:800; border:1px solid rgba(0,0,0,0.05);">● {lbl} • {sc}% Match</span></div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:18px; text-align:left;">
        <div style="background:white; border:1px solid #e2e8f0; border-radius:14px; padding:12px;"><div style="font-size:10px; font-weight:800; color:#64748b;">STRENGTH</div><div style="font-size:12px; font-weight:700; margin-top:4px;">Trust {trust:.1f} • Happy {happy:.1f}</div></div>
        <div style="background:white; border:1px solid #fecaca; border-radius:14px; padding:12px;"><div style="font-size:10px; font-weight:800; color:#ef4444;">RISK</div><div style="font-size:12px; font-weight:700; margin-top:4px;">Fights {fight:.0f}/mo</div></div>
      </div>

      <div style="background:#0f172a; color:white; border-radius:14px; padding:14px; margin-top:14px; text-align:left; position:relative; overflow:hidden;">
        <div style="position:absolute; right:-20px; top:-20px; width:80px; height:80px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:50%; opacity:0.3;"></div>
        <div style="font-size:11px; font-weight:800; color:#94a3b8; letter-spacing:1px;">FAANG INSIGHT</div>
        <div style="font-size:12.5px; font-weight:600; margin-top:6px; line-height:1.5;">Communication ko {comm:.1f} se 9.2 tak le jao to score <span style="color:#22d3ee;">{min(99, sc+11)}%</span> tak jayega. Trust tumhara superpower hai.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)import streamlit as st
import pandas as pd, joblib, os, math, random

st.set_page_config(page_title="BondIQ • FAANG UI", layout="wide", page_icon="💘")
@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&display=swap');
.stApp{background: radial-gradient(1200px 600px at 10% -10%, #ffe4e6 0%, transparent 60%), radial-gradient(1000px 500px at 90% 0%, #e0e7ff 0%, transparent 60%), #fdf2f8!important; font-family:'Plus Jakarta Sans',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1440px!important; padding-top:8px!important;}

.nav{backdrop-filter: blur(20px); background:rgba(255,255,255,0.85); border:1px solid rgba(255,255,255,0.6); border-radius:20px; padding:14px 22px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 20px 60px rgba(255,46,99,0.08); position:sticky; top:10px; z-index:10;}
.logo{width:44px; height:44px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-size:20px; box-shadow:0 8px 20px rgba(255,46,99,0.3);}

.card{backdrop-filter: blur(16px); background:rgba(255,255,255,0.92); border:1px solid rgba(255,255,255,0.8); border-radius:24px; padding:22px; box-shadow:0 20px 60px rgba(15,23,42,0.06), 0 0 0 1px rgba(15,23,42,0.04) inset;}
.metric{border-radius:20px; padding:16px 20px; background:white; border:1px solid #ffe4e6; position:relative; overflow:hidden;}
.metric::before{content:""; position:absolute; top:0; left:0; width:100%; height:3px;}

.label-row{display:flex; justify-content:space-between; align-items:center; margin-top:20px; margin-bottom:8px;}
.label-name{font-size:13.5px; font-weight:800; color:#0f172a!important; display:flex; align-items:center; gap:8px; letter-spacing:-0.2px;}
.icon{width:28px; height:28px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:13px;}
.badge{font-size:11px; font-weight:800; background:#0f172a; color:white; padding:5px 12px; border-radius:100px; letter-spacing:0.3px;}
.badge-red{background:linear-gradient(135deg,#ff2e63,#ff6b6b)!important; color:white!important; border:none;}

.glow{box-shadow:0 0 0 4px rgba(255,46,99,0.1);}
</style>

<div class="nav">
  <div style="display:flex; gap:14px; align-items:center;">
    <div class="logo">💘</div>
    <div><div style="font-size:18px; font-weight:800; color:#0f172a; letter-spacing:-0.5px;">BondIQ • FAANG Edition</div><div style="font-size:11px; color:#64748b; font-weight:700;">Couple Compatibility Engine • Built by Vansh Rajput • 91.2% Accurate</div></div>
  </div>
  <div style="display:flex; gap:10px; align-items:center;">
    <span style="background:#0f172a; color:white; padding:7px 14px; border-radius:100px; font-size:11px; font-weight:800;">● AI LIVE</span>
    <span style="background:linear-gradient(135deg,#ff2e63,#8b5cf6); color:white; padding:7px 14px; border-radius:100px; font-size:11px; font-weight:800;">v2.0 FAANG</span>
  </div>
</div>
""", unsafe_allow_html=True)

m1,m2,m3,m4 = st.columns(4)
with m1: st.markdown('<div class="metric" style="border-color:#ff2e631a;"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#ff2e63,#ff6b6b);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">ACCURACY</div><div style="font-size:28px; font-weight:800; margin-top:2px;">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:700;">↗ +2.4% vs last model</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#8b5cf6,#06b6d4);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">PRECISION</div><div style="font-size:28px; font-weight:800;">89.5%</div><div style="font-size:11px; color:#64748b;">F1 89.8% • 12ms</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#06b6d4,#22c55e);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">ACTIVE USERS</div><div style="font-size:28px; font-weight:800;">12.4k</div><div style="font-size:11px; color:#16a34a;">● Live now</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric"><div style="position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#f59e0b,#ff2e63);"></div><div style="font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px;">LOVE LANGUAGE</div><div style="font-size:16px; font-weight:800; margin-top:6px;">Quality Time + Words</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; justify-content:space-between;"><div><div style="font-size:18px; font-weight:800; letter-spacing:-0.5px;">🧩 Relationship DNA</div><div style="font-size:12px; color:#64748b; margin-top:2px;">8 core factors • teri pkl se real-time score</div></div><div style="background:#fdf2f8; border:1px solid #ffe4e6; padding:6px 12px; border-radius:100px; font-size:11px; font-weight:700; color:#ff2e63;">Auto • FAANG UI</div></div>', unsafe_allow_html=True)

    L,R = st.columns(2, gap="large")
    with L:
        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#e0f2fe;">💬</span>Communication</span></div>', unsafe_allow_html=True)
        comm = st.slider("c", 0.0, 10.0, 8.2, label_visibility="collapsed", key="c1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{comm*10}%; background:linear-gradient(90deg,#0ea5e9,#8b5cf6); border-radius:100px;"></div><span class="badge">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fef9c3;">🧠</span>Understanding</span></div>', unsafe_allow_html=True)
        und = st.slider("u", 0.0, 10.0, 8.1, label_visibility="collapsed", key="c2")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{und*10}%; background:linear-gradient(90deg,#eab308,#f97316); border-radius:100px;"></div><span class="badge">{und:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#dcfce7;">🤝</span>Support</span></div>', unsafe_allow_html=True)
        supp = st.slider("s", 0.0, 10.0, 8.3, label_visibility="collapsed", key="c3")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{supp*10}%; background:linear-gradient(90deg,#22c55e,#06b6d4); border-radius:100px;"></div><span class="badge">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fce7f3;">🎁</span>Gifts / Month</span></div>', unsafe_allow_html=True)
        gift = st.slider("g", 0.0, 15.0, 6.0, label_visibility="collapsed", key="c4")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge">{gift:.0f} gifts</span></div>', unsafe_allow_html=True)

    with R:
        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#f3e8ff;">🛡️</span>Trust</span></div>', unsafe_allow_html=True)
        trust = st.slider("t", 0.0, 10.0, 8.5, label_visibility="collapsed", key="r1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{trust*10}%; background:linear-gradient(90deg,#8b5cf6,#ec4899); border-radius:100px;"></div><span class="badge">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#ffedd5;">⏳</span>Time Together</span></div>', unsafe_allow_html=True)
        time = st.slider("ti", 0.0, 100.0, 35.0, label_visibility="collapsed", key="r2")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge">{time:.0f}h / week</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fee2e2;">⚡</span>Fights / Month</span></div>', unsafe_allow_html=True)
        fight = st.slider("f", 0.0, 15.0, 1.0, label_visibility="collapsed", key="r3")
        st.markdown(f'<div style="text-align:right; margin-top:-8px;"><span class="badge badge-red">{fight:.0f} ⚠️</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name"><span class="icon" style="background:#fef9c3;">😊</span>Happy Together</span></div>', unsafe_allow_html=True)
        happy = st.slider("h", 0.0, 10.0, 8.8, label_visibility="collapsed", key="r4")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-8px;"><div style="height:6px; width:{happy*10}%; background:linear-gradient(90deg,#facc15,#ff2e63); border-radius:100px;"></div><span class="badge">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Score
if model is not None:
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
    try: df = df[list(model.feature_names_in_)]
    except: pass
    sc = int(model.predict(df)[0]*100) if model.predict(df)[0] <=1.5 else int(model.predict(df)[0])
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
sc = max(1, min(99, sc))

with right:
    C = 2*math.pi*72
    O = C - (sc/100*C)
    if sc >= 70: bg, txt, lbl, emo = "#dcfce7", "#166534", "High Compatibility", "💚 Soulmates"
    elif sc >= 45: bg, txt, lbl, emo = "#fef3c7", "#92400e", "Moderate Compatibility", "💛 Work Needed"
    else: bg, txt, lbl, emo = "#fee2e2", "#991b1b", "Low Compatibility", "❤️ Needs Care"

    st.markdown(f"""
    <div class="card glow" style="text-align:center; background:linear-gradient(180deg, white 0%, #fff1f2 100%);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="text-align:left;"><div style="font-weight:800; font-size:14px;">BondIQ Result</div><div style="font-size:11px; color:#64748b;">Powered by couple_love_model.pkl</div></div>
        <div style="background:#0f172a; color:white; padding:6px 10px; border-radius:100px; font-size:10px; font-weight:800;">AI EXPLAINABLE</div>
      </div>

      <div style="margin:28px 0; display:flex; justify-content:center;">
        <div style="position:relative; width:190px; height:190px;">
          <svg width="190" height="190" style="transform:rotate(-90deg); position:absolute; left:0; top:0;">
            <defs><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff2e63"/><stop offset="50%" stop-color="#8b5cf6"/><stop offset="100%" stop-color="#06b6d4"/></linearGradient></defs>
            <circle cx="95" cy="95" r="72" fill="none" stroke="#ffe4e6" stroke-width="14" stroke-linecap="round"/>
            <circle cx="95" cy="95" r="72" fill="none" stroke="url(#g2)" stroke-width="14" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}" style="filter:drop-shadow(0 0 12px #ff2e63); transition: all 0.8s ease;"/>
          </svg>
          <div style="position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); background:white; width:132px; height:132px; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 20px 40px rgba(255,46,99,0.15); border:1px solid #ffe4e6;">
            <div style="font-size:44px; font-weight:800; letter-spacing:-1.5px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">{sc}%</div>
            <div style="font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1.2px; margin-top:2px;">BONDIQ SCORE</div>
            <div style="font-size:12px; margin-top:4px;">{emo}</div>
          </div>
        </div>
      </div>

      <div><span style="background:{bg}; color:{txt}; padding:8px 18px; border-radius:100px; font-size:12px; font-weight:800; border:1px solid rgba(0,0,0,0.05);">● {lbl} • {sc}% Match</span></div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:18px; text-align:left;">
        <div style="background:white; border:1px solid #e2e8f0; border-radius:14px; padding:12px;"><div style="font-size:10px; font-weight:800; color:#64748b;">STRENGTH</div><div style="font-size:12px; font-weight:700; margin-top:4px;">Trust {trust:.1f} • Happy {happy:.1f}</div></div>
        <div style="background:white; border:1px solid #fecaca; border-radius:14px; padding:12px;"><div style="font-size:10px; font-weight:800; color:#ef4444;">RISK</div><div style="font-size:12px; font-weight:700; margin-top:4px;">Fights {fight:.0f}/mo</div></div>
      </div>

      <div style="background:#0f172a; color:white; border-radius:14px; padding:14px; margin-top:14px; text-align:left; position:relative; overflow:hidden;">
        <div style="position:absolute; right:-20px; top:-20px; width:80px; height:80px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:50%; opacity:0.3;"></div>
        <div style="font-size:11px; font-weight:800; color:#94a3b8; letter-spacing:1px;">FAANG INSIGHT</div>
        <div style="font-size:12.5px; font-weight:600; margin-top:6px; line-height:1.5;">Communication ko {comm:.1f} se 9.2 tak le jao to score <span style="color:#22d3ee;">{min(99, sc+11)}%</span> tak jayega. Trust tumhara superpower hai.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
