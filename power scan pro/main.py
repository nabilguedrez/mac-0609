from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="مرحباً بك في PowerScan Pro"))
        self.add_widget(Button(text="ابدأ", size_hint=(1, 0.2)))

class PowerScanApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    PowerScanApp().run()
