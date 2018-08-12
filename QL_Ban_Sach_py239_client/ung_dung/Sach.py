from flask import Flask, redirect, render_template, request, url_for, Markup, jsonify, session
from ung_dung import app
from ung_dung.Xu_ly.Xu_ly_Sach import *
from ung_dung.Xu_ly.Xu_ly_Ban_do import *
from flask_googlemaps import Map


# Tạo menu bar tại trang layout
@app.route("/", methods=['GET','POST'])
def index():
# bản đồ
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    if(request.form.get('Th_Ma_so')!=None):
        dia_chi = Doc_Doc_Dia_Chi_Nha_Sach_Theo_Ma_So(request.form.get('Th_Ma_so'))
        dia_chi = dia_chi[0]
    # print(dia_chi.kinh_do)
    # print(dia_chi.vi_do)
    # sách
    dsLoaiSach = Doc_DS_loai_Sach()
    dsSlider = Doc_DS_Slidder()
    dsSachNoiBat = Doc_DS_Sach_noi_Bat()
    
    return render_template('Layout.html',dsDiaChi=dsDiaChi, dia_chi=dia_chi,dsSlider=dsSlider,
        dsSachNoiBat=dsSachNoiBat,dsLoaiSach=dsLoaiSach)

# Tìm kiếm sách
@app.route("/tim-kiem", methods=['GET','POST'])
def TimKiem():
    dsLoaiSach = Doc_DS_loai_Sach()
    dsSlider = Doc_DS_Slidder()
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None
    
    ds_sach=Doc_DS_Sach()
    chuoi_tra_cuu=''
    if(request.form.get('search')!=None):
        chuoi_tra_cuu=request.form.get('search')
        ds_sach=Doc_DS_Tim_kiem(chuoi_tra_cuu,ds_sach)
    return render_template('Sach/Tim_kiem.html',ds_sach=ds_sach,chuoi_tra_cuu=chuoi_tra_cuu,dsLoaiSach=dsLoaiSach,
        dsDiaChi=dsDiaChi, dia_chi=dia_chi,dsSlider=dsSlider)

@app.route("/sach/<int:id>", methods=['GET','POST'])
def ChiTietSach(id):
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    sach = Doc_sach_Theo_id(id)
    dsLoaiSach = Doc_DS_loai_Sach()
    dssach_cung_loai=DSSachCungLoai(sach.id, sach.id_loai_sach)
    dssch_cung_tac_gia=DSSachCungTacGia(sach.id, sach.id_tac_gia)
    return render_template("Sach/Chi_tiet.html",sach=sach,DSSachCungLoai=dssach_cung_loai, dsLoaiSach=dsLoaiSach,
        DSSachCungTacGia=dssch_cung_tac_gia,dsDiaChi=dsDiaChi, dia_chi=dia_chi)

@app.route("/<int:id>/<string:tenloaisach>", methods=['GET','POST'])
def LoaiSach(id,tenloaisach):
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    tenloaisach=tenloaisach
    dsSlider = Doc_DS_Slidder()
    dsLoaiSach = Doc_DS_loai_Sach()
    dssach_theo_loai=Doc_sach_Theo_loai_Sach(id)
    return render_template("Layout.html",dsSachTheoLoai=dssach_theo_loai,dsSlider=dsSlider,
        dsLoaiSach=dsLoaiSach,tenloaisach=tenloaisach,dsDiaChi=dsDiaChi, dia_chi=dia_chi)
