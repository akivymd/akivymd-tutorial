from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
import kivymd_extensions.akivymd 
kv = '''
MDScreen:
	AKToolbarLayout:
		id:toolbar
		AKToolbarClass:
			MDToolbar:
				title:"Hide on scroll"
				left_action_items:[['menu']]
		AKToolbarPinClass:
			id:pin
			height:dp(40)
			MDChooseChip:
				MDChip:
					text:"kivy"
					icon:"play"
				MDChip:
					text:"kivymd"
					icon:"play"
				MDChip:
					text:"akivymd"
					icon:"play"
		AKToolbarContent:
			id:box
		AKToolbarFloatingButton:
			MDFloatingActionButton:
				icon:"arrow-up"
				on_release:toolbar.scroll_to(1)
		
	
			
			

'''
class Main(MDApp):
	def build(self):
  	  return Builder.load_string(kv)
	def on_start(self):
   	 for x in range(30):
   	     self.root.ids.box.add_widget(OneLineListItem(text=f"List {x}"))
   	 return super().on_start()
Main().run()