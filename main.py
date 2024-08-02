from sorteio import sorteio_unitario
import streamlit as st


with st.form("my_form"):
   st.write("Formulário para sorteio de organizador de HH!!")
   nomes = st.text_input("Quais os nomes você gostaria de sortear?")
   submit = st.form_submit_button('Sortear')
   if submit:
    sorteado = sorteio_unitario(nomes)
    st.write(f'O sorteado foi {sorteado}.')
