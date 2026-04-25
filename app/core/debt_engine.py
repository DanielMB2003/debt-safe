from app.core.formatters import round_money


MAX_MONTHS = 1200


def simulate_debt(balance: float, annual_rate: float, monthly_payment: float) -> dict:
    monthly_rate = annual_rate / 100 / 12
    current_balance = balance
    total_paid = 0.0
    months = 0
    first_month_interest = current_balance * monthly_rate

    if monthly_payment <= 0:
        return {
            "months": 0,
            "total_paid": 0.0,
            "total_interest": 0.0,
            "payoff_possible": False,
            "ending_balance": round_money(balance),
            "monthly_interest_first_month": round_money(first_month_interest),
        }
    if monthly_rate > 0 and monthly_payment <= first_month_interest:
        return {
            "months": 0,
            "total_paid": 0.0,
            "total_interest": 0.0,
            "payoff_possible": False,
            "ending_balance": round_money(balance),
            "monthly_interest_first_month": round_money(first_month_interest),
        }

    while current_balance > 0 and months < MAX_MONTHS:
        interest = current_balance * monthly_rate
        payment_this_month = min(monthly_payment, current_balance + interest)
        current_balance = current_balance + interest - payment_this_month
        total_paid += payment_this_month
        months += 1

    total_interest = max(total_paid - balance, 0.0)

    return {
        "months": months if current_balance <= 0 else 0,
        "total_paid": round_money(total_paid),
        "total_interest": round_money(total_interest),
        "payoff_possible": current_balance <= 0,
        "ending_balance": round_money(max(current_balance, 0.0)),
        "monthly_interest_first_month": round_money(first_month_interest),
    }
def get_health_score(months: int, interest_ratio: float, payoff_possible: bool) -> str:
    if not payoff_possible:
        return "critical"
    if months <= 12 and interest_ratio < 0.15:
        return "strong"
    if months <= 36 and interest_ratio < 0.45:
        return "fair"
    return "warning"


def build_headline(months_saved: int, interest_saved: float, payoff_possible: bool) -> str:
    if not payoff_possible:
        return "Tu pago actual no alcanza para liquidar la deuda."
    if months_saved <= 0 and interest_saved <= 0:
        return "Tu escenario actual ya está optimizado o el pago extra es muy pequeño."
    return f"Podrías ahorrar {months_saved} meses y ${interest_saved:,.2f} en intereses."
