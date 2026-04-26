from app.core.debt_engine import simulate_debt, get_health_score, build_headline
from app.models.debt import DebtInput


def compare_debt_scenarios(data: DebtInput) -> dict:

    if not current["payoff_possible"]:
        headline = "Tu pago actual NO reduce tu deuda."
    else:
        headline = f"Podrías ahorrar {months_saved} meses y ${interest_saved:,.2f}."

    current = simulate_debt(
        balance=data.balance,
        annual_rate=data.annual_rate,
        monthly_payment=data.monthly_payment,
    )

    improved_payment = data.monthly_payment + data.extra_payment
    improved = simulate_debt(
        balance=data.balance,
        annual_rate=data.annual_rate,
        monthly_payment=improved_payment,
    )

    months_saved = 0
    if current["payoff_possible"] and improved["payoff_possible"]:
        months_saved = max(current["months"] - improved["months"], 0)

    interest_saved = max(current["total_interest"] - improved["total_interest"], 0.0)

    interest_ratio = 0.0
    if current["total_paid"] > 0:
        interest_ratio = current["total_interest"] / current["total_paid"]

    health_score = get_health_score(
        months=current["months"],
        interest_ratio=interest_ratio,
        payoff_possible=current["payoff_possible"],
    )

    headline = build_headline(
        months_saved=months_saved,
        interest_saved=interest_saved,
        payoff_possible=current["payoff_possible"],
    )

    if not current["payoff_possible"]:
        recommended_payment = current["monthly_interest_first_month"] + 1
        summary = (
            "Con tu pago actual, la deuda no baja realmente porque cubres solo intereses o menos. "
            "Necesitas aumentar el pago mensual para empezar a reducir capital."
        )
    else:
        recommended_payment = data.monthly_payment + max(data.extra_payment, 500)
        summary = (
            f"Con tu pago actual tardarías {current['months']} meses y pagarías "
            f"${current['total_interest']:,.2f} de intereses."
        )

    return {
        "current": current,
        "improved": improved,
        "months_saved": months_saved,
        "interest_saved": round(interest_saved, 2),
        "recommended_payment": round(recommended_payment, 2),
        "health_score": health_score,
        "headline": headline,
        "summary": summary,
    }

