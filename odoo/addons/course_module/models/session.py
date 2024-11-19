# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date

class Session(models.Model):
    _name = 'session.management'
    _description = 'Session'

    name = fields.Char(string='Name', required=True)
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    is_done = fields.Boolean(string='Is Done')
    is_expired = fields.Boolean(string='Is Expired', compute='_compute_is_expired', store=True)
    course_id = fields.Many2one('course.management', string='Course')

    @api.constrains('from_date', 'to_date')
    def _check_dates(self):
        for record in self:
            if record.from_date and record.to_date and record.from_date > record.to_date:
                raise exceptions.ValidationError("From Date must be earlier than To Date.")

    @api.constrains('from_date', 'to_date', 'course_id')
    def _check_course_dates(self):
        for record in self:
            if record.course_id:
                if record.from_date and record.course_id.from_date and record.from_date < record.course_id.from_date:
                    raise exceptions.ValidationError("Session From Date cannot be before Course From Date.")
                if record.to_date and record.course_id.to_date and record.to_date > record.course_id.to_date:
                    raise exceptions.ValidationError("Session To Date cannot be after Course To Date.")

    @api.depends('to_date')
    def _compute_is_expired(self):
        for record in self:
            if record.to_date and record.to_date < date.today():
                record.is_expired = True
            else:
                record.is_expired = False