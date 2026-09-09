# Handover: what must happen before any of this goes live

Written September 2026. Ordered by importance, not by effort.

---

## 1. Confirm the VAT position (do this first, before the websites)

**Why it matters more than anything else here.** VAT registration attaches to the *legal person*,
not to a trading name. Checkatrade declares Deben Johnson as a **sole trader, not VAT registered**.
Companies House has no company for Bathroom Wizards, Kent HandyFix, Kentish Shipwrights or
Kentish Blockmakers, and no officer named Deben Johnson.

If all four trades belong to Deben, then:

- Their combined turnover counts **once** against a single **£90,000** threshold (rolling 12 months).
- Registration is required within 30 days of the end of the month in which the threshold is crossed.
- Four brand names do **not** create four thresholds.

**Do not split the businesses to stay under the threshold.** HMRC calls this disaggregation or
artificial separation. They do not need to prove intent to avoid VAT, only that an artificial split
resulted in VAT being avoided. Shared phone number, shared email, shared bank account, shared tools
and the same two people is close to a textbook single business. A direction can be backdated with
penalties and interest.

**Action:** an accountant adds up the last 12 months across every trade and confirms the position.
This is the single item on this list with real financial consequences.

### If Natasha genuinely runs one of the businesses

Two separate sole traders legitimately have **two separate £90,000 thresholds**. That is lawful,
but only if the separation is real. HMRC weighs financial, economic and organisational links.
Right now the public evidence points the wrong way:

- `07557 733363` appears on Kent HandyFix **and** Kentish Shipwrights
- `kentishblockmakers@gmail.com` serves the shipwright business
- Both domains were validated against the same registrant record on the same day
- The Shipwrights site calls Natasha "Operations & Shipwright Assistant", which is employee
  language, not owner language

To make a two business structure stand up, each business realistically needs its own phone number,
email, bank account, invoices and quotes, records, insurance, and its own jobs. A second mobile
number costs roughly £10 a month and is the cheapest fix to the weakest link.

Two further changes would be needed: **Bathroom Wizards is currently registered to Deben on
Checkatrade**, so it would have to move, and the "Assistant" wording would have to change.

**Nothing on the web side blocks either outcome.** The three sites are built separately and are
independently deployable, so reassigning ownership later is a text edit, not a rebuild.

---

## 2. Get the Checkatrade insurance verified

The Bathroom Wizards profile currently shows **"Public liability insurance is unverified"**.

Every competitor in Medway displays their accreditations prominently. This is free to fix if the
policy already exists: upload the certificate to Checkatrade. It will win more work than any
design decision in this project.

While in there, the profile has **one review**. It is a 10/10, which is excellent, but one review
from September 2024 means Checkatrade shows no overall rating at all. Asking the last handful of
customers for a review is the highest value hour available to them right now.

---

## 3. Confirm every price

**All prices in this prototype are drafts.** They are benchmarked against 2026 South East market
rates, not supplied by Deben. Nothing should be printed or published until he has confirmed or
changed each one.

Sources used for the benchmarks (Checkatrade cost guides and trade rate surveys, 2026):

| Item | Market range | Set here |
|---|---|---|
| Full refit, labour only | £1,500 to £3,000 | from £2,400 |
| Full refit, supply and fit | £5,500 to £8,000 | from £4,900 |
| Day rate, South East | £300 to £460 | £240 |
| Toilet installation | £175 to £350 | from £150 |
| Basin installation | £100 to £275 | from £140 |
| Bath installation | £250 to £400 | from £240 |
| Shower installation | £250 to £750 | from £180 |
| Shower enclosure | £350 to £800 | from £395 |
| Heated towel rail | £200 to £450 | from £165 |
| Wall tiling | £950 to £1,250 per room | from £45 per m2 |
| Strip out | £600 to £1,000 | from £450 |

These sit deliberately at or below the bottom of the market range, on the basis that a
non VAT registered sole trader can undercut VAT registered firms and still earn well. **If Deben
crosses the VAT threshold, every one of these numbers needs revisiting.**

Prices appear in three files and must be kept in step:

- `bathrooms/index.html`
- `print/datasheet-bathrooms.html`
- `print/business-cards.html` (back of the Bathroom Wizards card)

