import streamlit as st
import pandas as pd

# Настройка страницы
st.set_page_config(page_title="Сетевой Аналитик v1.0", page_icon="🚀")

st.title("🚀 Сетевой Аналитик v1.0")
st.write("Проект по расчету пропускной способности и анализу Goodput")

st.divider()

# Упрощенный блок расчета
st.header("Расчет полезной нагрузки (Goodput)")
st.write("Введите скорость из любого теста (например, со speedtest.net):")

# Поле ввода
manual_speed = st.number_input("Скорость от провайдера (Мбит/с):", value=100.0)

# Кнопка, которая СРАЗУ выводит всё под собой
if st.button("РАССЧИТАТЬ ДАННЫЕ"):
    st.balloons() # Праздничные шарики
    
    # Математика
    efficiency = 1460 / 1500 
    real_speed = manual_speed * efficiency
    overhead = manual_speed - real_speed
    
    # ВЫВОД РЕЗУЛЬТАТОВ (Делаем максимально крупно)
    st.markdown("---")
    st.subheader("📊 Результаты анализа:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Чистые данные (Goodput)", f"{real_speed:.2f} Мбит/с")
    with col2:
        st.metric("Потери (Overhead)", f"{overhead:.2f} Мбит/с", delta_color="inverse")
    
    st.info(f"💡 Реальная скорость скачивания: **{real_speed/8:.2f} Мбайт/с**")

    # ГРАФИК
    st.write("### Сравнение скоростей")
    chart_data = pd.DataFrame({
        "Показатель": ["Провайдер", "Реальные данные"],
        "Мбит/с": [manual_speed, real_speed]
    })
    st.bar_chart(chart_data, x="Показатель", y="Мбит/с")
    
    st.write(f"**Пояснение:** Мы вычли {(1-efficiency)*100:.1f}% на заголовки пакетов.")

st.divider()

# Справочник (всегда виден внизу)
st.write("### Справочник технологий")
tech_table = pd.DataFrame({
    "Технология": ["Ethernet", "Wi-Fi 6", "5G", "Starlink"],
    "Макс. (Мбит/с)": [1000, 9600, 2000, 250],
    "Средняя (Мбит/с)": [940, 600, 200, 100]
})
st.table(tech_table)


