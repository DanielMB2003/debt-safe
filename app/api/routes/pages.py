from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.debt_service import compare_debt_scenarios
from app.models.debt import DebtInput

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "page_title": "Calculadora PRO de deuda",
            "results": None,
        },
    )


@router.post("/calculate", response_class=HTMLResponse)
def calculate_from_form(
    request: Request,
    balance: float = Form(...),
    annual_rate: float = Form(...),
    monthly_payment: float = Form(...),
    extra_payment: float = Form(0),
):
    payload = DebtInput(
        balance=balance,
        annual_rate=annual_rate,
        monthly_payment=monthly_payment,
        extra_payment=extra_payment,
    )
    results = compare_debt_scenarios(payload)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "page_title": "Calculadora PRO de deuda",
            "results": results,
            "form": payload.model_dump(),
        },
    )