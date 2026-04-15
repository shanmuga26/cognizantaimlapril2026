"""
View layer responsible for displaying healthcare mappings.
"""

def display_mappings(mappings):
    print("\n==== Patient → Doctor Mapping ====\n")

    for patient, doctor in mappings:
        if doctor:
            print(
                f"{patient.name} ({patient.disease}) → "
                f"{doctor.name} [{doctor.specialty}, {doctor.years_of_experience} yrs]"
            )
        else:
            print(f"{patient.name} ({patient.disease}) → No Doctor Available")