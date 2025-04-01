import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers import (
    users,
    detail_doctor,
    specialty,
    appointment,
    bill,
    ca_kham_benh,
    clinics,
    detail_customer,
    doctor_certificates,
    patient_medical_records,
    reviews,
    service_doctor
)
from .database import engine, Base

app = FastAPI(title="Booking App API")

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(users.router)
app.include_router(detail_doctor.router)
app.include_router(specialty.router)
app.include_router(bill.router)
app.include_router(appointment.router)
app.include_router(ca_kham_benh.router)
app.include_router(clinics.router)
app.include_router(detail_customer.router)
app.include_router(doctor_certificates.router)
app.include_router(patient_medical_records.router)
app.include_router(reviews.router)
app.include_router(service_doctor.router)
