# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class CommentWizard(models.TransientModel):
    _inherit = "comment.wizard"

    # Override to make comment optional: the reviewer can validate without leaving a comment
    comment = fields.Char(required=False)
