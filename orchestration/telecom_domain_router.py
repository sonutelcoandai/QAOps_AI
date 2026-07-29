class TelecomDomainRouter:
    @staticmethod
    def get_agent(query):

        query = query.lower()

        if any(
            keyword in query
            for keyword in ["tmf", "tmforum", "tmf620", "tmf641", "service order"]
        ):
            return "tmforum_agent"

        if any(
            keyword in query for keyword in ["billing", "invoice", "charging", "rating"]
        ):
            return "billing_agent"

        if any(
            keyword in query
            for keyword in [
                "provisioning",
                "activation",
                "inventory",
                "fulfillment",
                "oss",
            ]
        ):
            return "oss_agent"

        if any(
            keyword in query
            for keyword in ["crm", "customer", "order", "product", "bss"]
        ):
            return "bss_agent"

        return "telecom_architect_agent"
