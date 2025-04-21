# example of assigning a function to a variable
from math import floor

# Same as before, but now we are going to assign the functions to a dictionary!

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