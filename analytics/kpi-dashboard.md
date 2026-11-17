# KPI Dashboard: Spec and Computed Read (synthetic data)

Run `python3 data/generate_data.py`, then read `orders.csv` and `customers.csv`. Every number below was computed from the generated dataset (seed 42) on 2026-11-16. They describe the synthetic data only.

## The dataset at a glance
- Customers: 3,595. Orders: 6,607. Total synthetic revenue: $395,420.
- Average revenue per customer: $109.99.
- Repeat buyer rate: 61.4% (2,208 of 3,595 customers ordered more than once, counting subscription renewals).
- Subscription share of orders: 47.7%.

## The honest finding in this data
Quiz completers repeat at 60.1%. Non-completers repeat at 63.0%. In this synthetic model, **taking the quiz does not lift repeat behaviour on its own.** What drives the repeat rate is subscription enrollment: a third of first orders are subscriptions, and their 45-day renewals are what push the repeat rate up.

That is the correct lesson, and it is why I do not let clients report "quiz engagement" as a retention result. The quiz earns its place by improving message match and conversion at signup, and by feeding the segment map. Retention itself is carried by interval design and post-purchase. A dashboard that cannot deliver an unwelcome finding is decoration.

## Dashboard panels (weekly review)
1. Revenue per recipient by flow, with the 10% holdout read alongside.
2. Second-order rate by day 60, split subscription vs one-time first orders.
3. Subscription health: active count, skip rate, cancel rate, skip-to-cancel ratio.
4. First-order quality: refund rate, support tickets per 100 first orders.
5. List health: engaged share (60-day), sunset queue size, deliverability flags.
6. Segment read: repeat behaviour by quiz concern segment, to catch a segment the flows are underserving.

## How a number becomes a decision
Each panel carries a floor set in advance. Example: if second-order rate for one-time buyers sits under 35% by day 60 for two consecutive weekly reads, the second-order push flow gets rebuilt, not "optimized". Deciding the threshold before seeing the number is what keeps a dashboard from becoming a story we tell ourselves.
