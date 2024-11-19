# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date

class Course(models.Model):
    _name = 'course.management'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_process', 'In Process'),
        ('done', 'Done')
    ], string='State', compute='_compute_state', store=True)
    session_ids = fields.One2many('session.management', 'course_id', string='Sessions')

    @api.constrains('from_date', 'to_date')
    def _check_dates(self):
        for record in self:
            if record.from_date and record.to_date and record.from_date > record.to_date:
                raise exceptions.ValidationError("From Date must be earlier than To Date.")

    @api.depends('session_ids.is_done')
    def _compute_state(self):
        for record in self:
            if not record.session_ids:
                record.state = 'draft'
            elif all(session.is_done for session in record.session_ids):
                record.state = 'done'
            else:
                record.state = 'in_process'

    def action_set_in_process(self):
        self.state = 'in_process'

    def action_set_done(self):
        self.state = 'done'

    def action_set_draft(self):
        self.state = 'draft'