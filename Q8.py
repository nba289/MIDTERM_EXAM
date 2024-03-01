def is_valid_url(text):
    # Check if the text starts with 'http://' or 'https://'
    if text.find("http://") == 0 or text.find("https://") == 0:
        # Further checks can be added here (e.g., for a domain name)
        return True
    else:
        return False

# Example usage
url1 = "http://example.com"
url2 = "https://example.com"
not_url = "example.com"

print(is_valid_url(url1))  # Expected output: True
print(is_valid_url(url2))  # Expected output: True
print(is_valid_url(not_url))  # Expected output: False
