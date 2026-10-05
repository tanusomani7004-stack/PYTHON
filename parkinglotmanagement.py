parking_slots = {}
vehicle_history = []


def show_slots():
    print("\n========== PARKING SLOTS ==========")

    for slot in range(1, 11):
        if slot in parking_slots:
            vehicle = parking_slots[slot]
            print(f"Slot {slot}: Occupied - {vehicle['number']}")
        else:
            print(f"Slot {slot}: Available")


def park_vehicle():
    print("\n========== PARK VEHICLE ==========")

    number = input("Enter vehicle number: ").upper().strip()

    if not number:
        print(" Vehicle number cannot be empty.")
        return

    for vehicle in parking_slots.values():
        if vehicle["number"] == number:
            print(" Vehicle is already parked.")
            return

    available_slot = None

    for slot in range(1, 11):
        if slot not in parking_slots:
            available_slot = slot
            break

    if available_slot is None:
        print(" Parking is full!")
        return

    vehicle_type = input("Enter vehicle type (Car/Bike): ").strip()

    parking_slots[available_slot] = {
        "number": number,
        "type": vehicle_type
    }

    print(f" Vehicle parked successfully!")
    print(f" Assigned Slot: {available_slot}")


def remove_vehicle():
    print("\n========== REMOVE VEHICLE ==========")

    number = input("Enter vehicle number: ").upper().strip()

    found_slot = None

    for slot, vehicle in parking_slots.items():
        if vehicle["number"] == number:
            found_slot = slot
            break

    if found_slot is None:
        print(" Vehicle not found.")
        return

    vehicle = parking_slots[found_slot]

    parking_slots.pop(found_slot)

    vehicle_history.append({
        "number": vehicle["number"],
        "type": vehicle["type"],
        "slot": found_slot
    })

    print(" Vehicle removed successfully.")
    print(f" Vehicle: {vehicle['number']}")
    print(f" Slot: {found_slot}")


def search_vehicle():
    print("\n========== SEARCH VEHICLE ==========")

    number = input("Enter vehicle number: ").upper().strip()

    for slot, vehicle in parking_slots.items():

        if vehicle["number"] == number:
            print("\n Vehicle Found!")
            print("Vehicle Number:", vehicle["number"])
            print("Vehicle Type  :", vehicle["type"])
            print("Parking Slot  :", slot)
            return

    print(" Vehicle not found.")


def show_history():
    print("\n========== PARKING HISTORY ==========")

    if not vehicle_history:
        print("No vehicle history available.")
        return

    for record in vehicle_history:
        print("\nVehicle Number:", record["number"])
        print("Vehicle Type  :", record["type"])
        print("Slot Used     :", record["slot"])
        print("------------------------------------")


def parking_statistics():
    total_slots = 10
    occupied = len(parking_slots)
    available = total_slots - occupied

    print("\n========== PARKING STATISTICS ==========")
    print("Total Slots     :", total_slots)
    print("Occupied Slots  :", occupied)
    print("Available Slots :", available)

    if occupied == total_slots:
        print(" Parking is FULL!")
    elif available <= 2:
        print(" Only a few slots remaining.")
    else:
        print(" Parking space available.")


def main():

    while True:

        print("\n====================================")
        print("       SMART PARKING SYSTEM")
        print("====================================")
        print("1. Show Parking Slots")
        print("2. Park Vehicle")
        print("3. Remove Vehicle")
        print("4. Search Vehicle")
        print("5. Parking History")
        print("6. Parking Statistics")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_slots()

        elif choice == "2":
            park_vehicle()

        elif choice == "3":
            remove_vehicle()

        elif choice == "4":
            search_vehicle()

        elif choice == "5":
            show_history()

        elif choice == "6":
            parking_statistics()

        elif choice == "7":
            print("\n Thank you for using Smart Parking System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
