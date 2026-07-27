from self_healing.continuous_learning.learning_result import LearningResult


class LearningService:
    @staticmethod
    def learn(source):

        result = LearningResult(
            source=source, lesson="capture_and_reuse_knowledge", learned=True
        )

        return result.to_dict()
