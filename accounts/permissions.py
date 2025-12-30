from django.contrib.auth.models import Group

def is_waiter(user):
    return user.is_authenticated and user.groups.filter(name="Waiter").exists()

def is_cashier(user):
    return user.is_authenticated and user.groups.filter(name="Cashier").exists()

def is_manager(user):
    return user.is_authenticated and user.groups.filter(name="Manager").exists()
