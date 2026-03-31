# Dynamic Financial Report for Odoo 18

This module is a local Odoo 18 port of `ks_dynamic_financial_report`.

## Status

- Target version: Odoo 18
- Port status: Completed and smoke-tested locally
- Module version: `18.0.1.1.0`

## Reports covered

- Profit and Loss
- Balance Sheet
- Cash Flow Statement
- Executive Summary
- Trial Balance
- General Ledger
- Partner Ledger
- Aged Receivable
- Aged Payable
- Consolidate Journal
- Tax Report

## Odoo 18 migration notes

The local port includes:

- ORM/query compatibility updates for Odoo 18
- report action compatibility fixes
- account/accounting model field updates
- OWL frontend compatibility fixes
- dropdown/control-panel compatibility fixes
- aging report cleanup for zero-balance partners

## Important settings

Settings are available under `Accounting > Configuration > Settings > DFR`.

- `Enable Net Tax`
  Enables `Total (Sales - Purchase)` in the Tax Report.
- `Enable Ledger Initial Balance`
  Enables initial balance in partner/general ledger.
- `Disable Trial Initial Balance`
  Disables initial balance from income/expense accounts.
- `Disable Balance Sheet Sign`
  Disables negative signs for assets and liabilities in the balance sheet.

## Verified locally

The following flows were checked on the local Odoo 18 database:

- module upgrade
- report loading
- line drilldowns
- journal item actions
- general ledger action
- XLSX export
- PDF print action
- tax report filters
- aged receivable/payable behavior

## Notes

- Zero-balance partners are intentionally hidden in aged reports.
- `Total (Sales - Purchase)` is shown only when `Enable Net Tax` is enabled.
- Remaining upgrade log noise, if any, is from other custom modules outside this addon.
