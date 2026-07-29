from release_v1.release_report import ReleaseReport

from release_v1.version_metadata import VersionMetadata

from release_v1.platform_certification_service import PlatformCertificationService


class ReleaseReportService:
    @staticmethod
    def generate():

        report = ReleaseReport(
            metadata=VersionMetadata.get_metadata(),
            certification=PlatformCertificationService.certify(),
        )

        return report.to_dict()
