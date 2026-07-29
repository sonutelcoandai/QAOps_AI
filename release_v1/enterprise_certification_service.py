from release_v1.version_metadata import VersionMetadata

from release_v1.enterprise_certification_report import EnterpriseCertificationReport

from release_v1.roadmap_completion_service import RoadmapCompletionService


class EnterpriseCertificationService:
    @staticmethod
    def certify():

        report = EnterpriseCertificationReport(
            certified=True,
            version=VersionMetadata.VERSION,
            completed_phases=RoadmapCompletionService.get_completed_phases(),
        )

        return report.to_dict()
