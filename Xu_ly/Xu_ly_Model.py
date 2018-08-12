from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_admin.contrib import sqla
from ung_dung import db

class bs_loai_tin_tuc(db.Model):
    __tablename__='bs_loai_tin_tuc'
    id = db.Column(Integer, primary_key = True)
    ten_loai_tin = db.Column(String(200), nullable = False)
    alias = db.Column(String(200), nullable = True)
    def __str__(self):
        return self.ten_loai_tin

class bs_tin_tuc(db.Model):
    __tablename__='bs_tin_tuc'
    id = db.Column(Integer, primary_key = True)
    tieu_de_tin = db.Column(String(225), nullable = False)
    noi_dung_tom_tat = db.Column(String(500), nullable = False)
    noi_dung_chi_tiet = db.Column(String(1000), nullable = False)
    trang_thai = db.Column(db.Boolean, nullable = False)
    hinh_dai_dien = db.Column(String(200), nullable = False)
    id_loai_tin_tuc = db.Column(Integer, db.ForeignKey('bs_loai_tin_tuc.id'), nullable = False)
    loai_tin_tuc = db.relationship('bs_loai_tin_tuc', backref=db.backref('bs_tin_tuc'), lazy=True)
    ngay_dang = db.Column(db.DateTime, nullable = False)

class bs_loai_nguoi_dung(db.Model):
    __tablename__ = "bs_loai_nguoi_dung"
    id = db.Column(Integer, nullable = False, primary_key = True)
    ten_loai_nguoi_dung = db.Column(String(255), nullable = False)
    def __str__(self):
        return self.ten_loai_nguoi_dung

class bs_khach_hang(db.Model):    
    __tablename__ = "bs_khach_hang"
    ma_khach_hang = db.Column(db.Integer, primary_key=True)
    ten_khach_hang   = db.Column(db.String(100), nullable=False)
    phai = db.Column(db.Boolean)
    ngay_sinh      = db.Column(db.DateTime)
    dia_chi    = db.Column(db.String(200))
    dien_thoai    = db.Column(db.String(20))
    email     = db.Column(db.String(120))
    ngay_mua = db.Column(db.DateTime)
    sach_mua     = db.Column(db.String)
    ghi_chu     = db.Column(db.String)
    def __str__(self):
        return self.ten_khach_hang

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    ma_loai_nguoi_dung = db.Column(db.String(50), db.ForeignKey('bs_loai_nguoi_dung.id')) 
    loai_nguoi_dung = db.relationship('bs_loai_nguoi_dung', backref=db.backref('user', lazy=True))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.last_name

    def __str__(self):
        return self.ho_ten    

class bs_loai_sach(db.Model):
    __tablename__ = "bs_loai_sach"
    id = db.Column(Integer, nullable = False, primary_key = True)
    ten_loai_sach = db.Column(String(255), nullable = False)
    id_loai_cha = db.Column(Integer, nullable = False)
    sap_xep = db.Column(String(255), nullable = True)
    trang_thai = db.Column(db.Boolean, nullable = False)
    def __str__(self):
        return self.ten_loai_sach

class bs_nha_xuat_ban(db.Model):
    __tablename__='bs_nha_xuat_ban'
    id = db.Column(Integer, primary_key = True)
    ten_nha_xuat_ban = db.Column(String(100), nullable = False)
    dia_chi = db.Column(String(200), nullable = False)
    dien_thoai = db.Column(String(50), nullable = False)
    email = db.Column(String(100), nullable = False)
    def __str__(self):
        return self.ten_nha_xuat_ban

class bs_tac_gia(db.Model):
    __tablename__='bs_tac_gia'
    id = db.Column(Integer, primary_key = True)
    ten_tac_gia = db.Column(String(200), nullable = False)
    ngay_sinh = db.Column(String(200), nullable = False)
    gioi_thieu = db.Column(String(500), nullable = True)
    def __str__(self):
        return self.ten_tac_gia

class bs_sach(db.Model):
    __tablename__='bs_sach'
    id = db.Column(Integer, primary_key = True)
    ten_sach = db.Column(String(255), nullable = False)
    id_tac_gia = db.Column(String(255), db.ForeignKey('bs_tac_gia.id'), nullable = False)
    tac_gia = db.relationship('bs_tac_gia',backref=db.backref('bs_sach'),lazy=True)
    gioi_thieu = db.Column(String(500), nullable = False)
    doc_thu = db.Column(String(255), nullable = True)
    id_loai_sach = db.Column(Integer, db.ForeignKey('bs_loai_sach.id'), nullable = False)
    loai_sach = db.relationship('bs_loai_sach',backref=db.backref('bs_sach'),lazy=True)
    id_nha_xuat_ban = db.Column(Integer, db.ForeignKey('bs_nha_xuat_ban.id'), nullable = False)
    nha_xuat_ban = db.relationship('bs_nha_xuat_ban',backref=db.backref('bs_sach'),lazy=True)
    so_trang = db.Column(Integer, nullable = True)
    ngay_xuat_ban = db.Column(String(50), nullable = True)
    kich_thuoc = db.Column(String(255), nullable = True)
    sku = db.Column(String(255), nullable = True)
    trong_luong = db.Column(String(255), nullable = True)
    trang_thai = db.Column(db.Boolean, nullable = False)
    hinh = db.Column(String(255), nullable = False)
    don_gia = db.Column(Integer, nullable = False)
    gia_bia = db.Column(Integer, nullable = False)
    noi_bat = db.Column(db.Boolean, nullable = False)
    def __str__(self):
        return self.ten_sach

