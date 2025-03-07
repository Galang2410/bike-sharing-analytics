import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat data
df_hour = pd.read_csv('../data/hour.csv')
df_day = pd.read_csv('../data/day.csv')

# Fungsi untuk analisis kepadatan penyewaan sepeda per jam
def check_density(hour):
    df_filtered = df_hour[df_hour['hr'] == hour]
    avg_rentals = df_filtered['cnt'].mean()
    st.write(f'Rata-rata penyewaan sepeda pada jam {hour} adalah: {avg_rentals}')
    
    # Visualisasi
    plt.figure(figsize=(8, 6))
    sns.histplot(df_filtered['cnt'], kde=True, color='skyblue')
    plt.title(f'Kepadatan Penyewaan Sepeda pada Jam {hour}')
    plt.xlabel('Jumlah Penyewaan Sepeda')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)

# Fungsi untuk melihat pengaruh cuaca terhadap penyewaan sepeda
def analyze_weather_impact(weather_type):
    df_filtered = df_day[df_day['weathersit'] == int(weather_type)]
    avg_rentals = df_filtered['cnt'].mean()
    st.write(f'Rata-rata penyewaan sepeda dengan cuaca {weather_type} adalah: {avg_rentals}')
    
    # Visualisasi
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df_day)
    plt.title('Pengaruh Cuaca terhadap Penyewaan Sepeda')
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah Penyewaan Sepeda per Hari')
    st.pyplot(plt)

# Fungsi untuk analisis suhu
def analyze_temperature(temp_range):
    df_filtered = df_hour[(df_hour['temp'] >= temp_range[0]) & (df_hour['temp'] <= temp_range[1])]
    avg_rentals = df_filtered['cnt'].mean()
    st.write(f'Rata-rata penyewaan sepeda pada suhu antara {temp_range[0]} dan {temp_range[1]} adalah: {avg_rentals}')
    
    # Visualisasi
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='temp', y='cnt', data=df_filtered)
    plt.title(f'Pengaruh Suhu terhadap Penyewaan Sepeda')
    plt.xlabel('Suhu (Normalized)')
    plt.ylabel('Jumlah Penyewaan Sepeda per Jam')
    st.pyplot(plt)

# Streamlit Layout
st.title('Analisis Penyewaan Sepeda Interaktif')

# Pilih analisis yang diinginkan
option = st.selectbox(
    'Pilih jenis analisis yang ingin dilakukan:',
    ('Cek Kepadatan Penyewaan Sepeda', 'Pengaruh Cuaca', 'Pengaruh Suhu')
)

# Input dan analisis berdasarkan pilihan pengguna
if option == 'Cek Kepadatan Penyewaan Sepeda':
    hour = st.slider('Pilih Jam (0-23):', min_value=0, max_value=23)
    if st.button('Tampilkan Kepadatan'):
        check_density(hour)

elif option == 'Pengaruh Cuaca':
    weather_type = st.selectbox('Pilih Cuaca:', ('0', '1', '2', '3')) # 0: clear, 1: mist, 2: light rain, 3: heavy rain
    if st.button('Tampilkan Pengaruh Cuaca'):
        analyze_weather_impact(weather_type)

elif option == 'Pengaruh Suhu':
    temp_range = st.slider('Pilih rentang suhu:', min_value=0.0, max_value=1.0, value=(0.0, 1.0), step=0.01)
    if st.button('Tampilkan Pengaruh Suhu'):
        analyze_temperature(temp_range)

# Menampilkan visualisasi dari pertanyaan bisnis 1, 2, dan 3 secara langsung di bawah
# 1. Faktor Apa Saja yang Mempengaruhi Jumlah Penyewaan Sepeda per Hari?
st.header('1. Faktor Apa Saja yang Mempengaruhi Jumlah Penyewaan Sepeda per Hari?')

# Korelasi
correlation_day = df_day[['cnt', 'season', 'weathersit', 'temp', 'hum', 'windspeed']].corr()
st.subheader("Korelasi antara jumlah penyewaan sepeda dan faktor lain:")
st.write(correlation_day)

# Visualisasi Korelasi dengan heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_day, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap Korelasi antara Penyewaan Sepeda dan Faktor Lain')
st.pyplot(plt)

# Visualisasi Pengaruh Suhu dan Kelembaban dengan Line Chart
st.header("2. Bagaimana Suhu dan Kelembaban Mempengaruhi Penyewaan Sepeda per Jam?")

# Pengaruh Suhu terhadap penyewaan sepeda
plt.figure(figsize=(10, 6))
sns.lineplot(x='temp', y='cnt', data=df_hour, color='blue')
plt.title('Pengaruh Suhu terhadap Penyewaan Sepeda per Jam')
plt.xlabel('Suhu (Normalized)')
plt.ylabel('Jumlah Penyewaan Sepeda per Jam')
st.pyplot(plt)

# Pengaruh Kelembaban terhadap penyewaan sepeda
plt.figure(figsize=(10, 6))
sns.lineplot(x='hum', y='cnt', data=df_hour, color='green')
plt.title('Pengaruh Kelembaban terhadap Penyewaan Sepeda per Jam')
plt.xlabel('Kelembaban (Normalized)')
plt.ylabel('Jumlah Penyewaan Sepeda per Jam')
st.pyplot(plt)


# Visualisasi Pengaruh Cuaca dengan Bar Chart
st.header('3. Apakah Cuaca Mempengaruhi Penyewaan Sepeda?')

# Pengaruh Cuaca terhadap Penyewaan Sepeda per Hari
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=df_day, palette='Set2')
plt.title('Pengaruh Cuaca terhadap Penyewaan Sepeda per Hari')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Penyewaan Sepeda per Hari')
plt.xticks([0, 1, 2, 3], ['Cuaca Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Berat'], rotation=0)
st.pyplot(plt)
# Menampilkan grafik di Jupyter
plt.show()

