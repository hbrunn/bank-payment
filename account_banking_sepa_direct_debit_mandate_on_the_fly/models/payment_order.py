# -*- coding: utf-8 -*-
# © 2014,2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class PaymentOrder(models.Model):
    _inherit = 'payment.order'

    is_missing_mandates = fields.Boolean(
        compute='_compute_is_missing_mandates',
    )

    @api.multi
    @api.depends('line_ids.mandate_id', 'payment_order_type')
    def _compute_is_missing_mandates(self):
        for this in self:
            if this.payment_order_type != 'debit':
                continue
            this.is_missing_mandates = any(
                not l.mandate_id for l in this.line_ids
            )

    @api.multi
    def action_create_missing_sdd_mandates(self):
        sdd_type = self.env['ir.config_parameter'].get_param(
            'account.banking.sepa.direct.debit.create.mandates', 'oneoff'
        )
        for line in self.mapped('line_ids'):
            if line.mandate_id:
                continue
            mandate = self.env['account.banking.mandate'].create({
                'type': sdd_type,
                'recurrent_sequence_type':
                'first' if sdd_type == 'recurrent' else False,
                'signature_date': fields.Date.context_today(line),
                'partner_bank_id': line.bank_id.id,
                'partner_id': line.partner_id.id,
            })
            mandate.validate()
            line.mandate_id = mandate
