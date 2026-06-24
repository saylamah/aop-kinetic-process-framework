from aop_framework.treatment_train import (
    classify_scavenging_capacity,
    screen_aop_readiness,
)


def test_classify_scavenging_capacity_low():
    assert classify_scavenging_capacity(5.0e3) == "low"


def test_classify_scavenging_capacity_moderate():
    assert classify_scavenging_capacity(5.0e4) == "moderate"


def test_classify_scavenging_capacity_high():
    assert classify_scavenging_capacity(2.0e5) == "high"


def test_classify_scavenging_capacity_very_high():
    assert classify_scavenging_capacity(8.0e5) == "very_high"


def test_screen_aop_readiness_favorable():
    result = screen_aop_readiness(
        k_scav_s=5.0e3,
        doc_mg_C_L=1.0,
        turbidity_NTU=2.0,
        nitrite_mg_L=0.05,
        target="micropollutants",
    )

    assert result.classification == "favorable"
    assert result.main_limitation == "none dominant at screening level"


def test_screen_aop_readiness_challenging():
    result = screen_aop_readiness(
        k_scav_s=2.0e5,
        doc_mg_C_L=4.0,
        turbidity_NTU=3.0,
        nitrite_mg_L=0.1,
        target="micropollutants",
    )

    assert result.classification == "challenging"
    assert "matrix radical scavenging" in result.main_limitation


def test_screen_aop_readiness_severe():
    result = screen_aop_readiness(
        k_scav_s=8.0e5,
        doc_mg_C_L=8.0,
        turbidity_NTU=15.0,
        nitrite_mg_L=2.0,
        target="micropollutants",
    )

    assert result.classification == "severe"
    assert "high DOC" in result.main_limitation
    assert "high turbidity or optical attenuation" in result.main_limitation
    assert "nitrite scavenging" in result.main_limitation
