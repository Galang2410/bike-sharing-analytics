# Analisis Penyewaan Sepeda Interaktif 🚲📊

## Setup Environment - Anaconda

Untuk menyiapkan lingkungan di **Anaconda**, ikuti langkah-langkah berikut:

1. Membuat environment baru dengan Python 3.9:
    ```
    conda create --name bike-sharing-ds python=3.9
    ```

2. Mengaktifkan environment:
    ```
    conda activate bike-sharing-ds
    ```

3. Install semua dependensi yang dibutuhkan dengan menggunakan `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal

Jika Anda tidak menggunakan **Anaconda** dan lebih memilih menggunakan **Pipenv**, ikuti langkah-langkah berikut:

1. Membuat direktori proyek baru:
    ```
    mkdir bike-sharing-analytics
    cd bike-sharing-analytics
    ```

2. Install dependensi menggunakan `pipenv`:
    ```
    pipenv install
    pipenv shell
    ```

3. Install dependensi dari `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Setelah setup selesai, jalankan aplikasi Streamlit dengan perintah berikut di terminal:

streamlit run dashboard/dashboard.py



Aplikasi akan terbuka di browser Anda, biasanya di **http://localhost:8501**.

## Deskripsi Proyek

Proyek ini adalah **analisis penyewaan sepeda interaktif** menggunakan data dari sistem **bike-sharing**. Aplikasi ini menyediakan beberapa jenis analisis interaktif mengenai pengaruh **cuaca**, **suhu**, dan **kelembaban** terhadap jumlah penyewaan sepeda.

Fitur utama yang tersedia:
- **Cek Kepadatan Penyewaan Sepeda per Jam**: Menampilkan kepadatan penyewaan sepeda berdasarkan jam yang dipilih.
- **Pengaruh Cuaca terhadap Penyewaan Sepeda**: Menampilkan rata-rata penyewaan sepeda berdasarkan jenis cuaca.
- **Pengaruh Suhu dan Kelembaban terhadap Penyewaan Sepeda per Jam**: Menampilkan pengaruh suhu dan kelembaban terhadap jumlah penyewaan sepeda per jam.

## Struktur Folder

Berikut adalah struktur folder untuk proyek ini:

```plaintext
submission/
├── dashboard/
│   ├── dashboard.py        # Aplikasi Streamlit
├── data/
│   ├── hour.csv            # Data penyewaan sepeda per jam
│   ├── day.csv             # Data penyewaan sepeda per hari
├── main_data.csv           # Hasil data yang telah dianalisis
├── notebook.ipynb          # Notebook untuk analisis data
├── requirements.txt        # Daftar dependensi yang dibutuhkan
├── Readme.txt              # Penjelasan lebih lanjut mengenai data


Dependencies
Proyek ini menggunakan beberapa dependensi utama, yang dapat ditemukan di requirements.txt. Beberapa dependensi utama adalah:

pandas: Untuk manipulasi dan analisis data.
numpy: Untuk operasi matematika.
matplotlib dan seaborn: Untuk visualisasi data.
streamlit: Untuk membangun aplikasi interaktif.
Install dependensi dengan:
nginx
Salin
Edit

pip install -r requirements.txt