# Mortgage Calculator

principal = 500000  # loan amount
interest_rate = 0.04  # annual interest rate
term_years = 5  # loan term in years

num_payments = term_years * 12  # total number of payments
monthly_rate = interest_rate / 12  # monthly interest rate

# Calculate monthly payment
monthly_payment = principal * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1)

# Display results
print("Loan Amount: $%.2f" % principal)
print("Interest Rate: %.2f%%" % (interest_rate * 100))
print("Loan Term: %d years" % term_years)
print("Monthly Payment: $%.2f" % monthly_payment)
