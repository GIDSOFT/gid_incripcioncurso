#-*- encoding utf-8 -*-
from osv import osv,fields

class docente  (osv.Model):
	_name ='gid.cursos.docente'

	_columns= {
		'name':fields.char('Nombre',required=True,size=200),
		'identificacion': fields.char('iden',required=True,size=300),
		'correo': fields.char('email',required=True,size=300),
		'telefono': fields.char('tel',required=True,size=200),
		'active':fields.boolean('active'),
		'universidad_id':fields.many2one('gid.cursos.universidad',required=True, size=200),
	}