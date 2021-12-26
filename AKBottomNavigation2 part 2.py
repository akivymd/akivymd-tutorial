from kivy.lang import Builder
from kivymd_extensions.akivymd import*
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
Builder.load_string(
    """
<BottomNavigation>:
	ScreenManager:
		id:scr
		MDScreen:
			name:'youtube-gameing'
			MDLabel:
				text:"Youtube gameing screen"
				halign:"center"
		MDScreen:
			name:'youtube-studio'
			MDLabel:
				text:"Youtube studio screen"
				halign:"center"
		MDScreen:
			name:'youtube-subscription'
			MDLabel:
				text:"Youtube subscription screen"
				halign:"center"
	AKBottomNavigation2:
		Button_Item:
			text:"youtube-gameing"
			icon:"youtube-gaming"
			badge_disabled:True
			on_release:scr.current='youtube-gameing'
		Button_Item:
			text:"youtube-studio"
			icon:"youtube-studio"
			badge_disabled:True
			on_release:scr.current='youtube-studio'
		Button_Item:
			text:"youtube-subscription"
			icon:"youtube-subscription"
			badge_disabled:True
			on_release:scr.current='youtube-subscription'
		
"""
)
class BottomNavigation(MDScreen):
	pass
class Test(MDApp):
	def build(self):
		return BottomNavigation()
Test().run()