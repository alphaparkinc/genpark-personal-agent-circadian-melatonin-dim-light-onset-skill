# Circadian Melatonin Dim Light Onset (DLMO) & Phase Shift Sentinel Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

DLMO (Dim Light Melatonin Onset) timing estimator, phase response curve (PRC), blue-blocker scheduling, and evening lux taper. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `predict_dim_light_melatonin_onset`: Predict DLMO clock time from habitual morning wake time and evening lux exposure.
- `generate_phase_advance_delay_light_protocol`: Synthesize lux timing protocol to phase advance or phase delay circadian clock for jet lag or shift work.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_circadian_melatonin_dim_light_onset_skill.server --test
```
