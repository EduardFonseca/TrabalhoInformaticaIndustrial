from sqlalchemy.engine import interfaces
from sqlalchemy.sql.sqltypes import BOOLEAN
from db import Base
from sqlalchemy import Column, Integer, DateTime, Float, Boolean

class DadosIndustria(Base):
    __tablename__ = 'DadosEsteira'
    id = Column(Integer,primary_key = True, autoincrement = True)
    timestamp = Column(DateTime)
    estado_atuador = Column(Boolean)
    bt_desliga = Column(Boolean)
    t_part = Column(Integer)
    freq_des = Column(Integer)
    freq_mot = Column(Float)
    tensao = Column(Integer)
    rotacao = Column(Integer)
    pot_entrada = Column(Integer)
    corrente = Column(Float)
    temp_estator = Column(Float)
    vel_esteira = Column(Float)
    carga = Column(Float)
    peso_obj = Column(Integer)
    cor_obj_R = Column(Integer)
    cor_obj_G = Column(Integer)
    cor_obj_B = Column(Integer)
    num_obj_est_1 = Column(Integer)
    num_obj_est_2 = Column(Integer)
    num_obj_est_3 = Column(Integer)
    num_obj_est_nc = Column(Integer)
   #Filtros e suas classificacoes
    filtro_est_1 = Column(Boolean)
    filtro_est_2 = Column(Boolean)
    filtro_est_3 = Column(Boolean)
    filtro_cor_r_1 = Column(Integer)
    filtro_cor_g_1 = Column(Integer)
    filtro_cor_b_1 = Column(Integer)
    filtro_massa_1 = Column(Integer)
    filtro_cor_r_2 = Column(Integer)
    filtro_cor_g_2 = Column(Integer)
    filtro_cor_b_2 = Column(Integer)
    filtro_massa_2 = Column(Integer)
    filtro_cor_r_3 = Column(Integer)
    filtro_cor_g_3 = Column(Integer)
    filtro_cor_b_3 = Column(Integer)
    filtro_massa_3 = Column(Integer)

    def get_attr_printable_list(self):
        return{
            'timestamp': self.timestamp.strftime('%d/%m/%Y %H:%M:%S.%f'),
            'estado_atuador': self.estado_atuador,
            'bt_desliga': self.bt_desliga,
            't_part': self.t_part,
            'freq_des': self.freq_des,
            'freq_mot': self.freq_mot,
            'tensao': self.tensao,
            'rotacao': self.rotacao,
            'pot_entrada': self.pot_entrada,
            'corrente': self.corrente,
            'temp_estator': self.temp_estator,
            'vel_esteira': self.vel_esteira,
            'carga': self.carga,
            'peso_obj': self.peso_obj,
            'cor_obj_R': self.cor_obj_R,
            'cor_obj_G': self.cor_obj_G,
            'cor_obj_B': self.cor_obj_B,
            'num_obj_est_1': self.num_obj_est_1,
            'num_obj_est_2': self.num_obj_est_2,
            'num_obj_est_3': self.num_obj_est_3,
            'num_obj_est_nc': self.num_obj_est_nc,

            #filtros e classificacoes
            'filtro_est_1':self.filtro_est_1,
            'filtro_est_2':self.filtro_est_2,
            'filtro_est_3':self.filtro_est_3,
            'filtro_cor_r_1':self.filtro_cor_r_1,
            'filtro_cor_g_1':self.filtro_cor_b_1,
            'filtro_cor_b_1':self.filtro_cor_g_1,
            'filtro_massa_1':self.filtro_massa_1,
            'filtro_cor_r_2':self.filtro_cor_r_2,
            'filtro_cor_g_2':self.filtro_cor_b_2,
            'filtro_cor_b_2':self.filtro_cor_g_2,
            'filtro_massa_2':self.filtro_massa_2,
            'filtro_cor_r_3':self.filtro_cor_r_3,
            'filtro_cor_g_3':self.filtro_cor_b_3,
            'filtro_cor_b_3':self.filtro_cor_g_3,
            'filtro_massa_3':self.filtro_massa_3,
            }

