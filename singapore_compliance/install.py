import frappe

from singapore_compliance.events.setup import create_charts_of_accounts


def setup_ledgers_and_template():
	if not frappe.db.exists("Company"):
		return
	company_list = frappe.db.get_list("Company", pluck="name")
	if company_list:
		for row in company_list:
			create_charts_of_accounts(row)
