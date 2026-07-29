class QueryIntentClassifier:
    @staticmethod
    def classify(query):

        query = query.lower()

        if "test case" in query:
            return "generate_test_cases"

        if "validate" in query:
            return "validation"

        if "review" in query:
            return "review"

        if "explain" in query:
            return "knowledge"

        return "general"
