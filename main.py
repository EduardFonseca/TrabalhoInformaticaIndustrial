from kivymd.app import MDApp
from mainwidget import MyWidget
from kivy.lang.builder import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Blue"
        self._addr ={
            'estado_atuador':[801,1],
            'bt_desliga':[802,1],
            't_part':[798,10],
            'freq_des': [799,1], # somente Escrita
            'freq_mot': [800,10],
            'tensao': [801,1],
            'rotacao': [803,1],
            'pot_entrada': [804,1],
            'corrente': [805,100],
            'temp_estator': [806,10],
            'vel_esteira': [807,100],
            'carga': [808,100],
            'peso_obj': [809,100],
            'cor_obj_R': [810,1],
            'cor_obj_G': [811,1],
            'cor_obj_B': [812,1],
            'num_obj_est_1': [813,1],
            'num_obj_est_2': [814,1],
            'num_obj_est_3': [815,1],
            'num_obj_est_nc': [816,1],
            #Filtros e suas classificacoes
            'filtro_est_1': [901,1], #coil
            'filtro_est_2': [902,1], #coil
            'filtro_est_3': [903,1], #coil
            'filtro_cor_r_1':[1001,1],
            'filtro_cor_g_1':[1002,1],
            'filtro_cor_b_1':[1003,1],
            'filtro_massa_1':[1004,1],
            'filtro_cor_r_2':[1011,1],
            'filtro_cor_g_2':[1012,1],
            'filtro_cor_b_2':[1013,1],
            'filtro_massa_2':[1014,1],
            'filtro_cor_r_3':[1021,1],
            'filtro_cor_g_3':[1022,1],
            'filtro_cor_b_3':[1023,1],
            'filtro_massa_3':[1024,1],
            }
        self._widget = MyWidget(modbus_addr= self._addr)
        return self._widget


if __name__ == "__main__":
    Builder.load_string(open("mainwidget.kv",encoding='utf-8').read(),rulesonly=True)
    MainApp().run()