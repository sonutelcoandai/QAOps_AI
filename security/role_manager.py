class RoleManager:
    ROLES = {
        "head_of_quality",
        "quality_director",
        "qa_manager",
        "qa_lead",
        "release_manager",
        "test_architect",
    }

    @classmethod
    def is_valid_role(cls, role):

        return role in cls.ROLES
