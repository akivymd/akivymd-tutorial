from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd_extensions.akivymd import*
from kivymd.app import MDApp
Builder.load_string(
    """
<ProgressWidget>:
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			orientation:"vertical"
			padding:dp(30)
			spacing:dp(30)
			AKCircularProgress:
				id:progress_widget
				pos_hint:{"center_x":.5,"center_y":.7}
				size_hint:None,None
				size:dp(200),dp(200)
				percent_type:"relative"
				start_deg:180
				end_deg:500
				max_percent:100
			MDRaisedButton:
				text:"33"
				on_release:progress_widget.current_percent=33
			MDRaisedButton:
				text:"60"
				on_release:progress_widget.current_percent=60
				
#Thanks for watching			
			
			
"""
)

class ProgressWidget(MDScreen):
    pass
    
class Test(MDApp):
	def build(self):
		return ProgressWidget()
Test().run()