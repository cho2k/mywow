import random

num_tenants = 40
total_slots = 50
outdoor_slots = list(range(1, 21))
indoor_slots = list(range(21, total_slots + 1))

# Shuffle the slots
random.shuffle(outdoor_slots)
random.shuffle(indoor_slots)

# Read the tenant choices from the text file
tenant_choices = {}

# Read tenant choices from the text file
try:
    with open('tenant_choices.txt', 'r') as file:
        for line in file:
            tenant_id, choice = line.strip().split(';')
            tenant_choices[int(tenant_id)] = choice.lower()
except FileNotFoundError:
    print("tenant_choices.txt not found.")

# Assign slots based on tenant choices
assigned_slots = []

# Iterate through each tenant
for tenant in range(1, num_tenants + 1):
    # Check if the tenant made a choice
    if tenant in tenant_choices:
        choice = tenant_choices[tenant]

        # Assign a slot based on the choice
        if choice == 'indoor':
            # Assign an indoor slot if available
            if indoor_slots:
                slot = indoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'indoor'))
            else:
                # Assign an outdoor slot if no indoor slots are left
                slot = outdoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'outdoor'))
        elif choice == 'outdoor':
            # Assign an outdoor slot if available
            if outdoor_slots:
                slot = outdoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'outdoor'))
            else:
                # Assign an indoor slot if no outdoor slots are left
                slot = indoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'indoor'))
        elif choice == 'na':
            # Handle NA preference by assigning any available slot
            if outdoor_slots:
                slot = outdoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'outdoor'))
            elif indoor_slots:
                slot = indoor_slots.pop(0)
                assigned_slots.append((tenant, slot, 'indoor'))
    else:
        # Assign any available slot if the tenant did not make a choice
        if outdoor_slots:
            slot = outdoor_slots.pop(0)
            assigned_slots.append((tenant, slot, 'outdoor'))
        elif indoor_slots:
            slot = indoor_slots.pop(0)
            assigned_slots.append((tenant, slot, 'indoor'))

# Sort the assigned slots by tenant ID
assigned_slots.sort(key=lambda x: x[0])

# Print the assigned slots for each tenant
print("Tenant;Slot;Area；Choice")
for tenant, slot, choice in assigned_slots:
    print(f"{tenant};{slot};{choice};{tenant_choices.get(tenant, 'NA')}")

