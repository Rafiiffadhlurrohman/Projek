import streamlit as st
import pandas as pd

# Inisialisasi data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Nama Baju', 'Ukuran', 'Jumlah'])

# Fungsi untuk menambah stok baju
def tambah_baju(nama, ukuran, jumlah):
    new_data = pd.DataFrame({'Nama Baju': [nama], 'Ukuran': [ukuran], 'Jumlah': [jumlah]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

# Fungsi untuk menghapus stok baju
def hapus_baju(index):
    st.session_state.data = st.session_state.data.drop(index).reset_index(drop=True)

# Judul aplikasi
st.title('Manajemen Stok Baju Konveksi')

# Form untuk menambah baju
with st.form('Tambah Baju'):
    nama_baju = st.text_input('Nama Baju')
    ukuran_baju = st.selectbox('Ukuran', ['S', 'M', 'L', 'XL', 'XXL'])
    jumlah_baju = st.number_input('Jumlah', min_value=1, step=1)
    submit = st.form_submit_button('Tambah')

    if submit:
        tambah_baju(nama_baju, ukuran_baju, jumlah_baju)
        st.success(f'{nama_baju} ukuran {ukuran_baju} sebanyak {jumlah_baju} berhasil ditambahkan!')

# Tampilkan data stok baju
st.subheader('Stok Baju')
st.dataframe(st.session_state.data)

# Pilih baju untuk dihapus
hapus_index = st.selectbox('Pilih index baju untuk dihapus', st.session_state.data.index)
hapus_button = st.button('Hapus Baju')

if hapus_button:
    hapus_baju(hapus_index)
    st.success('Baju berhasil dihapus!')

# Menjalankan aplikasi Streamlit
if _name_ == '_main_':
    app.py()

