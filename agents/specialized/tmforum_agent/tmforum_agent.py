from agent_registry.base_agent import BaseAgent

from ai_providers.ollama.ollama_provider import OllamaProvider


class TMForumAgent(BaseAgent):
    def execute(self, task):

        print("DEBUG: TMForumAgent started")

        query = task.get("query", "")

        print("DEBUG: Query received")

        provider = OllamaProvider()

        print("DEBUG: Calling Ollama")

        answer = provider.generate(query)

        print("DEBUG: Ollama returned")

        return {
            "agent": "tmforum_agent",
            "query": query,
            "response": {"provider": "ollama", "model": "qwen3", "response": answer},
        }

    def validate(self, task):

        return isinstance(task, dict) and "query" in task

    def get_agent_info(self):

        return {"name": "TM Forum Agent", "domain": "tmforum"}
