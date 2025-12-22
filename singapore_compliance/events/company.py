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

	tax_assets_parent = frappe.db.get_value(
		"Account",
		{
			"company": doc.name,
			"account_name": "Tax Assets",
			"is_group": 1,
		},
		"name",
	)

	duties_taxes_parent = frappe.db.get_value(
		"Account",
		{
			"company": doc.name,
			"account_name": "Duties and Taxes",
			"is_group": 1,
		},
		"name",
	)

	if tax_assets_parent and duties_taxes_parent:
		# ✅ Safe to run for newly created company
		create_charts_of_accounts(doc.name)
		doc.update({"company_name": doc.name})
		params = doc
		update_gst_settings(params)
	else:
		frappe.enqueue(create_chart_of_accounts_in_rq, doc=doc, queue="short")

def create_chart_of_accounts_in_rq(doc):
	import time
	time.sleep(3)

	tax_assets_parent = frappe.db.get_value(
		"Account",
		{
			"company": doc.name,
			"account_name": "Tax Assets",
			"is_group": 1,
		},
		"name",
	)

	duties_taxes_parent = frappe.db.get_value(
		"Account",
		{
			"company": doc.name,
			"account_name": "Duties and Taxes",
			"is_group": 1,
		},
		"name",
	)

	if tax_assets_parent and duties_taxes_parent:
		create_charts_of_accounts(doc.name)
		doc.update({"company_name": doc.name})
		params = doc
		update_gst_settings(params)
	else:
		frappe.enqueue(create_chart_of_accounts_in_rq, doc=doc, queue="short")