class bs_slide_banner(db.Model):
    __tablename__='bs_slide_banner'
    id = db.Column(Integer, primary_key = True)
    ten_slide = db.Column(String(255), nullable = False)
    hinh  = db.Column(String(255), nullable = False)
    trang_thai  = db.Column(db.Boolean, nullable = False)

class bs_dia_diem_nha_sach(db.Model):
    __tablename__='bs_dia_diem_nha_sach'
    ma_dia_diem = db.Column(Integer, primary_key = True)
    ten_dia_diem = db.Column(String(100), nullable = False)
    vi_do  = db.Column(String, nullable = False)
    kinh_do  = db.Column(String, nullable = False)
    trang_thai = db.Column(db.Boolean)

# class bs_binh_luan(db.Model):
#     __tablename__ = "bs_binh_luan"
#     id = db.Column(Integer, nullable = False, primary_key = True)
#     id_sach = db.Column(Integer, db.ForeignKey('bs_sach.id'), nullable = True)
#     sach = db.relationship('bs_sach',backref=db.backref('bs_binh_luan'),lazy=True)
#     id_nguoi_dung = db.Column(Integer, db.ForeignKey('User.id'), nullable = True)
#     nguoi_dung = db.relationship('User',backref=db.backref('bs_binh_luan'),lazy=True)
#     noi_dung = db.Column(String(225), nullable = True)
#     id_binh_luan_cha = db.Column(Integer, nullable = True)
#     ngay_binh_luan = db.Column(Integer, nullable = True)
#     trang_thai = db.Column(Integer, nullable = True)

# class bs_chat_truc_tuyen(db.Model):
#     __tablename__ = "bs_chat_truc_tuyen"
#     id = db.Column(Integer, nullable = False, primary_key = True)
#     id_nguoi_dung = db.Column(Integer, db.ForeignKey('User.id'), nullable = True)
#     nguoi_dung = db.relationship('User',backref=db.backref('bs_chat_truc_tuyen'),lazy=True)
#     ip = db.Column(String(255), nullable = True)
#     dang_online = db.Column(Integer, nullable = True)
#     da_duoc_tra_loi = db.Column(Integer, nullable = True)
#     session_id_chat = db.Column(Integer, nullable = True)
#     ho_ten = db.Column(String(255), nullable = True)
#     email = db.Column(String(255), nullable = True) 

# class bs_chi_tiet_chat(db.Model):
#     __tablename__ = "bs_chi_tiet_chat"
#     id = db.Column(Integer, nullable = False, primary_key = True)
#     session_id_chat = db.Column(Integer, nullable = True)
#     id_nguoi_dung_tl = db.Column(Integer, nullable = True)
#     time_chat = db.Column(Integer, nullable = True)
#     noi_dung = db.Column(String(255), nullable = True)

# class bs_danh_gia_sach(db.Model):
#     __tablename__ = "bs_danh_gia_sach"
#     id = db.Column(Integer, nullable = False, primary_key = True)
#     danh_gia = db.Column(Integer, nullable = True)
#     id_nguoi_dung = db.Column(Integer, db.ForeignKey('User.id'), nullable = True)
#     nguoi_dung = db.relationship('User',backref=db.backref('bs_danh_gia_sach'),lazy=True)

# class bs_sach_yeu_thich(db.Model):
#     __tablename__='bs_sach_yeu_thich'
#     id = db.Column(Integer, primary_key = True)
#     id_nguoi_dung = db.Column(Integer, db.ForeignKey('User.id'), nullable = False)
#     nguoi_dung = db.relationship('User',backref=db.backref('bs_sach_yeu_thich'),lazy=True)
#     id_sach = db.Column(Integer, db.ForeignKey('bs_sach.id'), nullable = False)
#     sach = db.relationship('bs_sach',backref=db.backref('bs_sach_yeu_thich'),lazy=True)

# class bs_menu(db.Model):
#     __tablename__='bs_menu'
#     id = db.Column(Integer, primary_key = True)
#     tieu_de = db.Column(String(100), nullable = False)
#     alias = db.Column(String(200), nullable = False)
#     trang_thai = db.Column(Integer, nullable = False)
#     menu_cha = db.Column(Integer, nullable = False)
    
db.create_all()
