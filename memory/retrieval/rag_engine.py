from knowledge.knowledge_search import KnowledgeSearch
from model_orchestration.router.model_execution_resolver import ModelExecutionResolver


class RAGEngine:
    @staticmethod
    def answer(question, task_name="test_case_generation"):
        results = KnowledgeSearch.search(question)

        context_parts = []

        for item in results:
            if isinstance(item, dict):
                context_parts.append(item.get("content", ""))
            else:
                context_parts.append(str(item))

        context = "\n".join(context_parts)

        prompt = f"""
Context:
{context}

Question:
{question}
"""

        response = ModelExecutionResolver.execute(task_name=task_name, prompt=prompt)

        return response
