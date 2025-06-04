from odoo import models, fields, api, _


class AccountAnalyticLine(models.Model):
	_inherit = 'account.analytic.line'

	status_name = fields.Char(string='Status', compute='_compute_status_name', store=True)
	task_id = fields.Many2one(
        'project.task', 'Task', index='btree_not_null',
        compute='_compute_task_id', store=True, readonly=False,
        domain="[('allow_timesheets', '=', True), ('project_id', '=?', project_id)]")

	@api.depends('task_id.stage_id')
	def _compute_status_name(self):
		for rec in self:
			if rec.task_id.stage_id:
				rec.status_name = rec.task_id.stage_id.name
			else:
				pass