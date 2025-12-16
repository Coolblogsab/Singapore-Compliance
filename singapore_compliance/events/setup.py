import frappe
from frappe import _


def create_charts_of_accounts(company):
	frappe.flags.ignore_permissions = True

	# -----------------------------
	# TAX ACCOUNTS
	# -----------------------------
	tax_asset_accounts = [
		"Input-GST-TX9",
		"Input-GST-ZP",
		"Input-GST-IM9",
	]

	liability_tax_accounts = [
		"Output-GST-SR9",
		"Output-GST-ZR",
		"Output-GST-ES33",
	]

	# -----------------------------
	# TAX ASSET PARENT
	# -----------------------------
	tax_assets_parent = frappe.db.get_value(
		"Account",
		{
			"company": company,
			"account_name": "Tax Assets",
			"is_group": 1,
		},
		"name",
	)

	if not tax_assets_parent:
		frappe.throw(_("Tax Assets account not found. Chart of Accounts missing."))

	for account_name in tax_asset_accounts:
		if frappe.db.exists("Account", {"account_name": account_name, "company": company}):
			continue

		frappe.get_doc(
			{
				"doctype": "Account",
				"account_name": account_name,
				"parent_account": tax_assets_parent,
				"company": company,
				"account_type": "Tax",
				"is_group": 0,
			}
		).insert(ignore_permissions=True)

	# -----------------------------
	# TAX LIABILITY PARENT
	# -----------------------------
	duties_taxes_parent = frappe.db.get_value(
		"Account",
		{
			"company": company,
			"account_name": "Duties and Taxes",
			"is_group": 1,
		},
		"name",
	)

	if not duties_taxes_parent:
		frappe.throw(_("Duties and Taxes account not found."))

	for account_name in liability_tax_accounts:
		if frappe.db.exists("Account", {"account_name": account_name, "company": company}):
			continue

		frappe.get_doc(
			{
				"doctype": "Account",
				"account_name": account_name,
				"parent_account": duties_taxes_parent,
				"company": company,
				"account_type": "Tax",
				"is_group": 0,
			}
		).insert(ignore_permissions=True)

	# -----------------------------
	# SALES TAX TEMPLATES
	# -----------------------------
	sales_tax_templates = [
		{"name": "GST-SR9", "rate": 9},
		{"name": "GST-ZR", "rate": 0},
		{"name": "GST-ES33", "rate": 0},
	]

	for row in sales_tax_templates:
		if frappe.db.exists(
			"Sales Taxes and Charges Template",
			{"title": row["name"], "company": company},
		):
			continue

		account_head = frappe.db.get_value(
			"Account",
			{"account_name": f"Output-{row['name']}", "company": company},
			"name",
		)

		if not account_head:
			continue

		frappe.get_doc(
			{
				"doctype": "Sales Taxes and Charges Template",
				"title": row["name"],
				"company": company,
				"taxes": [
					{
						"charge_type": "On Net Total",
						"account_head": account_head,
						"rate": row["rate"],
						"description": row["name"],
					}
				],
			}
		).insert(ignore_permissions=True)

	# -----------------------------
	# PURCHASE TAX TEMPLATES
	# -----------------------------
	purchase_tax_templates = [
		{"name": "Purchase-GST-TX9", "account": "Input-GST-TX9", "rate": 9},
		{"name": "Purchase-GST-ZP", "account": "Input-GST-ZP", "rate": 0},
		{"name": "Purchase-GST-IM9", "account": "Input-GST-IM9", "rate": 9},
	]

	for row in purchase_tax_templates:
		if frappe.db.exists(
			"Purchase Taxes and Charges Template",
			{"title": row["name"], "company": company},
		):
			continue

		account_head = frappe.db.get_value(
			"Account",
			{"account_name": row["account"], "company": company},
			"name",
		)

		if not account_head:
			continue

		frappe.get_doc(
			{
				"doctype": "Purchase Taxes and Charges Template",
				"title": row["name"],
				"company": company,
				"taxes": [
					{
						"charge_type": "On Net Total",
						"account_head": account_head,
						"rate": row["rate"],
						"description": row["name"],
					}
				],
			}
		).insert(ignore_permissions=True)

	frappe.db.commit()


def get_setup_wizard_stages(params=None):
	# Run only during first setup
	if frappe.db.exists("Account"):
		return []

	return [
		{
			"status": _("Setting up Singapore Compliance"),
			"fail_msg": _("Singapore Compliance setup failed"),
			"tasks": [
				{
					"fn": run_sg_tax_setup,
					"args": params,
				}
			],
		}
	]


def run_sg_tax_setup(params):
	company = params.company_name
	from singapore_compliance.events.setup import create_charts_of_accounts

	create_charts_of_accounts(company)
