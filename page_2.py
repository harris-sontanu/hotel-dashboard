import pandas as pd
import streamlit as st
import plotly.express as px


def page_2_section():
    
    df_1 = pd.read_json('datas/2_1.json')
    df_2 = pd.read_json('datas/2_2.json')
    df_3 = pd.read_json('datas/2_3.json')
    df_4 = pd.read_json('datas/2_4.json')
    df_5 = pd.read_json('datas/2_5.json')

    st.title('Jumlah Tamu dan Demografi')


    st.subheader('Jumlah & Jenis Tamu')
    cols_1 = st.columns(2)

    with cols_1[0]:
        fig = px.pie(df_2, 
                    names='Tipe_Tamu', 
                    values='Persentase', 
                    title='Rata-rata Mingguan',
                    hole=0.3)
        st.plotly_chart(fig)
    with cols_1[1]:
        df_melted = df_1.melt(id_vars=['Bulan'], value_vars=['Tamu_Bisnis', 'Tamu_Leisure', 'Tamu_Grup', 'Tamu_Keluarga'],
                            var_name='Tipe_Tamu', value_name='Jumlah')
        
        fig = px.bar(df_melted, 
                    x='Bulan', 
                    y='Jumlah', 
                    color='Tipe_Tamu', 
                    title='Berdasarkan Jenis',
                    barmode='group')

        st.plotly_chart(fig)

    st.subheader('Distribusi Negara')
    fig = px.choropleth(
        df_4,
        locations='Code',
        color='Jumlah_Tamu',
        hover_name='Country',
        color_continuous_scale=px.colors.sequential.Plasma,
        labels={'Jumlah_Tamu': 'Jumlah Tamur'},
        title='Tamu per Negara'
    )

    fig.update_geos(showcoastlines=True, coastlinecolor="Black")
    fig.update_layout(
        geo=dict(
            scope='world',
            projection_type='natural earth',
        )
    )
    st.plotly_chart(fig)


    st.subheader('Kelompok Usia')
    cols_2 = st.columns(2)
    with cols_2[0]:
        total_pria = df_5['Pria'].sum()
        total_wanita = df_5['Wanita'].sum()

        pie_data = pd.DataFrame({
            'Gender': ['Pria', 'Wanita'],
            'Count': [total_pria, total_wanita]
        })

        fig = px.pie(pie_data, 
                    values='Count', 
                    names='Gender', 
                    title='Jenis Kelamin',
                    color='Gender',
                    hole=0.3)

        st.plotly_chart(fig)
    with cols_2[1]:
        df_melted = df_5.melt(id_vars=['Kelompok_Usia'], value_vars=['Pria', 'Wanita'],
                            var_name='Gender', value_name='Count')

        fig = px.funnel(df_melted, 
                        x='Count', 
                        y='Kelompok_Usia', 
                        color='Gender',
                        title='Rentang Usia')

        st.plotly_chart(fig)

