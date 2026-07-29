from fastapi import APIRouter

from portal.adapters.health_adapter import HealthAdapter

router = APIRouter()


@router.get("/health")
def health():

    return HealthAdapter.get_health()
