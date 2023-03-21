import os
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)


app = Dash(__name__)
server = app.server
# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")


# os.chdir('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Onderzoek/n supraorbi occipitalis major/python xlsx files/Plotly xlsx files')

# df = pd.read_csv('https://raw.githubusercontent.com/ExanVUB/SONGON_Dash-app/main/app_data.csv')
df = pd.read_csv('app_data2.csv')

# df_son41 = pd.read_excel('41 supraorb plotly.xlsx')
# df_son70 = pd.read_excel('70 supraorb plotly.xlsx')
# df_son74 = pd.read_excel('74 supraorb plotly.xlsx')
# df_son80 = pd.read_excel('80 supraorb plotly.xlsx')
# df_son103 = pd.read_excel('103 supraorb plotly.xlsx')
# df_son122 = pd.read_excel('122 supraorb plotly.xlsx')
# df_son158 = pd.read_excel('158 supraorb plotly.xlsx')
# df_son183 = pd.read_excel('183 supraorb plotly.xlsx')
# df_son197 = pd.read_excel('197 supraorb plotly.xlsx')

# df.reset_index(inplace=True)
# print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Supra orbital nerve and greater occipital nerve", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_specimen",
                 options=[
                     {"label": "SON specimen 41", "value": 41},
                     {"label": "SON specimen 70", "value": 70},
                     {"label": "SON specimen 74", "value": 74},
                     {"label": "SON specimen 80", "value": 80},
                     {"label": "SON specimen 103", "value": 103},
                     {"label": "SON specimen 122", "value": 122},
                     {"label": "SON specimen 158", "value": 158},
                     {"label": "SON specimen 183", "value": 183},
                     {"label": "SON specimen 197 ", "value": 197},
                     {"label": "GON specimen 41 ", "value": 541},
                     {"label": "GON specimen 70 ", "value": 570},
                     {"label": "GON specimen 74 ", "value": 574},
                     {"label": "GON specimen 80 ", "value": 580},
                     {"label": "GON specimen 103 ", "value": 5103},
                     {"label": "GON specimen 122 ", "value": 5122},
                     {"label": "GON specimen 158 ", "value": 5158},
                     {"label": "GON specimen 183 ", "value": 5183},
                     {"label": "GON specimen 197 ", "value": 5197},
                     {"label": "SON-GON specimen 41 ", "value": 941},
                     {"label": "SON-GON specimen 70 ", "value": 970},
                     {"label": "SON-GON specimen 74 ", "value": 974},
                     {"label": "SON-GON specimen 80 ", "value": 980},
                     {"label": "SON-GON specimen 103 ", "value": 9103},
                     {"label": "SON-GON specimen 122 ", "value": 9122},
                     {"label": "SON-GON specimen 158 ", "value": 9158},
                     {"label": "SON-GON specimen 183 ", "value": 9183},
                     {"label": "SON-GON specimen 197 ", "value": 9197},
                 ],
                 multi=False,
                 value=41,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='3D plot',style={
        # 'width': '90vh',
        'height': '90vh'})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='3D plot', component_property='figure')],
    [Input(component_id='slct_specimen', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "Showing 3D plot for specimen: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["specimen"] == option_slctd]
    # dff = dff[dff["Affected by"] == "Varroa_mites"]
    # # Plotly Express
    # fig = px.choropleth(
    #     data_frame=dff,
    #     locationmode='USA-states',
    #     locations='state_code',
    #     scope="usa",
    #     color='Pct of Colonies Impacted',
    #     hover_data=['State', 'Pct of Colonies Impacted'],
    #     color_continuous_scale=px.colors.sequential.YlOrRd,
    #     labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    #     template='plotly_dark'
    # )

    fig1 = px.line_3d(dff, x='x', y='y', z='z',
                      color='line'
                      )
    fig2 = px.scatter_3d(dff, x='x', y='y', z='z',
                         color='scatter'
                         )

    fig1.update_traces(patch={"line": {
        "dash": "solid",
        # "shape": "spline",
        "width": 5
    }
    })

    fig2.update_traces(marker={
        "size": 7,
        "color": "blue",
        "opacity": 0.5,
        "line": {"width": 2, "color": "cyan"},
        # "symbol": "square"
    })

    fig = go.Figure(data=fig1.data + fig2.data)

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)