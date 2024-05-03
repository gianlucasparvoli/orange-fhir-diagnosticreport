from setuptools import setup 

setup(
    name="OWFhirDiagnosticReport",
    packages=["DiagnosticReport-WidgetOrange"],
    # package_data={"orangedemo": ["icons/*.svg"]},
    classifiers=["Example :: Invalid"],
    # Declare orangedemo package to contain widgets for the "Demo" category
    entry_points={"orange.widgets": "OWFhirDiagnosticReport = DiagnosticReport-WidgetOrange"},
)

