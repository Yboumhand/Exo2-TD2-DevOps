def authenticate(password):
  return len(password) >= 8 and any(c.isdigit() for c in password)