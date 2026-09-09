# Kent Trades, website prototypes

Prototype websites, business cards and a price datasheet for **Deben Johnson and Natasha**,
who trade in Medway, Kent under several names. Built as a first pass to show them what is
possible, hosted on GitHub Pages. **Nothing here is live and nothing overwrites their existing sites.**

## The businesses

| Brand | Trade | Existing site | Notes |
|---|---|---|---|
| Bathroom Wizards | Bathroom fitting, wet rooms, disabled access | none | Checkatrade since Feb 2024, 1 review at 10/10, Gillingham |
| Kent HandyFix | Handyman, small property repairs | kenthandyfix.co.uk (WordPress/Divi) | Based in Hoo |
| Kentish Shipwrights | Marine carpentry, restoration | kentishshipwrights.co.uk (WordPress/Divi) | Trusted on Thames barges |
| Kentish Blockmakers | Custom block making | none, used as the email identity | Sold as a service under Shipwrights |

All four share the phone number `07557 733363` and the email `kentishblockmakers@gmail.com`.

## Critical context: legal structure

- Checkatrade declares **Deben Johnson, Sole Trader, not VAT registered**.
- Companies House has **no company** for any of the four brands, and no officer named Deben Johnson.
- Natasha's position is **unconfirmed**. Sole traders are not publicly listed, so this cannot be
  verified from public record. The Shipwrights site currently calls her
  "Operations & Shipwright Assistant", which reads as employee rather than owner.

**The £90,000 VAT threshold applies per legal person, not per trading name.** If all the trades
belong to Deben, their combined turnover counts once. Splitting them to stay under the threshold
is disaggregation and HMRC treats it harshly. This needs an accountant, not a web developer.
See `docs/handover.md`.

The three sites are built **separately and independently deployable** so that whichever ownership
structure the accountant confirms, the sites can follow without a rebuild.

## Tech stack

Static HTML and CSS. No framework, no build step, no JavaScript beyond a mobile nav toggle.
That is deliberate: the people maintaining this are tradespeople, not developers, and a static
site costs nothing to host and cannot break.

- `assets/css/base.css` holds the entire design system, shared by all three sites
- Brand theming via `data-brand` on `<html>`, which swaps CSS custom properties
- Google Fonts (Inter, plus Newsreader for Shipwrights); everything else is local
- Contact forms post to [FormSubmit](https://formsubmit.co) and **need activating** by confirming
  the first email it sends

## Layout

```
index.html              prototype hub, DELETE before any real launch
handyfix/               Kent HandyFix
bathrooms/              Bathroom Wizards (carries the full price list)
shipwrights/            Kentish Shipwrights
assets/css/base.css     shared design system
assets/img/             their real photos and logos, optimised
print/business-cards.html        3 designs, front and back, 85x55mm plus 3mm bleed
print/datasheet-bathrooms.html   A4 one page price guide
print/make-qr.py        regenerates every QR code from one base URL
print/qr/               generated QR SVGs
docs/handover.md        what must happen before this goes live
```

## Running locally

No build. Open `index.html`, or serve the folder:

```sh
python3 -m http.server 8000
# then http://localhost:8000
```

## Common tasks

**Repoint every QR code at a real domain.** Do this before printing anything:

```sh
cd print
python3 make-qr.py https://bathroomwizards.co.uk
```

**GitHub Pages paths are case sensitive.** The repo is `Bathroom-Wizards`, so the live URL is
`https://009695.github.io/Bathroom-Wizards/`. The lowercase spelling returns a 404. Always verify a
regenerated QR code resolves before sending anything to a printer.

Regenerate the print PDFs:

```sh
cd print
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --no-pdf-header-footer --print-to-pdf=business-cards.pdf business-cards.html
"$CHROME" --headless=new --no-pdf-header-footer --print-to-pdf=datasheet-bathrooms.pdf datasheet-bathrooms.html
```

**Change a price.** Prices appear in two places and must be kept in step:
`bathrooms/index.html` and `print/datasheet-bathrooms.html`.

**Never put prices on the business cards.** Cards last years, material costs do not, and a printed
price is something a customer can hold you to. The QR code exists so pricing lives somewhere that
can be updated. The cards say "scan for our current prices" instead, which also gives the QR code
a real job.

## Gotchas

- The datasheet fits one A4 page with very little to spare. Adding a row will push the footer onto
  a second page, so re-render and check the page count after any edit.
- Screen only styling in the datasheet lives in `@media screen` on purpose. Moving it out makes
  `min-height: 297mm` fight the `@page` box and spill to two pages.
- Grid templates use `minmax(min(300px, 100%), 1fr)`. The `min()` is load bearing: without it the
  contact card's inner grid overflows on phones.
- The Kent HandyFix logo has had its background flood filled to transparent from the edges inward,
  so the white "KENT" lettering inside the mark survives. Do not blanket replace white with alpha.
- House style forbids em dashes and en dashes anywhere, including HTML entities. Use commas, full
  stops, colons or the word "to" for ranges.
