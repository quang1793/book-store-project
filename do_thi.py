from pprint import pprint
from flask import Flask, redirect, render_template, request, url_for, Markup, jsonify, session, jsonify
from ung_dung import app
from ung_dung.Xu_ly.Xu_ly_Sach import *
from ung_dung.Xu_ly.Xu_ly_gio_hang import *
from ung_dung.Xu_ly.Xu_ly_tin_tuc import *
from ung_dung.Xu_ly.Xu_ly_Model import *
from ung_dung.Xu_ly.Xu_ly_Ban_do import *
from sqlalchemy import func


@app.route('/do_thi')
def line():
    dsDiaChi = Doc_Dia_Chi_Nha_Sach()
    dia_chi=None

    dsLoaiSach = Doc_DS_loai_Sach()
    res = db.engine.execute("select sum(sach_mua), strftime('%Y-%m-%d', ngay_mua)  from bs_khach_hang group by strftime('%Y-%m-%d', ngay_mua) ")
    res = list(res)
    labels  = []
    for item in res:
        labels.append(item[1])

    values = []
    for item in res:
        values.append(item[0])

    line_labels=labels
    line_values=values
    return render_template('do_thi/do_thi.html',dsDiaChi=dsDiaChi, dia_chi=dia_chi,
        title='VNĐ',max=max(values)+10000, labels=line_labels, values=line_values,dsLoaiSach=dsLoaiSach)
