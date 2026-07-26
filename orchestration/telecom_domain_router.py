class TelecomDomainRouter:
    @staticmethod
    def get_agent(query):

        query = query.lower()

        if any(
            keyword in query for keyword in ["billing", "invoice", "charging", "rating"]
        ):
            return "billing_agent"

        if any(
            keyword in query
            for keyword in ["provisioning", "activation", "inventory", "fulfillment"]
        ):
            return "oss_agent"

        if any(keyword in query for keyword in ["crm", "customer", "order", "product"]):
            return "bss_agent"

        if any(keyword in query for keyword in ["tmf", "tmforum", "service order"]):
            return "tmforum_agent"

        return "telecom_architect_agent"
