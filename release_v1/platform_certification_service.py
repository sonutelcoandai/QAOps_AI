from release_v1.release_readiness_service import ReleaseReadinessService

from release_v1.architecture_validation_service import ArchitectureValidationService


class PlatformCertificationService:
    @staticmethod
    def certify():

        readiness = ReleaseReadinessService.evaluate()

        architecture = ArchitectureValidationService.validate()

        certified = readiness["platform_ready"] and architecture["architecture_valid"]

        return {
            "certified": certified,
            "readiness": readiness,
            "architecture": architecture,
        }
