class EnterpriseCertificationReport:
    def __init__(self, certified, version, completed_phases):

        self.certified = certified

        self.version = version

        self.completed_phases = completed_phases

    def to_dict(self):

        return {
            "certified": self.certified,
            "version": self.version,
            "completed_phases": self.completed_phases,
        }
