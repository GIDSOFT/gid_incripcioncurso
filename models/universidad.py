# -*- coding: utf-8 -*-
from osv import osv,fields

class universidad(osv.Model):
	_name = 'gid.cursos.universidad'
	

	_columns = {
		'name':fields.char('Nombre',required=True,size=200),
		'codigo_entidad':fields.char(u'Código',required=True),
		'direccion':fields.char('Dirección',required=True,size=100),
		'telefono':fields.char('Teléfono',required=True,size=100),
		'ciudad' : fields.selection([('tulua', 'Tuluá'), ('cali', 'Cali'), ('buga', 'Buga'), ('sevilla', 'Sevilla')], string="Ciudad"),
		'email':fields.char('E-mail',required=True,size=100),
		'logo' : fields.binary(string='Logo', filters='*.png, *.jpeg'),
		'active':fields.boolean('Active'),

	}
	_defaults={
		'active' : True,
	}

