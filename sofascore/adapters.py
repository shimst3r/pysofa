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

import sofascore

class Adapter(Protocol):
    def compute_sofa_score(self, condition: sofascore.Condition) -> int:
        """Computes the SOFA score based on the patient's condition."""

    def condition(self, patient_id, timestamp) -> sofascore.Condition:
        """Determine the condition for a patient at a given timestamp."""

class MimicExtract(Adapter):
    """
    An adapter for the MIMIC Extract dataset based on:
        https://arxiv.org/abs/1907.08322
    """
