# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    """Recompute the payment review state of existing posted vendor reversal entries."""
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})
    moves = (
        env["account.move"]
        .search(
            [
                ("move_type", "in", ("in_invoice", "in_refund")),
                ("state", "=", "posted"),
                ("reversed_entry_id", "!=", False),
            ]
        )
        .with_context(skip_validation_check=True, skip_payment_review_manual_check=True)
    )
    moves._compute_invoice_payment_review_state()
    moves._compute_payment_locked()
