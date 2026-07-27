class LearningResult:
    def __init__(self, source, lesson, learned):

        self.source = source

        self.lesson = lesson

        self.learned = learned

    def to_dict(self):

        return {"source": self.source, "lesson": self.lesson, "learned": self.learned}
