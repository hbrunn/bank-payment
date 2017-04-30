.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

==================================
Create mandates for payment orders
==================================

When switching to SEPA payments, the mandates to be created can be a
serious show stopper. Usually, they are available in one form or the other,
but not in OpenERP. This plugin adds a button on payment orders to create
mandates for the current payment order where necessary.

Configuration
=============

By default, this module creates one-off mandates. If you rather want to create
recurring mandates (i.e. because your available mandates are recurring ones),
set the config parameter
'account.banking.sepa.direct.debit.create.mandates' to 'recurrent'.

Attention
---------

Only use this if you actually have the mandates!

Usage
=====

On your payment order, the button ``Create missing mandates`` will appear if
there are lines without a mandate. Clicking it will create the missing mandates.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
    :alt: Try me on Runbot
    :target: https://runbot.odoo-community.org/runbot/173/8.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account_banking_sepa_direct_debit_mandate_on_the_fly/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Holger Brunn <hbrunn@therp.nl>

Do not contact contributors directly about help with questions or problems concerning this addon, but use the `community mailing list <mailto:community@mail.odoo.com>`_ or the `appropriate specialized mailinglist <https://odoo-community.org/groups>`_ for help, and the bug tracker linked in `Bug Tracker`_ above for technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
