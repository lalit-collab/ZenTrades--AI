#!/usr/bin/env python3
"""
Builds prompts for agent specification or other pipeline components.
"""
import json

def make_agent_spec_prompt(memo: dict, version: str) -> dict:
    # build JSON structure for agent spec according to rules
    spec = {
        "agent_name": memo.get("company_name", "") + " Support Agent",
        "voice_style": "professional and friendly",
        "version": version,
        "key_variables": {
            "timezone": memo["business_hours"]["timezone"],
            "business_hours": memo["business_hours"],
            "office_address": memo.get("office_address", "")
        },
        "system_prompt": "",
        "call_transfer_protocol": "",
        "transfer_failure_protocol": "",
        "tool_invocation_placeholders": []
    }
    # fill protocol sections
    return spec

if __name__ == '__main__':
    import sys
    memo = json.load(sys.stdin)
    version = sys.argv[1] if len(sys.argv) > 1 else "v1"
    print(json.dumps(make_agent_spec_prompt(memo, version), indent=2))