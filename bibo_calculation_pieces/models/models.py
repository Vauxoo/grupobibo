# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, date, time, timedelta

class AddCampHandWorkProd(models.Model):
	_inherit = 'account.invoice'

	no_piezas = fields.Float(string='Numero de Piezas', readonly=True,
	 compute='_compute_piezas', )

	@api.one
	@api.depends('invoice_line_ids.quantity')
	def _compute_piezas(self):
		self.no_piezas = sum(line.quantity for line in self.invoice_line_ids)

class AddCampHandWorkProd(models.Model):
	_inherit = 'sale.order'

	no_piezas = fields.Float(string='Numero de Piezas',
	 readonly=True, compute='_piezas')


	@api.one
	@api.depends('order_line.product_uom_qty')
	def _piezas(self):

		self.no_piezas = sum(line.product_uom_qty for line in self.order_line)