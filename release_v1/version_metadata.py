class VersionMetadata:
    VERSION = "1.0.0"

    RELEASE_NAME = "QAOps-AI Enterprise"

    RELEASE_STATUS = "certified"

    @classmethod
    def get_metadata(cls):

        return {
            "version": cls.VERSION,
            "release_name": cls.RELEASE_NAME,
            "release_status": cls.RELEASE_STATUS,
        }
