import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

layout = html.Div(className='root', children=[

	html.Div(className='box', children=[

		html.Div(className='head', children=[
			html.P(className='header-text', children=['New York Oil and Gas']),
			html.P(className='header-sub-text', children=['Production Overview'])
		]),

		html.Div(className='div1', children=[
			
			html.Div(className='div1-1', children=[
				html.P('Put Content Here')
			]),
			html.Div(className='div1-2', children=[

				html.Div(className='div1-2-1', children=[

					html.Div(className='div1-2-1-1', children=[
						html.P('Put Content Here')						
					]),
					html.Div(className='div1-2-1-2', children=[
						html.P('Put Content Here')
					]),
					html.Div(className='div1-2-1-3', children=[
						html.P('Put Content Here')
					]),
					html.Div(className='div1-2-1-4', children=[
						html.P('Put Content Here')
					])

				]),
				html.Div(className='div1-2-2', children=[
					html.P('Put Content Here')
				])

			])

		]),

		html.Div(className='div2', children=[

			html.Div(className='div2-1', children=[
				html.P('Put Content Here')
			]),
			html.Div(className='div2-2', children=[
				html.P('Put Content Here')
			])

		]),

		html.Div(className='div3', children=[

			html.Div(className='div3-1', children=[
				html.P('Put Content Here')
			]),
			html.Div(className='div3-2', children=[
				html.P('Put Content Here')
			])

		])

	]),
])