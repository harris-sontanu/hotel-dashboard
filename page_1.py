import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def page_1_section():

    df_1 = pd.read_json('datas/1_1.json')
    df_2 = pd.read_json('datas/1_2.json')
    df_3 = pd.read_json('datas/1_3.json')
    df_4 = pd.read_json('datas/1_4.json')
    df_5 = pd.read_json('datas/1_5.json')

    st.title('Pendapatan')

    st.subheader('Pendapatan total dari kamar, makanan dan minuman, fasilitas (spa, gym, dll.), dan layanan tambahan')
    cols_1 = st.columns(2)
    with cols_1[0]:
        month_order = ["Juni", "Mei", "April", "Maret", "Februari", "Januari"]
        df_1['Bulan'] = pd.Categorical(df_1['Bulan'], categories=month_order, ordered=True)
        df = df_1.filter(['Bulan', 'Total_Penjualan_IDR'])
        df = df.sort_values('Bulan')
        fig = go.Figure()

        fig.add_trace(go.Bar(
            y=df['Bulan'],
            x=df['Total_Penjualan_IDR'],
            name='Total Penjualan IDR',
            orientation='h',
            marker_color='green'
        ))

        fig.update_layout(
            title='Total',
            yaxis_title='Bulan',
            xaxis_title='Total Penjualan IDR (IDR)',
        )
        st.plotly_chart(fig)
    with cols_1[1]:
        df = df_1.drop('Total_Penjualan_IDR', axis=1)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Bulan'],
            y=df['Kamar_IDR'],
            name='Kamar IDR',
            marker_color='blue'
        ))
        fig.add_trace(go.Bar(
            x=df['Bulan'],
            y=df['F&B_IDR'],
            name='F&B IDR',
            marker_color='orange'
        ))
        fig.add_trace(go.Bar(
            x=df['Bulan'],
            y=df['Spa_IDR'],
            name='Spa IDR',
            marker_color='green'
        ))
        fig.add_trace(go.Bar(
            x=df['Bulan'],
            y=df['Gym_IDR'],
            name='Gym IDR',
            marker_color='red'
        ))
        fig.add_trace(go.Bar(
            x=df['Bulan'],
            y=df['Layanan_Lainnya_IDR'],
            name='Layanan Lainnya IDR',
            marker_color='purple'
        ))

        fig.update_layout(
            title='Detail Penjualan',
            xaxis_title='Bulan',
            yaxis_title='Amount (IDR)',
            barmode='stack'
        )
        st.plotly_chart(fig)

    st.subheader('Pendapatan rata-rata yang dihasilkan per kamar')
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_3['Bulan'],
        y=df_3['RevPAR_IDR'],
        mode='lines+markers',
        name='RevPAR IDR',
        marker=dict(color='blue'),
        line=dict(width=2)
    ))

    fig.update_layout(
        title='RevPAR (IDR)',
        xaxis_title='Bulan',
        yaxis_title='RevPAR IDR',
        yaxis_tickprefix='IDR ',
        xaxis=dict(tickmode='array', tickvals=df_3['Bulan']),
        template='plotly_white'
    )
    st.plotly_chart(fig)

