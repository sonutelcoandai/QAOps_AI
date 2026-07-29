from fastapi import APIRouter

from portal.adapters.command_center_adapter import CommandCenterAdapter

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return CommandCenterAdapter.get_dashboard()
