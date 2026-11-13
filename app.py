with col_j1:
        st.markdown("""
            <div style="background: #FFFFFF; border: 2.5px solid #81D4FA; border-radius: 18px; padding: 18px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 42px; margin-bottom: 6px;">💧</div>
                    <h3 style="color: #01579B; margin: 0 0 8px 0; font-size: 18px;">AquaPou</h3>
                    <p style="color: #0277BD; font-size: 13px; line-height: 1.35;">
                        Atrapa agua limpia y esquiva industrias contaminantes.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🎮", key="btn_pou", use_container_width=True):
            st.session_state.juego_activo = "pou"
            st.rerun()

    with col_j2:
        st.markdown("""
            <div style="background: #FFFFFF; border: 2.5px solid #81D4FA; border-radius: 18px; padding: 18px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 42px; margin-bottom: 6px;">🚰</div>
                    <h3 style="color: #01579B; margin: 0 0 8px 0; font-size: 18px;">Cierra la Llave</h3>
                    <p style="color: #0277BD; font-size: 13px; line-height: 1.35;">
                        Detén fugas y desperdicios domésticos a contratiempo.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🎮", key="btn_llave", use_container_width=True):
            st.session_state.juego_activo = "llave"
            st.rerun()

    with col_j3:
        st.markdown("""
            <div style="background: #FFFFFF; border: 2.5px solid #81D4FA; border-radius: 18px; padding: 18px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 42px; margin-bottom: 6px;">🌱</div>
                    <h3 style="color: #01579B; margin: 0 0 8px 0; font-size: 18px;">Rescata el Río</h3>
                    <p style="color: #0277BD; font-size: 13px; line-height: 1.35;">
                        Limpia los desechos flotantes antes de que contaminen el río.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🎮", key="btn_rio", use_container_width=True):
            st.session_state.juego_activo = "rio"
            st.rerun()
            
