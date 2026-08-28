---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_materials", "rar_sha256": "605e7abd8187fc259558d99152d3ef84f8b8f5c918501c915638cbc0ee8c68bc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_bills_of_materials_agent.py` and in the RCI capsule.

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

Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 605e7abd8187fc25…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_materials',
    "version": '2.0.1',
    "display_name": 'Manage bills of materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72b9e7b8cc16d629',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfMaterials'
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
    print(AdaptiveCardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOj1rLmv6Kp94PtR3exiUV9wxHDogUQQhICgdw3yiwHhNg3CfD4f5+DpKp2P1+/uZ6YiFEvJcQhly8zv8xzVL+9OG1zzquXLy86cLLJ0kmS6AyqiZP5EyG/5VUMf+SxC/9NvDxrqshtm7yqXz69+KD2qqhoojyDj2+r3G89UE+cSQXa2nETMOF8B96+gongVP5E1rXNpM6coj7nzSQPJqmTOSGYuFGS1I/rBlSRAy/qxmnaehLk1QSkLvD9KAsnUTbxnfrs5lBY/QnecKIE/oRrDsBJ61doEuictEhA/fLll39+eong+5cvv714iVPDj17ezRmtUe+6+VG1FqjviqGIxMlCuLboISwZvC5ABc1I4Uc+CCbPqx9rkASfJv/5n/HNqcL6py9fs8nz9fVl/LNvs0lzBpMmd+oG+BPPKRzoZ9T0rxMuuTl9DVFq2iob8aohqln4+njym6S8mPw83vvxoeQ1BM2PX19yaIIzYv715afR968vVTu+fx2lFD/+9JrkN1D9+NM3OXXrXoDXjMKg1a9vz+unWLjw29IouGv9GUp9RNcFX1/+4Nz4etg9+gmffHm95FH240NwUeVXkDmZB3786a/EemfgxUlUN/+W3F8egs/A8aFPT8N/+nQH+Z8T5OnQh8y/VlvAsP4dT+Dyd3WfJk+g/kr2Hf//IjqJMlgK74j/S3H/6gHk58kvf+nbf/fAp0nw9UUECczuaiy9L5Pf3vTtXPjlB//bhz/883co+v8oRs/byrtLeIMVGgWgbt7efvmhvn/8wz9/+aEtYK7Bkntrq+RfyfxXuN71fIfgc9WP3z8L9RtZnOW3bPKR6ZPf8uJ/VL+/Tkwnifxvn9dfJn+sl/GFTEYn3pU+IPhDzdTQ1j/g+NPL75AlMuhN691vwyr/j/+YqJFX5XUeNBPdy9tmAgPcRCkYjT+co3oC/461XQGIax2NRPdYB/N/jPBoMWSzX/+nd+fPz96TP1HnyT9vHiSgtwf7vd3Z7y0P3j7Y79fXyQGKz6sojDInmey57fbruDZrRtVFBWpQXSGpuH0DPkM6+jy+Genx139Tw9td2GvR/3rn+ejBVXtBGnmqbhPwOvp6PIPs6ZkHWwPogNdCPUnuQaOCCNLsJ4hBnSeQ4JsRlzqGmiZ+VEEQ8qq/y4bYfRmF/frrry4k76/Zg1jJyaN31Chc8GHO5PNn6F2QROG5+ZoB75xPfvjt9x8m/2vy3z11Fz7q2EKaf0YGWnhvN7DS2hQug0GDYYY0co/Mb78/MYZiMtjsYByjIAKPh2GmxsB/B1xfcZ8Jip64AAINQU6LvGru3ah5nUjB5MNeqHS8NfL5Oa+biQ8KkPkg83oo1YHufCCZwe5Xw3Ssg/7TpK3BXeuvbuXcTUxhyTvNrxNV2MLukSfwv9HM+yL4cJ5FEP6PdHh8DoVUP9QT/l3E62Qz5uakcCqnOFfOU0fgPOICu8b741C4M8nA7Ws2NkswQnUvlAc8cBFExnuG9PMYczgEpDCv/Ppd932NM/a4w73XVV+z+lkETjWGwoNNASoN28gfW8M/nikFh4A28e/4QUtHSc8o+M+o3HNQ/csRQX+MCN+PGF9bAsOnk///s8hoO7dc7udL7jAXJ/PNYW8/MB2HqBH7x9wFB4K75Hv9fBsS3inmnWm/ZkkEE6Tq//FYeY/Ec82DvdoKArfn9nf5MA0gpqPce5aOWVdVY347X7N3Sv8EwbnzFwwULGmY8mOmvSsc775beoaOjtff2vs9qhBFmAcwEydF6yYwSwIAfNfxYmhVNVbaMxgwZcGI6O0ceefvvJpA6TAzoPwJNCKCtQNp/w7dJoduQpiDKk+/LY/Goal4xNafwCkVvE6OsFjGhKlhhcLJZ1wDUfjhLmqSAogxNPED4frsFA9jxsH2aaAzxiIfA/7HCDxvfkvvuy2j+VAq5NkGYnkbWdcH3SOyH3Y+YwWNTceCvD/0fbifvk7+2Hv+8TW72/hB9LDOk3vqfgNnApMyre/EOtJUDakmBc8Egplw79Cvjyb76OIftnz50zT/498b+O9t0/g+cl8m56Yp6i8o+mh1753uFZIECnMkKkD90fU+jz3p86POPt/r7HMefP6os+/EP9D6Mvl7Jn4n4pnbXyb4K/aKjbfWkQfG5H2+ICLCZ97+PB3vfs324Fuon/kwMm3Swzb70Xbel8DeE1YgHBc/2lA9dq8bbJh33oXB+Jp9pMOzWCCtZ+HYM+v8D0V8778wuI/YfbQHeCtroG5/nN1CMO5tktH8Grx8ydok+fSSOSn4d/c0Yx+AWQsRGbdDsILgPNRE4H71MRuNF99v6e61BUnBz7+MJfZpMs6xnyYfI+mnyfsm4b73ylq4S/plHIdHlXAp/PGx9mO/6IIXuDVr+mK0/rHzGaew53T8ZyPGyoIWQzavR1veS3XU+Cch8E0YgurPQrT7Gyd58gWk9LFTR817ldfQTh/OPZDJr2P1wYKCidrCB/6sBuqpQNnCluiP7n7D75tb+cOX3+8wNI/t428v77zxjMFzVITLYYF+rsemiMJchQrh9SOr4L3/2yHyKQYSHpxeoBwaowDjuD6Ls0zgEdSMolh/NsMpwidBwE4D1mUDypvhLIXh8AdFk6znehgArEezrgflPVL0bRwAotE0gAWAnOGE55M0QVHTGc4Qzsx3pozj+BjLMhgT+LAnfHs0hmz59Pfh3wjmxzw74vJ0+7cXl57ClatpLXGPl4DOTIex1m53tmYDHdjShc1lfWe0BKljKyOrI4Vh6l0gMdnmxO+0OhSO1NwOF7UtxEm6OV2lHfAkVveQWXvj+FheN75Y+kDWpVvLgKtVo8MFJ286J+2jWbwufKUTq3Ulcuv65JhKZc1XCDCrZV5dks3J3BZKtN+cinZtZSS7r7D2gOdpv8sLHTfdZbqvVKQOqJIKBKpSbgquUqUVNHaDtQKuKo1NmWlbsIq1a400sWp7ftPYJYfzCWKzU1f2PWIlEVo2YIxG4gSqudiSXNFsTZ5m9GJa41KkWmnCxpXUJuXJSDw3Sdqm4Y/yWtCJggimJbuO24o3BWt5OaggWYtgS6r6ostW7GLe5zGdt6ZeaZd6Zl83OqUkaV3F6+4qrcO62ccXfq6V+0Axz6pNxaVpFo13Ehyq0yql2Vz3jrLNhBzE1+lVt5TEo/JU2O9VUWBzdgUW1Oro0fNdm2BJmCYzTp4Xt4NXqFUNodIjUJFZPJdlz40jIgwV5kYP5ao3p07GoUvrtE+vJ0KNKaf0eGrTGaWpnA9Bddwl/aUkpcQ5tY5NaVva5u0UD1PyYBwbu6WUBcbqRkL3jrytXS9bWfRF702RA1npa4IvOdN0VypDSp8bazDX+JClA86yNB+HkUCu04TBKXRXdgSTr0+Mo+7pqWOHlHVC8GzpuSUezbl5FWGnZXaNE9yph0VFAWmVHUwsFRL7MC1uKOxIaidl55ya2l6XXbbk4laluzZL52sxaLtOmxteFhU2FSWNBHaIhyAVcYpM87jI9pgvu7cbC65Cp/TbOb+kje1JQs66K7VrvfTaXDkGBi70qWuc8OLQiIN3WCl+ZE61zVQ+0/NsCgIb2buZHikGym7xS3TaXhMEiTz1UjMGXs8RXtyfgmgbXVxeLu2rsrqYB6lKvCQt5LjfEvGNWIuedLrNIiMT+TJkuWzvKjpiSrygDAUl5P6ZHEqLO1nUkHAdIeUVw+NCoZk6E/bcptzk5UXGolC/sNYm4qZ7YqkvWK5IpeicGEZ3ynTN0+Roypp9uzDclTVcyQN/RRuRlnsB7Fksm2/zTJXSYqZeT/1VNGV8vrVZbDVsN0ei13apc3UpbcG3hX7ObAYV0Q5Jl6zpLWVZW3VAGoJCWUf40Zre+LloCvZ5c4pnJjZcF/OLtnW4QmsuNh9pCp2c0Gi6jioa36q7rS2YM1HZKmfNLBslyVOPlgd+V3onKmUQS1go6I4peZvcR/kwQ1jgS4lnTpmzuVZXs6IPMb9ytdQMuma9y5g8zqvthdGBSWZgI6vKxnKXl8rWNdPyVZmi2ULgdsPAyzAHQj8wCA50/rrsluZ6qvjIrrXsxXS2Q7Ww0ql9Kc8rXBqk+dJUj7J7qMyBCIwpO51SHGo1oVO3omBFRt0Q6WblnA7yvOkFfxW7J/uED8VaMKuDESElpnlG0WuGDyuBKxcbcOhQY3Yq6zM+sL3ma/EWZ9Oe1eiZnBgrlpGTU9Ilmyvnn9tp7SDYjigpgDHh5uzTiDoj0FkMBMSnPK288Irf+wm/CY5HJ+fpC3mR5+p1JtJoIVx2nrijvGZQ+VooVUMHdWA3mbGsM7mX5Bm7dtW1nJ0iQ0IuC3bwziodpVGmJRmVswR72wGMs8J+xxV9ZunyGc3JG9ZI4qJXC54LKTm3k6m7W+tNc2SrQIB8uptzmJ4urGOjmopYn5Joh4qJK7CemURC5V40DLvtPSkjqq14brWtKNsHQw2uGlf3x1XdaoesRLZ2Psw7dH+0ESSwqB65rtlkrgsOn1ae725caqOoUUUNLeQxfXM+EMM+txEHAYvtIuUJglzUqz7PdxXFLldIcs0HNI5222scoWAbmWKno8rysk9wgJRDGIcL/SbRBtasUmW+MObpquyweepz4Jy2SOTo5iGQWy5yROOwZhep6iqtQsrlXi7IjjelvUEejpEOuDzNzupOo28Zkc8Uu8/p4iBGUoafUjpaIGSRLLvj4VoJWuAf1uf9SveW0iFhUt2rMbaIFCWd5/0qEldgKGOCPwab5hLhijlITm1lS6TCbm7I2XvnWFMetoncrbwSjhAnqszD7sJvh9qqjZtMnBuALgYz7MPjyZ9KO2mmbxaeU06jYoXMmOvFj9bt3FnINzc4IcRBlY5WPY22ZwBZdVYvB51J8/QiIudFvVAVT7ku982MNPlkdyA5xjAOpFmURCoQK81DCaKB9ch3oX7DcB1t53aVdMo1tJE6rWI6kmcVV8gqsi+VZWkXc12UrHy74sWbOo1SEGHDEbjrnj2LFF8eC4zPpriVmMWslPKp26+kbOBXnHFY3bYUedVoypIdrpUD1Vha57UVCGuJ6KaYWUlwIxys51dMQXwiSI2zw13JphHnm8hojteLQM5SWZkZ64O51nJeGwK6LQxZpgatKzfS6rB0usTYmtnV45dnfGoUCrqcr87kIaYWdEJH0TxCdjsqESg0M7hFse27tS/A2r80YZuuj9NEKReRIG2S837B46dEGEKpsRh9er2c/YiZ5X18HnaCX+AIExIYD9ZDs4m9y2LoTW5/4Sm/Wfo+j2rF1mmjsKeva3k3Q2doEG2ufRca86wy4hVsb8ypoVTpktDWVoux23W+1BkE2WhJCjJybuW9dyiPJGPQ2XrDFRLmcp1JtW5nzLmDbIRrntdYZNPgltIfeTTa7OKjZDtLiY7YGcjk2U6+HA3ZbvzQ3Gx5g572JKnZwC6xswgHBp/vfAduoFbBJSwO5X6J+BgTmQJl7mmcpkxNo5HzvubCk4goTJzsToucSm5aKtGLnRWl5X571EQBDhY7m6RSutgtVoK6wsOjHgPKijm6oGK0XFlrnTrYOKrogxdepezWKAEy7zLHOURNoKshthw8Oj+ZmL6hUy8/7jQmolhsF57ky6LL7dSIpxbXrKNTr0SzQtX2uE3JrjrFCi1B673Vie2+8DDbDsJE25Yr8dCkBlr0kSpw/nIoGXW9MKm9uc7zPFQJb0+AssrAwPiCa6zxwyEuRCaXMdGiUvJS4+GmYa3catXAXRryPoc9TyMu2UzXDWtlM3sca5NlOY33ZJ0GUenMpueTcbpOIwHwvhkfDEvYR8a04BuYOQvxLM0Vn9RVQyxOymahmp5uNCq1qVJX47RwJyH0cMoLATlhNgFuzszcY2y2WixyeuMI7gq2DTg3c4u0JDIBcEp7qDSHSApHvPQCk+jx9IhXZbRQznM2d422oPTEbGowX6DXrpHafo2ZnAfJlo9PNaE2Ym8f1PR2NoMDEntUQezoo67jWk1LpDsHDLJLsHxXbpvYFbX9GgNxz8QpT5L5TYnNnlNW2/OxStVSrbyVys97ahrX1la1B7Y4b7MU5SxDjBZDcyLoQzloGJ7vZcPbamicxCbsT0i4jC2kLVOyXHaNsUPt5dIa0pTeIOLMPMppku3QAvJ2s07nkEtQHU7PiqSs14cCMkexTg7eruMYkdvXqy7P2UyaRwp2ysx8EZ3T3kutrqBdnSH0fdmK5YUz97PNeqVsekUrrsbxJuuCJyzSs8oS4qVjl7GZG8khPQLuFnuONmN3quxhg1IL7fHiqhc7ctt+Qe/SwxUH8mJ3U7dNaJkmG4cCX8hVxm+JYp1Fl4TXN5oh0gXoRT8FkFaL24mkEXSK6qW2JwOTKhpAHZmWXFRdjDK3qVrWgJ6R2B7xRDwgqjpeCkNzuZFHNdpVq3qNry+W4+mR70v7gvBF8ZTtlpZE1KVP+0N9s7L62MZEScrorfcjiTQGITrK2H5gA/ZYRyDijjfNPlkWPUVgLbu61q+56bpdIGccZ3ILsYzMdSruQrv+8TxgLgnornZnex3NjtXaumFy6idu4IbKrUMhRsz8SEcMjtQ8rW2FKzo7wX3yTnOS4zKZWSiyzqY0AMSMqTKCOhi03Fxll1ZuCcbNNnNjFZ7gksiCe87VRkd4Z72l50w0l/nrwOqpjds7zfNbYX6mzggnL1fUZhpq3CBnrMXbR+RkVZFZd5jFketKzcAF7qjEVSo0yXw4GyuvrchkpRlwMKr7TSwqcD5k824I1EiHoRYJ1HVLbrZEeW8zW2BCF6EyE0hXniKOuCVZs6tXgEQ1dSE+UMsbw2yRdCrymEqkKrKkSrm4dMgajwGTlNuZb9IVSuMoKS6Eo8+Zs3Bec/giFikKWXY3zQVB6rPdnNhYJHGmLnPdD4/kIm0qhrAK5rpsrI2DDyFlY3RHzgcE8buW7JfuTlJYXiPB2VW7YxDZ57nk2eqhdb2IEqTMvtC0jWZVkbTzUMSHo0wjomdsWD2/mhjL3qYbzBa7IQrVQKg7mjuS0Q4EnMalKEoqx1arpy0rwPLnmrAJ5hrTQ4xQIyNRhF3ObTi8iri9sNUZ2fi17K1i/banwuYmmDyhUWq9EsIbebOVskM39NKhL3YsWwyytwQPE7H5FU9I9zis/A5OKulUdxEQx4Tcni5C4E+1PvDafjcVFV5bmVS3QijPZzd4twpOV2+2cTYtqy/mWhA6F5EnUfPCrPiwUubilhpskbfbsNg2R7JFGirCV80VzA2BstdibW9qaGRNb61NQDl40Vx9MtDrXlyZbdlF2joreTJkWiFQl6EkDUgkiVdvDbJzuN9tYxtN91jQcIp2uHlX3d/7MYlnCyoG4rrxqzO/FQSsIZDC2wr+KSBJlNkQxyDYwKqp0kvA2GcuYK5Zi5WrlHOJzdT1boGSmehUUknYORGmTNOBQjqwbuuO6vLZlgQoHwSJcVmpBcO7QXe8Fs654Do2h5syf8kVrFMyNmGj1HpJlhdnb/fHqoqr605BKvZwPZcOby+UHVJVU9rxGH6/2hyzLVmDmc4OEZOcr9VwVKgU2OudVnXL8zIlNINf7ZgG4TjnImCJIG6Gw6mnbvTcT49V6Rpqm5KVO5iMw2Srw4U1y90idPZXX2SuW0MAQ8hqC+Ad8Q2QERb1bnytcuat0RZNLdbktM/7MCgHZ5/ulgHRRzuR6a/uBWaYXpWHBtxm/YB5p27B1gwJh1IZndHSAaYEak7XTNfs62iOtZYXDNYpcklixicN0iWn2U3lDitUlDJ/GV/MprenIZsImyN6UtwDY6nMkuC1puumYgV3dGpPznJJlzCclHaHesZhESLVWhmoORszFwbPvUDl/eG4sqmVzuCEZlk2uKA3ob1VpJRGMcdxP//88ullPJV+ni3/3W+Tx4O+/2fnjY+jwfdvnO4Hy8Dxv9x1ffnblv3z00vlRdCuxwlrnbTh8yDyv5yvfv43v64YhfSPr2vHr8m65v1cvnHC8dePXqLMb+um6t/qPGnvB72fXty2Hn8Non57Hmi/3F1Mi/F0/DuXHqflUZi9NflbBZqoAi/jbyqMX/8AH84M75fh8+wZru9h1CKvfiNp6g1Uxejy8zsQ6Cnxir3iL7//b2sTbmbvJQAA -->
