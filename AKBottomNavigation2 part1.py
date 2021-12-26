from kivy.lang import Builder
from kivymd_extensions.akivymd import*
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
Builder.load_string(
    """
<BottomNavigation>:
	AKBottomNavigation2:
		Button_Item:
			text:"youtube-gameing"
			icon:"youtube-gaming"
			badge_disabled:True
		Button_Item:
			text:"youtube-studio"
			icon:"youtube-studio"
			badge_disabled:True
		Button_Item:
			text:"youtube-subscription"
			icon:"youtube-subscription"
			badge_disabled:True
		
"""
)
class BottomNavigation(MDScreen):
	pass
class Test(MDApp):
	def build(self):
		return BottomNavigation()
Test().run()