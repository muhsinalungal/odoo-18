# Development Guide

This file documents the most common local development commands for `l10n_sa_report_layout`.

## Module

- Technical name: `l10n_sa_report_layout`
- Addon path: `/home/odoo/odoo18/custom-addons/l10n_sa_report_layout`
- Odoo root: `/home/odoo/odoo18/odoo`
- Config: `/home/odoo/odoo18/config/odoo.conf`
- Local DB: `golden_emerald_est_dev`

## Working Directory

Use this directory before running most commands:

```bash
cd /home/odoo/odoo18/odoo
```

## Start Odoo

Run Odoo in local development mode:

```bash
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev --dev=xml
```

## Upgrade This Module

Upgrade only `l10n_sa_report_layout`:

```bash
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev -u l10n_sa_report_layout --stop-after-init
```

## Upgrade Multiple Modules

Example:

```bash
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev -u l10n_sa_report_layout,sale,account --stop-after-init
```

## Open Odoo Shell

Useful for checking views, templates, and report rendering:

```bash
../venv/bin/python odoo-bin shell -c ../config/odoo.conf -d golden_emerald_est_dev --no-http
```

## Check Logs

Tail the Odoo log:

```bash
tail -f /home/odoo/odoo18/odoo.log
```

Search recent report errors:

```bash
rg -n "ParseError|QWebException|AssertionError|report" /home/odoo/odoo18/odoo.log
```

## Common Development Workflow

1. Edit the custom module files.
2. Upgrade the module:

```bash
cd /home/odoo/odoo18/odoo
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev -u l10n_sa_report_layout --stop-after-init
```

3. Start Odoo:

```bash
cd /home/odoo/odoo18/odoo
../venv/bin/python odoo-bin -c ../config/odoo.conf -d golden_emerald_est_dev --dev=xml
```

4. Generate a fresh PDF and verify the output.

## Useful Report Debug Commands

Render invoice HTML from shell:

```python
report = env.ref('account.account_invoices')
html = report._render_qweb_html('account.report_invoice_with_payments', [2])[0].decode('utf-8')
print(html[:3000])
```

Render invoice PDF from shell:

```python
report = env.ref('account.account_invoices')
pdf_bytes = report._render_qweb_pdf('account.report_invoice_with_payments', [2])[0]
with open('/home/odoo/odoo18/invoice_debug.pdf', 'wb') as f:
    f.write(pdf_bytes)
```

Check a view definition in DB:

```python
view = env.ref('l10n_sa_report_layout.sa_invoice_body_compact')
print(view.write_date)
print(view.arch_db[:3000])
```

Check inherited invoice views:

```python
base = env.ref('l10n_gcc_invoice.arabic_english_invoice')
views = env['ir.ui.view'].search([('inherit_id', '=', base.id)], order='priority,id')
for v in views:
    print(v.id, v.key or v.name, v.priority, v.active, v.write_date)
```

## Notes

- Local development uses `--dev=xml`, so XML/QWeb changes appear faster than production.
- For report changes, always test with a freshly generated PDF.
- If output looks unchanged, first upgrade the module, then restart Odoo, then test again.
