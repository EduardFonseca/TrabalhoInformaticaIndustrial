from kivymd.app import MDApp
from mainwidget import MyWidget
from kivy.lang.builder import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Blue"
        self._addr ={
            'freq_des': [799,1],
            'freq_mot': [800,10],
            'tensao': [801,1],
            'rotacao': [803,1],
            'pot_entrada': [804,1],
            'corrente': [805,100],
            'temp_estator': [806,10],
            'vel_esteira': [807,100],
            'carga': [808,100],
            'peso_obj': [809,1],
            'cor_obj_R': [810,1],
            'cor_obj_G': [811,1],
            'cor_obj_B': [812,1],
            'num_obj_est_1': [813,1],
            'num_obj_est_2': [814,1],
            'num_obj_est_3': [815,1],
            'num_obj_est_nc': [816,1],
            }
        self._widget = MyWidget(modbus_addr= self._addr)
        return self._widget


if __name__ == "__main__":
    Builder.load_string(open("mainwidget.kv",encoding='utf-8').read(),rulesonly=True)
    MainApp().run()