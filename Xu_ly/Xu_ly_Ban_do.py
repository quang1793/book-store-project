from flask import session
from ung_dung import db
from ung_dung.Xu_ly.Xu_ly_Model import *
from sqlalchemy import and_

def Doc_Dia_Chi_Nha_Sach():
    dsDiaChi = db.session.query(bs_dia_diem_nha_sach).filter_by(trang_thai=1).all()
    print(dsDiaChi)
    return dsDiaChi

def Doc_Doc_Dia_Chi_Nha_Sach_Theo_Ma_So(_maSo):
    diaChiChon = db.session.query(bs_dia_diem_nha_sach).filter(and_(bs_dia_diem_nha_sach.trang_thai==1,bs_dia_diem_nha_sach.ma_dia_diem==_maSo)).all()
    return diaChiChon