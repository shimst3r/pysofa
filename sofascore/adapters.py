# -*- coding: utf-8 -*-
"""
Copyright 2021 shimst3r

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

adapters.py contains a number of adapters for common datasets used in the
healthcare context.
"""

from typing import Protocol

import pandas as pd

import sofascore


class Adapter(Protocol):
    def compute_sofa_score(self, patient_id, time) -> int:
        """Computes the SOFA score based on the patient's condition."""
        condition = self._condition(patient_id, time)

        return sofascore.compute(condition)

    def _condition(self, patient_id, time) -> sofascore.Condition:
        """Determine the condition for a patient at a given time."""


class MimicExtract(Adapter):
    """
    An adapter for the MIMIC Extract dataset based on:
        https://arxiv.org/abs/1907.08322

    Attention: The MIMIC Extract dataset does not contain all data needed to
    compute the SOFA score (i.e. it is missing dosage information of
    catecholamines. Therefore the score computed by MimicExtract has to be
    understood as a lower bound!
    """

    def __init__(self, hdf_path: str):
        """
        :param str hdf_path: Path to MIMIC Express' HDF5 file
        """
        self.vent = pd.read_hdf(hdf_path, "interventions").loc[:, ["vent"]]
        self.vitals_labs = pd.read_hdf(hdf_path, "vitals_labs_mean").loc[
            :,
            [
                "systolic blood pressure",
                "diastolic blood pressure",
                "platelets",
                "creatinine",
                "bilirubin",
                "glascow coma scale total",
                "partial pressure of oxygen",
            ],
        ]

    def _condition(self, patient_id, time) -> sofascore.Condition:
        """
        Determine the condition for a patient at a given hour.

        :param str patient_id: Patient ID
        :param int time: Hours into the ICU stay
        :return: The patient's condition
        :rtype: sofascore.Condition
        """
        systolic_bp, diastolic_bp, *tail = self.vitals_labs.loc[patient_id].values[time]
        mean_arterial_pressure = systolic_bp + 2 / 3 * diastolic_bp
        is_mechanically_ventilated = self.vent.loc[patient_id].values[time][0]
        tail[0] *= 1000

        return sofascore.Condition(  # type: ignore
            mean_arterial_pressure, None, *tail, is_mechanically_ventilated
        )
