"""Synthetic dataset generator for Lifecycle in a Box.

Generates a fictional DTC skincare customer and order dataset.
Fixed seed: anyone running this gets the exact same data, so every
number in analytics/ is reproducible. This data describes nobody real.
"""
import csv, random
from datetime import date, timedelta

random.seed(42)
START = date(2026, 1, 1)
DAYS = 180
CONCERNS = ["dark spots", "fine lines", "sensitivity", "breakouts"]
CHANNELS = ["paid social", "paid search", "organic", "quiz organic"]

def main():
    customers, orders = [], []
    cid = 0
    for day in range(DAYS):
        d = START + timedelta(days=day)
        for _ in range(random.randint(14, 26)):
            cid += 1
            cust_id = f"C{cid:05d}"
            concern = random.choice(CONCERNS)
            channel = random.choices(CHANNELS, weights=[35, 25, 20, 20])[0]
            quiz = channel == "quiz organic" or random.random() < 0.45
            customers.append([cust_id, d.isoformat(), concern, channel, "yes" if quiz else "no"])
            # First order: serum, subscription or one-time
            sub = random.random() < 0.34
            price = 54.40 if sub else 68.00
            orders.append([f"O{len(orders)+1:06d}", cust_id, d.isoformat(), "Renewal Night Serum",
                           "subscription" if sub else "one-time", f"{price:.2f}"])
            if sub:
                # Subscription cycles at 45 days while active
                cycles = random.choices([1, 2, 3], weights=[45, 35, 20])[0]
                for c in range(cycles):
                    nd = d + timedelta(days=45 * (c + 1))
                    if nd <= START + timedelta(days=DAYS + 90):
                        orders.append([f"O{len(orders)+1:06d}", cust_id, nd.isoformat(),
                                       "Renewal Night Serum", "subscription renewal", "54.40"])
            elif random.random() < 0.42:
                # One-time buyers who come back once
                nd = d + timedelta(days=random.randint(30, 75))
                add = random.random() < 0.3
                orders.append([f"O{len(orders)+1:06d}", cust_id, nd.isoformat(),
                               "Gentle Cream Cleanser" if add else "Renewal Night Serum",
                               "one-time", "34.00" if add else "68.00"])
    with open("data/customers.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["customer_id", "signup_date", "concern", "channel", "quiz_completed"]); w.writerows(customers)
    with open("data/orders.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["order_id", "customer_id", "order_date", "product", "order_type", "revenue"]); w.writerows(orders)
    print(f"customers: {len(customers)}, orders: {len(orders)}")

if __name__ == "__main__":
    main()
