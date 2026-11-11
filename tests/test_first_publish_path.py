"""A brand-new agent's first publish: the submit tool and the approval job do every step the checks demand."""
import re
from pathlib import Path

import pytest

import rapp_sdk
from tools.stamp_ticket import stamp_source, strip_ticket

ROOT = Path(__file__).resolve().parent.parent
AGENT = {"name": "@someone/brand_new_agent", "_file": "agents/@someone/brand_new_agent.py"}
BODY = '"""A brand-new agent."""\nfrom agents.basic_agent import BasicAgent\n\n\nclass New(BasicAgent):\n    pass\n'


@pytest.mark.parametrize("head", ["", "#!/usr/bin/env python3\n", "# -*- coding: utf-8 -*-\n",
                                  "#!/usr/bin/env python3\n# coding=utf-8\n"])
def test_the_submit_tool_adds_exactly_the_header_the_catalog_checks_for(head):
    code = head + BODY
    stamped = rapp_sdk.with_ticket(code, AGENT["name"], AGENT["_file"])
    assert stamped.encode() == stamp_source(code.encode(), AGENT)
    assert strip_ticket(stamped.encode(), AGENT) == code.encode()
    assert rapp_sdk.with_ticket(stamped, AGENT["name"], AGENT["_file"]) == stamped


def test_windows_line_endings_get_the_same_header():
    code = BODY.replace("\n", "\r\n")
    assert rapp_sdk.with_ticket(code, AGENT["name"], AGENT["_file"]).encode() == stamp_source(code.encode(), AGENT)


@pytest.mark.parametrize("workflow", ["approve-agent.yml", "approve-agent-batch.yml"])
def test_approval_commits_the_page_it_builds(workflow):
    text = (ROOT / ".github" / "workflows" / workflow).read_text()
    first_add = re.search(r"git add agents/[^\n]*", text).group(0)
    assert " a/ " in first_add + " ", "the agent's page under a/ is built at approval and must be committed with it"

