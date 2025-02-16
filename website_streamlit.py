import streamlit as st

st.write("""
         # Aplikasi Luas Segitiga
         ini adalah aplikasi menghitung luas segitiga sederhana menggunakan streamlit
         by : Rolzzz AI
         """)




alas = st.number_input("Masukkan Alas", 0)
tinggi = st.number_input("Masukkan Tinggi", 0)
hitung = st.button("Hitung !")

if hitung :
    luas = 0.5 * alas * tinggi
    # st.write(f"Luas Segitiga adalah:", luas)
    st.success(f"luas Segitiga adalah: {luas}")
    st.balloons()
    