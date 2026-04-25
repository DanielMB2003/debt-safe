from pydantic import BaseModel, Field

class DebtInput(BaseModel):
    balance: float = Field(gt=0, description="Current debt balance")
    annual_rate: float = Field(ge=0, le=300, description="Annual interest rate in percent")
    monthly_payment: float = Field(gt=0, description="Current monthly payment")
    extra_payment: float = Field(default=0, ge=0, description="Optional extra monthly payment")


class DebtScenario(BaseModel):
    months: int
    total_paid: float
    total_interest: float
    payoff_possible: bool
    ending_balance: float
    monthly_interest_first_month: float


class DebtComparison(BaseModel):
    current: DebtScenario
    improved: DebtScenario
    months_saved: int
    interest_saved: float
    recommended_payment: float
    health_score: str
    headline: str
    summary: str