---

## 4. Replace the testimonials on the existing handyman site

The live kenthandyfix.co.uk carries three testimonials ("Sarah T., Rochester", "James W., Maidstone",
"Linda K., Chatham"). If those are not real, verbatim quotes from named customers, they should come
off. They read as generic, and a customer who senses invented reviews stops trusting the prices too.

**I have deliberately left testimonials out of the prototype.** They need real ones. The genuine
Checkatrade review is used on the Bathroom Wizards page instead, quoted accurately.

---

## 5. Decide domains

The prototype currently points every QR code at a GitHub Pages URL. Before printing anything,
pick real domains and re run the generator:

```sh
cd print
python3 make-qr.py https://the-real-domain.co.uk
```

Then re render the two PDFs (command in `CLAUDE.md`) and **scan the codes with a phone** before
sending anything to a printer.

### What they already own

| Domain | Website | Registered | DNS |
|---|---|---|---|
| `kentishshipwrights.co.uk` | live | 28 Oct 2025 | GoDaddy hosting, 92.205.8.200 |
| `kenthandyfix.co.uk` | live | 9 Feb 2026 | GoDaddy hosting, 92.205.8.200 |
| `bathroomwizards.co.uk` | **none** | 27 Feb 2025 | Cloudflare, email routing only |

**Check the GoDaddy account before buying any domain.** `bathroomwizards.co.uk` is already
registered and is very probably theirs: same registrar as the other two, registered a year after
they joined Checkatrade, no A record so no website, but Cloudflare email routing and an SPF record
are configured. That is the pattern of a domain bought and parked with email forwarding set up.
If it is theirs, the Bathroom Wizards site has a domain waiting for it and nothing needs buying.

### Who owns the domains

All three have the registrant name **withheld** in WHOIS, so ownership cannot be confirmed from
public record. The evidence points to a single registrant behind all three:

- all three are registered through GoDaddy
- the two live domains were validated against the same third party data source on the **same date**
  (26 Jun 2025), including one registered eight months later, which means an existing validated
  account was reused
- both live sites resolve to the same GoDaddy hosting IP

The only confirmed ownership anywhere is the **Checkatrade profile for Bathroom Wizards**, which
declares "Mr Deben Johnson, Sole Trader, VAT Registered: No".

Nominet only allows the registrant name opt out for individuals **not** using the domain for
business. All three are plainly business sites, so the opt out may be misapplied, and it suggests
they were registered as individuals rather than under a business name.

**Action:** log into the GoDaddy account and read the registrant details on all three. Do this at
the same time as the accountant conversation in item 1, because the VAT position depends on who
actually owns what.

---

## 6. Activate the contact forms

All three forms post to [FormSubmit](https://formsubmit.co) using `kentishblockmakers@gmail.com`.
FormSubmit requires a one time activation: submit each form once and click the confirmation link
in the email. **Until that is done the forms silently do nothing.**

If the businesses are to be kept separate, each form should go to that business's own email
address rather than all three to the blockmakers address.

---

## 7. Before launch, delete the prototype scaffolding

- Delete `index.html` (the prototype hub). It is not part of any real site.
- Remove the yellow `.proto-note` banner from the top of all three site pages.
- Remove "Prototype site, not yet live" from the three footers.
- Remove the draft warning box from `print/datasheet-bathrooms.html`.

---

## Recommended structure

Keep **Kentish Shipwrights separate** from the domestic work regardless of what the accountant
decides. Different customers (boat owners, not homeowners), different geography (Estuary moorings,
not Medway housing), different search terms. It is also a premium heritage craft brand, and putting
"we fix dripping taps" beside "trusted on the Thames barges" devalues the barge credential. Cite
the barge work as a trust signal on the domestic site instead, without merging the brands.

For the domestic side, the marketing answer and the tax answer differ, so the accountant decides:

- **One sole trader:** merge handyman and bathrooms into one site. Same customer, same van, same
  postcodes. Handyman jobs are cheap and frequent and act as the front door to £5,000 bathroom
  refits; two brands break that chain because the customer who trusted one has no idea the other is
  the same person.
- **Two genuine businesses:** keep them fully separate, with the substance to match (see item 1).

The prototype is built so either path works without a rebuild.
