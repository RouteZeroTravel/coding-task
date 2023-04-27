
import pytest
import requests

from helper import BUSINESS_FLIGHT, ECONOMY_FLIGHT, EPSILON, HOST, PORT, TRAIN


def test_train_emissions_50km():
    assert _carbon_emissions_kgco2(TRAIN, distance_km=50) == pytest.approx(1.7745, EPSILON)


def test_train_emissions_100km():
    assert _carbon_emissions_kgco2(TRAIN, distance_km=100) == pytest.approx(3.549, EPSILON)


def test_economy_flight_short_haul_450km():
    assert _carbon_emissions_kgco2(ECONOMY_FLIGHT, distance_km=450) == pytest.approx(67.959, EPSILON)


def test_economy_flight_long_haul_4000km():
    assert _carbon_emissions_kgco2(ECONOMY_FLIGHT, distance_km=4000) == pytest.approx(591.48, EPSILON)


def test_business_flight_short_haul_450km():
    assert _carbon_emissions_kgco2(BUSINESS_FLIGHT, distance_km=450) == pytest.approx(101.934, EPSILON)


def test_business_flight_long_haul_4000km():
    assert _carbon_emissions_kgco2(BUSINESS_FLIGHT, distance_km=4000) == pytest.approx(1715.28, EPSILON)


def test_unknown_transport_method_returns_400_status_code():
    resp = _carbon_emissions_resp("unknown", 100)
    assert resp.status_code == 400


def test_negative_distance_returns_400_status_code():
    resp = _carbon_emissions_resp(TRAIN, -50)
    assert resp.status_code == 400


def _carbon_emissions_resp(transport: str, distance_km: float) -> requests.Response:
    return requests.get(f"http://{HOST}:{PORT}/carbon-emissions/{transport}/{distance_km}")


def _carbon_emissions_kgco2(transport: str, distance_km: float) -> float:
    resp = _carbon_emissions_resp(transport, distance_km)
    assert resp.status_code == 200
    data = resp.json()
    return data["emissionsKgCO2"]
