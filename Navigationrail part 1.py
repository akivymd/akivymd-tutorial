
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from kivymd_extensions.akivymd import *

Builder.load_string(
    """
<Navigationrail>
    name: "Navigationrail"

    AKNavigationrail:
        id: rail

        AKNavigationrailCustomItem:
            size_hint_y: None
            height: dp(60)
            padding: dp(5)

            MDIconButton:
                icon: "arrow-left"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                on_release:
                    if rail.get_state() == "open": rail.dismiss(); self.icon="menu"
                    else: rail.open(); self.icon ="arrow-left"

        AKNavigationrailItem:
            text: "Withdraw"
            icon: "wallet-plus"
           

        AKNavigationrailItem:
            text: "Deposit"
            icon: "wallet-plus-outline"
           

        AKNavigationrailItem:
            text: "Profile"
            icon: "account-circle-outline"
            

        AKNavigationrailCustomItem:

        AKNavigationrailContent:
"""
)


class Navigationrail(MDScreen):
    pass


class Test(MDApp):
    def build(self):
        return Navigationrail()


Test().run()