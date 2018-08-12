from wtforms import form, fields, validators
from flask_ckeditor import CKEditorField
from datetime import datetime

class bs_khach_hangForm(form.Form):
	ten_khach_hang = fields.StringField(validators=[validators.required()])
	phai = fields.BooleanField()
	ngay_sinh = fields.DateField()
	dia_chi = fields.StringField(validators=[validators.required()])
	dien_thoai = fields.StringField(validators=[validators.required()])
	email = fields.StringField(validators=[validators.required()])
	ngay_mua = datetime.now()
	ghi_chu = CKEditorField(validators=[validators.required()])