from flask import Flask, redirect, render_template, request, url_for, Markup, jsonify, session
from ung_dung import app
from ung_dung.Xu_ly.Xu_ly_Sach import *
from ung_dung.Xu_ly.Xu_ly_gio_hang import *
from ung_dung.Xu_ly.Xu_ly_Ban_do import *

@app.route('/gio-hang/them-gio-hang', methods=['POST'])
def ThemGioHang():  
    json=request.get_json()
    So_luong=int(json['soLuong'])
    Ma_so=json['maSP']
    Sach=db.session.query(bs_sach).filter_by(id=Ma_so).first()
    if (Sach != None):
        Sach_Chon={"id":Ma_so,"ten_sach":Sach.ten_sach,"don_gia":Sach.don_gia}
        Danh_sach_Sach_chon=[]
        if session.get('Gio_hang'):
            Danh_sach_Sach_chon = session['Gio_hang']['Gio_hang']
            if Lay_chi_tiet_Sach(Danh_sach_Sach_chon, Ma_so)!=None:
                Sach_cu = Lay_chi_tiet_Sach(Danh_sach_Sach_chon, Ma_so)
                So_luong_cu = Sach_cu["so_luong"]
                So_luong = So_luong + int(So_luong_cu)
                Danh_sach_Sach_chon.remove(Sach_cu)
        Sach_Chon["so_luong"] = So_luong 
        Sach_Chon["thanh_tien"] = So_luong*int(Sach_Chon['don_gia'])
        Danh_sach_Sach_chon.append(Sach_Chon)
        session['Gio_hang'] = {'Gio_hang':Danh_sach_Sach_chon}
        return jsonify(ketqua=len(Danh_sach_Sach_chon))
    return jsonify(ketqua=0)

@app.route("/gio-hang/thong-tin-gio-hang", methods=['GET','POST'])
def thongtingiohang():
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None    

    dsLoaiSach = Doc_DS_loai_Sach()
    if request.form.get('cap_nhat'):
        Danh_sach_Sach_chon = session['Gio_hang']['Gio_hang']
        Danh_sach_Gio_hang_moi=[]
        for item in Danh_sach_Sach_chon:
            so_luong_moi=int(request.form.get(item['id']))
            if so_luong_moi>0:
                item['so_luong']=so_luong_moi
                item['thanh_tien']=so_luong_moi*item['don_gia']
                Danh_sach_Gio_hang_moi.append(item)
        if len(Danh_sach_Gio_hang_moi)==0:
            session.pop('Gio_hang', None)
        else:
            session['Gio_hang'] = {'Gio_hang':Danh_sach_Gio_hang_moi}
    # tieu_de_link = '<li><a href="/"><i class="fa fa-home"></i></a><i class="icon-angle-right"></i></li>'
    # tieu_de_link+='<li class="active">Thông tin giỏ hàng</li>'
    if request.form.get('xoa'):
        session.pop('Gio_hang', None)
    if session.get('Gio_hang'):
        Thong_tin_gio_hang = tao_html_gio_hang(session['Gio_hang']['Gio_hang'])
    else:
        Thong_tin_gio_hang='<h3 style="text-align:center">GIỎ HÀNG RỖNG</h3>'
    return render_template('gio_hang/thong_tin_gio_hang.html',Thong_tin_gio_hang=Markup(Thong_tin_gio_hang),
            dsLoaiSach=dsLoaiSach,dsDiaChi=dsDiaChi, dia_chi=dia_chi)
