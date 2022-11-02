# Copyright 2021 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TierDefinitionSelectionWizard(models.TransientModel):
    _name = "tier.validation.selection.wizard"
    _description = "Tier Definition Selection Wizard"

    res_model = fields.Char()
    res_id = fields.Integer()

    definition_ids = fields.Many2many(
        comodel_name="tier.definition",
        string="Tier Definitions",
        help="Select the definitions to apply for the current's record validation."
    )

    @api.multi
    def request_validation(self):
        self.ensure_one()
        rec = self.env[self.res_model].browse(self.res_id)
        if not self.definition_ids:
            raise ValidationError(_(
                "You need to select at least one Tier Definition."
            ))
        rec.request_custom_validation(self.definition_ids)
