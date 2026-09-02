---
name: "rar-cowork-cookbook-adaptive-card-manage-compensation-changes"
description: "Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_compensation_changes", "rar_sha256": "5b06b331d26d3acc33aea212243859bda8efc5bf3afa0ca618e1f03b76419540", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_compensation_changes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-compensation-changes:e6f9c727cf42200122c7b6da1d18d11602d785716851858ba6b6b66abb4ccf9d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_compensation_changes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_compensation_changes_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 5b06b331d26d3acc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_compensation_changes_agent.py` first:

```bash
python3 adaptive_card_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_compensation_changes_agent.py   # or on stdin
python3 adaptive_card_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_compensation_changes',
    "version": '2.0.0',
    "display_name": 'Manage compensation changes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2049405bac09391a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageCompensationChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageCompensationChanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(AdaptiveCardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZeiyLruX+Hk+VDdx6xkRsm99lpXUVAEUUBUunplMQSDjDIKffu/30DNrKrTu/fZvdf5cM2VKUPEOw9PRORvT1ZdBVnx9PqkAStFBCuOwwAUiJW6CJe1WRHBryyy4S/iZGlVhHZdZUX59PzkgtIpwrwKsxRO3xaZWzugRCykAHVp2TFApq4FXzcA4azCRURN2SBlauVlkFVI5iGJlVo+gGSTHKSlNRBCnMBKfUilrKyqLhEvKxCQ2MB1w9RHwhRxrTKwM0iufIYvrDCG33CMDqykfIFCgauV5DEon15/+fX5KYTXT6+/PTmxVcJHT+8CDfLIN+7cd8y5O29IJYYXcHjeQduk8D4HBZQkgY9c4CGPu59KEHvPyH/9V9RahV/+/PolRR6fL0/Dj1qnSBUApMqssgIu4li5ZYdxWHUvyDRura6EpqrqIh2MVkLTpv7LfeY3SlmO/H1499OdyYsPqp++PGVQhJvIX55+HtT/8lTUw/XLQCX/6eeXOGtB8dPP3+iUtX0GTjUQg1K/vD3uH2ThwG9DQ+/G9e+Q6t3FNvjy9J1yw+cu96AnnPn0cs7C9Kc74bzIGpBaqQN++vnPyDoBcKI4LKt/ie4vd8IBsFyo00Pwn59vRv4VGT0U+qD552xz6Na/ogkc/s7uGXkY6s9o3+z/30jHYQoj+d3i/5DcP5ow+jvyy5/q9s8mPCPel6c5iGGAF0P+vSK/vWnbBffLJ/fbw0+//g5J/49ktKwunBuFN5imoQfK6u3tl0/l7fGnX3/5VOcw1mDWvdVF/I9o/iO73vj8YMHHqJ9+nAv579MozdoU+Yh05Lcs/4/i9xfEsOLQ/fa8fEW+z5fhM0IGJd6Z3k3wXc6UUNbv7Pjz0++wUKRQm9q5vYZZ/p//icihU2Rl5lWI5mR1hUAHV2ECBuH1ICwR/ZHUX7X1SpJeEvcrAp8O6Q5LhFXHFSIUsDwhMB8Gjw8awJL39f84t6L62XkUVdR6lKQ3B9akt3tJfPu+JL49SuLXF0QPIP+sCP0wtWJEnW63CBydVgPnW4yUdfK5GZhDwcJ78VG51VB4yjoGf0O+/svc3m6EX/JuUOtLCv1kQee5SAWSPCusIow7xBrqlt1V4DOsurC2FFkc25YTIcOfOn8ZbHUIQPqwoAP7C7gCp64AEmcO1MALYaV+hkFQZjHsEtVg1zIK4xhxwwIaLSu6WyOCtn8diH39+tWG9f9Lei/MJHJvQCUKB3wIjHz+nBfAi0M/qL6kwAky5NNvv39C/i/yz2bdiA88trBT3AwHgzu+9yyYqXUCh5XIECawDN08+dvvd48M0qWwY8L8Cr0Q3CZDat/CYtDg7qZ3H0GdBxFB8eD0o92QNoB2QcIKWgvmfPn8JR1IZHBo0YYleDfiffLd9O9Ov/MZfFI+bAj95BVZcht7i8jBmU5WuC/IykM+LAXVhX6tBo8GWVnBIIYh4YLU6eBMq/rmwhT27iFUSq97RuoSqjpQ/mpD0oNxkiGAqq+IzG1h38ti+Gcw0I09nJ2l4eD4R9TeH0MixScYY7N3Ei/IBkBrIrlVWHlQWCW4jfOse0TAfvc+HxK3kBS0yNDoweCjWxDfIk/+J+hCu6OLH/HJl5rAcAr5/wHIDPJPBUFdCFN9MUcWG1093YNtwGCD7nfYBqHEjfItc77Bi/dK9F6jv6RxCB1UdH+7j/Ru8XUfc697dQGDR52qN/pDphc3umEFo2Rwe1EMkW19Sd+bwTM0D/RROagKkzkaSkP2wXB4+y5pABUd7r8BA+QegENiwNBG8tqOQwfxAHBvWVAFxZBjD3fAkAGDjWFSOMEPWiGQOgwHSB+BQoQwdmHDuJluA3NlMPMt8D+GhwPcyu/edRGYTOAFOQyxDeOzRGwAMdMwBlrh040UkgBoYyjih4XLwMrvwgy4+CGgNfgiS6wKfO+Bx0sYp0PXgfw+khBShVW4grZsoRNgjl3vnv2Q8+ErKGwyJMRt0o/ufuiKfN+1/jYkIpTxW0OAUP4WvN+MA6t3kZS3ggRbcVTCVE/AI4BgJNx6+8u9Pd/7/4csr39YDPz019YLt4a7/9Fzr0hQVXn5iqL3pvjeE19gIqEwRsIclB/98fPQsT7fM+3z95n2+ZFpPzC42+sV+WtC/kDiEd2vCP6CvWDDKyl0wBC+jw+0Cfd5dvpMDW+/pCr45uxHRAy1DtZfu/toOe9DYN/xC+APg+8tqBw6Vwub5a3y3VrIR0A80uWh5zN01HdpPOg0uPfuvY8KDV+lQ+13B9zng2FpFA/il+DpNa3j+PkptRLwF5ZEQzGGoQuNMiyoYBpBOFWF4Hb3Aa2Gmx+XhbcEg5XBzV6HPIOND8LgZ+QD0T4j72uM2+otreEi65cBTQ8s4VD49TH2Y81pgye4uKu6fFDgvnAaQNwDXP9RiCG9oMSwqJeDLO/5OnD8AxF44fug+CMR5XZhxY+iAev60C5hl36kegnldCHKguW8GVIQZhWM1hpO+CMbyKcAlxo2aHdQ95v9vqmV3XX5/WaG6r76/O3pvXgM13e0cA8fOOGvQ7vBtu8t+W3gYA10bgDsZuobjH2DaoZD6/3ulT/giLd7WD69whIEnp8GgxYhxOb9bfH9dBcL6vMNAEMKsJh8LgcogcKsgpRgg88HXSJYCL9jMDwO3dv44eL1T1Hz/1gVXgHjsc6YGDseRRAYhhOEM7YZ18JdfOLiOIMR7nhCj3FmQuMTemJbjA1/GMu2KcfxWBdKM3g2sR7SoPjgE6jHh+H/fUj/dCcE2wpBM5ASbWOMTZK4SzAuaTkOSVrAIqDIFDmhWdu1JsBzaNsjLc/CHIvBJwD3MNIeMxTO0tTNoA8seZfu7R23v3vpXiUGYZJwkJ2wLGfijHHKZccW4wASs0kH4ATujkmA0SzpTSaAAjcr3Kc+PDU48m6AIZghjIQgrhn4/Pbw/BCgDAVHLqlyNb1/OJQ1LIag7M3VHhWM5+spurIvhoqVJWe4llRfGL23RHHa12MVLNYl3ZpasmKFiBGW88pqsakHDXwS2bSJxK4Qk7F23Ul2uybj1TGmADf2Rjt6uVNn8rHhHLtVJXxN7WpgCpe8jQ803QSCdQzyal2yyp7HbMAtbaGjdXbUyM2YP+RYWMzmMr3eHyJgEquWGY2O5BiPlBrwZFjMcbGollWwrEnycEnUkKdKLPYSoTO7+Ciw59mRZwJ/UctoL6QbKBG5oxKzHQHSvKJ1j7FeRI63fcxQpbdrTEbrm0itNWHi5KWhpRuyzPADE5utX4KO6gCljeadcQj0XXyNsF4QNZTU2X5ROdoMnanyZSbqsSbGPOMcjXN3rLWwOggxx1bXqcPHa7l0FldaheUPk/MiUnPLPJvhhb4ml3NS41m1MfsQ22okdsjtSFcmmD7Ns4SbHxOgN9wkPCtmKe13ltPp1shfcA61qZ2MJzyTWNObaty3clSWbHcwd7tZMalLPChzZ01TmyvOHK3K3FyxeLXvL05OULkWKP1Y0kFZLKXNKRfyA32ZU9ioWkknvRQwxtp1RTW+tlC8jrgUQufRlytFZoccFza+JLTodr/e89buet3WQNAPuM/qE8OmJ7GwHU2c9SryOxG3R/UYFyfqhe6Y01EfmYcNtnNtrmOPzIHYB5XkrOX1EljzFcZOkmZTJVnqSf10wmSXRSsU8tHMt721ljaJWUYOux9lzDVFS4aX2nROzvlAIsrrermfnIP8dA3ieOXtRid0VNBWecGugUHVfBa7yTbAV4aY+KdwF7hTaZxvynMWSFCulK4IJ2lqhylzMo8v3RxXrusJv5zkK3YejPhzP++KfbtQrQKdkbXT2+jo5FH0LHSOWXq4zltRrKpRD2QW25cFxyz2rAjWtq5FxGaedGklBuXenZ6uoR0FZaKrZ6raTtNUXqDpoYshpWPqbv3xvF1OBF+md6ad9zOrPi36KTEH4qq4bFdY6JZSLabaase59owPW3OxFENCrHEj9a/yUj4DdyL2UwYCOdri6fFly69VnhFTHoRF7IQF9JmGSoQoCF4UHQuaSfeqY5N7m9QDSuxXmEMpaMmiAerXsb2ZaZucPSyDw3pCemvlOkqydbb2d8K2Wl2YNkStU7/JsGJ+6A+Kv7Yoh4OtdnkuznPsAhyIsTgjP4VyGOXBZJWATmz9nbXTFkaKNlpMSzrqtv2+w1w+9VAqXCT76/GY4Iuy9y5LcTsbwYWfq472JM+1crA67SbbdsRclgv0wlkGtccWy+UpnQQlQ1pxK84YdbWpdkcQ0BPVEehQSg6hU5/aBcqG8qWTukUwokEj4YsLpW97idhB2zgH0dYLvGc8A2NLPBSWjTR1TVmYNcf8VF2SzRKcpgLNO7tep4nyIq/pJJ5Js3ztOgm7jOP9VVrX/bU/uVy0NRlUCsurNfEcdBEmPSwBR7EE/aXWTXXKrnqlkC+KOB/NShfnqxQLUvxkHxrdo85RQY8dDBUUdcmOYr8byUpVBaLgCIRbWZfpsYpSQV9Vat/rp1ybH4AuMx5uT7kqWUhR4B7QlW6t4rHcs81+OxebE7ug99Zlm1297TEDhubqBLk5jupJ0qHqtp0drzttCrqE5PgczbBuH8iLNXWyZ21Giat9eipOilaRe9ayDwpjavsW3yWRvS8cdTUDTBKesVkiySOHCAPOPofraNLv3DmfFFsuZBWF753dvjwewDVvq4bPqvO5AEdHNSG+wvjoSPYUqpAsDfZUuLOTfQzfo40rimoiNPiBJmDaCquoVhotTAN0lE/5jL2SS7ZecsbFXKYkSo8sudnNM8/zUjOmRvT8qqFr4dziDD2xiOtqusZ9FcsLa6vsTTzbWXKBH0LTmBUzexmK5TUWeIbipGxz0Jqd1lydsJZrfR/O9Sbk6t05Xyebgz+ZXaFSJ8wlgm2rMoamRqN8P5uveoqwAD3zXM1UZRXWqetZUk462C4sv1D5c0gBzUkMVpss9rhhBEqkbS29WY6ntb09EKYVwzItmEXjFsexv22nzgqT1mFjmraqgVHCmV3ixhv75Pp7NbtU02OOtSIRlN7WIE3V1hK8mifu4sLtcy4/XPkTiXmsX7H9lvCngcgVY9GLGoGL14kUUZrKZM58LPTamCJcPUBNsVxOOH8eFJJ+IgkVNnAuE4vyonV4ooHVznX4Zh0vas3zkyk/YqLsZBDnep+sqIm4OGi4o0+OG8kXV+IRY9W+28WzqZ4fes5qp8w8lKRUUjZGmnTsVtCmuzy6mFOrdg/JxeAuxEVOt36MJf7a8OkCJjN1BHZsCAdyHkm63UZJz4oTyXEvhyu1slbH8iq583nkkmySJaXIbryeOO8iqUqZVUWeOnpd8PQ6uRRGUC5H5wuuqIqMsuZ8PcPWEOFMlkaEOopE8J3BnLVyjeaYFrHJKSRDzZdBu2ASP8WyaGKsttZE2gjuYZEqC0Bw5mmzvRhhvxZFX+d5LF8ciCDb7FjC2aTBiHRGkQcxQj6rfRbVM8eeFjPNrVA9PNVg1XJreRnboGSYRehqR8PgZymOAi0YoywxqnJviQeUZlXabnNdkaPW1qfqsiBGwDWKM1iN4iNOFO58hB4Nv1EjJsWqhsiWbsKImLoazWKJrcazyJ7OZ3vf3sx9AjcdbsRHh+WoNTjjFMTZSb9IkjFyU3wWb8Au0QxisyfdjV7ERU2z834pRKJ1DVRsCYFLPaPcFsxjJV/Y9FGvFbOIjEVv492F8AqGX7fcLNpSdpNsZjxxTo5T5nTO4xlYW7k8KlvpYIfhfIkursZFNVorLQ1xva0MXgNaU4nNwlDqqkvW7Vw72D5PyxM8h8AqKJa65hh2EWLxrD4ql9XRXSycax9PJzMKAs+0W/Dh6epohJiJCt9KYUatEpmIMGbJw0W3rCdxNt6jOkesGma2XZNbTt40rcym7iakN9YeFbty38kA9CW9LxYGfeqMvHZimg57TiCJOEKJXZ/pTGCd7QW58qrl1u/QrVCqqWwGJSCwVGiSvltcCEfSFCZMJ1poLc8HW8WxOlEuFKXWtIzye3LcF9Z5u90ctXbeYMEscGhhBfGBgOlnsFem/s7swUrdb+NFXuRcSMS2vlD5xk6npLMy5uuYxZOzt4vlcaFy6NlwtyrWBgIfJtS1W1lkrmv7aRlo2Env53zomqJROUJEg2nSHZgzZ0bVfGUsLuZCpHdYxuoMTA/PJXydRaM2OMvqpcPQ1peXkqFObWtLXBPOFq48fuoCMk7N+QWIm0PdZX5M2Lg3EZoZt1FZ+WyZFsdKsGDSiu+yjMzlaihO11stP8jG3kx3fFCaPowWNpD585ZTtiOg07Oq5c0lzUaSgV/CsXs8y5fd6cDOqnPXr3QI5serzbRiXXXThHa5Q08cf9QvKXM4T0eThtcFMrtG4931ELNLbdGPOofOmNNKKuyMXgoQYhtgR89wYUqflH56oJWFbPDxyZVOl73c7c66Yti95rJnzj5MjaPZa9NLNhKMJhSuMwEn/fUpChb1dWYH5Ribz2lWWJiZER2jg7LoogsEe+XpoI2CyDjxTmWNTOEqky5P4/hFgWWCEpf2nsQDfbXy48vpwhJ9Xl9oEFHZvvEyf7I6ElGNYTZEwM7WXZyvrNQRaUS6BiNVALXohsoz12zIoNUNix3bzeU8ooTLuDya7YZPbSGoy1L2sygf0a7T62djMc9PMW/CfO3ba9xul9Ky5mtQX60wZ5hq2DtaS9Np6Acibq5CEJkRj7KNv2wEuCImfK3vrMYNdjx6BJizlKYa6S9Hfp/JPMXPtMNVVsQtCYSz0GEesTp7mHsgigZTM2lOk+bhmHqzROOZvbc8aejpCHrcRw2KKlK6GKOT82y0K3ZtUXloP0dhfh/IxnVGVEGg6mYUK2GgqM3OJjJ9z3CwC7scM+unjd36Wo3Zaw9byFF74mIS5cpVGk4xinEms7l+7uZdsmntmewEI1umlJqqIqImnTT1T/6sMYBZu3ORImSlLMA0XyqFQuvHZi1412Sm9itGl5XGl8Jm7ZqOeZyOZoB0AbvbFseTdG6Ui388qKpHatt2bEvjIpJGfG24cWnuOINm/MKErTavp607V2K/CkZWaGlOWmyXKsRcmUfHRypFiyUJ5GjmYpcjtuiw6R62DKVpR0owNvtJXyWrur8Aglwc5J1crPHSPFsjNqbBUi2M3qpcSjE2SuleZbRJHbua+AnGcc20r8jMLDZ+OhYyV15ay8U4IUVlF4rECgeO1xnkcctNF2eHaSdAHXUKIR6PF8YBJrVknBnVdZ3iccFp7FfZiZqMZxNTHPPl1aRicgmcnbJw1vg5p1TQz8O+oMtjgTGbzbbtZ9iS8ZXrZq2RCYXacjnnMGvB7NbyotCrdBcd5ql6mu+3PFOxm4t0YeB6VkzJiZFyJiYQS6+WqqSqlfF6bIYulZAOK4qy7vSHNcHs3GTi9ilccBy4iVL03HbCmMv9qciVkQ5ohmFMl4rWK4fc9Ykya9AzT2zn8wO2WjY60Qoc680OXkkM8FKa1dtKd/g9R52keXUhRmqys9x+fGmc5GKxV1DZmCPu6Ml43Va8IbGcDRdYbdEusno9bZQNJ409exFO5+srOk1FTzmr5fk6ATtyUR93hozm1clOMYJZKpPdfFdUrE0d5suuL7yO9QmtL5ooZhyeZJt8sqFKmd3iLYPPO9+FOC09dSxR56jj2CDnp3rNbMfbpuGuLn7Z2stKr9CmPaI0f6LbtTIZ1zIcbbGFPKPO4zbQF1OcuhRqNp4cJ3HvCtko28GaztDhmOCaMyjnE1nfbWc5N8ddb3k+t5P1qrngI9+MxkLRb6QmBiNykyW4ZFuT2cUhCtU6h9HUxRRJP08Jvz1E2c6sLwdlqSx3fdkZrmcncX9gbctubN3VXGJ7PYjTg5ALLLGtJ+xOHCvzdmKFVB7ak7i4Xml/dipnRw6jDkm7ujZqrMdb70Dkgjk1MTOOsuWyS80Ki3lxTOyqjHBpX1FKn0CtZIIdRlJzTHfcET/JGjkHeRxtSqeOmKNKcqSSBxxe0Eujobm9O3fkrnGw9VFMJDPVipGxEneouUnlhPCY0X7qjIu4XSpTN123Vo3xomZpRSSvCCUeq970uDSkZA801yxY1vHU0aa3lyeTPPTHUyqVgiKik9luwquMHeXT6fTvT89PtzPfp1ccYyb489NwNPDY4P+39oX9PszfHiTJMUE8P/3vbVLeNwzfDwNv2/3Acl9v3F//DWl/fX4qnBBKdt9SLuPaf2xQ/reN2c//8q7xQKa7n2YPp5jX6v3QpLL82+52mLp1WRXdW5nF9W1vG3qgLof/bynfHkcNTzc1k3w4t/hBLXgfhAV4q7JhfxZePQ3/gDKczQE3tKr3W/9xJvD85HbQl6FTvpEM/QaKfFD5cTw17OEO51NPv/8/3eSEa8snAAA= -->
