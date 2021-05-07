# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from . import controllers
from . import models


def gubi_auto_fill(cr, registry):
    cr.execute(
        """
        UPDATE res_company
        SET date_format = '%d/%m/%Y', decimal_point = ',', thousands_sep = '.'
        """
    )
