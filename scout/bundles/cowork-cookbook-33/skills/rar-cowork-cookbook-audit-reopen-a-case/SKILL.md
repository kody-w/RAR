---
name: "rar-cowork-cookbook-audit-reopen-a-case"
description: "Audits reopen a case records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_reopen_a_case", "rar_sha256": "2d16379b90c30d95b59ef31b0dc5e41db0dd328946f686be7e8e6a7d25623e94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_reopen_a_case`. The original RAPP
agent is preserved byte-for-byte in `audit_reopen_a_case_agent.py` and in the RCI capsule.

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

Reopen a case Completeness Audit — Audits reopen a case records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 2d16379b90c30d95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_reopen_a_case_agent.py` first:

```bash
python3 audit_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_reopen_a_case_agent.py   # or on stdin
python3 audit_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Completeness Audit — Audits reopen a case records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_reopen_a_case',
    "version": '2.0.0',
    "display_name": 'Reopen a case Completeness Audit',
    "description": 'Audits reopen a case records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '079bf1a90c82bd86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditReopenACase(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReopenACase'
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
    print(AuditReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6aZPiyLLlX2Hyfajup6pEu6CutdkIIYQWEGgD0dVWrV1C+y7Rr//7hIDMqnq3+867ZjPUkkiK8HA/7n7cI5R/vFhtE+bVy+cX1bOyGWclSRR61czK3BmT93kVgx95bIN/MyfPmiqy2yav6pePL65XO1VUNFGegel060ZNPau8vPCymTVzrNoDV05eufXMzyswOy0Sr/Eyr67v4os8iZzxcT+yMsebWYEVZXUzq9rE+2QDAe7MCT0nrl/Bct5gTQLql8+//vbxJQLfXz7/8eIkVl2/La/cF6cZMBNMSKwsAE+KERiYgevCq4AeKbjlev7sefVT7SX+x9l//mfcW1VQ//z5SzZ7fr68TH+UNps1oTdrcqtuJoWswrKjJGrG1xmd9NY42dy0VQaMmtUAnyx4fcz8JikvZr9Mz356LPIaeM1PX16ArpU1offl5ecZAOjLS9VO318nKcVPP78mee9VP/38TU7d2lfPaSZhQOvXr8/rp1gw8NvQyL+v+guQ+vCT7X15+c646fPQe7ITzHx5veZR9tNDcFHlnZdNPvnp578Te/dMEtXN/0jurw/BoWe5wKan4j9/vIP82wx6GvQu8++XLYBb/x1LwPC35T7OnkD9new7/v9NdBKBgH1H/C/F/dUE6JfZr39r27+a8HHmf3lZe0nUgeiwE+/z7I+v6oFlfv3gfrv54bc/gej/qxg1byvnLuFramWR79XN16+/fqjvtz/89uuHtgCx5lnp17ZK/krmX+F6X+cHBJ+jfvpxLlhfz+Is77PZe6TP/siL/1X9+TozrCRyv92vP8++z5fpA80mI94WfUDwXc7UQNfvcPz55U/ACYA7qta5PwZZ/h//MdtFTpXXud/MVCdvJ2LJmij1JuW1MKpn4O+U25UHcK0jAOxzHIj/ycOTxrk/+/1/O3cm/OQ8mXBuTWzz9cF1X62vE9f9/jrTgKi8ioIos5KZQh8OXzIr8LJmWqaovNqrOkAg9th4nwD1fJq+zKJs9vtfSPt6n/hajL/fqTJ6cJDC8BP/1IAeXycbTiGg2ofGDiBvb/CcFshMcgco4EeALD8C2+o86QB/TfbWcZQkMzcCvAxIfLzLBph8noT9/vvvgHLDL9mDMLHZg93rORjwrs7s0ydgiZ9EQdh8yTwnzGcf/vjzw+y/Zv9q1l34tMYBkPUTcaChoMr7GcigNgXDgDOA+wA93BH/488nnkBMBsoR8E/kR95jMojA2HPfwFW39CeUIGe2B0AFgKZFXjWAhWdR8zrj/dm7vmDR6dHE02EOqozrAbxdLwM1qAktYM47klnezGoQZrU/fpy1tXdf9Xe7ulcnLwWpbDW/z3bMAVSFPAH/TWreB4HJeRYB+N9d/7gPhFQf6tnqTcTrbD/F3KywKqsIK+u5hm89/AKqwdt0INyaZV7/JZtKnjdBdU+ABzxgEEDGebr00+TzqaCCbHfrt7XvY6ypdmn3GlZ9yepncFvVo0YDVcZZ0EbuRPn/eIZUHeZt4t7xA5pOkp5ecJ9euceg8kPBZ74v8veaPPvSojCCz/7/9geTJjTHKSxHa+x6xu41xXwgNDUtE5KPPgeU7fti92z4VsrfiOCND79kSQTcXY3/eIy84/oc8+CYtgKLK7Rylw+0AghNcu8xN8VQVU3Ran3J3oj3I7D5zjIAdpCgIICnuHlbcHr6pmkIsnC6/laEnzhNqIC4mhWtDZCZ+Z7n2pYTA62qKW+eQIMA9KYc6sPICX+wagakAz8D+TOgxOQNQM536PY5MBOkjF/l6bfh0eQuoIXbOkBb0BV6r7MTCP3J/TXIN9CfTGMACh/uomapBzAGKr4jXIdW8VBmaiSfCloT30Ze/z3+z0ffQvWuyaQ8kGm5VgOQ7Ce2dL3h4dd3LZ+eAkLTKTruk3509tPS2ff14R9fsruG7wQNcjaZSut30MxArqSPWJwopwa0kXrP8AFxcK+ir49C+Ki077p8/qfe+ad/r72+lzb9R799noVNU9Sf5/NHOXqrRq8gQ+YgQqLCqx+V6dMjyz5Zn6Ys+0HUA5nPs39PnR9EPKP48wx5hV/h6ZEUOd4Ups8PsJ75tDI/4dPTiSG+uRUsn6eAvya0R1AK38vF2xBQM4LKC6bBj/JRT1WnB4XuzpcA+C/Zu+ufaQHoOAumWlfn36XrvW4CRz789E7r4FHWgLXdqZcKvGlnkUzqgy3D56xNko8vmZV6f72jmNgaxCOwf9p6gMwA3UgTefcrYAd4EFnT9x93RvL9i5U84rZugGJWdc/+Zx48ae3j1IpmgDmmtn8qSQ/6BpsVq02aSdFmLCbNHruMqeN5b4f+edV7ooI13PzzlK8fZ1Pr+nH23oV+nL3tC+6bq6wFG6Nfpw54shMMBT/ex75v9mzv5be/UOPZEP+NEtHEFRO7PMz13G9EcHdUYTWA73RFAirlzr0ZmApgPd4L5T+bDRasvLIFFc+dVP6GwTfV8oc+f95NaR67vj9e3qjk6bxnhweGg5z9VE81bw5CGiwIrh/BB579T3q/5xTAdqARAXNQFyExamkvYQeD3SVhE0vPxxAbdh3CwxEXfHExdLHESZ9ckLZHeQuPtCgXzEYxb4kDeY+o/TrV8mhSA7UsZ+FQCO4uKYt0PAy2McdDUMSlMA8mlpi/WHg4QOR9agzI8mnbw5YJuPc2dMLgaeIfLzaJg5FbvObpx4eZLw2Luki2srKXFOnnG21e00Yj10Et3Wr8FKNbvggKxgrFUx5YZ4vNGufkxuopERx70PSFsV7wx8V4Iah2bhSCuUkgnS3ZTef6fofOtSuGCebyRjROGQ3n8kJHca6rxDJuNUQt9ETX8XIUXTWBIC/JIDI+Flf/XDLBzVFZNFU2iksgO5PYZJGJy8sqPVmWynaCSUp6EZbxsTkGEa/YigHrWKiNl+w6LP3ztYc8bDuEdohDrTR6CLRAmbzWIm7YSHzZEJlCmBwmVh4Z0CKx3hrMbc40g3wsJbi8EhypkvsV72BhLqAEnLd5kW5Wm8vp1C+g80Uw261al/1pg5F4HAu9c8lDbb9zr5LBISfdIW5Yo4mbWyIqlz27Nwr3Ug/oHsmK9mJzCUVlwrls9TWKNMrKuuDb2OijMMqRozO2ASfHG+ZGX+QaUQWbOaCnAWk8yFFirpeFTUPTvsA08TKsS+dyK1wvwjHBbZFY0ylmnrHG0YGaXZ2fMRROThrcKGKk2uzy5hz6ghl4auV2XLyw+sGwU6M47DBpVbKh4FvUuUOL0TsvDhelsM0w0YNM3eyGStTjG1JntV1efeOaE8htfdRacXXBNRciqGxk+PzkrKzdeT16dWr3KUcduhhWOYdrqjXCljUlrxLoChfh2rZF12l26+500qPVpRYWl36+z8uaPawW8GFXt302ZESwNG68caW4TdgZJp7RYut2ec3kN50YaKJylxqJsU10u5mV4ShV34N90YLY8erCWt0MtU8EV2OIZs9IUeS3hVjrhg26hUxLPDpyo3MLzf2FN1wJNfZEvpGWvZMdNjgEnef9PlgwNFJkptx0gl7IxnrkFxHDj3IESRcNTuK9f1YSTCP41VLvrgRtcpJ5GsRVsYDXmR9uUSTxSlSUtZsy6jm57rJDG7it5sr1hj5xcCjYw1BFVcui6zFAGJMnt/iezvjKZhSMEXE6kKG0CTk3zqKlmamGTO2wxmMKjCkP2o2Eq02ld9UBXlvzJb1KtXlpdFeJ9aVtsW7I1hukTmC3uWARXUvXSJpV9Mm9rRcntW329nGt+NWiCeUKKey+rQ9FGV3VFt8Na51TBOXkmbdahyu62JOBQafBdQ5f9wtM1hP/IqFLThCVvhPXnN1KjVkIVivuVTGfZ+S+30rrxZHlkIRV5oeTdu33yaLNrFJRwnlmpOtMzW9FwRGGZwhcL6olhuPS+lzF1VAIRICIjXgkXLqw5oUtd9zRX7FX+UhTzf5GYTuxiM51Ge1s/ELaUL7BkZihJIyA29Wc5eqNO8+jXClUG2MZyo+RcZ5h/MkUTXchoDF/ism9XsCkGblJUKPi4iidjehiWoaWikzXXHPNS6mDTOtBx6MS2vN7LhWJcbkrPLtJBdgn94FVFo4NQ3vCdYIDn7rxJdXVtAvkldy3ZQtrGzZBNK/hzO0Gnnct5h394zWu6ssBW2qNfSt4Nagp+gTI8nYRhpjkYa/GvF0fBNs4l9PlaaSzSz5eCyZdmwm9FkY/gn2fQW8MqRTJTvc5BF560G6wybYSNmdLKZwkDC8B0y7iI8bR6iV3WYhe9LlKbSXWOu3rZFDpnBg41rVYQ1MunQhatNXZDVfboVA8HFWYa1+M/ZI9kKMbOgikrlkeXivyhuUUa4eLPgxT86rkYqaID8OJLtB2q9XdLQuhs3kRN+qtqhZlnRGDe8gQ6KjuGbva0zgJbeYxnI9qF6cqdXBjU1VkUVhLUEfM65rht+ezc+p9OgoZqsOWNba6nTECleYVfARhA+WxtJF83pozukHhhayq9FGir4VawpDBp6HKB4jQ7q9lztKSSSo1wuahdKIVly4JA2cCUogNxIiT3Rqu+qsEct66VCde7hlGqoNQOueaTnsp01fRGK8O6FnM6/609VeeO17U4HyVDlJQr059y251SSnMmrD7Kulg+CztMPE8MlzTZiVMEQ53SHjPWVjHZhdTKiFJDrwXpbW1J66ie+SjsHUFUVtSmsrsKMlNxHaVylLPK/MSj9GYzToPTYdzgxwEX1D2zL7mgkNtNpYW5/Fe7JpOdLHDsA45a7kFWc/OOS4RU6SFlYSCgkACTW/q2K2aVeRhpFPN4QEdyrXacae8UIOEXHVm3DVqJiqmeqxz7WpY511wXgXrq1pEiGHm6oIx9bpA+hapU13y5x67HunaDSB9y2KAJLabba6tcXTTy/MNK0iCmJOoFuJrWWeTMTPX8EGdh1Xc1xZKjpvd4przPeb2qGJBaxQdx1BSNZVd1bhqjFFkyujaQHPhoCp8ceSWwtyhHGq3ojtyg3fWnjm2aAVWaCKpdebntLykKSLR8xxtjfgUCWdPG48KY1DjqXalAT8SCLstzxfS1K/QVeE09CLSyvmclx1sHRMmxZxkiI+LBW+yW/J0WWGKlASIs5Kr6zFg1gavraQ9Iyg1zogGgdXrm6q153lD6xlq0Tt3Nx/w3b4qIPTmNrGZy9mNpweFQe0unR9vSaptEl0+l2UdUhSFLGMJweKbXmt5E21aUFJgTEmZfOmOt2uzvJyvNFwvu7qLepSZXyJ8a4za1d5eTx6dw5kZaDp5yuw86JiTFdCmefDSQ2ceo7gK5nCIRzdmVxxRf+AXPnYZtBrjjFXV16uSt9fdbiW4QgPrO0E+rThutTO0rWpszITFtIGgGzvYyCEWreekIq50wimLrSOv07DnrrxSaAJiSspojoMebxBeJlDGRSQDJ8ZY1vEDQve+dxQ9jVod9UxeqobKLliH3IjMAjmc9ydTPlbRkj+cwi1mi6FShG7HsCzOF8uwY67XYHOMGn599TZ2RtvLE8MepCbDUAE9VF2Y0gRZp6JvzgNlZNbRAMGmVo6Wjfm7+bwLtDKNy9wi5ZrXa88w7Su3aGLGqqhrcrsoFuiq0uO4LHpRnqPVrt3718N2qEm2cbDaAnvOvhEygkVU9Yp7Y7x198X6rAmGNQhGgcOLkdGcCJO8TRNTCVxHrjhkJmc3mn1BoB5FXY0bon67LCQa89dUTLFLr7iZZ4+nZQXHmjY+bQInqsaTI4nVJlFCkBf7QgINomVVaV33lNC6hTNgTHjEL61kj9A8TeSFcW3EValojklj7o00uPi4tWm3ZLeCIvjNkCJ2bkFhpeELq0vLUrrw3fmaICgELWHbXF8uTVAt+80Bxr0+JWx3gaU3jrmq1z6hZXG1XemA49tUsTaiC0sCveKxDUApui3riiB51+AZw8okFpTe0zE6BLuyUEm7iG8FTu1QVfR1jvU4KRqOKR/3StQcQBE8peqARqms8xkV52yg1VuJPhFDJsLLAR2SZDx2zklXXcUlQ3qje0OwVxrKkOjmKuntlo3wYxNkfClhlgJyvk7TqpNrmhjM3WnRHz1UGS4MkbYOJBk7MWjMZUFtNpq7uG6N+AhFDpP7Hr8xKokODr5yDMgdc7Nta2vmOsJiPH+ZSxsed+SSscfLye6vsNn1IMCXpgCLWGdwSmLoIYdeBA2+ybGIqHaJSWVJ7EGeLGTj6hWUkowkgShdzIno0Y5qnVJPIZTEkt6wEhPhBsuKbQ9cn7o4PAo7bLtbk6XvxYp/so18Q3K17sxhUqxW++tKb9LdPs7BpgWiY8NFWgFybA7rLCcz99tbU6mUDLYtWHp2bbxiipF0N4VKswu086PA64pFqxkWemuRbtNtC3iPFIWMGb5mnyu0kxY7y/QP0EJeQSXWhW6j+2d6eV6mJL4CXYi52CNrMeeF5ADbEWk5aom7kneuj+0S8tmdsd2xZzTu7Kw6+uuuoQ7DPGxLi9mAnT53tRHhNFRKdqgNzqm8wPNjEt4ell0ZIDS2161NCdFGBTVyDueIYGnO2YA0LL6g/qYd1lnbRVgqU2fuuNvlpDgurFEm+k67RO5SYlYtPFeDeWoHKS54vr8Q/FrKWbEHTYI+HxriAN3SVEabeQ1btLFVgmDIxuu6Udc3rcc2S+0Ao5ncXYRMvlVQKPGmZ+7RHtRb0Ya3KZKFh9I+8AeRxeSGEG4UsSMgdymYgKyuCVlfNyUNGM3D8suB6UO0sYUjh1LJIC8AAa53ZJyu4PCi2d5hCfy85jfdUAbQoWztaxX5WLX2NdfrzGDln9HtGmyDXATdYDImgRq454+y6o1li6SHUzM05pwpF8tTkUtFgXpRbm0HxL529tmyztDpMDfN+TUwIBreIQGX14F3OGCyPGTWraa6lE+DAoIQ9rRLlgxJ27sTwPhqeedkaW+OVIVZq/jmF9udL1PCfEt1vNJ07IIqGnzpFHaEz1nEMTU8NDPQHSs1pLAV43Ynn6ztGNzljvK43GNdFSRx28VWGKwwJCQ1NcykUDWZ/mANQJ/ASo/wqm4sPMW2nmPKrFNizgXkjMZGWrXM7QKjFuwam/vNasxb/ng18wOXDoiA8wveEjoSXR12W7kct7kjke4gl1JMrKlWSs9YAna4CLU41BUovJi/dRKk5VEns2Q5StILVlWu5uSgvPfK7SYodNQdgs1QwfZpgFiSdLu4qdwWTfVFuI5uCL4TqrhbobuMPrG77TwruP0mwhcOZYOt7UKzhfKwv3iqThM2taqRzPZvpiAfl8QZ5NzeQzCzGaW1LrvjVd7mZejnN2/Fp3uHJjaYeh3WeXFWKDM+0oR1mLMhdq5Wm9G5CoRG8k4K5UJ3BOy471qHb/AjF2EUteoX4j6Z2z5WopfLEsE0eekbFFRt+DVVLyA5OS5A81+CcoNJ+LrE5vhwaSMvWe62bA+REncuFsvLxraWoJmWsWWOH+eJr8sd6NybuRUy42pFKETEWLuVZgWRzdyuGIt3SrkuQMm3WlRpWKqyNxlupcFppcZSSUIyt1X6k4LWW5FLqXrd6TXq7o30qkuYfyIg+FKuTrVyOlM7+pY7aAc2x7TTCD6tWUlAIiKd6thpWTlJcj5BFKoDSnGt/VkMuFA0UncNxVIMNT2Nyxk+ihZaMRCk7ndgW0AnDq8MnkVfZYgzOONMxlhM5KtMSQ31aHriskVU3Um6ywm5ClSyVYYMxzDlXHhov4eWx/6EV/tF0fuUZ2lnVihaQCz6cBMx39a5E0ZxRnqjAcvsyXgQyf2KrezqsJB6iyWbxQifQbpsgv1OdO112G8txqXI5cXTOTEinZINBARie2UOqxuECzTZ8gfpus+UpYMKZ9Tt+XmmE40kEBJEcimDsVFM0/Qvv7x8fJnOR5/H0f/qJfF06Pf/7OzxcUz49urpfijsWe7n+1qf/6UWv318qZwI6PA4Ra2TNngeQP63M9RPf/GWYpowPt6uTu/BhubtOL6xgul3fl6izG3rphq/1nnS3g9uP77YbT39NkI9/cKKA36+3FVPi+nE+r7GdIo96djkX+8vwt8mRtn0bsdzI6vxnpfB8xT544s7Aswjp/6KkcRXryomw54vPSaAp7ceL3/+H+jD+gc6JQAA -->
