from flask import Flask, redirect, render_template, request, url_for, Markup, jsonify, session, jsonify
from ung_dung import app
from ung_dung.Xu_ly.Xu_ly_Sach import *
from ung_dung.Xu_ly.Xu_ly_gio_hang import *
from ung_dung.Xu_ly.Xu_ly_tin_tuc import *
from ung_dung.Xu_ly.Xu_ly_Ban_do import *

@app.route('/tin_tuc', methods=['GET','POST'])
def TinTucChung():
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    dsTinTuc = Doc_ds_tin_tuc()
    dsLoaiSach = Doc_DS_loai_Sach()
    return render_template('tin_tuc/tin_tuc_chung.html',dsTinTuc=dsTinTuc,dsLoaiSach=dsLoaiSach,
        dsDiaChi=dsDiaChi, dia_chi=dia_chi)

@app.route('/tin_tuc/<string:id>', methods=['GET','POST'])
def chitiettintuc(id):
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    tintuc = bs_tin_tuc.query.filter(bs_tin_tuc.id == id).first()
    dsLoaiSach = Doc_DS_loai_Sach()
    return render_template('tin_tuc/chi_tiet_tin_tuc.html',tintuc=tintuc,dsLoaiSach=dsLoaiSach,
            dsDiaChi=dsDiaChi, dia_chi=dia_chi)
   

