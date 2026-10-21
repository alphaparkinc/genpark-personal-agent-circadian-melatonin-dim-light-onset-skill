# -*- coding: utf-8 -*-
"""Circadian Melatonin Dim Light Onset (DLMO) Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class CircadianMelatoninDimLightOnsetSentinel:
    @staticmethod
    def predict_dim_light_melatonin_onset(wake_up_hour_decimal: float, evening_lux_average: float = 80.0) -> Dict[str, Any]:
        # Typically DLMO occurs ~14 hours after habitual morning spontaneous awakening
        base_dlmo = (wake_up_hour_decimal + 14.0) % 24.0
        # High evening lux delays DLMO (melatonin suppression)
        delay_minutes = min(120.0, (max(0.0, evening_lux_average - 30.0) / 10.0) * 15.0)
        adjusted_dlmo = (base_dlmo + (delay_minutes / 60.0)) % 24.0
        
        h = int(adjusted_dlmo)
        m = int((adjusted_dlmo - h) * 60)
        time_str = f"{h:02d}:{m:02d}"
        
        return {
            "wake_up_time": f"{int(wake_up_hour_decimal):02d}:{int((wake_up_hour_decimal%1)*60):02d}",
            "evening_lux": evening_lux_average,
            "estimated_dlmo": time_str,
            "melatonin_suppression_delay_min": round(delay_minutes, 1),
            "biological_sleep_gate": f"{(h+2)%24:02d}:{m:02d}",
            "lighting_curfew": "Dim ambient lighting to < 10 lux 2 hours prior to DLMO."
        }

    @staticmethod
    def generate_phase_advance_delay_light_protocol(target_shift_hours: float, direction: str) -> Dict[str, Any]:
        if direction == "advance":
            interventions = ["10,000 lux light box for 30 min immediately upon waking", "Strict amber blue-blocking glasses starting at 20:00", "0.5mg low-dose micro-melatonin 5 hours before desired sleep"]
        else:
            interventions = ["High lux bright light exposure in late evening (19:00-21:00)", "Dark sunglasses in morning to prevent early phase advance", "Shift dinner 2 hours later"]
        return {"shift_hours": target_shift_hours, "direction": direction, "circadian_re_entrainment_plan": interventions, "adjustment_velocity": "Approx 1.0 to 1.5 hours per calendar day"}
