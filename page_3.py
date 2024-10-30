import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def page_3_section():
    
    df_1 = pd.read_json('datas/3_1.json')
    df_2 = pd.read_json('datas/3_2.json')
    df_3 = pd.read_json('datas/3_3.json')
    df_4 = pd.read_json('datas/3_4.json')

    fig = go.Figure()

    # Add each expense category as a separate trace
    fig.add_trace(go.Bar(
        x=df_2['Bulan'],
        y=df_2['Gaji_dan_Upah_IDR'],
        name='Gaji dan Upah',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=df_2['Bulan'],
        y=df_2['Biaya_Operasional_IDR'],
        name='Biaya Operasional',
        marker_color='orange'
    ))

    fig.add_trace(go.Bar(
        x=df_2['Bulan'],
        y=df_2['Marketing_IDR'],
        name='Marketing',
        marker_color='green'
    ))

    fig.add_trace(go.Bar(
        x=df_2['Bulan'],
        y=df_2['Maintenance_IDR'],
        name='Maintenance',
        marker_color='red'
    ))

    fig.add_trace(go.Bar(
        x=df_2['Bulan'],
        y=df_2['Utilities_IDR'],
        name='Utilities',
        marker_color='purple'
    ))

    # Update layout
    fig.update_layout(
        title='Monthly Expenses Breakdown',
        xaxis_title='Month',
        yaxis_title='Expenses (IDR)',
        barmode='stack',  # Stack the bars
        yaxis_tickprefix='IDR ',
        template='plotly_white'
    )

    # Streamlit app
    st.title('Monthly Expenses Breakdown Overview')
    st.plotly_chart(fig)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_3['Bulan'],
        y=df_3['Total_Revenue_IDR'],
        name='Total Revenue (IDR)',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=df_3['Bulan'],
        y=df_3['Total_Expenses_IDR'],
        name='Total Expenses (IDR)',
        marker_color='red'
    ))

    fig.add_trace(go.Bar(
        x=df_3['Bulan'],
        y=df_3['Profit_Loss_IDR'],
        name='Profit/Loss (IDR)',
        marker_color='green'
    ))

    fig.update_layout(
        title='Monthly Financial Overview',
        xaxis_title='Bulan',
        yaxis_title='Amount (IDR)',
        barmode='group',
        yaxis_tickprefix='IDR ',
        template='plotly_white'
    )

    st.title('Monthly Financial Overview')
    st.plotly_chart(fig)


    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_4['Bulan'],
        y=df_4['Gross_Operating_Profit_IDR'],
        mode='lines+markers',
        name='Gross Operating Profit (IDR)',
        line=dict(color='green', width=2),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title='Gross Operating Profit by Month',
        xaxis_title='Month',
        yaxis_title='Gross Operating Profit (IDR)',
        yaxis_tickprefix='IDR ',
        template='plotly_white'
    )

    st.title('Gross Operating Profit Overview')
    st.plotly_chart(fig)
