import streamlit as st

# 1. Настройка темы и страницы
st.set_page_config(
    page_title="Сетевой Аналитик v1.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Кастомный CSS для "ламповой" фиолетовой темы
st.markdown("""
    <style>
    /* Основной фон и шрифт */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* Заголовки */
    h1, h2, h3 {
        color: #9D50BB !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Сайдбар */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
    /* Кнопка рассчитать */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #6E48AA, #9D50BB);
        color: white;
        border: none;
        padding: 0.5rem;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(157, 80, 187, 0.4);
    }
    /* Карточки с метриками */
    [data-testid="stMetricValue"] {
        color: #00FFC2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Боковая панель (Ввод данных)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/network-interlace.png", width=80)
    st.title("Панель управления")
    st.write("Введите параметры вашей сети для анализа.")
    st.markdown("---")
    
    speed_input = st.number_input("Скорость провайдера (Мбит/с)", min_value=1.0, max_value=10000.0, value=100.0)
    overhead = st.slider("Служебные заголовки (%)", 0, 20, 5)
    
    calculate = st.button("🚀 ЗАПУСТИТЬ АНАЛИЗ")

# 4. Основная часть интерфейса
st.title("🛰️ Система анализа пропускной способности")
st.info("Данный инструмент рассчитывает Goodput (полезную нагрузку) на основе технических параметров канала.")

col1, col2, col3 = st.columns(3)

if calculate:
    # Логика расчета
    loss_factor = (100 - overhead) / 100
    goodput_val = speed_input * loss_factor
    
    with col1:
        st.metric("Входная скорость", f"{speed_input} Mbps")
    
    with col2:
        st.metric("Потери (Overhead)", f"{overhead}%", delta_color="inverse")
        
    with col3:
        st.metric("Итоговый Goodput", f"{goodput_val:.2f} Mbps")

    st.markdown("---")
    
    # Секция с графиком или пояснением
    st.subheader("📝 Заключение аналитика")
    st.write(f"""
    При заявленной скорости в **{speed_input} Мбит/с**, реальная полезная нагрузка составит **{goodput_val:.2f} Мбит/с**. 
    Разница уходит на служебную информацию протоколов (TCP/IP заголовки) и проверку целостности данных.
    """)
    
    st.success("Данные актуальны для индивидуального проекта 'Расчет пропускной способности'.")
else:
    st.warning("⬅️ Настройте параметры слева и нажмите кнопку для расчета.")

# Подвал
st.markdown("---")
st.caption("© 2026 Разработано REGRONT | Специальность: Инфокоммуникационные сети")


