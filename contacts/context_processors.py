from .models import (
    PhoneNumber,
    WorkSchedule,
    ContactEmail,
)


def add_contact_data(request):
    phone_number = PhoneNumber.objects.first()
    work_schedule = WorkSchedule.objects.first()
    contact_email = ContactEmail.objects.first()

    return {
        "phone_number": phone_number,
        "work_schedule": work_schedule,
        "contact_email": contact_email,
    }
