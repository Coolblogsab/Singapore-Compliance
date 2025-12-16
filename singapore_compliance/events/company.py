import frappe

from singapore_compliance.events.setup import create_charts_of_accounts


def setup_charts_of_account_for_new_company(doc, method=None):
	company = doc.name
	create_charts_of_accounts(company)
