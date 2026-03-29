import streamlit as st
import pandas as pd
import joblib

# 1. Panggil si "Otak" AI
model = joblib.load('model_prediksi_nilai.pkl')

# 2. Bikin Judul dan Deskripsi ala-ala
st.title('🔮 Dukun Nilai Ujian (Machine Learning)')
st.write('Selamat datang di mesin peramal masa depan akademis! Masukkan kebiasaan belajarmu, dan AI kami akan menerawang nilai ujian akhirmu. Lebih akurat dari ramalan zodiak!')

# 3. Bikin Form Input di sebelah kiri (Sidebar)
st.sidebar.header('📝 Sesajen Data:')

jam_belajar = st.sidebar.slider('Berapa jam kamu belajar (atau pura-pura belajar)?', 0, 10, 5)
nilai_lama = st.sidebar.number_input('Nilai ujian sebelumnya (Jujur aja)', 0.0, 100.0, 75.0)
ekskul = st.sidebar.selectbox('Ikut Ekskul?', ['Nggak, mending rebahan', 'Iya, anak aktif nih'])
jam_tidur = st.sidebar.slider('Jam tidur semalam', 4, 10, 7)
latihan_soal = st.sidebar.slider('Berapa paket soal yang dikerjain?', 0, 10, 2)

# 4. Ubah teks ekskul jadi angka (1 = Iya, 0 = Nggak)
ekskul_angka = 1 if ekskul == 'Iya, anak aktif nih' else 0

# 5. Tombol Eksekusi
if st.button('🚀 Ramal Nilai Saya!'):
    # Susun data sesuai urutan waktu kita training model
    data_baru = pd.DataFrame([[jam_belajar, nilai_lama, ekskul_angka, jam_tidur, latihan_soal]], 
                             columns=['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced'])
    
    # Suruh model nebak
    prediksi = model.predict(data_baru)[0]
    
    # 6. Tampilkan Hasil dengan gaya
    st.markdown('---')
    st.success(f'✨ **TADAAA! Tebakan nilai ujianmu adalah: {prediksi:.2f}** ✨')
    
    # Kasih reaksi lucu berdasarkan nilai
    if prediksi >= 85:
        st.balloons()
        st.write('Wah, calon-calon cumlaude nih! Jangan lupa traktir temen kalau beneran dapet segini.')
    elif prediksi >= 65:
        st.write('Aman, lulus! Tapi kayaknya masih bisa digas dikit lagi belajarnya.')
    else:
        st.error('Waduh, agak mepet ya ges ya. Kurang-kurangin *scroll* sosmed, perbanyak doa!')