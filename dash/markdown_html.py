import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

options = [
    {'label': '佐藤', 'value': 'sato'},
    {'label': '鈴木', 'value': 'suzuki'},
    {'label': '田中', 'value': 'tanaka'}
]

app.layout = html.Div([
    dcc.Markdown('''
# 見出し1
## 見出し2

- 箇条書き
- 箇条書き
- 箇条書き
    '''),

    dcc.Markdown('---'),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=options,
        value='suzuki'
    ),

    dcc.Markdown('---'),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=options,
        value=['sato', 'suzuki'],
        multi=True
    ),

    dcc.Markdown('---'),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=options,
        value='suzuki'
    ),

    dcc.Markdown('---'),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=options,
        values=['suzuki', 'tanaka']
    ),

    dcc.Markdown('---'),
    html.Label('Checkboxes(Markdown)'),
    dcc.Markdown('''
- [x] 佐藤
- [ ] 鈴木
- [ ] 田中
    '''),

    dcc.Markdown('---'),
    html.Label('Text Input'),
    dcc.Input(
        value='佐藤',
        type='text'
    ),

    dcc.Markdown('---'),
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=5,
        marks={str(i): str(i) for i in range(1, 6)},
        value=3
    )
], style={'columnCount': 3})

if __name__ == '__main__':
    app.run_server(debug=True)
