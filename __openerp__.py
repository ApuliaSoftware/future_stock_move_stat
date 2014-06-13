# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2014 giuseppe (<g.dalo@cgsoftware.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Future Stock Move Statistic',
    'version': '1.0',
    'category': 'product',
    'description': """Questo modulo stampa i movimenti non ancora completati e simula la giacenza che l'aricolo assumerà nel futuro' """,
    'author': 'C & G Software sas',
    'website': 'http://www.cgsoftware.it',
    "depends" : ['jasper_reports','stock','product','sale'],
    "update_xml" :[ 'wizard/mastrini_view.xml', 'report.xml', 'security/ir.model.access.csv' ], #'security/ir.model.access.csv',
    "active": False,
    "installable": True
}
