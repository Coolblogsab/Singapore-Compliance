# Copyright (c) 2025, Kingstech and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
	mytodo = frappe.get_all("To DO") 
	frappe.db.get_value("To Do", "123", debug=True)

class SGSTDetail(Document):
	pass
