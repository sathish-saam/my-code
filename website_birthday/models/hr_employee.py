from odoo import fields, models, api, _

class HrEmployee(models.Model):
  _inherit = 'hr.employee'

  employee_dob = fields.Date("Date of Birth")

