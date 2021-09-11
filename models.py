from sqlalchemy.engine import interfaces
from db import Base
from sqlalchemy import Column, Integer, DateTime, Float

class DadosIndustria(Base):
    __tablename__ = 'DadosEsteira'
    id = Column(Integer,primary_key = True, autoincrement = True)
    timestamp = Column(DateTime)
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

    def get_attr_printable_list(self):
        return{
            'timestamp': self.timestamp.strftime('%d/%m/%Y %H:%M:%S.%f'),
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
            'num_obj_est_nc': self.num_obj_est_nc
            }