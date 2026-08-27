# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TierReview(models.Model):
    _inherit = "tier.review"

    constraint_type = fields.Selection(related="definition_id.constraint_type")
    constraint_message = fields.Text(related="definition_id.constraint_message")
