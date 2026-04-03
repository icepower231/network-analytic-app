import streamlit as st
import speedtest
import pandas as pd

# 1. Настройка страницы и темы
st.set_page_config(
    page_title="Сетевой Аналитик v1.1",
    page_icon="⚡",
    layout="wide"
)

# 2. Кастомный CSS для стиля REGRONT (Фиолетовый + Темный)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #9D50BB !important;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #6E48AA, #9D50BB);
        color: white;
        border-radius: 10px;
        border: none;
        height: 3em;
        font-weight: bold;
    }
    [data-testid="stMetricValue"] {
        color: #00FFC2 !important;
    }
    .stSidebar {
        background-color: #161B22;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Боковая панель
with st.sidebar:
    st.title("⚙️ Настройки")
    st.write("Параметры для ручного расчета:")
    manual_speed = st.number_input("Скорость провайдера (Мбит/с)", min_value=1.0, value=100.0)
    overhead = st.slider("Служебные заголовки (%)", 0, 20, 5)
    st.info("Обычно Overhead составляет 5-7% для TCP/IP соединений.")

# 4. Основной интерфейс
st.title("🛰️ Система анализа пропускной способности")

# Блок реального спидтеста
st.subheader("🌐 Реальный замер скорости")
st.write("Нажмите кнопку ниже, чтобы измерить текущую скорость вашего интернет-соединения.")

if st.button("🚀 ЗАПУСТИТЬ ТЕСТ СКОРОСТИ"):
    with st.spinner("Связываемся с сервером... Это займет около 20 секунд"):
        try:
            st_test = speedtest.Speedtest()
            st_test.get_best_server()
            
            # Замер загрузки
            download_res = st_test.download() / 1_000_000 
            
            st.success(f"Тест завершен успешно!")
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.metric("Реальная скорость (Download)", f"{download_res:.2f} Mbps")
            with col_res2:
                # Считаем Goodput на основе замера
                real_goodput = download_res * ((100 - overhead) / 100)
                st.metric("Чистый Goodput", f"{real_goodput:.2f} Mbps")
            
            st.warning(f"Из-за заголовков протоколов вы теряете около {download_res - real_goodput:.2f} Мбит/с полезной скорости.")
        except Exception as e:
            st.error("Ошибка при замере. Попробуйте еще раз или используйте ручной ввод.")

st.markdown("---")

# Блок ручного калькулятора (то, что было раньше)
st.subheader("📊 Теоретический расчет")
calc_col1, calc_col2, calc_col3 = st.columns(3)

loss_factor = (100 - overhead) / 100
calc_goodput = manual_speed * loss_factor

with calc_col1:
    st.metric("Входная скорость", f"{manual_speed} Mbps")
with calc_col2:
    st.metric("Потери (Overhead)", f"{overhead}%")
with calc_col3:
    st.metric("Итоговый Goodput", f"{calc_goodput:.2f} Mbps")

# 5. Заключение и подвал
st.info(f"При скорости {manual_speed} Мбит/с, реальная полезная нагрузка составит {calc_goodput:.2f} Мбит/с. Это данные для вашего проекта.")

st.markdown("---")
st.caption("© 2026 Разработано REGRONT | Специальность: Инфокоммуникационные сети")
