from sorteio import sorteio_unitario, sorteio_ordenado
import streamlit as st


with st.form("my_form"):
   st.write("Formulário para sorteio de organizador de HH!!")
   nomes = st.text_input("Quais os nomes você gostaria de sortear?")
   ordenada = st.toggle('Lista ordenada?')
   submit = st.form_submit_button('Sortear')
   if submit:
    if ordenada:
        sorteados = sorteio_ordenado(nomes)
        count = 1
        for sorteado in sorteados:
            st.write(f'O {count}° sorteado foi {sorteado}.')
            count += 1
    else:
        sorteado = sorteio_unitario(nomes)
        st.write(f'O sorteado foi {sorteado}.')
