#!/usr/bin/env python3
"""
Utility to parse transcript text and extract structured fields according to the assignment rules.
"""
import re
import json

# NOTE: rule-based extraction; no external APIs

def extract_fields(transcript: str) -> dict:
    memo = {
        "account_id": "",
        "company_name": "",
        "business_hours": {
            "days": [],
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {
            "priority_order": [],
            "fallback": ""
        },
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {
            "timeout_seconds": "",
            "retry_attempts": "",
            "fallback_message": ""
        },
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }
    # simplistic pattern matches as example
    # ... implement according to rules
    return memo

if __name__ == '__main__':
    import sys
    text = sys.stdin.read()
    print(json.dumps(extract_fields(text), indent=2))