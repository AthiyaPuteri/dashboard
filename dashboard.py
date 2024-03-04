"""
Author: Athiya Puteri Hidayat
Date: 05, March 2024
"""
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def create_sum_order_items_df(df):
    sum_order_items_df = df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

# Insert Data bike_data.csv
bike_df = pd.read_csv("bike_data.csv")

datetime_columns = ["dteday"]
bike_df.sort_values(by="dteday", inplace=True)
bike_df.reset_index(inplace=True)
 
for column in datetime_columns:
    bike_df[column] = pd.to_datetime(bike_df[column])

min_date = bike_df["dteday"].min()
max_date = bike_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("data:image/png;base64,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")
    st.header('Rental Bike Dashboard :sparkles:')
    
# Mengambil start_date & end_date dari date_input
start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)  # Ubah ke tuple
)

st.header('Rental Bike Dashboard :sparkles:')

# Inisialisasi variabel global untuk mengatur halaman
page_number = st.query_params.get("page_number", 1)
page_number = int(page_number) if page_number else 1

# Jumlah baris yang akan ditampilkan di setiap halaman
rows_per_page = 10
start_index = (page_number - 1) * rows_per_page
end_index = start_index + rows_per_page

# Tampilkan DataFrame dengan pagination
st.dataframe(bike_df.iloc[start_index:end_index])

# Tambahkan tombol "Previous Page" dan "Next Page" di dalam dataframe
if page_number > 1:
    prev_page = page_number - 1
    st.write(f"<div><a href='?page_number={prev_page}'>&lt;&lt; Previous Page</a></div>", unsafe_allow_html=True)

if end_index < len(bike_df):
    next_page = page_number + 1
    st.write(f"<div><a href='?page_number={next_page}'>Next Page &gt;&gt;</a></div>", unsafe_allow_html=True)

count_season = bike_df.groupby('season').agg({'cnt':'sum'}).reset_index()

season_highest = count_season.loc[count_season['cnt'].idxmax()]['season']
season_lowest = count_season.loc[count_season['cnt'].idxmin()]['season']

st.subheader('Total Penyewaan Sepeda di Setiap Musim')

# Buat plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(count_season['season'], count_season['cnt'], color='skyblue')
ax.set_xlabel('Season')
ax.set_ylabel('Total Users')
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
ax.ticklabel_format(style='plain', axis='y')

# Tampilkan plot menggunakan st.pyplot()
st.pyplot(fig)

# Tampilkan hasil penyewaan tertinggi dan terendah
st.write(f"Penyewaan sepeda terbanyak terjadi di musim {season_highest}")
st.write(f"Penyewaan sepeda terendah terjadi di musim {season_lowest}")
st.write("Kesimpulan:")
st.write("""
Berdasarkan visualisasi dari bar chart yang ditampilkan untuk jumlah 
penyewa sepeda terbanyak terdapat pada musim kemarau dan jumlah penyewa 
sepeda terendah pada musim winter(musim dingin).
""")

st.subheader('Rata-rata Penyewa Sepeda Setiap Tiap Masing-Masing Hari')

# Convert 'cnt' column to numeric
bike_df['cnt'] = pd.to_numeric(bike_df['cnt'], errors='coerce')

# Drop rows with missing values in 'cnt' column
bike_df = bike_df.dropna(subset=['cnt'])

# Define weekday order
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Sort DataFrame by weekday
bike_df['weekday'] = pd.Categorical(bike_df['weekday'], categories=weekday_order, ordered=True)
bike_df = bike_df.sort_values('weekday')

# Group by 'weekday' and calculate the mean count of bike rentals
hour_average = bike_df.groupby('weekday')['cnt'].mean()

# Plotting
st.line_chart(hour_average)

st.write("Kesimpulan:")
st.write("""
Berdasarkan visualisai dari line chart yang ditampilkan, dapat dilihat 
bahwa rata-rata orang menyewa sepeda pada hari kamis, sedangakn 
rata-rata orang untuk tidak menyewa sepeda terdapat pada hari minggu.
""")
 
st.caption('Athiya Puteri Hidayat')