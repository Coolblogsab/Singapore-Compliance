# Singapore Compliance

This app is for companies based in Singapore and enables the compliance with Singapore tax compliance. The app automatically creates accounts in the Chart-of-Accounts, Sales Taxes and Charges Template, Purchase Taxes and Charges Template and configures the accounts in the ‘Singapore GST Settings’ page. The app also comes with reports like ‘GST Detail Report’ and ‘GST F5 Summary Report’.

## Key Features

### 1. Ledgers in the Chart-of-Accounts(CoA)
This app automatically creates accounts for GST.

<img width="1440" height="812" alt="SL-GST-Accounts" src="https://github.com/user-attachments/assets/06b16130-1153-4dcc-ba31-43ce2f5ceb7c" />

### 2. Singapore GST Settings
The gst settings are configured automatically in the GST settings page.

<img width="1440" height="814" alt="SL-GST-Settings" src="https://github.com/user-attachments/assets/dfab50cf-3d4a-4485-83d0-8335c593bba1" />

### 3. Sales Taxes and Charges Template
App creates 'Sales Taxes and Charges Template' like 'GST-SR9', 'GST-ZR', and 'GST-ES33' as required by Singapore GST. 

<img width="1439" height="813" alt="SL-Sales-Taxes" src="https://github.com/user-attachments/assets/5727b42e-3b46-4ca1-8181-e693924d4f89" />

### 4. Purchase Taxes and Charges Template
App creates 'Purchase Taxes and Charges Template' like 'GST-IM9', 'GST-ZP', and 'GST-TX9' as required by Singapore GST. 

<img width="1440" height="812" alt="SL-Purchase-Taxes" src="https://github.com/user-attachments/assets/f28f45b3-1cad-409f-bb65-64dc6c8ce391" />

### 5. GST Reports
App ships with reports like 'GST F5 Summary Report' and 'GST Detail Report'.

<img width="1440" height="813" alt="SL-GST-Detail-Report" src="https://github.com/user-attachments/assets/ecc7a310-72fa-482a-9f58-23c7de91efe4" />

<br><br>

<img width="1440" height="814" alt="SL-GST-F5-Report" src="https://github.com/user-attachments/assets/49df798e-5f08-4d3f-a12c-14759534969c" />




## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app singapore_compliance
```

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/singapore_compliance
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


## License

This project is licensed under GNU General Public License (v3)
