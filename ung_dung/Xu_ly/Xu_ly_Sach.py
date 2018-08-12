from flask import Markup, jsonify, session
from ung_dung.Xu_ly.Xu_ly_Model import *
from sqlalchemy import and_
from werkzeug.security import generate_password_hash,check_password_hash
from ung_dung import db
import json

# import re
# import sys

# patterns = {
#     '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
#     '[đ]': 'd',
#     '[èéẻẽẹêềếểễệ]': 'e',
#     '[ìíỉĩị]': 'i',
#     '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
#     '[ùúủũụưừứửữự]': 'u',
#     '[ỳýỷỹỵ]': 'y'
# }

# def convert(text):
#     """
#     Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
#     text: input string to be converted
#     Return: string converted
#     """
#     output = text
#     for regex, replace in patterns.items():
#         output = re.sub(regex, replace, output)
#         # deal with upper case
#         output = re.sub(regex.upper(), replace.upper(), output)
#     return output

# Lấy danh sách sách
def Doc_DS_Sach():
    dsSach = bs_sach.query.all()
    return dsSach
# Lấy danh sách tìm kiếm
def Doc_DS_Tim_kiem(search,dsSach):
    dsSach = bs_sach.query.filter(bs_sach.ten_sach.like("%"+search+"%")).all()
    return dsSach
# Lấy danh sách slide
def Doc_DS_Slidder():
    dsSlide = bs_slide_banner.query.filter_by(trang_thai=1).all()
    return dsSlide

# Lấy danh sách sách nổi bật
def Doc_DS_Sach_noi_Bat():
    dsSach = bs_sach.query.filter_by(noi_bat=1).all()
    return dsSach

# Lấy sách theo theo id
def Doc_sach_Theo_id(_id):
    sach = bs_sach.query.filter_by(id=_id).first()
    return sach

#-----begin-----xử lý giỏ hàng-------
def Lay_chi_tiet_Sach(Danh_sach_sach, Ma_so):
    Danh_sach  = list(filter(lambda Sach: Sach["id"] == Ma_so, Danh_sach_sach))
    print(Danh_sach)
    Sach = Danh_sach[0] if len(Danh_sach)>=1 else None
    return Sach
#-----end------

# Lấy sách trong giỏ hàng theo id
def Doc_sach_Trong_gio_Hang_theo_Id(_dsSach,_id):
    sach = _dsSach.query.filter_by(id=_id)
    return sach

# Lấy danh sách cùng loại
def DSSachCungLoai(_id, ma_loai):
    DSSach = bs_sach.query.filter(and_(bs_sach.id !=_id, bs_sach.id_loai_sach==ma_loai)).all()
    return DSSach

# Lấy danh sách cùng tác giả
def DSSachCungTacGia(_id, ma_tac_gia):
    DSSach = bs_sach.query.filter(and_(bs_sach.id !=_id, bs_sach.id_tac_gia==ma_tac_gia)).all()
    return DSSach

# Lấy danh sách sách theo loại
def Doc_sach_Theo_loai_Sach(_id):
    sachTheoloai = bs_sach.query.filter_by(id_loai_sach=_id).all()
    return sachTheoloai

# Lấy danh sách loại sách
def Doc_DS_loai_Sach():
    dsLoaiSach = bs_loai_sach.query.filter_by(trang_thai=1).all()
    return dsLoaiSach

# Hiển thị sách tìm kiếm
# def Chuoi_html_sach_tim_kiem(dsSach,search):
#     Chuoi_html_ds_sach='''
#     <div style="width:100%; border-bottom:1px solid #cacbcc">
# 		<div style=" text-align:center; color:#fff; font-size:20px; margin-bottom: 5px; background: #0f5731; padding:8px 5px; 
# 	border-radius: 5px; width:250px; border-bottom:1px solid #cacbcc">TÌM KIẾM SÁCH: '''+search+''' </div>
# 		</div>'''
#     dem=1
#     for sach in dsSach:
#         if(dem==1):
#             Chuoi_html_ds_sach+='''<div class="content-top1">'''
#             if dem>2:
#                 Chuoi_html_ds_sach+='''<div class="col-md-3 col-md2 animated wow fadeInRight" data-wow-delay=".5s">'''
#             else:
#                 Chuoi_html_ds_sach+='''<div class="col-md-3 col-md2 animated wow fadeInLeft" data-wow-delay=".5s">'''
#             Chuoi_html_ds_sach+='''<div class="col-md1 simpleCart_shelfItem">
#             <a href="/sach/'''+(str(sach.id)+'''">
#                 <img class="img-responsive" src="'''+url_for('static', filename='image/'+sach.hinh)+'''" alt="'''+sach.ten_sach+'''" />
#             </a>
#             <h2 style="font-size:medium;"><a href="/sach/'''+(str(sach.id)+'''">'''+sach.ten_sach+'''</a></h2>
#             <div class="price">
#                 <h5 class="item_price">{:,}'''.format(sach.don_gia).replace(",",".")+'''đ</h5>
                
#                 <div class="clearfix"> </div>
#             </div>
#             </div>
#             </div>'''
#             dem+=1
#         else:
#             if(dem>2):
#                 Chuoi_html_ds_sach+='''<div class="col-md-3 col-md2 animated wow fadeInRight" data-wow-delay=".5s">'''
#             else:
#                 Chuoi_html_ds_sach+='''<div class="col-md-3 col-md2 animated wow fadeInLeft" data-wow-delay=".5s">'''

#             Chuoi_html_ds_sach+='''<div class="col-md1 simpleCart_shelfItem">
#             <a href="/sach/'''+(str(sach.id)+'''">
#                 <img class="img-responsive" src="'''+url_for('static', filename='image/'+sach.hinh)+'''" alt="'''+sach.ten_sach+'''" />
#             </a>
#             <h2 style="font-size:medium"><a href="/sach/'''+(str(sach.id)+'''">'''+sach.ten_sach+'''</a></h2>
#             <div class="price">
#                 <h5 class="item_price">{:,}'''.format(sach.don_gia).replace(",",".")+'''đ</h5>

#                 <div class="clearfix"> </div>
#             </div>
#             </div>
#             </div>'''
#             dem+=1
#             if(dem>4):
#                 Chuoi_html_ds_sach+='''</div>
#                 <div class="clearfix"> </div>'''
#                 dem=1

#     if(dem<4):
#         Chuoi_html_ds_sach+='''</div>
#         <div class="clearfix"> </div>'''
#     return Chuoi_html_ds_sach