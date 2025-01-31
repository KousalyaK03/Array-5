# Approach:
# - We process each tax bracket sequentially.
# - For each bracket, we calculate the taxable amount within that bracket and apply the corresponding tax rate.
# - If the salary exceeds all defined brackets, the remaining amount is taxed at the last bracket's rate.
# - We sum up the tax from all brackets to get the total tax.

def calculateTax(levels: List[List[Optional[float]]], salary: float) -> float:
    tax = 0.0  # Initialize total tax
    previous_limit = 0.0  # Keep track of previous bracket limit

    # Iterate over each tax bracket
    for limit, rate in levels:
        if limit is None:  # If the limit is None, apply the last bracket's rate to remaining salary
            tax += (salary - previous_limit) * rate
            break
        elif salary > limit:  # If salary exceeds this bracket, tax the full bracket amount
            tax += (limit - previous_limit) * rate
            previous_limit = limit  # Update previous limit to current bracket
        else:  # If salary falls within this bracket, tax only the remaining amount
            tax += (salary - previous_limit) * rate
            break  # No further processing needed

    return tax

# Time Complexity: O(N) where N is the number of tax brackets.
#     - We iterate over all brackets at most once.
# Space Complexity: O(1) 
#     - We use a few integer/float variables, no extra data structures.
# Example usage

levels = [
    [10000, 0.3],
    [20000, 0.2],
    [30000, 0.1],
    [None, 0.1]
]

salary = 45000
tax = calculateTax(levels, salary)
print(tax)  # Output: 7500.0
