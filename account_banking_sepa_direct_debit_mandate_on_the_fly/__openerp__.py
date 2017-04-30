# -*- coding: utf-8 -*-
# © 2014,2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Create mandates for payment orders",
    "version": "8.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Banking addons",
    "depends": [
        'account_banking_sepa_direct_debit',
        'account_payment',
    ],
    "data": [
        "views/payment_order.xml",
    ],
}
