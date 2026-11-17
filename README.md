# Lifecycle in a Box

A complete lifecycle marketing program, built end to end for a fictional DTC brand, with synthetic data. Nothing here is client work. No real customer, order, or revenue data is used anywhere in this repository.

**Brand:** Solmere Botanics (invented), a DTC skincare brand selling one hero subscription product.
**Stack it is designed for:** Shopify, Klaviyo (email and SMS), Recharge (subscription), a quiz front end.
**Built by:** Amy Kniss, Director of Lifecycle and Retention Marketing, as a public work sample.

## Why this exists

Director-level lifecycle work usually sits behind an NDA, so it cannot be shown. This repository shows the work itself instead: how I diagnose, architect, write, segment, and measure a retention program, on a brand I invented so every asset can be public.

## What is inside

| Folder | Contents |
|---|---|
| `brand/` | The fictional brand brief: product, pricing, customer, margin assumptions |
| `flows/` | The flow architecture map: every flow, its trigger, its job, its exit rules |
| `emails/` | Six emails written in full: welcome, browse abandon, cart abandon, post-purchase, winback, subscription reactivation |
| `quiz/` | The skin quiz: questions, answer-to-segment map, and how quiz answers change the flows |
| `data/` | A seeded Python generator that produces the synthetic customer and order dataset, plus the data dictionary |
| `analytics/` | The KPI dashboard spec and the computed results from the synthetic data: cohort repeat rate, subscription share, LTV |
| `calculator/` | A standalone Subscription Economics Calculator (open the HTML file in a browser): model interval, AOV, margin, and churn before changing a subscription program |
| `strategy/` | The measurement plan and the 90-day build sequence I would run in-house |

## The program in one paragraph

Acquisition promises a result in 90 days. Lifecycle's job is to make that promise land: a quiz captures the customer's skin concern and routine, the welcome flow teaches the routine instead of discounting, abandon flows answer the specific objection the data shows, post-purchase protects the first result, and the subscription program is built around the interval the product actually runs out at, not the interval that looks good in a forecast. Every flow has one job, an exit rule, and a metric it is accountable to.

## Synthetic data, honestly labelled

`data/generate_data.py` uses a fixed random seed, so anyone can regenerate the exact dataset and reproduce every number in `analytics/`. The numbers describe the synthetic dataset only. They are not results, and they are not presented as results anywhere.

## License and reuse

The audit rubric, flow architecture, and calculator are free to reuse with attribution. The email copy is a writing sample, please do not send it as your own brand.
