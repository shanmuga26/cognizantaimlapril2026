"""
HealthcareStore handles storage and mapping logic between patients and doctors.
"""

class HealthcareStore:

    def __init__(self):
        self.doctors = []
        self.patients = []

        self.disease_map = {
            "Heart Attack": "Cardiologist",
            "Diabetes": "Endocrinologist",
            "Fever": "General Physician",
            "Skin Allergy": "Dermatologist"
        }

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def assign_doctor(self, patient):
        """
        Assign doctor based on disease → specialization mapping
        """
        required_specialization = self.disease_map.get(patient.disease)

        # Optional improvement: choose best doctor (highest experience)
        eligible_doctors = [
            doc for doc in self.doctors
            if doc.specialty == required_specialization
        ]

        if not eligible_doctors:
            return None

        # Pick most experienced doctor 🔥
        return max(eligible_doctors, key=lambda d: d.years_of_experience)

    def get_all_mappings(self):
        """
        Returns list of (patient, doctor) tuples
        """
        return [
            (patient, self.assign_doctor(patient))
            for patient in self.patients
        ]