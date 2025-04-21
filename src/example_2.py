# example of assigning a function to a variable
from math import floor

# Same as before but convert logic in if/else to functions

# We will define some call records

call_records = [
    {"from": "Alice", "to": "Bob", "duration": 5, "date": "2023-10-01", "state": "Texas"},
    {"from": "Bob", "to": "Charlie", "duration": 7, "date": "2023-10-02", "state": "California"},
    {"from": "Charlie", "to": "David", "duration": 4, "date": "2023-10-03", "state": "New York"},
    {"from": "David", "to": "Eve", "duration": 6, "date": "2023-10-04", "state": "Florida"},
    {"from": "Eve", "to": "Frank", "duration": 8.1, "date": "2023-10-05", "state": "Illinois"},
    {"from": "Frank", "to": "Grace", "duration": 9, "date": "2023-10-06", "state": "Michigan"}
]


# Using the old way with if/else let's apply logic based on state
# update all records based on state.  The logic is as follows
# For Texas, cost is duration x 0.15 if the year is 2023, otherwise it's duration x 0.08
# For California, cost is duration x 0.20
# For New York, cost is duration x 0.25 if the year is 2023, otherwise it's duration x 0.10
# For Florida, cost is duration x 0.30
# For Illinois, cost is duration x 0.35 but truncate the cost down to the lowest 5 cent, so $1.23 becomes $1.20
# For Michigan, cost is duration x 0.40

def texas(record):
    if int(record['date'].split('-')[0]) == 2023:
        record['cost'] = round(record['duration'] * 0.15, 2)
    else:
        record['cost'] = round(record['duration'] * 0.08, 2)

def california(record):
    record['cost'] = round(record['duration'] * 0.20, 2)

def new_york(record):
    if int(record['date'].split('-')[0]) == 2023:
        record['cost'] = round(record['duration'] * 0.25, 2) 
    else:
        record['cost'] = round(record['duration'] * 0.10, 2)

def florida(record):
    record['cost'] = round(record['duration'] * 0.30, 2)

def illinois(record):
    temp = round(record['duration'] * 0.35, 2)
    record['cost'] = round(floor(temp / 0.05 + 1e-10) * 0.05, 2)

def michigan(record):
    record['cost'] = round(record['duration'] * 0.40, 2)


# Same loop as last time, but now our logic is nice and clean
for record in call_records:
    if record['state'] == 'Texas':
        texas(record)

    elif record['state'] == 'California':
        california(record)

    elif record['state'] == 'New York':
        new_york(record)

    elif record['state'] == 'Florida':
        florida(record)

    elif record['state'] == 'Illinois':
        illinois(record)

    elif record['state'] == 'Michigan':
        michigan(record)

for record in call_records:
    print(f"State: {record['state']}, Duration: {record['duration']}, Cost: ${float(record['cost']):5.2f}")



# As a bonus, we can "unit test" individual functions to make sure they work as expected
# Let's test Illinois, because it is tricky with the rounding down to nearest 5 cents
sample = {"duration":0}
illinois(sample)
assert(sample['cost'] == 0.0)
sample = {"duration":1}
illinois(sample)
assert(sample['cost'] == 0.35)
sample = {"duration":1.1}
illinois(sample)
assert(sample['cost'] == 0.35)
sample = {"duration":10.1}
illinois(sample)
assert(sample['cost'] == 3.50)
sample = {"duration":10.2}
illinois(sample)
assert(sample['cost'] == 3.55)

# from these tests I discovered that the illinois function needs to be fixed like so
def illinois(record):
    temp = round(record['duration'] * 0.35, 2)
    record['cost'] = round(floor(temp / 0.05 + 1e-10) * 0.05, 2)

# notice the "+ 1e-10" to fix the rounding issue

# having these kinds of tests for each function is really helpful for debugging and does not require you to have the full dataset
