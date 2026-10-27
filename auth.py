def authenticate(password):
  return len(password) >= 6 and any(c.isdigit() for c in password)