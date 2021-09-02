from kivymd.app import MDApp
from mainwidget import MyWidget
from kivy.lang.builder import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Blue"
        return MyWidget()



if __name__ == "__main__":
    Builder.load_string(open("mainwidget.kv",encoding='utf-8').read(),rulesonly=True)
    MainApp().run()