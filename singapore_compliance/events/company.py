import frappe

from singapore_compliance.events.setup import create_charts_of_accounts, update_gst_settings


def setup_charts_of_account_for_new_company(doc, method=None):
	"""
	Execute Chart of Accounts creation ONLY when:
	- Site setup is completed
	- A new company is created (not the first one)
	"""

	# 2️⃣ Ensure default company already exists (extra safety)
	default_company = frappe.db.get_single_value("Global Defaults", "default_company")
	if not default_company:
		return

	# ✅ Safe to run for newly created company
	create_charts_of_accounts(doc.name)
	doc.update({"company_name": doc.name})
	params = doc
	update_gst_settings(params)
