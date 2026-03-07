from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister(BaseModel):
    # Username: must be a string with at least 5 characters
    username: str = Field(..., min_length=5)
    
    # EmailStr: built-in Pydantic type for email validation
    email: EmailStr
    
    # Age: must be an integer and greater than or equal to (ge) 18
    age: int = Field(..., ge=18)

# --- Test Function ---
def validate_user(data):
    try:
        user = UserRegister(**data)
        print(f"✅ Success: User '{user.username}' is valid!")
    except ValidationError as e:
        print(f"❌ Validation Error for {data.get('username', 'Unknown')}:")
        for error in e.errors():
            # Grabs the field name and the specific error message
            print(f"   - {error['loc'][0]}: {error['msg']}")

# --- Testing Scenarios ---

print("--- Scenario 1: Valid Data ---")
validate_user({"username": "python_pro", "email": "test@example.com", "age": 25})

print("\n--- Scenario 2: Invalid Data ---")
validate_user({
    "username": "abc",        # Too short
    "email": "not-an-email",  # Invalid format
    "age": 16                 # Under 18
})