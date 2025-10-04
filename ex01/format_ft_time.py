from datetime import datetime

print(f"Seconds since January 1, 1970: {datetime.now().timestamp():,.4f} or {datetime.now().timestamp():,.2e} in scientific notation")
print(f"{datetime.now().strftime("%b %d %Y")}")