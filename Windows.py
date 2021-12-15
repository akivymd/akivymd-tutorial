from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd_extensions.akivymd import*
from kivymd.app import MDApp
Builder.load_string(
    """

<Windows>
	MDBoxLayout:
        orientation: "vertical"


        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "Open Facebook Window"
                on_release: facebook.open()
            MDRaisedButton:
            	text: "Open Youtube Window"
            	on_release:youtube.open()

    AKFloatingWindowLayout:
		AKFloatingWindow:
   	     id:facebook
            window_title: "Facebook"
            size_hint: None, None
    		size: dp(300), dp(300)
 		   orientation: "vertical"

            MDLabel:
                text: "Facebook"
                halign: "center"
                valign: "center"
		AKFloatingWindow:
        	id: youtube
       	 window_title: "Youtube"
       	 size_hint: None, None
    		size: dp(300), dp(300)
 		   orientation: "vertical"
	        MDLabel:
	      	  text: "Youtube"
	            halign: "center"
	            valign: "center"
	
           
                
"""
)


class Windows(MDScreen):
    pass
class Test(MDApp):
    def build(self):
        return Windows()


Test().run()
