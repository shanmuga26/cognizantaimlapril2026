from faker import Faker
import random

"""
Patient model representing a healthcare patient.
Includes Faker-based synthetic data generation.
"""

fake = Faker()

class Patient:
    DISEASES = [
        "Heart Attack",
        "Diabetes",
        "Fever",
        "Skin Allergy"
    ]

    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def __str__(self):
        return f"Patient {self.name} diagnosed with {self.disease}"

    @staticmethod
    def generate_fake_patient():
        """
        Generates a single fake patient.
        """
        name = fake.name()
        disease = random.choice(Patient.DISEASES)
        return Patient(name, disease)

    @staticmethod
    def generate_fake_patients(n=10):
        """
        Generates multiple fake patients.
        """
        return [Patient.generate_fake_patient() for _ in range(n)]