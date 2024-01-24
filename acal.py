import streamlit as st 
import pandas as pd
import math 

# ---------- PAGINA --------------
page_title = "Diluir Destilados"
page_icon = "⚗"
layout = "centered"

# --- CONFIG & MENU ---
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

#----------- ESTILO STREAMLIT ----------
hide_st_style ="""
            <style>
            #MainMenu {visibility hidden;}
            footer {visibility hidden;}
            header {visibility hidden;}
            </style>
"""
                
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- CONTENEDOR 1 ---
container = st.container(border=True)
with container:

        title_text = "🧪 Dilución de Destilados 🧪"
        st.markdown(f'<h1 style="color: #ffffff; font-style: sans-serif; text-align: center; padding-left: 20px;" id="titulin">{title_text}</h1>', unsafe_allow_html=True)

        # --- CONTENEDOR 2 ---
        container = st.container(border=True)
        with container:

                # --- CALCULADORA PARA DILUIR---
                st.subheader("Calculadora")
                st.write("Ingrese los datos solicitados y calcule tanto la cantidad de agua destilada necesaria para la dilución como el volumen final de su destilado.")
                # Medidas de litro y mililitro
                # --- INPUTS ---
                with st.form("entry_form", clear_on_submit=False):
                    vdes = st.number_input("Volumen actual del destilado (mL)", value=0, step=0)
                    grad = st.number_input("Graduación alcohólica actual (%)", value=0, step= 0, min_value=0, max_value=96,)
                    gradpe = st.number_input("Graduación alcohólica pretendida (%)", value=0, step=0, min_value=0, max_value=96)
                    voltot = 0
                    # Boton 'calcular'
                    submitted = st.form_submit_button("Calcular")
                    if submitted:
                        if vdes > 0 and grad > 0 and gradpe > 0 and grad > gradpe:
                            agn = ((grad - gradpe) / gradpe) * vdes 
                            voltot = grad * vdes / gradpe
                            enlitros = voltot / 1000
                            agl = agn / 1000
                            st.write("El agua destilada necesaria es de")
                            st.success(f"{agn:.0f} mL  ({agl:.1f} L)")
                            st.write("El volumen final de su destilado será de")
                            st.success(f"{voltot:.0f} mL  ({enlitros:.1f} L)")
                            # Guia de medidas de volumen
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown(":green[mL = Volumen expresado en mililitros.]")

                            with col2:
                                st.markdown(":green[L = Volumen expresado en litros.]")

                        else:
                            st.info("Por favor, ingrese un valor válido.", icon="❗")


                # --- EMBOTELLADO ---
                st.subheader("Embotellado")
                st.write("La siguiente tabla expresa la cantidad de botellas (y sus medidas) necesarias para embotellar el volumen final de su destilado.")
                st.set_option('deprecation.showPyplotGlobalUse', False)

                # Tabla
                df = pd.DataFrame(
                    {
                    "Medida de la Botella": ["250 mL", "375 mL", "500 mL", "750 mL", "1 L"],
                    "Botellas Necesarias": [f"{math.floor(voltot / 250)}", f"{math.floor(voltot / 375)}", f"{math.floor(voltot / 500)}", f"{math.floor(voltot / 750)}", f"{math.floor(voltot / 1000)}"],
                    "Sobrante": [f"{((voltot % 250) / 1 % 250):.0f} mL", f"{((voltot % 375) / 1 % 375):.0f} mL", f"{((voltot % 500) / 1 % 500):.0f} mL", f"{((voltot % 750) / 1 % 750):.0f} mL", f"{((voltot % 1000) / 1 % 1000):.0f} mL"],
                    }
                    )
                df_no_index = df.copy()
                df_no_index.index = [""] * len(df_no_index)

                # Muestra la tabla sin el índice
                st.table(df_no_index) 

        # --- EXPLICACION DE LA FORMULA ---
        with st.expander("Más Información"):
            st.subheader("Fórmula de Dilución de Alcohol")
            
            # Explicación de la fórmula
            st.write(
                "La dilución del alcohol se interpreta en términos de la siguiente fórmula matemática:"
            )
            st.latex(r'''C_1 \times V_1 = C_2 \times V_2''')
            
            st.write(
                "Donde:"
                "\n- \(C1\): Concentración inicial de alcohol (en este caso, 96%)."
                "\n- \(V1\): Volumen inicial de alcohol (en este caso, 100 mL)."
                "\n- \(C2\): Concentración final deseada de alcohol (en este caso, 50%)."
                "\n- \(V2\): Volumen final deseado después de la dilución."
            )
            
            # Ejemplo específico
            st.write(
                "Para el nuevo ejemplo donde tienes 100 mL de alcohol al 96% y deseas reducirlo al 50%,"
                " la fórmula se resuelve de la siguiente manera:"
            )
            
            # Paso 1: Sustituir valores conocidos en la fórmula
            st.latex(r'''C_1 \times V_1 = C_2 \times V_2''')
            st.latex(r'''96\% \times 100 \, \text{ml} = 50\% \times V_2''')
            
            # Paso 2: Resolver para V2
            st.latex(r'''V_2 = \frac{C_1 \times V_1}{C_2}''')
            st.latex(r'''V_2 = \frac{96\% \times 100 \, \text{ml}}{50\%}''')
            
            # Paso 3: Calcular el valor
            st.latex(r'''V_2 = 192 \, \text{ml}''')
            
            st.write(
                "Esto implica que necesitas agregar exactamente 92 mL de agua destilada para diluir los 100 mL de alcohol"
                " al 96% y obtener 192 mL de líquido con una graduación alcohólica del 50%."
            )