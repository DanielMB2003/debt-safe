from app.core.debt_engine import simulate_debt


def test_debt_is_payable():
    result = simulate_debt(balance=10000, annual_rate=24, monthly_payment=1000)
    assert result["payoff_possible"] is True
    assert result["months"] > 0
    assert result["total_interest"] >= 0


def test_debt_not_payable_when_payment_is_too_low():
    result = simulate_debt(balance=10000, annual_rate=120, monthly_payment=100)
    assert result["payoff_possible"] is False