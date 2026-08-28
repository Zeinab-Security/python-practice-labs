base_price = 15

print("=== Welcome to Cinema Ticket System ===")

age = int(input("Enter your age: "))
seat_type = input("Enter seat type (Premium / Gold / Regular): ")
show_time = input("Enter show time (Evening / Matinee): ")

is_member_input = input("Are you a member? (yes / no): ")
is_member = is_member_input.lower() == 'yes'

is_weekend_input = input("Is it a weekend show? (yes / no): ")
is_weekend = is_weekend_input.lower() == 'yes'

# Check if the age/show time rules allow booking
can_book = age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member))

if not can_book:
    print("Sorry, you don't meet the age or show time requirements to book this ticket.")
else:
    # Discount: members aged 21+ get $3 off
    discount = 0
    if is_member and age >= 21:
        discount = 3

    # Extra charges for weekend or evening shows
    extra_charges = 0
    if is_weekend or show_time == 'Evening':
        extra_charges = 2

    # Service charges based on seat type
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    final_price = base_price + extra_charges + service_charges - discount

    print("\n=== Ticket Summary ===")
    print(f"Base price: ${base_price}")
    print(f"Extra charges: +${extra_charges}")
    print(f"Service charges ({seat_type}): +${service_charges}")
    print(f"Discount: -${discount}")
    print(f"Final price: ${final_price}")
