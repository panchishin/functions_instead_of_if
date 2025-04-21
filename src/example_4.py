# example of assigning a function to a variable
from math import floor

# Same as before, but now we will use lambda function
# Lambda functions are like super small functions
# for example we can convert the following function
# def add(a, b):
#     return a + b
# to a lambda function like this:
# add = lambda a, b: a + b

# We will define some call records

def create_records():
    temp = [
        {"from": "Alice", "to": "Bob", "duration": 5, "date": "2023-10-01", "state": "Texas"},
        {"from": "Bob", "to": "Charlie", "duration": 7, "date": "2023-10-02", "state": "California"},
        {"from": "Charlie", "to": "David", "duration": 4, "date": "2023-10-03", "state": "New York"},
        {"from": "David", "to": "Eve", "duration": 6, "date": "2023-10-04", "state": "Florida"},
        {"from": "Eve", "to": "Frank", "duration": 8.1, "date": "2023-10-05", "state": "Illinois"},
        {"from": "Frank", "to": "Grace", "duration": 9, "date": "2023-10-06", "state": "Michigan"}
    ]
    return temp

call_records = create_records()

# Using the old way with if/else let's apply logic based on state
# update all records based on state.  The logic is as follows
# For Texas, cost is duration x 0.15 if the year is 2023, otherwise it's duration x 0.08
# For California, cost is duration x 0.20
# For New York, cost is duration x 0.25 if the year is 2023, otherwise it's duration x 0.10
# For Florida, cost is duration x 0.30
# For Illinois, cost is duration x 0.35 but truncate the cost down to the lowest 5 cent, so $1.23 becomes $1.20
# For Michigan, cost is duration x 0.40

# We notice that some of the states just have a simple rate
def simple_rate(record, rate):
    record['cost'] = round(record['duration'] * rate, 2)

# We also notice that we have some if 2023 else logic
def year_2023_logic(record, rate_2023, rate_else):
    if int(record['date'].split('-')[0]) == 2023:
        record['cost'] = round(record['duration'] * rate_2023, 2)
    else:
        record['cost'] = round(record['duration'] * rate_else, 2)

texas = lambda record: year_2023_logic(record, 0.15, 0.08)

california = lambda record: simple_rate(record, 0.20)

new_york = lambda record: year_2023_logic(record, 0.25, 0.10)

florida = lambda record: simple_rate(record, 0.30)

# illinois is kinda "special" so we leave it as-is
def illinois(record):
    temp = round(record['duration'] * 0.35, 2)
    record['cost'] = round(floor(temp / 0.05 + 1e-10) * 0.05, 2)

michigan = lambda record: simple_rate(record, 0.40)


# This is the new part where we assign the functions to a dictionary for fast lookup
function_calls = {
    'Texas': texas,
    'California': california,
    'New York': new_york,
    'Florida': florida,
    'Illinois': illinois,
    'Michigan': michigan,
}

# Same loop as last time, but now we don't need an if/else
for record in call_records:
    the_function = function_calls[record['state']]
    the_function(record)



for record in call_records:
    print(f"State: {record['state']}, Duration: {record['duration']}, Cost: ${float(record['cost']):5.2f}")


# Common practice is to keep the unit tests in another file and import what you want to test.
# In this case we would import the state functions.