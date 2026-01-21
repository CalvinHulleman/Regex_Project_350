import re
import matplotlib.pyplot as plt
from collections import Counter

data = open("mbox.txt")

months = []
days = []

for line in data:
    m = re.search('From .+@.+ ([A-Z][a-z]{2}) ([A-Z][a-z]{2})', line)
    if m:
        days.append(m.group(1))
        months.append(m.group(2))
# print(days)
# print(months)

## With in class plt.hist
plt.hist(months, bins = 12)
plt.xlabel('Month')
plt.ylabel('Number of Emails Sent')
plt.title('Emails Sent Per Month')
plt.savefig('months.png', dpi = 200)
plt.show()

counts = Counter(months)
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
values = [counts[m] for m in month_order]

## Better Version
plt.bar(month_order, values)
plt.xlabel('Month')
plt.ylabel('Number of Emails Sent')
plt.title('Emails Sent Per Month')
plt.tight_layout()
plt.savefig('months_ordered.png', dpi = 200)
plt.show()

## With in class plt.hist
plt.hist(days, bins = 7)
plt.xlabel('Days of the Week')
plt.ylabel('Number of Emails Sent')
plt.title('Emails Sent Per Day of the Week')
plt.savefig('days.png', dpi = 200)
plt.show()

day_counts = Counter(days)
weekday_order = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
values = [day_counts[d] for d in weekday_order]

## Better Version
plt.bar(weekday_order, values)
plt.xlabel('Day of Week')
plt.ylabel('Number of Emails Sent')
plt.title('Emails Sent Per Day of Week')
plt.tight_layout()
plt.savefig('days_ordered.png', dpi = 200)
plt.show()