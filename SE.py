# library
import streamlit as st

# write
st.title('SOFTWARE PERKALIAN')
st.subheader('ini adalah aplikasi untuk mengalikan bilangan')

#input bilangan pertama
number1 = st.number_input('masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1} ')

#input bilangan kedua
number2 = st.number_input('masukkan bilangan kedua')
st.write(f'Bilangan Kedua adalah {number2} ')

#hasil kali
tombol = st.button('Hitung perkalian')
if tombol:
    hasil_perkalian = number1*number2
    st.success(f'Hasil perkalian adalah {hasil_perkalian}')
    st.balloons()

else :
    st.warning('JGN LUPA PENCET TOMBOL YAH AYANGG', icon="😘")
    