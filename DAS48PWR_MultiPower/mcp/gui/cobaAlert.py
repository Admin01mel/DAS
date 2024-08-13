from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
#:import SweetAlert kivymd.components.sweetalert.SweetAlert


MDScreen:

    MDRaisedButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: SweetAlert(window_control_buttons="mac-style").fire("Message!")
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()