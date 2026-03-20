from kivy.app import App
from kivy.uix.button import Button
import webbrowser

class ZenoApp(App):
    def build(self):
        btn = Button(text="OPEN YOUTUBE", font_size=30)
        btn.bind(on_press=self.open_yt)
        return btn

    def open_yt(self, instance):
        webbrowser.open("https://youtube.com")

ZenoApp().run()
