"""
Main application entry point.
"""

from models.doctor import Doctor
from models.patient import Patient
from store.healthcare_store import HealthcareStore
from view.healthcare_view import display_mappings

def main():
    # Initialize store
    store = HealthcareStore()

    # Generate data from models
    doctors = Doctor.generate_fake_doctors(6)
    patients = Patient.generate_fake_patients(10)

    # Add to store
    for doc in doctors:
        store.add_doctor(doc)

    for pat in patients:
        store.add_patient(pat)

    # Get mappings
    mappings = store.get_all_mappings()

    # Display
    display_mappings(mappings)


if __name__ == "__main__":
    main()