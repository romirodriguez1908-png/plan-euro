import streamlit as st
from datetime import date

st.set_page_config(page_title="Plan Ahorro Euro", page_icon="€")
st.title("€ Planificador Euro Oficial")
st.write("Objetivo: 25/05/2026 al 17/12/2027")

EURO_OFICIAL = 1604.48
fecha_inicio = date(2026, 5, 25)
fecha_fin = date(2027, 12, 17)
dias_totales = (fecha_fin - fecha_inicio).days

st.info(f"Cotización: ${EURO_OFICIAL} | Plazo: {dias_totales} días")

euros_meta = st.number_input("¿Cuántos EUROS querés?", min_value=1, value=5000)
ingreso = st.number_input("Tu ingreso en Pesos", min_value=1, value=500000)
modo = st.radio("El ingreso es:", ["Por Mes", "Por Día"])

if st.button("CALCULAR PLAN"):
    pesos_totales = euros_meta * EURO_OFICIAL
    cuota_diaria = pesos_totales / dias_totales
    cuota_mensual = pesos_totales / (dias_totales / 30.41)
    ingreso_mensual = ingreso if modo == "Por Mes" else ingreso * 30
    sobra = ingreso_mensual - cuota_mensual

    st.subheader("Resultados")
    st.metric("Total en Pesos", f"${pesos_totales:,.2f}")
    col1, col2 = st.columns(2)
    col1.metric("Ahorro x Día", f"${cuota_diaria:,.2f}")
    col2.metric("Ahorro x Mes", f"${cuota_mensual:,.2f}")

    if sobra < 0:
        st.error(f"Faltan ${abs(sobra):,.2f} por mes para llegar.")
    else:
        st.success(f"Te sobran ${sobra:,.2f} por mes. ¡Vas bien!")
