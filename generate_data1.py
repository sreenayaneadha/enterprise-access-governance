import random
import pandas as pd

random.seed(42)
departments = ["HR", "Finance", "Engineering", "Sales", "IT"]
titles = {"HR": ["HR Specialist", "HR Manager"], "Finance": ["Accountant", "Financial Analyst"], "Engineering": ["Software Engineer", "DevOps Engineer"], "Sales": ["Sales Rep", "Account Exec"], "IT": ["SysAdmin", "Helpdesk"]}
permissions_pool = ["Read_Email", "Create_Vendor", "Approve_Invoice", "Delete_Database", "Access_Payroll", "Manage_Users"]

data = []
for i in range(1, 501):
    dept = random.choice(departments)
    perms = random.sample(permissions_pool, k=random.randint(1, 3))

    if i == 15: perms = ["Access_Payroll", "Delete_Database"] # Seeded HR Insider Threat
    if i == 42: perms = ["Delete_Database", "Manage_Users", "Approve_Invoice"] # Over-privileged

    data.append({
        "Employee_ID": f"EMP{i:03d}", "Name": f"Employee_{i}", "Department": dept, 
        "Title": random.choice(titles[dept]), "Permissions": ", ".join(perms)
    })

pd.DataFrame(data).to_csv("employee_access_audit.csv", index=False)
print("Dataset created successfully!")