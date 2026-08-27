# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Tier Validation - Request Actions",
    "summary": "Trigger actions and errors when tier validation is requested",
    "version": "19.0.1.0.2",
    "category": "Tools",
    "website": "https://github.com/OCA/server-ux",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base_tier_validation", "mail"],
    "data": [
        "views/tier_definition_view.xml",
    ],
    "demo": [
        "demo/tier_definition_demo.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "base_tier_validation_request_action/static/src/components/**/*",
        ],
    },
    "maintainers": ["LoisRForgeFlow"],
    "development_status": "Beta",
}
