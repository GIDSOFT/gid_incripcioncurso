# -*- coding: utf-8 -*-
from osv import osv,fields


class curso(osv.Model): 

	estado=[
		('abierto','Abierto'),
		('proceso','En Proceso'),
		('finalizado','Finalizado'),
		('cancelado','Cancelado'),
	]


	_name='gid.curso.curso'

	_columns={
		'codigo_curso':fields.char(u'Código Curso',required=True,size=10),
		'name':fields.char('Nombre Curso',required=True,size=80),
		'intensidad_horaria':fields.integer('Intensidad Horaria',required=True,size=3),
		'fecha_inicio':fields.date('Fecha Inicio Curso'),
		'fecha_fin':fields.date('Fecha Fin Curso'),
		'lunes':fields.boolean('Lunes'),
		'martes':fields.boolean('Martes'),
		'miercoles':fields.boolean('Miercoles'),
		'jueves':fields.boolean('Jueves'),
		'viernes':fields.boolean('Viernes'),
		'sabado':fields.boolean('Sabado'),
		'domingo':fields.boolean('Domingo'),
		'descripcion':fields.text(u'Descripción'),
		#'docente_id':fields.many2one('gid.cursos.docente','Docente',required=True),
		'state':fields.selection(estado,'Estado Curso'),
	}


