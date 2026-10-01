# Enterprise Access Governance Audit Lab
# Enterprise Access Governance Lab

This is a local auditing project I built to detect privilege creep and Segregation of Duties (SoD) violations. Because testing on a live active directory is difficult to set up, this tool generates synthetic enterprise access data, stores it in a local SQLite database, and runs Python scripts to flag security anomalies.

I created this to get hands-on experience with Identity and Access Management (IAM) principles and database auditing.

## How It Works

* **`generate_data.py`**: Builds a simulated company structure (users, departments, roles, and a history of access grants) and populates a local `governance.db` file.
* **`audit_permissions.py`**: Scans the database to find security risks. It specifically looks for:
  * **Privilege Creep:** Users who changed departments but never had their old access rights revoked. Intentionally made Employee 15 overprivileged and Employee 42 an SoD threat to ensure the commands worked.
  * **SoD Violations:** Users who hold "toxic combinations" of access (e.g., the ability to both submit and approve a financial request).

## Tech Stack
* **Python 3**: Core scripting and logic.
* **SQLite3**: Lightweight, zero-configuration database.

## Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/sreenayaneadha/enterprise-access-governance.git](https://github.com/sreenayaneadha/enterprise-access-governance.git)
   cd enterprise-access-governance
   ```

2. Generate the synthetic database (`governance.db`):
   ```bash
   python generate_data.py
   ```

3. Run the security audit:
   ```bash
   python audit_permissions.py
   ```

*The script will output a report directly to the terminal detailing which simulated accounts have excessive permissions.*

## Improvements
* Export the terminal output to a structured CSV report.
* Map the specific access violations to their corresponding NIST Cybersecurity Framework controls.
