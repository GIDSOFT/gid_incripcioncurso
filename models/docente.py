# -*- coding: utf-8 -*-
from osv import osv,fields

class docente  (osv.Model):
	_name ='gid.cursos.docente'

	_columns= {
		'name':fields.char('Nombre',required=True,size=200),
		'identificacion': fields.char(u'Identificación',required=True,size=300),
		'correo': fields.char('Email',required=True,size=300),
		'telefono': fields.char(u'Teléfono',required=True,size=200),
		'active':fields.boolean('Activo'),
		'universidad_id':fields.many2one('gid.cursos.universidad','Universidad', required=True),
	}

	_defaults= {
		'active' : True,

	}