import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([dcc.Input(id='input-div', value='initial value', type='text'),
              dcc.Input(id='input-div2', value='initial value', type='text')]),
    html.Div([html.Span(id='output-div'),
              html.Span(id='output-div2')])
])


@app.callback(
    [Output(component_id='output-div', component_property='children'),
     Output(component_id='output-div2', component_property='children')],
    [Input(component_id='input-div', component_property='value'),
     Input(component_id='input-div2', component_property='value')]
)
def update(input_value, input_value2):
    v1 = 'You entered "{}"'.format(input_value) if input_value else 'Please enter'
    v2 = 'You entered "{}"'.format(input_value2) if input_value2 else 'Please enter'
    return v1, v2


if __name__ == '__main__':
    app.run_server(debug=True)
