from flask import Markup, jsonify
from ung_dung.Xu_ly.Xu_ly_Model import *
from sqlalchemy import and_
from werkzeug.security import generate_password_hash,check_password_hash
from ung_dung import db
import json




# Lấy tất cả tin tức
def Doc_ds_tin_tuc():
    dsTinTuc=[]
    tin = bs_tin_tuc.query.all()
    for s in tin:
        tin_dict={}
        tin_dict['id']=s.id
        tin_dict['tieu_de_tin']=s.tieu_de_tin
        tin_dict['noi_dung_tom_tat']=s.noi_dung_tom_tat
        tin_dict['noi_dung_chi_tiet']=s.noi_dung_chi_tiet
        tin_dict['hinh_dai_dien']=s.hinh_dai_dien
        dsTinTuc.append(tin_dict)
    return dsTinTuc

def Doc_ds_loai_tin():
    dsLoaiTin=[]
    loaitin = bs_loai_tin_tuc.query.all()
    for s in loaitin:
        loaitin_dict={}
        loaitin_dict['id']=s.id
        loaitin_dict['ten_loai_tin']=s.ten_loai_tin
        loaitin_dict['alias']=s.alias
        dsLoaiTin.append(loaitin_dict)
    return dsLoaiTin

