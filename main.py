import json

class User:
    """Represents a citizen with various types of personal data."""
    def __init__(self, user_id, name, address, phone, health_info=None, financial_info=None):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.phone = phone
        self.health_info = health_info # Sensitive data
        self.financial_info = financial_info # Highly sensitive data

    def to_dict(self):
        """Converts user data to a dictionary for display/storage."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "health_info": self.health_info,
            "financial_info": self.financial_info
        }

# --- Simulating a collection of user data without centralized access control ---
# In a real scenario, this might be a database or multiple disparate databases.
user_database = [
    User(1, "Ayşe Yılmaz", "Atatürk Cd. No:1, Ankara", "5321234567",
         health_info={"blood_type": "A+", "allergies": ["pollen"]},
         financial_info={"bank_account": "TR1234567890", "income": 50000}),
    User(2, "Mehmet Demir", "Cumhuriyet Sk. No:5, İzmir", "5059876543",
         health_info={"blood_type": "B-", "allergies": []},
         financial_info={"bank_account": "TR0987654321", "income": 75000}),
    User(3, "Zeynep Kaya", "İstiklal Cd. No:10, İstanbul", "5441112233") # Less sensitive data
]

print("--- Simulating 'Local Tools' Accessing User Data Directly ---")
print("This demonstrates a lack of centralized privacy controls, where different 'tools' might access data without proper authorization or data classification.\n")

# --- Scenario 1: Water Billing Department (needs name, address, phone) ---
print("1. Water Billing Department Tool:")
for user in user_database:
    # This tool only needs basic contact info, but has direct access to all data.
    # It might inadvertently log or expose sensitive data if not properly restricted.
    print(f"  User ID: {user.user_id}, Name: {user.name}, Address: {user.address}, Phone: {user.phone}")
    # Privacy Issue: The tool has access to user.health_info and user.financial_info,
    # even though it doesn't need them. This illustrates a 'zero security barrier' due to over-privilege.
    # In a robust system, access would be restricted to only necessary fields via a central policy.
print("\n")

# --- Scenario 2: Social Services Department (needs name, address, health info, financial info) ---
print("2. Social Services Department Tool:")
for user in user_database:
    if user.health_info or user.financial_info: # This tool might specifically look for sensitive data
        print(f"  User ID: {user.user_id}, Name: {user.name}, Address: {user.address}")
        print(f"    Health Info: {user.health_info}")
        print(f"    Financial Info: {user.financial_info}")
        # Privacy Issue: While this department might legitimately need this data,
        # without strict, centrally managed access controls and audit trails, this direct access
        # can lead to misuse or unauthorized exposure. The article highlights that different tools
        # might have different needs, but a central, unifying privacy policy is often missing.
    else:
        print(f"  User ID: {user.user_id}, Name: {user.name} - No sensitive info found (or not applicable).")
print("\n")

# --- Scenario 3: Event Registration Tool (needs name, maybe phone) ---
print("3. Event Registration Tool:")
for user in user_database:
    # This tool needs minimal data, but again, has full access.
    print(f"  User ID: {user.user_id}, Name: {user.name}, Phone: {user.phone}")
    # Privacy Issue: Similar to the Water Billing tool, this tool accesses
    # more data than required. If this tool is less secure, it becomes a weak point
    # for all user data, not just the data it needs. This exemplifies the "183 local tools"
    # problem, where each tool might be a potential privacy leak due to lack of central governance.
print("\n")

print("--- Summary of the Privacy Issue Illustrated ---")
print("The examples above demonstrate how, without a centralized privacy framework,")
print("different 'local tools' can directly access a citizen's entire data profile.")
print("This leads to:")
print("1.  **Over-privilege:** Tools access data they don't need (e.g., Water Billing accessing health info).")
print("2.  **Lack of granular control:** No clear distinction between public, sensitive, and highly sensitive data access.")
print("3.  **Increased attack surface:** Each tool becomes a potential point of data breach for all data it can access.")
print("A robust system would implement a central 'Privacy Manager' or 'Access Control Layer' that:")
print("    - Classifies data by sensitivity.")
print("    - Defines roles and permissions for each tool/department.")
print("    - Provides a controlled API for data access, returning only necessary and authorized fields.")
print("    - Logs all data access for auditing purposes.")