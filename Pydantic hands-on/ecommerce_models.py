from pydantic import BaseModel, Field, EmailStr, ValidationError

class Address(BaseModel):
    city: str = Field(..., min_length=3)
    pincode: str = Field(..., pattern=r"^\d{6}$")

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    address: Address

def get_user_input():
    print("--- E-commerce User Registration ---")
    try:
        # Collecting data from terminal
        u_id = input("Enter User ID: ")
        u_name = input("Enter Name: ")
        u_email = input("Enter Email: ")
        u_age = input("Enter Age: ")
        u_city = input("Enter City: ")
        u_pin = input("Enter 6-digit Pincode: ")

        # Creating the dictionary structure
        user_data = {
            "user_id": u_id,
            "name": u_name,
            "email": u_email,
            "age": u_age,
            "address": {
                "city": u_city,
                "pincode": u_pin
            }
        }

        # The moment of truth: Pydantic validates it all at once
        valid_user = User(**user_data)
        print("\n✅ Registration Successful!")
        print(valid_user.model_dump_json(indent=2))

    except ValidationError as e:
        print("\n❌ Input Rejected. Reasons:")
        for error in e.errors():
            # This makes the error messages user-friendly
            field = " -> ".join(str(loc) for loc in error['loc'])
            print(f"   - {field}: {error['msg']}")

# Run the function
get_user_input()