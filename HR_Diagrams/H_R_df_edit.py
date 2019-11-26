from ipywidgets import widgets
from IPython.display import display

class Interactive_df_editor():
	def __init__(self, df, editable_columns, types=None):
		self.dataFrame = df
		self.editables = editable_columns
		self.types = types
		self.widgets = []
	
	def make_inputs(self):
		for edit in editables:
			self.widgets.append(widgets.Text(value=0.0,description=edit,disabled=False))
		self.widgets.append(widgets.Button(description='Submit', disabled=False, tooltip='Click to submit'))

	def display_widgets(self):
		for widget in self.widgets:
			display(widget)

def a(math):
	print(math)
