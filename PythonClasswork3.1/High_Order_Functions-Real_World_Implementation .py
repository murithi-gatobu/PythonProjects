# Medical Risk Assessment System using Higher-Order Function

def filter_custom(predicate, lst):
    """
    Custom implementation of the built-in filter() function.
    Returns a list of elements from lst for which predicate(x) is True.
    
    Parameters:
    - predicate: A function that takes one argument and returns True or False
    - lst: A list of items to filter
    
    Returns:
    - A new list of filtered elements
    """
    results = []
    for x in lst:
        if predicate(x):
            results.append(x)
    return results


# Sample patient data: list of dictionaries
patients = [
    {"name": "Alice", "temp": 36.9, "oxygen": 96},
    {"name": "Bob", "temp": 38.4, "oxygen": 90},
    {"name": "Carol", "temp": 37.8, "oxygen": 92},
    {"name": "Dave", "temp": 36.5, "oxygen": 99},
    {"name": "Eve", "temp": 38.0, "oxygen": 93},
    {"name": "Frank", "temp": 37.2, "oxygen": 88},
]

# Define a function that checks whether a patient is high-risk
def is_high_risk(patient):
    """
    Determines if a patient is high-risk.
    A high-risk patient has:
    - Temperature above 37.5°C
    - Oxygen level below 94%
    """
    return patient["temp"] > 37.5 and patient["oxygen"] < 94

# Use the custom higher-order function to filter high-risk patients
high_risk_patients = filter_custom(is_high_risk, patients)

# Display the results
print("=== High-Risk Patients Report ===\n")
if not high_risk_patients:
    print("No high-risk patients found.")
else:
    for p in high_risk_patients:
        print(f"Name      : {p['name']}")
        print(f"Temperature: {p['temp']}°C")
        print(f"Oxygen     : {p['oxygen']}%")
        print("-" * 30)
# End of report
"""=== High-Risk Patients Report ===

Name      : Bob
Temperature: 38.4°C
Oxygen     : 90%
------------------------------
Name      : Carol
Temperature: 37.8°C
Oxygen     : 92%
------------------------------
Name      : Eve
Temperature: 38.0°C
Oxygen     : 93%
------------------------------
No high-risk patients found.
"""