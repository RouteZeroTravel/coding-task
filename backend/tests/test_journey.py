
import requests
from helper import HOST, PORT, TRAIN


def test_returns_journey_id():
    resp = _add_journey_resp(
        transport=TRAIN,
        distance_km=100,
        duration_hours=1.5
    )
    assert resp.status_code == 201
    data = resp.json()
    assert "id" in data


def test_unknown_transport_method_returns_400_status_code():
    resp = _add_journey_resp(
        transport="unknown",
        distance_km=100,
        duration_hours=1.5
    )
    assert resp.status_code == 400


def test_negative_distance_returns_400_status_code():
    resp = _add_journey_resp(
        transport=TRAIN,
        distance_km=-50,
        duration_hours=1.5
    )
    assert resp.status_code == 400


def test_negative_duration_returns_400_status_code():
    resp = _add_journey_resp(
        transport=TRAIN,
        distance_km=-50,
        duration_hours=-1.5
    )
    assert resp.status_code == 400


def _add_journey_resp(transport: str, distance_km: float, duration_hours: float) -> requests.Response:
    return requests.post(
        f"http://{HOST}:{PORT}/journey",
        json={
            "transport": transport,
            "distanceKm": distance_km,
            "durationHours": duration_hours
        }
    )


def add_journey_id(transport: str, distance_km: float, duration_hours: float) -> requests.Response:
    resp = _add_journey_resp(transport, distance_km, duration_hours)
    assert resp.status_code == 201
    data = resp.json()
    return data["id"]
