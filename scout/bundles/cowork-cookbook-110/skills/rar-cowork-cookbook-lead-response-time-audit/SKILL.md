---
name: "rar-cowork-cookbook-lead-response-time-audit"
description: "Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_response_time_audit", "rar_sha256": "7a09c5fa30021f3131695f8ed14499eb11e2279148e40c9f17beaa9a0bf3c9d0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/lead_response_time_audit`. The original RAPP
agent is preserved byte-for-byte in `lead_response_time_audit_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_response_time_audit_agent.py` and embedded as the fenced Python below (sha256 7a09c5fa30021f31…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_response_time_audit_agent.py` first:

```bash
python3 lead_response_time_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_response_time_audit_agent.py   # or on stdin
python3 lead_response_time_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_response_time_audit',
    "version": '2.0.1',
    "display_name": 'Lead Response Time Audit',
    "description": 'Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'lead-response-time-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-response-time-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cbb47434cf8126e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-response-time-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LeadResponseTimeAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadResponseTimeAudit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(LeadResponseTimeAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66bLbRprlq3Bu/7DdlESsXFRREQOCJECQAIl9sRwy9n3f4fG7T4LkleyuclV3xEQMFFckgMxvz3O+BPjbm9k2QV69fX4TXTNbUGaShIFbLczMWZB5n1cx+MhjC/wt7DxrqtBqm7yq3z68OW5tV2HRhHkGprOuWbeVWy+CvF8keeYvEtd06kVvhs3Ccr28chd1nrp55i68sKqbxSy8XjSBm354qAtCP0jAX/O4+JreBGazMOe5TZgkizpsmhDIbrMmb+3AdT4BQ9zBTIvErd8+//zLh7cQfH/7/NubnZg1uPR2BXIEty7yrHalMHWJ1gkbMCsxMx/cLkbgfwbOC7cCRqbgkuN6i9fZj7WbeB8W//mfcW9Wfv3T5y/Z4nV8eZv/CW32sLbJzbpxnYVtFqYVJmEzfloQSW+O9aJym7bK6oUJfKiA8Z+eM79LyovF3+d7Pz6VfPLd5scvbzkwwZyD++Xtp0VeAX1VO3//NEspfvzpU5L3bvXjT9/l1K0VuXYzCwNWf/r6On+JBQO/Dw29h9a/A6nPNFrul7c/ODcfT7tnP8HMt09RHmY/PgUXVd65mZnZ7o8//ZVYkBw7TsK6+W/J/fkpOAC5Aj69DP/pwyPIvyyWL4e+yfxrtQVI6//EEzD8Xd2HxStQfyX7Ef//IjoJM1Dz7xH/p+L+2YTl3xc//6Vv/2rCh4X35e3gJmEHqsNK3M+L376K9yP58w/O94s//PI7EP1vxYh5W9kPCV9TMws9t26+fv35h/px+Ydffv6hLUCtuWb6ta2Sfybzn8X1oedPEXyN+vHPc4F+OYuzvM8W3yp98Vte/K/q908LxUxC5/v1+vPij+tlPpaL2Yl3pc8Q/GHN1MDWP8Txp7ffATBkwJvWftwGq/w//mPBhnaV17nXLEQ7b5sFSHADEGI2XgrCehE+kahyQVzrEAT2NQ7U/5zh2eLcW/z6v+0HUH60X0C5mqHra/XCnK+zyK/mjDq/flpIQF5ehX6YmclCIO73L5npu1kz6yrAFLfqAIpYY+N+BPjzcf6yCLPFr38l8utj9qdi/PWBoeETjQTyPCNR3Sbup9kbNXCzl+02QHl3cO0WCE5yG1jhhQA7PwAv6zzpAJLNntfxjLZOWAE382p8yAbR+TwL+/XXXy2zDr5kT+hEF08aqFdgwDdzFh8/Ane8B55/yVw7yBc//Pb7D4v/s/hXsx7CZx13gN2v2AMLGfHGARLw2xQMA2kBiQTheMT+t99fQQViMsBbIFOhF7ovCgmz2HXeIyzSxEcEX7+TEeCJvHqQSdh8Wpy9xTd7gdL51ozYQQ6IynELN3PczB4fdPQl+xbJLG8WNSi42hs/LNrafWj91arMh4kpWNRm8+uCJe+AH/IE/Deb+RgEJudZCML/Lf/P60BI9UO92L+L+LTg5upbFGZlFkFlvnR45jMvgBfepwPh5iJz+y/ZzIDuHKrHUniGBwwCkbFfKf045xzweQrWvVO/636MMWcWkx5sVn0BtfYs85mBwUQA+0Cp34bODP5/e5VUHeRt4jziByydJb2y4Lyy8qjBmYcX70S8mJl48aDixZcWgWBs8f+rgZhtIyhKOFKEdDwsjpwk6M+Yzf3OHNtniwQofQGMeK6P7zT/DhLvWPklS0JQANX4t+fIR6RfY574A5wEgSCEh3yQZhCzWe6jCueqqqq5fs0v2TsoA+8WDwQCiQBLFpT0XEnvCue775YGYF3O598J+pG1ypnjAyptUbRWAqrAc13HMu0YWFXNaXmlIJtjC1ZVH4R28CevFkA6yDyQvwBGhCDCALgfoeNy4CYIqFfl6ffh4dz2ACuc1gbWgobS/bRQ50yAgqhBNkHvMo8BUfjhIWqRuiDGwMRvEa4Ds3gaM/egLwPNGYtDt/9j/F+3vhfvw5LZeCDTdMwGRLKfQdRxh2dev1n5yhQQms7L7THpz8l+ebr4I3f87Uv2sPAbboNVnMy0+4fQLMDqSetHVc4gNBc1qPenc3MZzwz76UmSTxb+Zsvnf2i7f/yfdeYP2pP/nLfPi6BpivrzavWkqnem+gQgYAUqJCzc+sFaH98p5uNMMR8fFPMnec/wfF78z2z6k4hXKX9ewJ+gT9B86xra7lyrrwOEgPy41z9i890vmeB+zy1Qn6cA1uaQj4Amv7HI+xBAJX7l+vPgJ6vUMxn1gP8eMAqi/yX7lv/X2gAonfkzBdb5H9bsg05BNp/J+ob24FbWAN3O3Gz57rz/SGbza/ftc9YmyYe3zEzdf7HvmJEcVCYIwrxLAWsE9CxN6D7OgDPgRmjO3/+8vbo9vpjJs4LrBlhnVg8ceK0I038wxoe5Yc0Ahsybgxn8ntAOtjRmmzSztc1YzOY99yJzX/StafpHrY8lC3Q4+ed55X5YzA3uh8W3XvXD4n338NiHZS3YPv0898mzn2Ao+Pg29tuO0XLffvknZrza5r8wIpxRY8aZp7uu8x0SHtkqzAYgnyxcgUm5/WgUZnKsxweJ/qPbQGHlli1gQ2c2+XsMvpuWP+35/eFK89wb/vb2Diqv5L36QDAcrN6P9cyHK1DXQCE4f1YguPff7hBf8wD4gU4FTNyY0M7GPROFIAT2UBiF1zvc27oOjGG7nWvBsIsgmx2MbV0MsncevLFc09yZkOWh9s6Z7XjW79eZ7MPZFhfyXHQHI7aDrhEcx3bwBjF3joltTNOBttsNtPEcwA/fp8YAO18OPh2ao/etWZ0D8fLztzdrjYGRNFafiedBrnaKucY21hBoy2rt6my0jCVRujjNCMVWc4KLljO3eyS6atKZ888TQ9iie0tEyqSaS9+e6uCAE9nE3NGbRoYi1hQMtL6cMZsXjaXFttom431lz9IAYdm8DcT1VSM6RE2x023dSKp18ryuNO6CY8NQkYMuALmS3cjZba9ZrDNghl4ReZKSaySv/ZMKpcllo1fwVUlh2agLbMouTnfeidbBwxV8fcY1CsYGKbWrVFXYcV2K+QnNFOWYUThF5TvaiEdXO0Grm5bstqOIu911s72mYmdLfbGNq/h2arQUujJmvSKIOmAmgXG3SZDujpPZLgtRgap+I4ZS7TLlahu0GpuwSxLVZdJWmDN/mUKMc0V8yvnBUHWtNnmNFOM0989L5M6APY3YnIcGuxSqKvBjxnAyrgka61RavuTgoVvTbRFWdoijcZjuGSZXruLER/f1FEqkUjOxrW9b3riH9bAv6x1TbNXLRtJHRJNi3STrXSxaPn8Edpsbmiw2skwsS5pKwhYO2FFQCNB8OPx5yUEXJqbh6zJx4CqlDwfGOtG5v+JySVdiEl2bgVBxmx7KziQ0VOqNDJeJetXgKN5pfZtHiYsN1Z64n1ldQrOTMHX5/bg63ZCODqImo4KDzXe0ejmh0a1LeiTIr2Lj3oVcn7pQd6gdGKPvAjhnlyqpyUpQaxMlLCUBY6eNQcb2Sr0ENE+pt25iXSrm5c0VG30cUgbaZVdcFicuu3YxImc2QnpZiXBshVrUhqV892nO2pSqWu05xVDWrLHN8PQQTrnC1AZ6oBG+2DF9qK8Nm2axcrhRrDyMyKhk3JULOmwdcL2VNX4D3TeYhtZ3hmXyqw11yH55c6dht+LolBkcEpRLrSmDYWhxIu6MFeWuZYmpG2bqRi1cb2TR3OU2Zd/zmpsO7oZiRSir8q1VXn1TPNgrjY93QZQYeRwFsUDVEXKw7mGf67F+TKsYS8YLHLT9wef0PKRxQRiOG2PSwyN5EAiDbQ97vpav29bQVfsW6rdCs1e4ku7h1VmFh21vDXs/2MbmeSRCgbWvOq1JZb5h7zl72KyyuHSMbPBcnkF7tZw0PIBdJ19ZOx+uuGil59hSRVzc3mneBR6WackeL7sAQ5E4XPfp2jYkLsergzwpN/98YbxQy1o6asopj3e3zjWFa6wIgiLzKziWk/WFZi86frp0WbAcqhYH6OUigc1E1Xp3ZVcCXmR8vtSi0j4yO/OEFJxcKSw3TSs1OxNXITAou5YA82+GgdrxWO2YfRgKI7cUbbajnFIm4lZmYv+8O2wwn8E7WmO7o5tt/CbbHLXIxOjN2dNOl7Psp1mFrgnGpXdlIvlVATCH7rdsA9YCwfO1COdnxV+Lcu/wAY9OlN6b6JmDkiFNUsMexz7RjqOindQg7LeSmh7cIe9gXzS2W2+Ey1qDaspChekCh211nO4BlmFLMmtrdnMZFCHoPAJbNTyMrWJ7U3IGsiEnlj6gKFb5u/1WPBinkNclCu5GP7AbRz0FO3XvmOdAQZnzdsxGBhoYsPHcoFJ22seBS2Wmpfp316Y3Nzpb0fY5ZdCLcI50YNIqX3M3lZM25/RoLy93ru6wE0wE2KVnxpV8CunhipG7aVdSh8uu7o7c2Y5wrKBtHBUli/FpC6vpzNvu7zwCqFG5RBlZXe4mxSuSOfEEUZLl2iywyI+JqzX2ZRQpDaVi3JkWmghUu4L4tLK6DtFEp/bJo2yDgVYuWiy37lXZG6fjSQFS/COzGhIlT+jBgRTXOm/zw8GXSAlFl1sWpfI9jExMfeqnMz/hd6yLAm3Al8tob6w8belvl0d7ENALFfqwMWyVIdWIvbGPBhHCbnqVpck+JwPtgmcyZe5rWx99SnbbHYFpvlmfXIza+oXSaMZJOC8vW8HEj/UxM+Hy0Bwof1MjQWUbDX9XmJPsxoPBU3f8eivTUxxrGwuRrbOORqbmc8ql6vRpyaEsceCXKdxT5tIilI5L8MoMTiGVZfcUqiOBYkqQj7svwRBC2mqndJEU2FCwl8RR67gSKwQ8cyCWjNI6l5RtNBiMzS3ZoxOWiI6zI7IPzFBHsNNyK8ZKwrln2EX1ES/VqJDBjlWMrOiAZFunrswC6ZOj3nluvlkfLoJBCPBuewN8vfVUw5wu5x6+l5ZmVKuw3BYbQCdZK/OJcjmliFsGVSmFF24nUhuyLXVEZ1DupK51XesLoojZMOuuAbXGlJElXRuimCAeVsuNH4Bm4Cgyw0UrOJ84W/ABFS66oYi3DZldXQbKKMi+9wrh07g88lCGl/n5RE4Wythru5NLQmZpeaeMrbAbQFM3thgRBNqNyFNZuJ/cdWBg/Wk/Le3BtOJztuvZ5K7F+n51927lWbsyoAwiIVmmAZ23ptoOZeDX0H1fqqYU4pkOUTmd90UP325tuVH0fd+KyPUknejmFrFoPh47clmn1zvEOylRoKHSa/wuPhfN/kbFkXbEbDL0TRDuky+LhkDJkiSck27PH6Me6i1T6vHNmt81pBrT64xe42g4jHyaBSu8567XmzxoBINHW+hUIbfYrOQE0QzZcG5KliPo0u40i+tsijxdZWgkYKgxsX1Ac1DbFEWJqtxuitaDpgqb1N201ik06ESUKofuRPhg9bXH8zSCRcRJP0uCTtBHt0VQ01DhI2NSNe9cw16i4711kD2pxG0ZbyQm8v17ANkFgu7FqqjFiaTLfc4NEm0kohBDcaHyEA5JA6BRBHSlAGnvMoRPZEDiCbwk7MQUSe7Ch2SqlZtlFItJSpyvIIITQ+/k3IC2fLzRTtsztzyG+xtE9vz15Gld2Y9EKcY2RxTZOkwaY7hKwVnSCdSTY7IrGx1hJNGJ6g4y0PPWPPREDQU6FqRQcLDy3eTZLUK7GKr77XQnjkk5cJF1P2k5znNseEFgV6aFq4hYaI/p9/tFWF4iuqD6wBJxJtHSfcqej71qSck1Vw03N6Vzq9i26LPVGu0TFIKHWrkFMJ4qSaxHjR/QKIBBbnlWCu/A7eGEg63spDEYugtFJT1bVL/JmCM8DZVdF+0+RWUYcz0EXQvFxujPh9224CsWY0Z9SJdFdOnS6ILzPh8OmZsSukuOZng2eqyhtjhEW8s9oodlyidM6kfGuh5NxIY30rXZIxp96apky4XKqrJs+UD4WafbcDMeE4r2aefsjufINJKVkIk+38DLgybmK9DaBCKDnTvH2Z31PVFmqnOo9sEFsfwhAx166w8b3g3CU0EmF7Exsp0b2u0w+T1esFDTC14Z9cvwMibUJYoKlOAPMtPRA8mQVgv5xn2lurroSGQq09MeGcNhGo8I0evqlZcjOWEPqmCdriS3NlhjdaAuElFd+S7OyqzJ8q4OjrorivWlQXRSZ9eHdW1ZJO7XCiWvHclvO5+MLtpdF/HRuY2l2baWsByXhM7lx253oo/6PVWhaJukLiyI7CbPKIMcdlKqRKvbxa198sK6rpuN8jYbiFjbnnvqNBz2pR/viSIhd014uifnkwez+Yq8C4BRSPM8CBFfby4xIpckgNiwVJbkUOypNrKpAvSeWVFhTK/YoH2vieIga8fbVrxvhL71vAF3m+CGVIwS5DB26t2zNDmbbTQd0kBfQjlmxPtB2JqyqsMTK1ABFlCg+k+enwZ8doh9LrFVRJa4+4W+W9yxi87S1slbik95mDvUmWY4vE+S+E4gupEutrbllPTNaN3OsD1+Ym1qO7mVOjlTI0W8saHyTS3uINCgei2jxtyAJGg72Z4pb9pq015Gb3OeQKgc64KCSs7q4FQXqJBM3K2VFSQh1H0Q7Zt7RMuRabP3i5TFa5LuJ6tBtxpkxNly19zUPdHIscfDtoWwxsm0KD/01nKZrrYdFJc9VWqyP+CEM60tOcn9y+kAB0GKr5wY9MSW1bsshhlTKWQEx1elC9EVfkP3MdLUGT4CpgZI1nTwtrgJ5UpZLb04Wx21IWmp2ElWqyO9s6gbyeJhha0HdM1yKEmEJVttVVctYQa7AwF+E2tFqV5AOaar9Lhn4mNnVt65OxedQlnq7Rw08Y7Y5hJL9Xx2dtIpYwYoCo/uxGanWE+FI1IqyE4RNsiRRg86cQ0ieWxlzJpOmc7kej12x4msMBVe9xTMFdpK6z06q1ysgzYQvUITzT8MSa7tsJCoxwGZjIMV76dkbQ7F6XDNqkuFGwdkw8tqh4q9dpcUwWluEpxEOXLnIA8aq622giNcjfakcipLi5TAoiz5e72CkNstq6YW70o99QukhQlVSXY3k3AoOaw3FFyvrqN6SZBscvf55JShyqFOqw4NOpImdiWao5fuSEav45UOi4W/IXSREjlBWgrn69FBaXpVuDDBU1wQrdnMijmYB5WXi6G/R/sB1uDilpGtXgYRP7RrdH8xjny5OlUALo6trd8Ie0TFAhNllTmj2trT0A7NWVoXIvOAC7ZeCGHnrU06Y9XDfl+Z3WVDhFO9tQ51i1VBN8D8PcpgcgjR1ZhjIhKudWfdISsTM6y6alIeDR1ugvx8aCdOvzbNDQFd600sVYW4outA9zcRetk2gSPACHBIukVOrRxG+oaDntxfNlpNW6IMW55/XS7Pbe5ohJYFGw81gnI0yQFJDyPRmnvUopm8LupDZa0344rZc7pb6Cf3us8Nk52IgwDbjoBs1f1usgl434vSLssPnrXHsoAQxDsmdJBW3KiRzZg1cdvb5VgWK4ka9pq7y3VrSXD2cnUgSezs0W63PKQHgabaVYxW3c1bkdlK2/YTtro3VXa/HLR7a8DRkCqOtk11vIosI2bKmq7bod8wWhOXzaVF9bu3NG5cfVx1Jh5xXdmqS0mLWPdyYwnN9S+eTEXGxHVOFMlUB3oWtkjGyYeukrNhVxKTUkRxs+Gbdoqm7VLMI/m4M1RbvkVQxdXCwE7loJtrKx3OnXrIYkGgG3tfCZUJ+/f80GMJbwRCvzuXB60fcO/WXEd816UwfYVhkJ8WV+/85QSIzDOWm9tVPqpTsGXjsB352Msjx77xhCoB1sTli6Sf9S6Hr4myYpqwKNybxJ3jgd8mV3Mn+naBKil8YKsxCwpA3AOennPXv253F1/Frtzu2nv4aDY0zQRtiy3lYSJRr4JOh24tVw1Ci/utt72FDmRKo4oKUpIN/KXMVqN0MWkcrYQeH5BbRoBdwGmqD1NOQiPLsDBHclERQGp/6uNiOwajELErBPfZA8rc+GBFHbwEbAGJLEe3B1zF7xuULQiC+Pvbh7f54errgfa/fQU9PzH8f/bg8vmM8f011uOxMtD/+aHr87835ZcPb5UdAkOeD2PrpPVfjzD/y6PYj3/12mOeNT7f4s5v14bm/fl+Y/rzT43ewsxp66Yav9Z50j4eAn94s9p6/v1DPf9Exgafbw8n0mKW9i4VXKgL126+NvnXss0b923+bcL8wsh1QvPbqf96IP3hzRlBBkK7/oqu8a+1Of/SCbj3eo0CvEI+QZ/gt9//L2gFi2bMJQAA -->
