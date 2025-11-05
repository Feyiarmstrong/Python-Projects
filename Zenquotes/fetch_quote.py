import requests
def fetch_quote():
    """Fetch a quote from ZenQuotes API and return as a string."""
    url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract quote and author
        if isinstance(data, list) and len(data) > 0:
            quote_text = data[0].get("q", "")
            author = data[0].get("a", "")
            return f'"{quote_text}" — {author}'
        else:
            print("Malformed response")
            return None
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return None

# Allows testing this file directly
if __name__ == "__main__":
    quote = fetch_quote()
    if quote:
        print("Fetched quote:", quote)
    else:
        print("No quote fetched.")

