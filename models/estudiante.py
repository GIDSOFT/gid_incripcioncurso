# -*- coding: utf-8 -*-
from osv import osv,fields

class estudiante(osv.Model):
	_name = 'gid.cursos.estudiante'
	

	_columns = {
		
		'name':fields.char('Nombre',required=True,size=200),
		'identificacion' : fields.char(u'Identificación',required=True, size=11 ),
		'direccion':fields.char(u'Dirección',required=True,size=100),
		'telefono':fields.char(u'Teléfono',size=100),
		'email':fields.char('E-mail',required=True,size=100),
		'active':fields.boolean('Active'),

	}
	_defaults={
		'active' : True,
	}