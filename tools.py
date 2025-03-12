from agents.tool import function_tool

@function_tool
def check_medical_knowbase(symptoms: str) -> dict:
    """Query medical database for potential conditions"""
    return {
        "possible_conditions": ["Viral upper respiratory infection", "Allergic rhinitis"],
        "red_flags": ["fever >39°C", "difficulty breathing"]
    }

@function_tool
def check_appointment_availability(specialty: str) -> dict:
    """Check real-time appointment availability"""
    return {
        "next_available": {
            "general_practice": "2024-03-15 10:00 AM",
            "cardiology": "2024-03-17 02:30 PM"
        }
    }

@function_tool
def check_medication_stock(medication: str) -> dict:
    """Check pharmacy inventory system"""
    return {
        "in_stock": True,
        "alternatives": ["Loratadine", "Cetirizine"] if medication == "Fexofenadine" else []
    }

@function_tool
def alert_emergency_team(location: str) -> str:
    """Simulate emergency protocol activation"""
    return f"Emergency team dispatched to {location} - ETA 8 minutes"
