days = int(input())
plunder_per_day = int(input())
expected_robbery = float(input())

count = 0

for day in range(1, days + 1):
    count += plunder_per_day

    if day % 3 == 0:
        count += (plunder_per_day / 2)

    if day % 5 == 0:
        count = count * 0.70  # 0.30, 1.30

if count >= expected_robbery:
    print(f"Ahoy! {count:.2f} plunder gained.")
elif count < expected_robbery:
    percent = abs(((expected_robbery - count) / expected_robbery) * 100)
    percent = 100 - percent
    print(f"Collected only {percent:.2f}% of the plunder.")
