import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="조윤혁 자기소개서",
    page_icon="👨‍🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

    .main {
        background: linear-gradient(135deg, #fef7ed 0%, #fff7ed 50%, #fef3e2 100%);
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fef7ed 0%, #fff7ed 50%, #fef3e2 100%);
    }

    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(234, 88, 12, 0.1);
        border: 2px solid #fed7aa;
        padding: 2rem;
        margin: 1rem 0;
    }

    .accent-orange {
        background: linear-gradient(135deg, #ea580c, #f97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: bold;
    }

    .cert-badge {
        background: linear-gradient(135deg, #f97316, #ea580c);
        color: white;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
    }

    .achievement-card {
        background: linear-gradient(135deg, #fff7ed, #ffedd5);
        border-left: 4px solid #ea580c;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }

    .strength-item {
        background: rgba(249, 115, 22, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(249, 115, 22, 0.2);
    }

    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #fff7ed, #ffedd5);
    }

    h1, h2, h3 {
        font-family: 'Noto Sans KR', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# 사이드바 네비게이션
st.sidebar.title("📋 목차")
page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    ["🏠 인사 및 소개", "🎓 학력 및 자격증", "🏆 대회 성과", "⭐ 핵심 강점", "🌟 취미와 미래 비전"]
)

# 메인 콘텐츠
if page == "🏠 인사 및 소개":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # 제목
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="font-size: 4rem; margin-bottom: 0.5rem;" class="accent-orange">조윤혁</h1>
        <h2 style="font-size: 2rem; color: #92400e; margin-bottom: 1.5rem;">Cho Yunhyuk</h2>
    </div>
    """, unsafe_allow_html=True)

    # 직업 아이콘
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🍳</div>
            <h3 style="color: #c2410c; font-size: 1.5rem;">요리사</h3>
            <p style="color: #ea580c;">Chef</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center; font-size: 2.5rem; color: #fb923c; padding-top: 2rem;">
            +
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔥</div>
            <h3 style="color: #b91c1c; font-size: 1.5rem;">소방관</h3>
            <p style="color: #dc2626;">Firefighter</p>
        </div>
        """, unsafe_allow_html=True)

    # 소개 메시지
    st.markdown("""
    <div style="background: linear-gradient(to right, #fed7aa, #fecaca); padding: 2rem; border-radius: 15px; text-align: center; margin-top: 2rem;">
        <p style="font-size: 1.2rem; line-height: 1.8; color: #374151;">
            안녕하세요! 요리와 생명을 구하는 일에 열정을 가진 <span style="font-weight: bold; color: #c2410c;">조윤혁</span>입니다.<br>
            14살부터 시작한 요리의 길과 사람들을 돕고 싶은 마음이 만나<br>
            <span style="font-weight: bold; color: #b91c1c;">요리사</span>와 <span style="font-weight: bold; color: #b91c1c;">소방관</span>이라는 두 가지 꿈을 키우고 있습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🎓 학력 및 자격증":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 2rem;" class="accent-orange">
        🎓 학력 및 자격증
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3 style="color: #c2410c; font-size: 1.5rem; margin-bottom: 1.5rem;">🏫 학력 사항</h3>
            <div style="margin: 1rem 0;">
                <div style="display: flex; align-items: center; margin: 1rem 0;">
                    <div style="width: 16px; height: 16px; background: #ea580c; border-radius: 50%; margin-right: 1rem;"></div>
                    <span style="font-size: 1.1rem;">가사초등학교 졸업</span>
                </div>
                <div style="display: flex; align-items: center; margin: 1rem 0;">
                    <div style="width: 16px; height: 16px; background: #ea580c; border-radius: 50%; margin-right: 1rem;"></div>
                    <span style="font-size: 1.1rem;">팔봉중학교 졸업</span>
                </div>
                <div style="display: flex; align-items: center; margin: 1rem 0;">
                    <div style="width: 16px; height: 16px; background: #ea580c; border-radius: 50%; margin-right: 1rem;"></div>
                    <span style="font-size: 1.1rem;">태안고등학교 졸업</span>
                </div>
                <div style="display: flex; align-items: center; margin: 1rem 0;">
                    <div style="width: 16px; height: 16px; background: #dc2626; border-radius: 50%; margin-right: 1rem;"></div>
                    <span style="font-size: 1.1rem; font-weight: bold;">건양대학교 재학중</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3 style="color: #c2410c; font-size: 1.5rem; margin-bottom: 1.5rem;">📜 보유 자격증</h3>
            <div style="margin: 1rem 0;">
                <span class="cert-badge">🍚 한식조리기능사</span>
                <span class="cert-badge">🍽️ 양식조리기능사</span>
                <span class="cert-badge">🍣 일식조리기능사</span>
                <span class="cert-badge">🥢 중식조리기능사</span>
                <span class="cert-badge">🍷 조주기능사</span>
                <span class="cert-badge">🐡 복어기능사</span>
                <span class="cert-badge">🍞 제빵기능사</span>
            </div>
            <div style="margin-top: 1.5rem; padding: 1rem; background: #fff7ed; border-radius: 10px; text-align: center;">
                <p style="color: #9a3412; font-weight: bold;">
                    🏆 총 7개 조리 관련 자격증 보유
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🏆 대회 성과":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 2rem;" class="accent-orange">
        🏆 대회 성과
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3 style="color: #c2410c; font-size: 1.5rem; margin-bottom: 1.5rem; text-align: center;">🍳 요리 대회 성과</h3>
        """, unsafe_allow_html=True)

        competitions = [
            "2017년 이금기 대회",
            "2017년 요리 전국대회", 
            "2018년 요리 전국대회",
            "2019년 요리 전국대회",
            "2020년 요리 전국대회"
        ]

        for comp in competitions:
            st.markdown(f"""
            <div style="background: linear-gradient(to right, #fef3c7, #fed7aa); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 1.1rem; font-weight: bold;">{comp}</span>
                <span style="font-size: 1.5rem; font-weight: bold; color: #d97706;">🏆 대상</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div style="margin-top: 1.5rem; padding: 1rem; background: #fff7ed; border-radius: 10px; text-align: center;">
                <p style="font-size: 1.2rem; font-weight: bold; color: #9a3412;">5년 연속 대상 수상!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

   

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "⭐ 핵심 강점":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 2rem;" class="accent-orange">
        ⭐ 핵심 강점
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    strengths = [
        {
            "icon": "⏰",
            "title": "8년간의 꾸준한 경험",
            "description": "14살부터 요리를 시작하여 22살 군대 취사병까지, 8년간 한결같은 열정으로 요리의 길을 걸어왔습니다.",
            "color": "#c2410c"
        },
        {
            "icon": "🌡️",
            "title": "강인한 체력",
            "description": "온도 80도까지 버틸 수 있는 뛰어난 체력을 보유하고 있어, 고온의 주방 환경과 소방 현장에서도 끈기있게 일할 수 있습니다.",
            "color": "#dc2626"
        },
        {
            "icon": "🧠",
            "title": "탁월한 기억력",
            "description": "한 번 요리한 메뉴는 바로 외워지고 맛까지 정확히 기억하는 뛰어난 기억력으로 요리의 품질을 일정하게 유지할 수 있습니다.",
            "color": "#7c3aed"
        },
        {
            "icon": "⛰️",
            "title": "불굴의 의지",
            "description": "남들이 무시했던 꿈이지만 신경 쓰지 않고 계속해서 나의 희망 직무를 위해 끊임없이 노력하는 강한 정신력을 가지고 있습니다.",
            "color": "#059669"
        }
    ]

    for i, strength in enumerate(strengths):
        if i % 2 == 0:
            col = col1
        else:
            col = col2

        with col:
            st.markdown(f"""
            <div class="strength-item">
                <div style="display: flex; align-items: flex-start;">
                    <div style="font-size: 2rem; margin-right: 1rem; margin-top: 0.5rem;">{strength['icon']}</div>
                    <div>
                        <h3 style="font-size: 1.2rem; font-weight: bold; color: {strength['color']}; margin-bottom: 0.75rem;">{strength['title']}</h3>
                        <p style="color: #374151; line-height: 1.6;">{strength['description']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 군 복무 경험
    st.markdown("""
    <div style="margin-top: 2rem; padding: 2rem; background: linear-gradient(to right, #fff7ed, #fef2f2); border-radius: 15px; text-align: center;">
        <h3 style="font-size: 1.5rem; font-weight: bold; color: #c2410c; margin-bottom: 1rem;">
            🛡️ 군 복무 경험
        </h3>
        <p style="font-size: 1.1rem; color: #374151;">
            군대에서 취사병으로 복무하며 대량 조리 경험과 팀워크, 책임감을 함양했습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)



    # 마무리 메시지
    st.markdown("""
    <div style="background: linear-gradient(to right, #fff7ed, #fecaca, #fef3c7); padding: 2rem; border-radius: 20px; text-align: center; margin-top: 2rem;">
        <h3 style="font-size: 2rem; font-weight: bold; color: #c2410c; margin-bottom: 1.5rem;">
            🤝 마무리 인사
        </h3>
        <p style="font-size: 1.2rem; color: #374151; line-height: 1.8; margin-bottom: 1.5rem;">
            <span style="font-weight: bold; color: #c2410c;">음식</span>으로 사람들의 마음을 따뜻하게 하고,<br>
            <span style="font-weight: bold; color: #b91c1c;">용기</span>로 사람들의 생명을 지키는<br>
            그런 사람이 되고 싶습니다.
        </p>
        <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; margin: 1.5rem 0;">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🍳</div>
                <p style="font-weight: bold; color: #c2410c; margin: 0;">따뜻한 음식</p>
            </div>
            <div style="font-size: 1.5rem; color: #6b7280;">+</div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🛡️</div>
                <p style="font-weight: bold; color: #b91c1c; margin: 0;">든든한 보호</p>
            </div>
            <div style="font-size: 1.5rem; color: #6b7280;">=</div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">❤️</div>
                <p style="font-weight: bold; color: #ec4899; margin: 0;">더 나은 세상</p>
            </div>
        </div>
        <p style="font-size: 1.5rem; font-weight: bold; color: #ea580c; margin-top: 1.5rem;">
            감사합니다! 🙏
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 사이드바 추가 정보


st.sidebar.markdown("### 🎯 주요 키워드")
tags = ["#요리사", "#소방관", "#CPR", "#조리기능사", "#열정", "#체력", "#기억력", "#의지"]
for tag in tags:
    st.sidebar.markdown(f"`{tag}`")
