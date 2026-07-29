from orchestration.telecom_query_service import TelecomQueryService


class ChatAdapter:
    @staticmethod
    def ask(query):

        try:
            result = TelecomQueryService.execute(query)

            response = result.get("response", {})

            return {
                "success": True,
                "query": query,
                "agent": result.get("agent"),
                "provider": response.get("provider"),
                "model": response.get("model"),
                "answer": response.get("response"),
                "artifacts": [],
            }

        except Exception as exc:
            return {"success": False, "query": query, "error": str(exc)}
