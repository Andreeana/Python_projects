Bitcoin Investment Value Tracker 💸

In this project, you'll create a program that tells you
when the USD value of your Bitcoin investment falls below $30,000.

You will need to:
- Create a function to convert Bitcoin to USD
- Use that function to calculate the value of your investment
- Print a message if the investment value is below $30,000

Assume:
- You own 1.2 Bitcoin
- 1 Bitcoin is worth $40,000 (changeable for testing)
"""

# Your current investment values
investment_in_bitcoin = 1.2      # Amount of Bitcoin you own
bitcoin_to_usd = 40000           # Current price of 1 Bitcoin in USD

1) Define a function to calculate your Bitcoin investment value in USD
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    """
    Converts Bitcoin amount to USD value.

    Parameters:
    - bitcoin_amount: float — the amount of Bitcoin owned
    - bitcoin_value_usd: float — the value of 1 Bitcoin in USD

    Returns:
    - float — the total value in USD
    """
    return bitcoin_amount * bitcoin_value_usd

2) Use the function to calculate your total USD investment value
usd_value = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
print(f"Your Bitcoin investment is worth: ${usd_value}")

3) Check if your investment is below the $30,000 threshold
if usd_value < 30000:
    print("⚠️ Alert: Your Bitcoin investment has dropped below $30,000!")
else:
    print("✅ Your Bitcoin investment is above $30,000.")
