from fastapi import APIRouter
from app.models.debt import DebtInput
from app.services.debt_service import compare_debt_scenarios

router = APIRouter(prefix="/api/debt", tags=["debt"])


@router.post("/compare")
def compare_debt(data: DebtInput):
    return compare_debt_scenarios(data)