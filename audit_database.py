import sqlite3
import pandas as pd

conn = sqlite3.connect("enterprise_audit.db")

# 1. Query the vulnerabilities
query_hr = "SELECT Employee_ID, Name, Department, Permissions FROM employees WHERE Department = 'HR' AND Permissions LIKE '%Access_Payroll%'"
query_sod = "SELECT Employee_ID, Name, Title, Permissions FROM employees WHERE Permissions LIKE '%Delete_Database%' AND Permissions LIKE '%Manage_Users%'"

df_hr = pd.read_sql(query_hr, conn)
df_sod = pd.read_sql(query_sod, conn)

# 2. Create text file
with open("Security_Audit_Report.txt", "w") as file:
    file.write("ENTERPRISE SECURITY AUDIT REPORT\n")
    file.write("================================\n\n")
    
    file.write("CRITICAL RISK: Unauthorized HR Payroll Access\n")
    file.write("Action Required: Revoke payroll access immediately.\n")
    file.write("-" * 50 + "\n")
    file.write(df_hr.to_string(index=False) + "\n\n\n")
    
    file.write("CRITICAL RISK: Separation of Duties (SoD) Violations\n")
    file.write("Action Required: Account holds conflicting administrative privileges.\n")
    file.write("-" * 50 + "\n")
    file.write(df_sod.to_string(index=False) + "\n")

print("Audit complete! 'Security_Audit_Report.txt' has been generated in your folder.")
conn.close()
