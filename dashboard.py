"""
Author: Athiya Puteri Hidayat
Date: 06, March 2024
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Insert Data bike_data.csv
bike_df = pd.read_csv("bike_data.csv")
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("data:image/png;base64,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")
    st.header('Rental Bike Dashboard :sparkles:')

st.header('Rental Bike Dashboard :sparkles:')    

menu_choice = st.selectbox('Choose Conent', ('Dataset', 'Visualisasi 1', 'Visualisasi 2', 'Visualisasi 3', 'Analisis Lanjutan'))

if menu_choice == 'Dataset':
    # Tampilkan DataFrame dengan pagination
    st.header('Dataset')
    st.dataframe(bike_df)
    st.caption('Athiya Puteri Hidayat')
    
elif menu_choice == 'Visualisasi 1':

    st.subheader('Total Penyewaan Sepeda di Setiap Musim')
    
    # Menghitung rata-rata dan variasi jumlah penyewaan sepeda pada setiap musim untuk tahun 2011 dan 2012
    average_rentals_per_season = bike_df.groupby(['yr', 'season'])['cnt'].agg(['mean', 'std']).reset_index()
    
    # Mengganti nama header 'yr' menjadi 'year'
    average_rentals_per_season.rename(columns={'yr': 'year'}, inplace=True)
    
    # Tampilkan hasil analisis dalam bentuk tabel
    st.write("Rata-rata dan Variasi Jumlah Penyewaan Sepeda per Musim untuk Tahun 2011 dan 2012:")
    st.write(average_rentals_per_season)
    
    st.write("Penjelasan:")
    st.write("""Musim panas menjadi puncak penyewaan sepeda pada tahun 
            2011 dengan rata-rata sekitar 187.34, menandakan tingginya 
            minat masyarakat untuk bersepeda selama musim panas. Sementara
            itu, musim gugur mengalami sedikit penurunan dalam jumlah 
            penyewaan sepeda menjadi sekitar 152.83, namun masih menunjukkan 
            aktivitas yang signifikan dengan standar deviasi sekitar 133.23. 
            Pada musim panas tetap menjadi musim dengan jumlah penyewaan 
            sepeda tertinggi, dengan rata-rata sekitar 284.34 dan tingkat 
            variasi yang cukup tinggi dengan standar deviasi sekitar 226.01. 
            Musim gugur tahun 2012 menunjukkan sedikit penurunan dalam jumlah 
            penyewaan sepeda menjadi sekitar 245.70, namun tetap lebih tinggi 
            daripada tahun sebelumnya, dengan standar deviasi sekitar 212.46.
    """)

    # Visualisasi Pertanyaan 1
    count_season = bike_df.groupby('season').agg({'cnt':'sum'}).reset_index()

    season_highest = count_season.loc[count_season['cnt'].idxmax()]['season']
    season_lowest = count_season.loc[count_season['cnt'].idxmin()]['season']

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

    # Konversi kolom 'dteday' ke tipe data datetime
    bike_df['dteday'] = pd.to_datetime(bike_df['dteday'])

    # Menambahkan kolom 'month'
    bike_df['month'] = bike_df['dteday'].dt.month

    # Plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='month', y='cnt', hue='season', style='yr', data=bike_df, markers=True)
    plt.title('Tren Penyewaan Sepeda per Musim (2011-2012)')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.xticks(range(1, 13))
    plt.legend(title='Musim')
    plt.grid(True)

    # Tampilkan plot menggunakan Streamlit
    st.pyplot(plt.gcf())

    st.write("Kesimpulan:")
    st.write("""Dari hasil analisis musiman menunjukkan bahwa musim panas 
            menjadi puncak penyewaan sepeda dalam dua tahun terpisah, 
            yakni 2011 dan 2012. Penyewaan sepeda pada musim panas memiliki
            rata-rata tertinggi dibandingkan musim lainnya. Namun, terdapat 
            peningkatan yang signifikan dalam jumlah penyewaan sepeda pada 
            musim semi tahun 2012, menunjukkan potensi pertumbuhan yang 
            penting dalam bisnis penyewaan sepeda. Selain itu, musim 
            gugur cenderung memiliki jumlah penyewaan sepeda yang lebih 
            rendah, mengindikasikan perlunya strategi pemasaran yang lebih 
            efektif untuk mempromosikan penyewaan sepeda selama musim ini.
    """)
    
    st.caption('Athiya Puteri Hidayat')
    
elif menu_choice == 'Visualisasi 2':
    st.subheader('Rata-rata Penyewa Sepeda Setiap Tiap Masing-Masing Hari')
    
    # Menghitung rata-rata jumlah penyewaan sepeda pada setiap hari dalam seminggu
    average_rentals_per_day = bike_df.groupby('weekday')['cnt'].mean().reset_index()
    
    # Mengganti nama header 'cnt' menjadi 'count'
    average_rentals_per_day.rename(columns={'cnt': 'count'}, inplace=True)

    # Tampilkan hasil analisis dalam bentuk tabel
    st.write("Rata-rata Jumlah Penyewaan Sepeda per Hari dalam Seminggu:")
    st.write(average_rentals_per_day)
    
    st.write("Penjelasan:")
    st.write("""Diketahui bahwa Kamis dan Jumat menonjol sebagai hari 
            dengan rata-rata jumlah penyewaan sepeda tertinggi, dengan 
            nilai sekitar 196.44 dan 196.14 secara berturut-turut. 
            Sementara itu, Minggu tercatat sebagai hari dengan rata-rata 
            jumlah penyewaan sepeda terendah, dengan nilai sekitar 
            177.47. Analisis ini memberikan wawasan yang berharga bagi 
            pemilik bisnis atau manajer operasional untuk merencanakan 
            strategi pemasaran yang lebih efektif atau alokasi sumber 
            daya yang tepat pada hari-hari tertentu dalam seminggu. 
            Dengan memahami pola permintaan seperti ini, bisnis penyewaan
            sepeda dapat meningkatkan efisiensi operasional mereka dan 
            memberikan layanan yang lebih baik kepada pelanggan.
    """)

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
    hour_average.index = hour_average.index.astype(str)
    st.line_chart(hour_average)
    
    st.write("Penjelasan:")
    st.write("""Didapati bahwa Kamis dan Jumat menjadi hari-hari yang paling 
            diminati bagi para penyewa sepeda, dengan jumlah penyewaan yang 
            cenderung tinggi, sementara Minggu menjadi hari dengan permintaan 
            terendah. Analisis ini memberikan pemahaman yang berharga bagi 
            pemilik bisnis atau manajer operasional, karena mereka dapat 
            menggunakan informasi ini untuk mengarahkan strategi pemasaran 
            dan mengalokasikan sumber daya dengan lebih efisien. Dengan 
            memahami pola permintaan ini, bisnis penyewaan sepeda dapat 
            meningkatkan efisiensi operasional mereka dan memberikan 
            pengalaman yang lebih baik kepada pelanggan, mungkin dengan 
            menyesuaikan jam operasional atau menawarkan promosi khusus
            pada hari-hari dengan permintaan tinggi.
    """)

    hourly_rentals = bike_df.pivot_table(index='hr', columns='weekday', values='cnt', aggfunc='mean')

    plt.figure(figsize=(12, 6))
    sns.heatmap(hourly_rentals, cmap='YlGnBu')
    plt.title('Rata-rata Penyewaan Sepeda per Hari dan Jam')
    plt.xlabel('Hari')
    plt.ylabel('Jam')
    plt.yticks(rotation=0)

    st.pyplot(plt.gcf())

    st.write("Kesimpulan:")
    st.write("""Dari hasil analisis, dari segi hari dalam seminggu, 
             kami melihat bahwa Kamis dan Jumat menjadi hari dengan jumlah 
            penyewaan sepeda tertinggi, sementara Minggu menunjukkan jumlah 
            penyewaan terendah. Ini menandakan bahwa masyarakat lebih 
            cenderung menyewa sepeda pada akhir pekan atau menjelang akhir 
            pekan, mungkin karena waktu luang yang lebih besar atau kegiatan
            rekreasi yang lebih sering dilakukan pada hari-hari tersebut.
    """)
    
    st.caption('Athiya Puteri Hidayat')

elif menu_choice == 'Visualisasi 3':
    
    st.subheader('Distribusi Penyewaan Sepeda Berdasarkan Jam Dalam Sehari')
    
    # Hitung rata-rata, median, minimum, dan maksimum jumlah penyewaan sepeda pada setiap jam dalam sehari
    hourly_rentals_stats = bike_df.groupby('hr')['cnt'].agg(['mean', 'median', 'min', 'max']).reset_index()
    
    # Mengganti nama header 'hr' menjadi 'hour'
    hourly_rentals_stats.rename(columns={'hr': 'hour'}, inplace=True)

    # Tampilkan hasil analisis dalam bentuk tabel
    st.write("Statistik Jumlah Penyewaan Sepeda per Jam dalam Sehari:")
    st.write(hourly_rentals_stats)
    
    st.write("Penjelasan:")
    st.write("""Dari hasil ini, kita dapat melihat pola harian dalam jumlah 
            penyewaan sepeda. Penyewaan sepeda cenderung meningkat secara signifikan 
            pada jam-jam sibuk, seperti pagi hari (jam 7-9) dan sore hari (jam 16-18). 
            Jumlah penyewaan sepeda puncak terjadi pada jam 17, dengan rata-rata sekitar 
            461.45. Pada jam-jam malam, seperti jam 0-4, jumlah penyewaan sepeda cenderung 
            rendah, namun masih ada penyewaan yang terjadi.
    """)

    plt.figure(figsize=(10, 6))
    sns.pointplot(x='hr', y='cnt', data=bike_df, errorbar=None)
    plt.title('Distribusi Penyewaan Sepeda berdasarkan Jam dalam Sehari')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.show()

    st.pyplot(plt.gcf())

    st.write("Kesimpulan:")
    st.write("""Dari hasil analisis, analisis terhadap distribusi penyewaan 
            sepeda berdasarkan jam dalam sehari menunjukkan pola yang 
            menarik. Penyewaan sepeda cenderung meningkat secara 
            signifikan pada jam-jam sibuk, terutama pagi hari (jam 7-9) dan 
            sore hari (jam 16-18). Jam 17 menjadi puncak penyewaan sepeda, 
            menandakan bahwa banyak orang menggunakan sepeda untuk pulang 
            kerja atau untuk keperluan rekreasi sore hari. Di sisi lain, 
            jam-jam malam memiliki jumlah penyewaan sepeda yang rendah, 
            namun masih ada aktivitas penyewaan yang terjadi, menunjukkan 
            adanya permintaan penyewaan sepeda pada malam hari.
    """)
 
    st.caption('Athiya Puteri Hidayat')

elif menu_choice == 'Analisis Lanjutan':
    st.subheader('Analisis Lanjutan')
    
    # Hitung Recency, Frequency, dan Monetary
    current_date = pd.to_datetime('2012-12-31')
    rfm_data = bike_df.groupby('season').agg({
        'dteday': lambda x: (current_date - pd.to_datetime(x.max())).days,
        'cnt': ['count', 'sum']
        })
    rfm_data.columns = ['Recency', 'Frequency', 'Monetary']

    # Plotting RFM
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    axes[0].bar(rfm_data.index, rfm_data['Recency'], color='skyblue')
    axes[0].set_xlabel('Season')
    axes[0].set_ylabel('Recency (days)')
    axes[0].set_title('Recency by Season')

    axes[1].bar(rfm_data.index, rfm_data['Frequency'], color='skyblue')
    axes[1].set_xlabel('Season')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Frequency by Season')

    axes[2].bar(rfm_data.index, rfm_data['Monetary'], color='skyblue')
    axes[2].set_xlabel('Season')
    axes[2].set_ylabel('Monetary')
    axes[2].set_title('Monetary by Season')

    plt.tight_layout()
    st.pyplot(fig)
    
    st.write("Penjelasan:")
    st.write("""Pada visusalisa si atas dapat dilihat musim yang paling 
            diminati oleh penyewa untuk menyewa sepeda yaitu musim summer. 
            Lalu. musim yang paling tidak diminati oleh penyewa untuk 
            menyewa sepeda yaitu musin winter.
    """)
    
    st.caption('Athiya Puteri Hidayat')