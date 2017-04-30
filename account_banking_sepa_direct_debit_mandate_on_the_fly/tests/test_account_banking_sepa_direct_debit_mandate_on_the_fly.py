# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests.common import TransactionCase


class TestAccountBankingSepaDirectDebitMandateOnTheFly(TransactionCase):
    def test_account_banking_sepa_direct_debit_mandate_on_the_fly(self):
        partner = self.env['res.partner'].search([
            ('bank_ids', '!=', False),
            ('bank_ids.mandate_ids', '=', False),
        ], limit=1)
        order = self.env['payment.order'].create({
            'payment_order_type': 'debit',
            'mode': self.env.ref(
                'account_banking_sepa_direct_debit.sepa_direct_debit_mode'
            ).id,
            'line_ids': [
                (
                    0, 0,
                    {
                        'communication': 'test',
                        'amount_currency': 42,
                        'partner_id': partner.id,
                        'bank_id': partner.bank_ids.filtered(
                            lambda x: not x.mandate_ids
                        )[:1].id,
                    },
                ),
            ],
        })
        self.assertTrue(order.is_missing_mandates)
        order.action_create_missing_sdd_mandates()
        self.assertFalse(order.is_missing_mandates)
