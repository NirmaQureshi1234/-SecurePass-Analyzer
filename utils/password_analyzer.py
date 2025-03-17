import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Strength rating
    if score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }