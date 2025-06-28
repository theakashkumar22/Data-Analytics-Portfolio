import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv('data/superstore.csv')

# Prepare data
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()

# Save aggregated data
sales_by_category.to_csv('sales_by_category.csv', index=False)
sales_by_region.to_csv('sales_by_region.csv', index=False)
sales_by_segment.to_csv('sales_by_segment.csv', index=False)

# Initialize Dash app
app = dash.Dash(__name__)

# Create initial plots
fig_category = px.bar(sales_by_category, x='Category', y='Sales', title='Sales by Category')
fig_region = px.pie(sales_by_region, names='Region', values='Sales', title='Sales Distribution by Region')
fig_segment = px.bar(sales_by_segment, x='Segment', y='Sales', title='Sales by Segment')

# Dashboard layout
app.layout = html.Div([
    html.H1('Superstore Sales Dashboard', style={'textAlign': 'center'}),
    html.H3('Interactive dashboard to visualize sales metrics', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in df['Region'].unique()] + [{'label': 'All Regions', 'value': 'All'}],
        value='All',
        placeholder='Select a Region',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='category-bar', figure=fig_category),
    dcc.Graph(id='region-pie', figure=fig_region),
    dcc.Graph(id='segment-bar', figure=fig_segment)
])

# Callback for interactivity
@app.callback(
    [dash.dependencies.Output('category-bar', 'figure'),
     dash.dependencies.Output('segment-bar', 'figure')],
    [dash.dependencies.Input('region-dropdown', 'value')]
)
def update_charts(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    # Update category bar plot
    category_data = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_category = px.bar(category_data, x='Category', y='Sales', title=f'Sales by Category ({selected_region})')

    # Update segment bar plot
    segment_data = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
    fig_segment = px.bar(segment_data, x='Segment', y='Sales', title=f'Sales by Segment ({selected_region})')

    return fig_category, fig_segment

# Run app
if __name__ == '__main__':
    app.run(debug=True)