ZONE_POLICY = {
    "Core Identity": {"Core Identity", "Employee Zone", "Finance Zone"},
    "Employee Zone": {"Core Identity"},
    "Finance Zone": {"Core Identity"},
    "Guest Zone": set(),  
}

ROLE_PERMISSIONS = {
    "Employee": {"email", "shared_drive", "internal_tools"},
    "Manager": {"email", "shared_drive", "internal_tools", "team_reports", "approvals"},
    "IT Admin": {"system_config", "user_accounts"},
    "Finance": {"accounting_software", "payment_system"},
    "Guest": {"internet"},
}


MFA_REQUIRED_RESOURCES = {"payment_system", "system_config", "user_accounts", "accounting_software"}


class AccessRequest:
    def __init__(self, user, role, source_zone, target_zone, resource, mfa_verified):
        self.user = user
        self.role = role
        self.source_zone = source_zone
        self.target_zone = target_zone
        self.resource = resource
        self.mfa_verified = mfa_verified


def evaluate_request(req: AccessRequest):
   

    # 1. Micro-segmentation check
    allowed_zones = ZONE_POLICY.get(req.source_zone, set())
    if req.target_zone not in allowed_zones and req.source_zone != req.target_zone:
        return "DENY", f"Blocked by micro-segmentation: {req.source_zone} cannot reach {req.target_zone}"

    # 2. Role-based access control check
    permitted_resources = ROLE_PERMISSIONS.get(req.role, set())
    if req.resource not in permitted_resources:
        return "DENY", f"Blocked by RBAC: role '{req.role}' has no permission for '{req.resource}'"

    # 3. MFA check for sensitive resources
    if req.resource in MFA_REQUIRED_RESOURCES and not req.mfa_verified:
        return "DENY", f"Blocked by MFA policy: '{req.resource}' requires a verified second factor"

    return "ALLOW",

TEST_SCENARIOS = [
    AccessRequest("guest_device", "Guest", "Guest Zone", "Finance Zone", "accounting_software", mfa_verified=False),
    AccessRequest("stolen_cred_user", "Finance", "Core Identity", "Finance Zone", "payment_system", mfa_verified=False),
    AccessRequest("legit_finance_user", "Finance", "Core Identity", "Finance Zone", "payment_system", mfa_verified=True),
    AccessRequest("employee_user", "Employee", "Employee Zone", "Core Identity", "email", mfa_verified=True),
]


if __name__ == "__main__":
    print(f"{'User':<20}{'Role':<10}{'Resource':<22}{'Result':<8}Reason")
    print("-" * 100)
    for req in TEST_SCENARIOS:
        result, reason = evaluate_request(req)
        print(f"{req.user:<20}{req.role:<10}{req.resource:<22}{result:<8}{reason}")
