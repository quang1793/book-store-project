def tao_html_gio_hang(Danh_sach_mat_hang):
	chuoi='<h3 style="text-align:center">THÔNG TIN GIỎ HÀNG</h3>'
	chuoi+='<form id="frmCapNhatGioHang" method="POST"><table class="table table-striped"><thead><tr><th>#</th> <th>Mã sách</th> <th>Tên sách</th> <th>Giá bìa</th> <th style="text-align:center">Số lượng</th> <th style="text-align:right">Thành tiền</th> </tr></thead><tbody>'
	i=1
	tong_cong=0
	for sach in Danh_sach_mat_hang:
		chuoi+='<tr><th scope="row">'+str(i)+'</th>'
		chuoi+='<td>'+sach['id']+'</td>'
		chuoi+='<td>'+sach['ten_sach']+'</td>'
		chuoi+='<td>'+"{:,.0f}".format(sach['don_gia'])+'</td>'
		chuoi+='<td style="text-align:right"><input type="number" class="form-control" value="'+str(sach['so_luong'])+'" name="'+sach['id']+'" style="width:100px; text-align:center"/></td>'
		chuoi+='<td style="text-align:right">'+"{:,.0f}".format(sach['thanh_tien'])+'</td>'
		chuoi+='</tr>'
		tong_cong+=sach['thanh_tien']
		i+=1
	chuoi+='<tr><td colspan=5>Tổng tiền</td><td style="text-align:right">'+"{:,.0f}".format(tong_cong)+'</td></tr>'
	chuoi+='<tr><td colspan=6 style="text-align:center">'
	chuoi+='<input type="submit" value="Cập nhật" name="cap_nhat" class="btn btn-warning">   '
	chuoi+='<input type="submit" value="Xóa" name="xoa" class="btn btn-primary">  '
	chuoi+='<a href="/gio-hang/dat-hang" class="btn btn-info">Tiến hành đặt hàng</a>'
	chuoi+='<p><i>Nhập số lượng 0 nếu muốn xóa mặt hàng</i></p></td></tr>'
	chuoi+='</tbody></table></form>'
	return chuoi