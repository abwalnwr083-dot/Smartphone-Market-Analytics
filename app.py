import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px
import os

csv_file = "smartphones.csv"
if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame([
        {"Phone Name": "Samsung Galaxy S24", "Brand": "Samsung", "Price (EGP)": 45000, "Rating": 4.8, "Storage (GB)": 256}
    ])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📱 لوحة تحكم سوق الهواتف الذكية", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Label("اختر الماركة (Brand):", style={'fontWeight': 'bold'}),
    dcc.Dropdown(
        id='brand-filter',
        options=[{'label': i, 'value': i} for i in df['Brand'].dropna().unique()],
        placeholder="كل الماركات",
        clearable=True
    ),
    html.Br(),
    
    # الكروت العلوية (KPIs)
    html.Div([
        html.Div([html.H4("إجمالي الموبايلات"), html.H2(id="kpi-phones")], style={'border': '1px solid #ccc', 'borderRadius': '8px', 'padding': '10px', 'width': '22%', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': '#f8f9fa'}),
        html.Div([html.H4("عدد الماركات"), html.H2(id="kpi-brands")], style={'border': '1px solid #ccc', 'borderRadius': '8px', 'padding': '10px', 'width': '22%', 'display': 'inline-block', 'textAlign': 'center', 'marginLeft': '2%', 'backgroundColor': '#f8f9fa'}),
        html.Div([html.H4("متوسط الأسعار (ج.م)"), html.H2(id="kpi-avg-price")], style={'border': '1px solid #ccc', 'borderRadius': '8px', 'padding': '10px', 'width': '22%', 'display': 'inline-block', 'textAlign': 'center', 'marginLeft': '2%', 'backgroundColor': '#f8f9fa'}),
        html.Div([html.H4("أعلى تقييم"), html.H2(id="kpi-top-rating", style={'fontSize': '22px'})], style={'border': '1px solid #ccc', 'borderRadius': '8px', 'padding': '10px', 'width': '22%', 'display': 'inline-block', 'textAlign': 'center', 'marginLeft': '2%', 'backgroundColor': '#f8f9fa'}),
    ]),
    
    html.Br(),
    
    # الرسوم البيانية
    html.Div([
        dcc.Graph(id='chart-prices', style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id='chart-brands', style={'width': '49%', 'display': 'inline-block'}),
    ]),
    
    html.H3("جدول بيانات الهواتف:", style={'marginTop': '20px'}),
    dash_table.DataTable(
        id='data-table', 
        page_size=5,
        style_table={'overflowX': 'auto'},
        style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white', 'fontWeight': 'bold'},
        style_cell={'textAlign': 'center', 'padding': '10px'}
    )
])

@app.callback(
    [Output('kpi-phones', 'children'),
     Output('kpi-brands', 'children'),
     Output('kpi-avg-price', 'children'),
     Output('kpi-top-rating', 'children'),
     Output('chart-prices', 'figure'),
     Output('chart-brands', 'figure'),
     Output('data-table', 'data')],
    [Input('brand-filter', 'value')]
)
def update_dashboard(selected_brand):
    filtered_df = df if not selected_brand else df[df['Brand'] == selected_brand]
    
    total_phones = len(filtered_df)
    total_brands = filtered_df['Brand'].nunique() if not filtered_df.empty else 0
    avg_price = int(filtered_df['Price (EGP)'].mean()) if not filtered_df.empty else 0
    top_rating = filtered_df['Rating'].max() if not filtered_df.empty else 0
    
    fig1 = px.bar(filtered_df, x='Phone Name', y='Price (EGP)', color='Brand', title="أسعار الهواتف الذكية")
    fig2 = px.pie(filtered_df, names='Brand', title="توزيع الهواتف حسب الماركة")
    
    return total_phones, total_brands, f"{avg_price:,} ج.م", top_rating, fig1, fig2, filtered_df.to_dict('records')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8050, debug=True)