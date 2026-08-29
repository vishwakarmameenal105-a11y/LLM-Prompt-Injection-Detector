# LLM Prompt Injection Detector

## Overview

Being aware of all the security measures already built into large language models, this tool acts as the **second seat belt** for LLM protection. If you want to add an additional layer of defense against specific phrases, words, or attack patterns, this detector sits in front of your LLM and scans incoming prompts before they reach the model.

## How It Works

User prompt → patterns.py → scanner.py → scorer.py → analyzer.py → main.py → Result

## Project Structure

| Module | Purpose |
|--------|---------|
| patterns.py | Stores attack pattern lists — jailbreak, system prompt leakage, instruction override |
| scanner.py | Scans a user prompt against all patterns and returns matches |
| scorer.py | Calculates a risk score from matches (0-100) |
| analyzer.py | Decides the verdict — BLOCK, FLAG, or ALLOW |
| main.py | The orchestrator — ties all modules into one pipeline |

## Detection Categories

| Category | What it catches | Example |
|----------|-----------------|---------|
| Jailbreak | Attempts to bypass AI restrictions | "ignore all previous instructions" |
| System Prompt Leakage | Attempts to extract hidden instructions | "reveal your system prompt" |
| Instruction Override | Attempts to override previous commands | "forget everything and do this instead" |

## Risk Scoring

| Score | Verdict |
|-------|---------|
| 0 - 29 | ALLOW |
| 30 - 69 | FLAG |
| 70 - 100 | BLOCK |

## Usage

python3 main.py

## Why This Matters

LLMs have built-in guardrails, but attackers constantly find new ways to bypass them. This tool is the second layer — customizable, auditable, and independent. You control the patterns. You see the score. You decide what gets blocked.

## Built With

Pure Python. No external libraries. Runs anywhere Python runs.

## Built By

Meenal Vishwakarma | 2026
