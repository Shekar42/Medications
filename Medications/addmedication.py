print("addprescription.py")
medications = []

def add_medication(aspirin, mg):
    medications.append('name': aspirin, 'dosage': 5mg)

# Example usage
add_medication("Aspirin", "100mg")
add_medication("Paracetamol", "500mg")

print("Medications List:")
for med in medications:
    print(f"{med['name']} - {med['dosage']}")

    # Save to a text file
with open("medications.txt", "w") as file:
    for med in medications:
        file.write(f"{med['name']} - {med['dosage']}\n")
        