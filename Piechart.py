from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd_extensions.akivymd import*
from kivymd_extensions.akivymd.uix.charts import AKPieChart
Builder.load_string(
    """
<Piechart>
	MDBoxLayout:
		orientation:"vertical"
		ScrollView:
			MDBoxLayout:
				id:chart_box
				orientation:"vertical"
				padding:dp(24)
				adaptive_height:True
				
				
"""
)


class Piechart(MDScreen):
	items=[{"kivy":30,"kivymd":20,"akivymd":15,"django":35}]
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	def on_enter(self):
		self.piechart=AKPieChart(
			items=self.items,
			pos_hint={"center_x":.5,"center_y":.5},
			size_hint=[None,None],
			size=(dp(300),dp(300)),
			)
			
			
		self.ids.chart_box.add_widget(self.piechart)
		
		
		
		
class Test(MDApp):
    def build(self):
        self.window = Piechart()
        return self.window
    def on_start(self):
    	self.window.dispatch("on_enter")
Test().run()
