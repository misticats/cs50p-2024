import sys
import requests

def main():
    # Ensure the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to convert the argument to a float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Query the CoinDesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        sys.exit("Failed to retrieve data")

    # Extract the Bitcoin price
    try:
        price = data["bpi"]["USD"]["rate_float"]
    except KeyError:
        sys.exit("Unexpected data format")

    # Calculate total cost
    total_cost = num_bitcoins * price
    formatted_cost = "{:,.4f}".format(total_cost)
    print(f"${formatted_cost}")

if __name__ == "__main__":
    main()
