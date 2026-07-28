# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})
    definition = env.ref(
        "s6r_invoice_payment_tier_validation.account_tier_definition_validation",
        raise_if_not_found=False,
    )
    if not definition:
        return
    if env["tier.review"].search_count([("definition_id", "=", definition.id)]):
        definition.active = False
        env["ir.model.data"].search(
            [
                ("module", "=", "s6r_invoice_payment_tier_validation"),
                ("name", "=", "account_tier_definition_validation"),
            ]
        ).noupdate = True
    else:
        definition.unlink()
