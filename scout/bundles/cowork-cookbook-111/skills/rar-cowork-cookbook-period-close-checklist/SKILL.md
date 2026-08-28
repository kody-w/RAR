---
name: "rar-cowork-cookbook-period-close-checklist"
description: "Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/period_close_checklist", "rar_sha256": "43f8a9a6fcbdb093287deefa0dd7a4e1c8e5883f93a23ffcdc3b2c3a0c9abf84", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/period_close_checklist`. The original RAPP
agent is preserved byte-for-byte in `period_close_checklist_agent.py` and in the RCI capsule.

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

Period Close Checklist Generator — Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `period_close_checklist_agent.py` and embedded as the fenced Python below (sha256 43f8a9a6fcbdb093…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `period_close_checklist_agent.py` first:

```bash
python3 period_close_checklist_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 period_close_checklist_agent.py   # or on stdin
python3 period_close_checklist_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Checklist Generator — Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/period_close_checklist',
    "version": '2.0.1',
    "display_name": 'Period Close Checklist Generator',
    "description": "Generates a tailored period-close checklist with item owners and ETA estimates based on the active legal entity's configuration.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'period-close-checklist',
        "upstream_url": 'https://coworkcookbook.com/recipes/period-close-checklist',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3a2559184fc7b56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/period-close-checklist', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PeriodCloseChecklist(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PeriodCloseChecklist'
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
    print(PeriodCloseChecklist().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOi6LbmX6H3/ZBZl51bZCZPVEQjkzIoIipSWZHFJPMMIlbXf+8XdWdm3VN1zz0RHdHmoMj7ruFZaz1rAf7+4vRdVDYvn192gVNAkpNlcRQ0kFP4EFcOZZOCtzJ1wT/IK4uuid2+K5v25fXFD1qviasuLguwXQqKoHG6oIUcqHPirGwCH6qCJi79T15WtgHkRYGXZnHbQUPcRVDcBTlUDmBXe9cmmCwUtF2c34W4Tgv2lwXURQHkeF18CaAsCJ0MCoou7sYP7WTOOQ57oBRY8AYMCq5OXmVB+/L5l19fX2Lw+eXz7y9e5rTgqxf9bgs3mcK9WwI2ZU4RgrPVCGAowDEw+Vw2OfjKD87Q8+hjG2TnV+g//zMdnCZsf/r8pYCery8v0x+jf1jalU7bAcM9p3LcOAOGvkFsNjhjCzVB1zfFBE8LUCzCt8fO75LKCvp5OvfxoeQtDLqPX17KKnh4+OXlJ6hsgL6mnz6/TVKqjz+9ZeUQNB9/+i6n7d0k8LpJGLD67evz+CkWLPy+ND7ftf4MpD6i6QZfXn5wbno97J78BDtf3pIyLj4+BFdNeQkKp/CCjz/9ndhvQf8fyf3lITgKHB/49DT8p9c7yL9C8NOhbzL/Xm0FwvrveAKWv6t7hZ5A/Z3sO/7/RXQWFyBp3xH/S3F/tQH+Gfrlb3377za8QucvL3yQgbJoHDcLPkO/f93pAvfLB//7lx9+/QOI/pdidmXfeHcJX3OniM+gCL9+/eVDe//6w6+/fOgrkGuBk3/tm+yvZP4Vrnc9f0Lwuerjn/cC/fsiLQAPQN8yHfq9rP5X88cbdHCy2P/+ffsZ+rFephcMTU68K31A8EPNtMDWH3D86eUPwAsF8Kb37qdBlf/Hf0Ba7DVlW547aOeVfQeBAAMaCibjzShuIfB3qu0mALi2MQD2uQ7k/xThyeLyDP32v707X37ynnw5e7Df1zv7fQ/sb2+QCaSVTRzGBeAzg9X1L4UTAl6bNFVN0AbNBXCIO3bBJ8A+n6YPUFxAv/21wK/3vW/V+NudR+MHExncamKhts+Ct8mTYxQUT7s9QPTBNfB6IDYrPWDDOQa0+Qo8bMsMEG03ed2mcZZBftwAF8tmvMsGyHyehP3222+AoKMvxYM2MejRCdoZWPDNHOjTJ+DMOYvDqPtSBF5UQh9+/+MD9H+g/27XXfikQwe0/cQdWCjvNmsI1FGfg2UgJCCIgCTuuP/+xxNSIAZ0EwhEKT7HwWMzyMM08N/x3S3ZTyhBQm4AcAWY5lXZdICLQTN6g1Zn6Ju9QOl0amLrqAQdyw+qoPCDwhuBVAe48w3JouygFiRbex5fob4N7lp/cxvnbmIOwuR0v0Eap4PeUGbgv8nM+yKwuSxiAP+36D++B0Ia0N4W7yLeoPWUeVDlNE4VNc5Tx9l5xAX0hPftQLgDFcHwpZiaXzBB9WiOd3jCqUPH3jOkn6aYgx6ag5r323fd4bOL+5B572TNl6J9prjTTKHwAOUDpWEf+xPx/+OZUm1U9pl/xw9YOkl6RsF/RuWeg48WDN17MPStCUPP0WFqbj2KzHHo//csMdnKSpIhSKwp8JCwNo3TA8NpBJqwfkxNYC8EEulRL99b/jthvPPmlyKLQUI04z8eK+/IP9c8uKifHDRY4y4fhB1gOMm9Z+WUZU0z5bPzpXgn6FeAzJ2NgFeghEGKT5n1rnA6+25pBOp0Ov7erO9RbPwJKJB5UNW7GciKcxD4ruOlwKpmqqxnKECKBlOVDVHsRX/yagIPZAKQP0Ebg1oBAbhDty6Bm6Cozk2Zf18eTyMQsMLvPWAtmDGDN+gIimNKEBCjAMwx0xqAwoe7KCgPAMbAxG8It5FTPYyZxtKngc7Ey3Ew/Ij/89T3ZL5bMhkPZDq+0wEkh4lS/eD6iOs3K5+RAkLzqfweKfOnYD89hX7sI//4Utwt/MbioKqzqQX/AA0Eqil/pOdESi0gljx4pg/Ig3u3fXs0zEdH/mbL53+axD/+e8P6vQXu/xy3z1DUdVX7eTZ7tK33rvUGKGEGMiSugnb2Y819+j7K/SjtAc5n6N+z6E8inon8GZq/IW/IdEqNvWDK1OcLAMB9Wpw+4dPZL4URfI8sUF+CKp9oNBtBy/zWU96XgMYSNqDYweJHj2mn1jSAbngnVYD9l+Jb9J+VATi7CKeG2JY/VOy9uYJYPkL1jfvBqaIDuv1p7AqD6UIkm8xvg5fPRZ9lry+Fkwd/fwEy0TpIS4DBdLUCCgSA3sXB/Qj4Ak7EzvT5z5dbm/sHJ3ukb9sB45zmTgLPcnDCe/t4nSbXAhDIdJUw9a4HC4JrG6fPusnYbqwm6x4XJdOA9G16+met93oFOvzy81S2r9A06b5+Z+NX6P0y4n49VvTgOuqXaWCe/ARLwZv3g+vvi19+/QsznvPz3xgRT5QxkczD3cD/zgf3YFVOB2hvb6jApNK7Tw1Tp2zHe0f9Z7eBwiaoe9Aa/cnk7xh8N6182PPH3ZXucZH4+8s7ozyD9xwIwXJQup/aqTnOQFoDheD4kYDg3P9wVHzuArwHhhawDcfOtMM45NlzfRdhMJSm/ABEEvF9ysGDuUcHBE1jZwZzUOx89nwPc1EPcxCPcdwzjQN5j+T9OvX9eLIkQM4BxsxRz8dIlCBwZk6hDuM7OOU4PkLTFEKdgQ7/+9YU0ObTvYc7E3bfptYJhqeXv7+4JA5WLvF2xT5e3Iw5OCROudfIghsyOLUJnJo7U8luUUccSYM5uomUht4JRhCOP3GbUV4iRVjxrRYd5ieLg7cRXRpEWhCF2oyyFfvreFQkAem93NQLuEJUcWsuSHlfVkJzCpwaOW18VzjAxb46t70XCcO+O7QyM5tp2UwgquuhUOw6XaUq7xU2JRCS7xUMpXpalivLw5oqNMVQJcFyafKEKJYn7VZNU4iB7dw8rnWTfYevsrJcm0Sx2mVpcK0aUckuqnk6qJXXcEiQtPBZV2PYL9wRh+2rd8HmV1ikVthm1fnyCR+s6uAeAjY94nrixd0i3Pi0fFiTUc4ge9tq2mhBr5Emq3texEGt97JT0WI/lKdGjesdpastQqi5IKycVhV0tAzNqKy4NPaljY2t1rXjbscQSReO1x7OwtysgvpSEkfdZtymOSP6brZPvAgXw+4Yi+GB22VVtDkflGp/PQ690SwjmrcJdmUK+Shu81ysb7ODK6E4TleqGW9VQ65cdV8t45JSjtx5nUvNtp87N5tHUjWc1TsFFOlR5OQUA3k2nso6RA9CfXGQBazo/E5CBWbRaXV5qCmP7oixxLt6uKbLq1FWzBE+I+fNhpYboRU0OrxG64DuhGDT0jvao8CA527y7Unw5xy93jdWL+BwobpS2KlzhFhGicSsrrSLOl5laVKf8HNHOeU+o9mW3R1ttzP0zRFdYAfjeA01/BSgCDwvhxZV0zGs8MZ3Me6M3sbjhdN0zzsIXXkT9c4d16NoifvVEkO4vGMQ1T2EKKVqzHEFJzS2QGVEPVFHd7gyqXrZ0csDets0jXNVroHY3yza3+S4fEUHg5R4erU86tnuWioeckEX9Ca42cxsrbfLmBRXCNOaB64W2p0vLLukHJaGN6ozy3PxArczLSwbgdBy1zhZJEuhKzsj1I1BWWtrawpHgugimeIkBWPl5XIVrW2ulcZjbcuVKu2zJsXZpbeXsrBlbUcr6ViwjWDcYydiFQsLPri1gSpGW5ofz5Ll5ikfn9DLUaMGABjB2A490ht7kFf5hqt5d4Eu5rex3pgJycHRjCBWxTGgUz0dLXx12nS3IW4MJLzBGME33XHDJKxJ+BaVX3cNYfQ6MjeSyAJ+R0jcdMqquWYaamV7B1aq+ULYKSDqzED7vtWtCiu2dmeV7YVqX7OFUw3JaEqnI7LjzJRmaCwrCjKPriG7KBpSlwpzlA1is8lOYyLNSqTmY2NHIrc1zdIHedipuzjXUJW7WUJvwPqBm4m8vO2jlc17KaoqqDWSrCPmGiHwekjPVlhgby+ra8ezRk9eZ3Z9bWbbma1n1zE2NJUZsRlHXYWlcSDZ/kjFXrUc59rWoDboitqz6slfy3a6Nxs1iuxQEKqNuMp6p07r4hoN5i5zJFVcrNPTmpCS5jBbgjqd1U55VQ27nbXJbn9JrMtOS2ZnIt7ExM3jN3UaVfgNGVCTShlDr7o1qMbjsl3ytxG3L/0CNhZlPC81LXGwaru7SnWzGOCehXvDp7qk2QUcvVrQ1NJt/UHbX40wVQf0BtrOwryFM5uG4ROVCIY0tkKvnS1qjgtEubuOvpPi10JJW53DwiMXL8Nk7xr7YNjyZ5rz9URzvWRA2hMRceYyvPm90yQj5/qboXFYmt+zSok64kY61tliV5+vbHaqDmtXA92jFDHeUPe1yMd5eFGAe26VteyoHsYqUlhSQPmaz4nr3LxlQXVs5/L8klsqjV+shoRbNd4pIxKRsADCXiK7C7GxjxVmSEs22ydl79PnS3dg66Y/ntyOPUlqrVkzhNCy8/JCESlm0YCJTJNAk15YL3inyAlQ1D1rDNyyTkN2j1mzxZ5DZL4/UGovlAtm1SWkMBBabWM9G3n7PUHRm8RET1rRIoHueEGvtDku7IvtqmoTXDFtqhfRRRP7gn91VpyvJUOd7RI0X0rswhWdOvf0q31sXfvULCwLwEkvxJXipqQ3SmXiFI3HAII4yhnmOqVqjal8CZ2FrC6dlFCpAPGXZgaTK9++WUipMFkeKVgHayc546jWSwWXvRoHxFm5iKR32Ywl5irpKQTajxU/Hne3m6t0l/riamaQNaKQ+YvrAuV2Y+0X45mCUYp022Wk7DY6Hs0Mbi07Me5LAZHwu9aqpJNpODR9yzWyOO038aEmZSRw0khJ2lKLjBm1jRwy4mqiqyyZJ/YlH27X+4HTbqjScBlycBpUGzJYjbx5AattMQqxOOLWyrBlb1mayDI/rE6ybYjNylI3h4OY075+jvFt2ch7Mz9Qy72czRctFffHjdX6LBZz9bEvLL3HMLLeNz23MsVbqMiFZwaHBhnIfsHBlSZermyL8PBJMXOjViT91uQHDxRmj6nt8ggnqwNyCHZdXc3HI8fl2VldVfvGJ3WDE7YWUY8Lc+4rHVoC0ee0gQdbN+tEHvWrGtnE6BJcTHjKeiWelRVfGgcpPNy4fcNJDou3TmgoVzsTUg0vyMCRxb50Fqm6KdZH5bxeXioeRWRnGyjuuSkCVZLgbpMzRr9u9M2ea1g+vfn+iaTtjmsOB5ss5kvOjFyKgZnUnVOeiwrJtsZ1b6vpNRhZcIP0o8J1SKTbL4wbTB3aLOoq2lUQ51jRasXUUWcfIxffbcr6gKO8iScku1dXazBSCIjVrI7DejUwR0WOl8IG5ZCzQc49i2B2RbJMF7EuDLbdVVzm8JvryVSvHLsYy7WA1PvW3a23e2FvYdfew1Tpyncsu0JCl011MAEQcatxSMUpilxXgbMxSVqJF0Eu9rJmc5msRNwpd06zhB0l3Sq5+owrbJo1N3/XxMhlq0rNflifruZAS0oUzYRls497ZReuu/oUCAjIHxWX/FGHw2gv0pGEL2I0Mo2SMLezXuLPOHZK+mRxEw7xqNWWyhctse3EsIKzY70e8sJEVssbA5tStqnW263QOFu5hemhvWksKo2O1sqxzBCRvYqJOXEd9eg4v2TOpbrEp9rnmpvWqHuEcSWbxZRttgaNz9IjdMh3o9JswpHSnSIhdXRJXOTjkOOsde6tkcsxgar84jonTz6hpGt+HV52WBRVadeDMRw7qOhhP7pWLPACvCaQOXNDg1NU8DHi3ordPAh74NP+RlUCQqmimN2ONwk+nvhS3eGVwXizIsv0cY5mwrCSbwjru15kGx2+wLZLpxazfU5U/My8SDnBuswxiE0k8jBR5pQN0ZLWygsVcF1F5nZvjkkpB0iGnyJ7rCQ4XfWX7FjtNqcjNayUbMmSlHPuGq3cDzN+Md/n1prA+a2cCB6LejfxeolFZrBccRFklqazK/eyWvHiYrHQcjK+HvZ0G4e236at5lbpWNAqXYFCkEVXXc9VZ6YkaMTtXS9uWl9Iq6yQlQXZ2S7HhS2XN9uJA7g5Z3vlkbmKOVqSSkUOHHMdVaTCjriEoaV4TILtZuUW2el4hm/CNdjXZ+GaujwWF7rCWpwOBqb4wndoKMcm25KYE97Ebn7abUNhiALY4ZZevrjM9+KsWpYimGx91SP4XaJhvNYbQkrMbce9Sv6Gnm9df75u6k7RvLBdHRinpQaURbqFeRF0AV24YMIPvAo/g6KauwcmBElA6vFyl8gafWukdLGC8xMbZFuqDZVxtJVVse2HzLxhcTeYp5XJmzZv7y6uZ6dFpnTdqbFuy0Tva8dj0tF1+2jrLDQp41Fxces3t9LDbq3k+v7M253ySLJOetVXxwAlM0LXzF2g72Bjibm7YA3r4skslo4VwJueCZMe9Fmckmctr17JxbxrZmAyV2BxHwWEpvSAQ2sN2R50KdOWSMAGu7U8Dt1q4/C9GiRZi80Iz0A3PpbP8HW8dqtTH9Uss8EVUVClltBrv5FmcJuy+RVVvN1WRLjOInxkEUV1226HDUVnznDzAt4Pl7x/3tGD1hzsLTZ0jgzTjkmSw9la7fxS5TY5Zo0IIzWNO4Md70wbZ/FYNSa2NuDZAaPdvcRqRN2gygwj1Q7hhroUVPy4QOtOLpdujJd9Kmb9sebZdd7kAiMnSx2MN6vLspoZoyspcsSEMOulppbT22JlpDfsOiJJLgU8W4iIlxupU8bt2CdFqW+YGBWNMSRhYyzU4KSNi3WyTg+n/OTP+INJre39PPOYtTgL4AMew4fL9oJ5PixoEir7WMwubpRCrVO5v12EmXnkqm1PkGMNH7dMj4hiwyCteEPme8s1U8Z2nXVy85eMVoPVzAk+lMPWN+w6H1KEnSspT+mMmiQVSVO9S+ZyqfhNtxWzyjRxeY7ao3LtKGekdTC/YIG/xjfx+tirp+IwJyjQGHCiDLUNut24CJh9r4nf7DeS2ouGZq/mAFmhvRgBTs7oBCk49tZqZzO1vKiv/Wjuc8d9KMFSH9OtTOMHU0A0R9L04yCbq1rELJB31FUvJD5cah1CBsI+i3frOVxgc1yTEgMVTmgI78G68rpsmDWP5eoiDA/ZOaWGfgDK+Lan6+jCoGASOexrBvbO/SVsNqcqKvKDm3XRvEd7VFb9qKV0L+gEVaNC+DhStjnfEEFyrPMVfqB8tt0xXJYGPdyXNaG7tya79vAquoJZg+Ed3A0PjXybZ8wWw8exj7FWnHtrko75s5kgh649ujt243BYI8rI3LQW84rxq3NmJNZaVLnG2K75xs6t0Nk0Sa1b8bDuqVAoe8U4y92iIVM7DlhePM3CY+EHqVzIo3ap2HIxNmR4ZOAlqEQKi8QLzs5RKjjul0OJ6v5hVqtwllBXX2GI2c0NGPfGzy40LMVnGucDrIqxdX5C5hdMjNF87WNpXbPOrUHN9rAZq3pfU37IwDhJX4aEZBpUQD3CBqW0xLlCXOasfBnEdc1veiK/XMDku7CWu7VkOZQ9OHzVd8WlSq98uM825EWNjSvty3uj5nZ90ytLgxRzshpy+7Dt1/R6OKV+tTARNbtiYJ7HHZTZ8mRInlIO6DiKdRbu4PysUvOrY+kdjJVV0G3Ouw0mNCh3PfgIhnq9GWMLMSTPvKw0Hq0sSXZu8SUrpqPo9Qe2yDdLtRZNIrJGt6xt6xbedjK716sjekFSUaHIubPIj0RF2/aCoLE9w0rwuk/2J16lM1xhUn8b33AUtVhfxZnILfLZIsSYrKa8KE3PS1VvkjWXMVmE1rPVTOTictaKZm6aOuMoy00wR3CpZu1iM7j6VpRTZ3eNTwKlb5uVH6uRbNginyf5gQlM1l1uuCBKYMWB63xdEbpxGSSrX3qWuUtZlv3555fXl+nW6fNu9b941jzdD/x/dlvycQfx/fnU/ZZx4Pif77o+/ytDfn19abwYmPG4zdpmffi8PflfbrJ++uunGdOe8fGodnpkdu3eb9t3Tjj9lOglLvy+7Zrxa1tm/f3m7uuL27fTDxza6TcwHnh/uTuQV5M0p/fj+63b+8OEr1359fEw+WX67cH0ECjwY6cLnofh8z7z64s/Auhjr/2KkcTXoKkmz56PRoBD6BvyNn/54/8CK8tS+bElAAA= -->
