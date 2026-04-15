from faker import Faker
import random

"""
Doctor model representing a healthcare professional.
Includes Faker-based synthetic data generation.
"""

fake = Faker()

class Doctor:
    SPECIALIZATIONS = [
        "Cardiologist",
        "Endocrinologist",
        "General Physician",
        "Dermatologist"
    ]

    def __init__(self, name, specialty, years_of_experience):
        self.name = name
        self.specialty = specialty
        self.years_of_experience = years_of_experience

    def __str__(self):
        return (
            f"Doctor {self.name} is a {self.specialty} with "
            f"{self.years_of_experience} years of experience."
        )

    @staticmethod
    def generate_fake_doctor():
        """
        Generates a single fake doctor with realistic specialization.
        """
        name = fake.name()
        specialty = random.choice(Doctor.SPECIALIZATIONS)
        years_of_experience = fake.random_int(min=1, max=40)

        return Doctor(name, specialty, years_of_experience)

    @staticmethod
    def generate_fake_doctors(n=5):
        """
        Generates multiple fake doctors.
        """
        return [Doctor.generate_fake_doctor() for _ in range(n)]