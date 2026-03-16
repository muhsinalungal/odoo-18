# AGENTS.md

## Project
Odoo 18 Community development environment for Saudi accounting and reporting.

## Environment
- OS: WSL Ubuntu 24.04
- Main local DB: golden_emerald_est_dev
- wkhtmltopdf: /usr/bin/wkhtmltopdf
- Python venv: /home/odoo/odoo18/venv

## Repository structure
- Core Odoo source: /home/odoo/odoo18/odoo
- Custom addons: /home/odoo/odoo18/custom-addons
- Config: /home/odoo/odoo18/config/odoo.conf

## Development rules
- Never modify Odoo core files directly unless explicitly requested.
- All customizations must be done in custom modules under custom-addons.
- Use inherited views and inherited QWeb templates.
- Use XPath for report changes.
- Keep changes compatible with Odoo 18 Community.

## Reports
The invoice, quotation, and proforma should follow a shared layout approach where possible.

Saudi report requirements:
- Arabic + English labels
- ZATCA-compatible invoice layout
- A4 portrait
- compact layout to avoid overflow
- keep wkhtmltopdf compatibility in mind

## Run locally
Start Odoo with:

cd /home/odoo/odoo18/odoo
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev --dev=xml

## Safety
- Do not edit report templates directly in the database UI unless explicitly requested.
- Prefer reusable module-based overrides.
- Avoid destructive changes unless asked.