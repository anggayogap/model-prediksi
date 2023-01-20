#library yang dibutuhkan
import pickle
import streamlit as st

#membaca model
kelapasawit_model = pickle.load(open('kelapasawit_model.sav', 'rb'))

#judul web
st.title('Prediksi Waktu Panen tanaman Kelapa Sawit untuk mempermudah Pengepulan')
#membuat input menjadi 2 kolom
col1, col2 = st.columns(2)

with col1 :
    CUACA = st.text_input ('Masukkan nilai cuaca')

with col2 :
    HARI = st.text_input ('Masukkan nilai Hari')

with col1 :
    BERATAWAL = st.text_input ('Masukkan nilai berat awal')

with col2 :
    BERATAKHIR = st.text_input ('Masukkan nilai berat akhir')

#code untuk prediksi
kelapasawit_prediksi = ''

#membuat tombol prediksi
if st.button('prediksi pengepulan'):
    kelapasawit_prediction = kelapasawit_model.predict([[CUACA, HARI, BERATAWAL, BERATAKHIR]])
#index ke [0] karena atribut yang diambil adalah index ke 0(x) dan index ke 1 adalah label(y)     
    if(kelapasawit_prediction[0] == 0):
        kelapasawit_prediksi = 'pengepulan kelapa sawit tepat waktu'
    else :
        kelapasawit_prediksi = 'pengepulan kelapa sawit ditunda' 
        
    st.success(kelapasawit_prediksi)




