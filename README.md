# Function Extraction Tutorial

This tutorial demonstrates several methods for extracting `if/else` logic into reusable functions, which can help improve code organization and readability.

## Table of Contents
1. [Example 1: Basic If/Else Logic](#example-1-basic-if-else-logic)
2. [Example 2: Using Functions for State-Specific Logic](#example-2-using-functions-for-state-specific-logic)
3. [Example 3: Using Regular Functions](#example-3-using-regular-functions)
4. [Example 4: Using Lambda Functions](#example-4-using-lambda-functions)
5. [Example 5: Inline Lambda Functions](#example-5-inline-lambda-functions)

## Example 1: Basic If/Else Logic

In this example, basic `if/else` logic is used to calculate the cost based on the state.

## Example 2: Using Functions for State-Specific Logic

In this example, functions are defined for each state's cost calculation logic.

```python
def texas(record):
    if int(record['date'].split('-')[0]) == 2023:
        record['cost'] = round(record['duration'] * 0.15, 2)
    else:
        record['cost'] = round(record['duration'] * 0.08, 2)
...

for record in call_records:
    if record['state'] == 'Texas':
        texas(record)
    ...

```

## Example 3: Get rid of the if/else

Replace the if/else with a dictionary

```python
# This is the new part where we assign the functions to a dictionary for fast lookup
function_calls = {
    'Texas': texas,
    'California': california,
    'New York': new_york,
    ...
}

# Same loop as last time, but now we don't need an if/else
for record in call_records:
    the_function = function_calls[record['state']]
    the_function(record)

```

## Example 4: Using Lambda Functions

In this example, lambda functions are used for simplicity and readability.

```python
def simple_rate(record, rate):
    record['cost'] = round(record['duration'] * rate, 2)

def year_2023_logic(record, rate_2023, rate_else):
    if int(record['date'].split('-')[0]) == 2023:
        record['cost'] = round(record['duration'] * rate_2023, 2)
    else:
        record['cost'] = round(record['duration'] * rate_else, 2)


# Using lambda functions for each state's cost calculation logic.
texas = lambda record: year_2023_logic(record, 0.15, 0.08)
california = lambda record: simple_rate(record, 0.20)
# ... other states

function_calls = {
    'Texas': texas,
    # ... other states
}
```

## Example 5: Inline Lambda Functions

Finally we get rid of the temporary variables that hold the lambda functions and just store them directly in a dictionary.

```python
# This is the new part where we assign the functions to a dictionary for fast lookup
function_calls = {
    'Texas': lambda record: year_2023_logic(record, 0.15, 0.08),
    'California': lambda record: simple_rate(record, 0.20),
    'New York': lambda record: year_2023_logic(record, 0.25, 0.10),
    'Florida': lambda record: simple_rate(record, 0.30),
    'Illinois': lambda record: illinois(record),
    'Michigan': lambda record: simple_rate(record, 0.40),
}
```

## Conclusion

By extracting `if/else` logic into functions, you can improve code organization, reusability, and flexability.
You'll notice that there is very little code duplication.  All the logic for the year 2023 is in one place,
and all the simple rate logic is in one place.

This approach also makes it easier to add new states or change existing ones without having to modify multiple parts of the codebase.
It also makes testing with asserts a lot easier, because we can directly test the individual functions,
and now there are only 3 functions to test, year_2023_logic, simple_rate, and illinois!