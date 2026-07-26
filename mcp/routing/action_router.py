class ActionRouter:
    ROUTES = {
        "create_ticket": "jira",
        "update_ticket": "jira",
        "create_page": "confluence",
        "update_page": "confluence",
        "create_pr": "github",
        "create_commit": "github",
        "create_work_item": "azure_devops",
        "update_work_item": "azure_devops",
        "create_collection": "postman",
        "run_collection": "postman",
    }

    @classmethod
    def get_target(cls, action):

        return cls.ROUTES.get(action)
