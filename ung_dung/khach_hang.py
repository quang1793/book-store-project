from ung_dung import app
from flask import redirect, render_template, request, session, abort, url_for, Markup, jsonify
from ung_dung.Xu_ly.Xu_ly_Sach import *
from ung_dung import db,mail
# from ung_dung.config import *
from ung_dung.Xu_ly.Xu_ly_gio_hang import *
from ung_dung.Xu_ly.Xu_ly_Form import *
from flask_admin import helpers
from datetime import datetime
from flask_mail import Mail, Message
from ung_dung.Xu_ly.Xu_ly_Ban_do import *
@app.route("/gio-hang/dat-hang", methods=['GET','POST'])
def khachHangDatHang():
	dsDiaChi = Doc_Dia_Chi_Nha_Sach()
	dia_chi=None
	form = bs_khach_hangForm(request.form)
	htmlThongTinGioHang=""
	if helpers.validate_form_on_submit(form):
		khach_hang = bs_khach_hang()
		form.populate_obj(khach_hang)
		gio_hang=session['Gio_hang']['Gio_hang']
		khach_hang.ngay_mua=datetime.now()
		khach_hang.sach_mua=str(gio_hang)
		db.session.add(khach_hang)
		#db.session.flush()
		#print(khach_hang.ma_khach_hang)
		db.session.commit()
		session.pop('Gio_hang', None)  
		htmlThongTinGioHang='<h3 style="text-align:center">THÔNG TIN ĐƠN ĐẶT HÀNG</h3>'
		htmlThongTinGioHang+='<table border="0" width="100%" cellspacing="10" class="table">'
		htmlThongTinGioHang+='<tr><th>#</th><th>Mã sách</th><th>Tên sách</th><th style="text-align:right">Số lượng</th><th style="text-align:right">Đơn giá</th><th style="text-align:right">Thành tiền</th></tr>'
		i=1
		tongtien=0
		for item in gio_hang:
			htmlThongTinGioHang+='<tr><td>'+str(i)+'</td><td>'+item['id']+'</td><td>'+item['ten_sach']+'</td><td style="text-align:right">'+str(item['so_luong'])+'</td><td style="text-align:right">'+"{:,.0f}".format(item['don_gia'])+'</td><td style="text-align:right">'+"{:,.0f}".format(item['thanh_tien'])+'</td></tr>'
			tongtien+=item['thanh_tien']
			i=i+1
		htmlThongTinGioHang+='<tr><td colspan="5" style="text-align:right">Tổng tiền</td><td style="text-align:right">'+"{:,.0f}".format(tongtien)+'</td></tr>'
		htmlThongTinGioHang+='</table>'

		ngayHienHanh = datetime.now()
		ngay=ngayHienHanh.day
		thang=ngayHienHanh.month
		nam=ngayHienHanh.year
		chuoiMail=	'<div style="padding-left:20px;padding-right:20px;border-bottom: 1px solid #cacbcc;"'
		chuoiMail+=	'<p style="border-bottom: 1px solid #cacbcc;"><b>THÔNG TIN ĐƠN HÀNG #'+str(khach_hang.ma_khach_hang)+'</b> (Ngày '+str(ngay)+' tháng '+str(thang)+' năm '+str(nam)+')</p>'
		chuoiMail+=	'<table border="0" width="100%" cellspacing="10">'
		chuoiMail+=		'<tr>'
		chuoiMail+=			'<th><b>Thông tin thanh toán<b></th>'
		chuoiMail+=			'<th><b>Địa chỉ giao hàng<b></th>'		
		chuoiMail+=		'</tr>'
		chuoiMail+=		'<tr>'	
		chuoiMail+=			'<td>'+ khach_hang.ten_khach_hang +'</td>'
		chuoiMail+=			'<td>'+ khach_hang.dia_chi +'</td>'
		chuoiMail+=		'</tr>'
		chuoiMail+=		'<tr>'	
		chuoiMail+=			'<td>'+ khach_hang.email +'</td>'
		chuoiMail+=			'<td>'+ khach_hang.ghi_chu +'</td>'
		chuoiMail+=		'</tr>'
		chuoiMail+=		'<tr>'	
		chuoiMail+=			'<td>'+ khach_hang.dien_thoai +'</td>'
		chuoiMail+=			'<td></td>'
		chuoiMail+=		'</tr>'		
		chuoiMail+=	'</table>'
		chuoiMail+=	'</div>'
		chuoiMail+=	htmlThongTinGioHang
		msg=Message('Xác nhận đơn hàng #'+str(khach_hang.ma_khach_hang), sender='quang1234.py@gmail.com', recipients=[khach_hang.email])
		msg.body=Markup(chuoiMail)
		msg.html = msg.body
		mail.send(msg)

		htmlThongTinGioHang+='<p>Thông tin đơn hàng đã được gửi tới email của quý khách.</p>'
	
	return render_template('gio_hang/them_khach_hang.html',form=form,htmlThongTinGioHang=Markup(htmlThongTinGioHang),
			dsDiaChi=dsDiaChi, dia_chi=dia_chi)
