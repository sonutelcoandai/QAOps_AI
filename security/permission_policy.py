class PermissionPolicy:
    POLICIES = {
        "head_of_quality": ["approve_release", "view_dashboard", "manage_integrations"],
        "quality_director": ["approve_release", "view_dashboard"],
        "qa_manager": ["view_dashboard", "approve_workflow"],
        "qa_lead": ["execute_workflow"],
        "release_manager": ["approve_release"],
        "test_architect": ["execute_workflow"],
    }

    @classmethod
    def get_permissions(cls, role):

        return cls.POLICIES.get(role, [])
