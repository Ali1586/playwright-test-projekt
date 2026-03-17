"""
Logger - ENKEL VERSION
Bara print-statements
"""


def log_test_start(test_name: str):
    """Logga test-start"""
    print(f"\n{'='*50}")
    print(f"TEST: {test_name}")
    print(f"{'='*50}")


def log_step(step_number: int, description: str):
    """Logga ett teststeg"""
    print(f"  STEG {step_number}: {description}")


def log_success(message: str):
    """Logga success"""
    print(f"  ✅ {message}")


def log_error(message: str):
    """Logga error"""
    print(f"  ❌ {message}")


def log_info(message: str):
    """Logga info"""
    print(f"  ℹ️  {message}")