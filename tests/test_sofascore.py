# -*- coding: utf-8 -*-
import pytest

import sofascore
from sofascore import Catecholamine, Condition


def test_version():
    assert sofascore.__version__ == "1.0.0"


@pytest.mark.parametrize(
    "condition,score",
    [
        (Condition(70, None, 150_000, 1.1, 1.1, 15, 450, False), 0),
        (
            Condition(
                50, Catecholamine("epinephrine", 0.5), 100_000, 3.3, 6.1, 7, 150, True
            ),
            16,
        ),
        (
            Condition(
                50, Catecholamine("dobutamine", 1), 90_000, 2.3, 4.1, 10, 250, False
            ),
            12,
        ),
    ],
)
def test_compute_score(condition, score):
    assert score == sofascore.compute(condition=condition)


@pytest.mark.parametrize(
    "map,catecholamine,score",
    [
        (50, Catecholamine("dopamine", 5), 2),
        (50, Catecholamine("dopamine", 10), 3),
        (50, Catecholamine("dopamine", 20), 4),
        (50, Catecholamine("dobutamine", 1), 2),
        (50, Catecholamine("epinephrine", 0.1), 3),
        (50, Catecholamine("epinephrine", 0.5), 4),
        (50, Catecholamine("norepinephrine", 0.1), 3),
        (50, Catecholamine("norepinephrine", 0.5), 4),
        (50, None, 1),
        (70, None, 0),
    ],
)
def test_compute_score_for_cardiovascular_system(map, catecholamine, score):
    assert score == sofascore.compute_score_for_cardiovascular_system(
        mean_arterial_pressure=map, catecholamine=catecholamine
    )


@pytest.mark.parametrize(
    "platelets,score",
    [
        (200_000, 0),
        (150_000, 0),
        (149_000, 1),
        (100_000, 1),
        (99_000, 2),
        (50_000, 2),
        (49_000, 3),
        (20_000, 3),
        (19_000, 4),
        (1_000, 4),
    ],
)
def test_compute_score_for_coagulation(platelets, score):
    assert score == sofascore.compute_score_for_coagulation(platelets_count=platelets)


@pytest.mark.parametrize(
    "creatinine,score",
    [
        (0.0, 0),
        (1.1, 0),
        (1.2, 1),
        (1.9, 1),
        (2.0, 2),
        (3.4, 2),
        (3.5, 3),
        (4.9, 3),
        (5.0, 4),
        (7.0, 4),
    ],
)
def test_compute_score_for_kidneys(creatinine, score):
    assert score == sofascore.compute_score_for_kidneys(creatinine_level=creatinine)


@pytest.mark.parametrize(
    "bilirubin,score",
    [
        (0.0, 0),
        (1.1, 0),
        (1.2, 1),
        (1.9, 1),
        (2.0, 2),
        (5.9, 2),
        (6.0, 3),
        (11.9, 3),
        (12.0, 4),
        (42.0, 4),
    ],
)
def test_compute_score_for_liver(bilirubin, score):
    assert score == sofascore.compute_score_for_liver(bilirubin_level=bilirubin)


@pytest.mark.parametrize(
    "coma_scale,score",
    [
        (15, 0),
        (14, 1),
        (13, 1),
        (12, 2),
        (11, 2),
        (10, 2),
        (9, 3),
        (8, 3),
        (7, 3),
        (6, 3),
        (5, 4),
        (4, 4),
        (3, 4),
        (2, 4),
        (1, 4),
        (0, 4),
    ],
)
def test_compute_score_for_nervous_system(coma_scale, score):
    assert score == sofascore.compute_score_for_nervous_system(
        glasgow_coma_scale=coma_scale
    )


@pytest.mark.parametrize(
    "pressure,ventilation,score",
    [
        (50, False, 2),
        (50, True, 4),
        (150, False, 2),
        (150, True, 3),
        (250, False, 2),
        (250, True, 2),
        (350, False, 1),
        (350, True, 1),
        (450, False, 0),
        (450, True, 0),
    ],
)
def test_compute_score_for_respiratory_system(pressure, ventilation, score):
    assert score == sofascore.compute_score_for_respiratory_system(
        partial_pressure_of_oxygen=pressure, is_mechanically_ventilated=ventilation
    )
