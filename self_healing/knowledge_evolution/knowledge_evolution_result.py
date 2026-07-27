class KnowledgeEvolutionResult:
    def __init__(self, knowledge_area, evolution_action, evolved):

        self.knowledge_area = knowledge_area

        self.evolution_action = evolution_action

        self.evolved = evolved

    def to_dict(self):

        return {
            "knowledge_area": self.knowledge_area,
            "evolution_action": self.evolution_action,
            "evolved": self.evolved,
        }
