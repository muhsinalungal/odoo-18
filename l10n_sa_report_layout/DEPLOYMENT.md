# Deployment Guide

This addon changes Odoo report views, QWeb templates, and report assets. In production, these changes can appear stale until Odoo is restarted and the module is upgraded.

## Module

- Technical name: `l10n_sa_report_layout`
- Location: `/home/odoo/odoo18/custom-addons/l10n_sa_report_layout`

## Before Deployment

1. Pull the latest code into the exact `custom-addons` path used by the running Odoo service.
2. Confirm the server config points to the expected addons path.
3. Confirm you know the correct production database name.

## Production Deployment Steps

1. Pull the latest code.
2. Restart the Odoo service.
3. In Odoo UI, go to `Apps`.
4. Search for `Saudi Report Layout`.
5. Click `Upgrade`.
6. Generate a fresh PDF for:
   - Customer invoice
   - Sales quotation
   - Proforma, if used

## CLI Upgrade Option

If you prefer CLI upgrades:

```bash
cd /home/odoo/odoo18/odoo
../venv/bin/python odoo-bin -c ../config/odoo.conf -d <PROD_DB> -u l10n_sa_report_layout --stop-after-init
```

Then restart Odoo again before testing from the UI.

## Verification Checklist

Check these after every deployment:

- English company details appear on the left side of the header
- Logo appears in the middle
- Arabic company details appear on the right side of the header
- VAT appears in the intended header area
- Invoice QR code renders correctly
- Invoice body sizing matches the expected compact layout
- Quotation and proforma still print correctly

## Important Cache Note

Local development may appear to update faster because local Odoo often runs with `--dev=xml`.

Production usually does not run with `--dev=xml`, so report changes may not appear until:

- Odoo is restarted
- The module is upgraded
- A fresh PDF is generated

If a report still looks unchanged, test with a newly generated PDF file rather than reopening an older downloaded PDF.

## Troubleshooting

If production does not reflect the latest code:

1. Verify the code was pulled into the same addons path used by Odoo.
2. Verify the correct database was upgraded.
3. Verify Odoo was fully restarted.
4. Verify `l10n_sa_report_layout` was upgraded successfully.
5. Check whether another module inherits the same report and overrides this addon's result.
6. Check the Odoo log for view loading or QWeb errors.

## Quick Diagnostics

Useful things to confirm in Odoo shell:

- the loaded Python module path
- the current `ir.ui.view` content for this addon
- other inherited views targeting `l10n_gcc_invoice.arabic_english_invoice`

Example shell entry:

```bash
cd /home/odoo/odoo18/odoo
../venv/bin/python odoo-bin shell -c ../config/odoo.conf -d <PROD_DB> --no-http
```

## Recommended Release Notes

Record this for each deployment:

- Date/time
- Database name
- Commit hash
- Deployed by
- Reports tested
- Result
