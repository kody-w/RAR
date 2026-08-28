---
name: "rar-cowork-cookbook-teams-update-return-goods-to-suppliers"
description: "Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_return_goods_to_suppliers", "rar_sha256": "8231ae2f140d15fc920f35614c3aaab720b7b672ca0132644cddcc305397c1c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_return_goods_to_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_return_goods_to_suppliers_agent.py` and in the RCI capsule.

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

Return goods to suppliers Teams Channel Update — Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 8231ae2f140d15fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_return_goods_to_suppliers_agent.py` first:

```bash
python3 teams_update_return_goods_to_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_return_goods_to_suppliers_agent.py   # or on stdin
python3 teams_update_return_goods_to_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to suppliers Teams Channel Update — Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_return_goods_to_suppliers',
    "version": '2.0.1',
    "display_name": 'Return goods to suppliers Teams Channel Update',
    "description": 'Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-return-goods-to-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fc853d383a5bbf1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/return-goods-to-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-return-goods-to-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReturnGoodsToSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReturnGoodsToSuppliers'
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
    print(TeamsUpdateReturnGoodsToSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObyLbnV2Hq/WH3wy6xS/jGjRgtCCEBQmIRot3hZgex70tPf/dJJFXZ/fr2m9sTEzF4KSAzz35+52RSv72YTR1k5cuXF9k1U4g14zgM3BIyUwdaZ11WRuBHFlngH2RnaV2GVlNnZfXy6cVxK7sM8zrMUrB8U5peXUEmpLhmUkF2YKapG0N5VtVQlkKlWzdlCvlZ5lRQnUFVk+dx6JYVVNVm3VRQF9YB4AqFae2Wpl2HrQstHTO/36zN0oG8rISKJrQjCEhh+u4rkMHtzSSP3erly8+/fHoJwf3Ll99e7NiswKuXuyhq7pi1e77zZyf2Sia/MQcUYjP1wdR8AGZIwXPuloBRAl45rgc9nz5Wbux9gv7zP6POLP3qpy9fU+h5fX2Z/pybFKoDF2hmVrXrQLaZm1YYh/XwCi3jzhyqpwUmC1VA/tR/faz8TinLoX9OYx8fTF59t/749SUDIpiTjb++/AQBC3x9KZvp/nWikn/86TXOOrf8+NN3OlVj3Vy7nogBqV+/PZ+fZMHE71ND7871n4Dqw5uW+/XlB+Wm6+k5IClY+fJ6y8L044NwXmatm5qp7X786a/I2oFrR3FY1f8W3Z8fhAPXdIBOT8F/+nQ38i8Q/FToneZfs82BW/+OJmD6G7tP0NNQf0X7bv//QjoOU7d6t/i/JPevFsD/hH7+S93+uwWfIO/ry8aNQXKUphW7X6DfvskSs/75g/P95Ydffgek/49k5Kwp7TuFb4mZhp5b1d++/fyhur/+8MvPH5ocxBpIpW9NGf8rmv/Krnc+f7Dgc9bHP64F/NU0SrMuhd4jHfoty/9H+fsrpJlx6Hx/X32BfsyX6YKhSYk3pg8T/JAzFZD1Bzv+9PI7AIkUaNPY92GQ5f/xH5AQ2mVWZV4NyXbW1BBwcB0m7iS8EoQVBP5OuV26wK5VCAz7nAfif/LwJHHmQb/+T/uOl5/tJ17O6gl+vjV3/Pn2UP/bHQC/1dm3dwD89RVSAPWsDP0wNWPovJSkrynAt7SeOOelW7llCzDFGmr3M0Cjz9MNwEno13+Pwbc7rdd8+PWO6uEDqc5rbkKpqond10nTS+CmT71sAMNu79oNYBNnNpDJCwHGfgIWqLIYwHE9WaWKwjiGnLAEJsjK4U4bWO7LROzXX3+1zCr4mj5gFYcelaKagQnv4kCfPwPlvDj0g/pr6tpBBn347fcP0P+C/rtVd+ITDwlg/NMvQMK9fBQhkGdNAqYBlwEnAxC5++W3358mBmRSUNqAF0MvdB+LQZxGrvNmb3m3/IyRFGS5wM7AxkmelTXAaiisXyHOg97lBUynoQnNg6nCOW7upo6b2gOgagJ13i2ZZjVUgWCsvOET1FTuneuvVmneRUxAwpv1r5CwlkDtyOKpNJbPWgIWZ2kIzP8eDY/3gEj5oYJWbyReIXGKTCg3SzMPSvPJwzMffgE14205IG5Cqdt9TadK6U6muqfJwzxgErCM/XTp58nnoOQnABOc6o33fY45VTjlXunKr2n1TAGznFxhg5IAmPpN6EyF4R/PkKqCrImdu/2ApBOlpxecp1fuMXj+yybh0VSsn03Fo6RDXxsMQQno/0PnMQm7ZNkzwy4VZgMxonK+Pow49UiTsR9tFaj/98X3hPneE7whyhuwfk3jEEREOfzjMfNu+uecB1g1JbDUeXm+0wd+B0ac6N7DcgqzspwC2vyaviH4J2CPO1wBC4AcBjE+6f7GcBp9kzQAiTo9f6/mdzcCtYHjQehBeWPFICw813Usc7JBUE6p9bQ+iFF3SrMuCO3gD1pBgDoIBUB/ckMIXARQ/m46MQNqgqzyyiz5Pj2ceiQghdPYQFrQhLqv0AVkxxQhFUhJ0OhMc4AVPtxJQYkLbAxEfLdwFZj5Q5ipb30KaE6+yJIpYH7wwHPwezzfZZnEB1RNEF7Alt2Eso7bPzz7LufTV0DYZMrA+6I/uvupK/RjqfnH1/Qu4zuwg8SOpyr9g3EgEIAggicknXCpAtiSuM8AApFwL8ivj5r6KNrvsnz5U7P+8e/18/cqqf7Rc1+goK7z6sts9qhsb4XtFaDCDMRImLvVo8h9ftSgz49c+3zPtc919vk91/5A/WGsL9Dfk/APJJ6h/QVCX5FXZBriQ9udYvd5AYOsP6+un4lpdEKW755+hsOErPEAqup7mXmbAmqNX7r+NPlRdqqpWnWgQN5xFvjia/oeDc9cmVDHn2pklf2Qw/d6C3z7cN17OQBDaQ14O1On9tjIxJP4lfvyJW3i+NNLaibuv7mBmWAfxOz0ALY+IH9A81OH7v3pvRGaHv64X7tnFoAEJ/syJdgnaGpaP0Hv/ecn6G1HcN9npQ3YEv089b4TSzAV/Hif+74ZtNwXsA2rh3wS/rHNmVquZyv8ZyGmvAIS2251h+a3RJ04/okIuPF9t/wzkeP9xoyfaAFQfSrMYf2W4xWQ0wFtzicIuA/kHkgngJINWPBnNoBP6QKoB3A7qfvdft/Vyh66/H43Q/3YK/728oYaTx88+0IwHaTn52qqgTMQqoAheH4EFRj7v+wYn1QA2oFeBZBZYDhqupiHEoiDkp5NY4iHkxRK2LhpmtYcQ6y5Rc0x20RQHKMIwnYc28YREqfnNmrTgN4jQL9N5T6cJHMRz8VpFLMdnMJIkqDROWbSjknMTdNBFos5MvccUBC+L40AVD7Vfag32fK9eZ3M8tT6txeLIsDMHVFxy8e1ntGaaV1m1jng4TKG+x6nTriaq1jcSYHOwejuYuvcMtkYPBJWnIatL2QEwr5ZDnp9EMaNdN7RKw+L6W6sFpWuWgeF3i0JkfGthByc1MB0gySNwylcI3KtoRe10Soz0uIzi/FZJhTo4UATWWPtQmuNjzqrh/BwAMOH2WxWWO52PBiXy5ZeHfbxEArlVdmf9SQ9x+2+KK3wEjslpx+DBVJoQpEiYF1ayCMRjKKRJ/tcblkMrZK4YLJaGzL7plKelKLorFWQ0YtvtjcPR7PyTrNtUqrnMFsf2+AwlLUco7V7iVGt3PDblLuwHrLhaY05EPyFVDvXUPJmr8R0zij6MRdEmTsVq+O1RPmeak9aQdqUNlxKVFOzNNZO+t4wCW+43ewRVeu4WMa0TVyXZr6gBYC12nHnjjsLrefbnm8oywvpvV1oYxJeD3MmE27D2DmEHjnGmJ1lSpcvIt+j9PpU1c4YgaY9bvZUaUjomEaMuHcsJMIbtAvFxp4HVWCz5KLWr3FiKrIrROT1AFMOury1ehHLAcwy9QE4ujlf+qHq0MHdEFf0Gol+ASuqW19h1NxWhKyi1GAa/MIaTXU3Yi1CNprfSp2009hI1E57cnuw05NYwqAnb+wQc8rU74SbiK/p9aJuXAnZV06xXWMUfkOMisW5rd5YmUEmAuPcjlzHG0Eqb7P5ducl6RZLBnXsHQavz/Epi5KebeFK0SK+IoTdTBcSobrOiOSGdmUO92fLlEJJPAEhjuv41rAXJCA35MydV0bBO5qqOTfK2ltdt3Dbdc/2ybAMnMOmKQt+SMSz56JbXYsPdXHJ4/yCajRpk5I92/Z0q6LwRnbDxWyzgplNK8WXPVHKqASvhAWV4LOOmMm1u7w1FCxlAnJUiPIa4l1oxnyYzU3kFDZaoZmRvmau3j6o1At2HXVsfw4FNh870WY4uz5gp2SNDLV29KktyqhCZJOj2iW8hifbEryVmeTEnDbOOd6pWzZSw7PYC9R+s9oYBjdv1s0pOFzOZ0VMXJbpbIUeKZ0lLjhB0Y5zMER323Nc4MoDp0ZEvmLia2pG3ECzDS0g7WmLSzG5GEetrm6RmBQYrPiCVaoZiR1m3Wyxis81r4vFmTnDuivglFwQlRbDgn+yUTVZWhdD0hx+05+58Yb5h3V5RZYXP4Xzi0fYmqjSW2HGtfJ86LLDeWBxmttIFcrmtM8jcJftKeuSXpDzaj8aFMzbLYeqF4JQ8UO2Wwz52TrGRqtcWgRDM3lkVC1l/KEQezF1xT2HLovjoVbFmCe3BtogtlmrwpqWGEbJXG+FkjJToaBVsG6HNT9me3gfY4OzXlhiy8VsoZ4VbaR8VmMcI+ZXTb3YkXCaMuhVMxd2hiGcFmJJTBmat8ZYhjpfmChGl7XjGkhf6kc1KvxaVPhDq6AdQrELk3L11QEhr3hqLXJTsXJcCn3Kuc7Nwkz7Nu6VLSHZR3llxH20x/1jMlMvojccLFSuTRpjOBfdbGHcg48rf9YwkXRahRKMcMbSElEvyXzYXs2RgtXheKWq6TkM9un6yFLR0tSKcb9i+tJdAOqDE5owrG19ZpiX/UG2pQXstafEONz0OolbCj0qhpPNheXcv8bLDSfP41XjddbN5PMZ1bOaTwg2ExwU9lxGBIVZTl0fcIfJWUa+rof6UHGNShzN5LLnb4JL6rdQ9fdX2TSGNLG4INb7UcvOHb5sg3VUFgkjpsuLUN6ww1iR+GlseKHfCBQFj5aBeSmPUl6EZN0hEdCxLOkrmhmDe5pHZCum2XVTqJddetMHQl5c1J1lreGuUbdr1uM1oW3L4eqVXQHAdhgDV8xxju9yEz9etPmQH9fuUp0x/nZzadxB6Ao/amj9WESjvxoXOFqNsgJAQuwYczDD3vVLPRwLuTqYkXyh6ZN2YM7iNZwyfLdRF/sgmHEMvN3mCqvv0PXKxjQpYHiwn7vx6mlmbI32ZDoioe+2e9D3aGRwkrtqXvO2zZzzs3xIQqLbFZttswLNlH/RFdFVsDarDf6SaPMK82TfP+3Z7QAP8XjjKGyBECdDEYxqFEGeBbERSt7RMBWaQw6bHdgejs3pgJU8NmejKBqbHu9DccWpqZyDfthIXQsexP7Yb5BC3KcLMW28m39BblusOPLVrUfEa1IEQkSz3mLnL9tYBtV9rDI7SaNwtSD2UhjKZC2q2CnI5imIHq2R9SpZrlfJ7XpF+5t3Wm/HDjSMZEEERLNAr2qReBtxK9CiyqCrqES2yTIlxOmoL1THi2vxGBwvmdUNK5BVnFHHplBAMa4ICx8FpVwJvqpIo002nkDN9b25bPZIpbJ6IOAexm9xpzMOiyTi82tsBMphtaMTLhH2c95T+tsl4uN0vqlxKsRTzUaw0IijPczDKGrEXHB0MHGVryhj1IWSpIKauO3VfbuOxQsR1BSIcukM2sIsyw+SYFeJHAsJshBUyVzwG3Zdra96yM5XLXfJtDW63bLpKZd9qgpzi4tWGZwLFyRbzC9evuHC7d4XJEWaVS2Gkh0SYdeM3PJplS3jfjNYN98Z9+Mxt+aIzp1h+OjlACVX3WqtLKOLP69W0ZxxuL0APL4Z840167dRM2tvSu6kGU0MATsWlgzjRnsMzOstZ24cq7Zgx8ScHF9gqFUlCPxYsZhm3zJiF3Lo2jCD3dW8UZLOL0bB9BbmsBLEkjk0BlbEl8TzydVm6gI5K5bLrNnk2pof5oa63dPWAR+bhI5BS4dYgdto/G3bVky/5I6nWdGQhsrCORP5GWUr0WXVrq2aQU3COew5uwrSPCKNTo6L6/bos8f4uHIvJ7Ml960qik1dJJxBV1pCrHpd3JMybF/R0Fb44RK3UQfvDNaGi4PJlPFurY3R7haAKOaEZbrKZQNTAmJNmQc3Hw/g/7gjeU0Be9iRwxJWT8a4Lzzsttss1s15ccpcpwpb+qiwJ1+nK8od170oC5e9pBVon4zhEVRle457nqHsMF8V0OrUsBvnRC4Mh2DFTLJcsQwSZXspQ4ljMoxjiaYmUFpV613Pspjj5JmS9GOQekMuH7v57tbHZAhLS5GMzwZoVmUOy8+DvRZGTF51asgL8/xorvoqPobJvikGlWkuEbmbB5tsj0tHeEG5pQzqhI0ffYYEPe7sVMhl2mjNEZbjzK74RZOjALuKdQ0KSiAulu35KERLTF4L9QqNV61cK7aEIe2KF0+Do8oXhatIhcJ3PL+e9zus5oiYvwRHAcfVUMUtk/TZ6pyMe65sC0U+njuYu3iH/SHCHdVSQ8+B+RDWuP0NJ530sq/hs7x1t4qmUwZzuB4ITM0uB58ONIWYg0jYN8sD7Szogc/9bHWjhDYXLF9kJXIoCcoicmzeypYKIoM97/y6GjK1nEVuHuMZTKJUQKY6E7KrAMVWOZyumHaph3lsIDLmZFUte8h2xQ0tLVfbTOYkXrzlpL7P+Vhx/X652yyNatlnWZhyzOywMEox2w5BOtiJ3seUpcxpWSuCTXHbwstVwsJaiu47JxuxY9f6crTlGEVKDLTa7edUx0Vdd2iFytZA4i1c5uqbOhkkqCHaM1iZ73QPI0LqkPYr3UtEW1THsTgWfZsgzEnkcntPwojkrFBncVCNuPNqgT3NF8hRBNtnFSZwUtrO+fMgzZtSE8fGafmYMOea5MQLia/mVIxXejMs9I5U5zF22QQWinf4RYhO+dbUneZIlzjKlPmu3nYJJ+1b/7S+5UWOs7qknLzLdXRutVYr9Co+ROckTzQhUYgbRrSLOmBoZgmv7W5dtGK/2MEqnjoLedlZ4WZ2Q8d5gmxhsqDm5TqlrjQWdoKFn+ddZdGFPIuo0tM7YR/SseU4p/p6ksbs6PS8QzpkUwWUJDHtbGY53uLsIoehzWAgBlx4BDbU5Q7XpVaGW0HdGXoaKbmFMGSy5Y5+seBZ83o62tvNCAJknhJ7pFNkZeNTqD0UXWQy/OmWjwMDr7bqLhYJH14S+c6/nBf2fJgpcmmMbeAEnj6TLMTdBJuYqmO1O6s7u7HwVDoKRiBUA81djpfOmZ1vLHzl0IWw3NU9hnRbSoHXhDXns23KUDxGnF2ArXUDnzzyQMqkRKDqPkiLdeRRJ5pG2E1mVNXel3BVC/eDG94cFiaxYJY6XuH1lecQ/Wmbyrh3UkCvp5P+Qmt9+BjMyX4xIhijW/X5CC+rq69UB2ouiGBnNmQ1nY8FuffPLk4F+G7tkm5P4QPmXffFkpHwY0kutmtvfW3iDMTa6J9XRAR33qnYFsI8Lukqj+zsuN5s4PZcH1iK0/SEdhue3FmnDQHgaSfF6lUgeHN19OiOEqLZegeeFadH093oS+Khjxf7/TVAHXQRSzQhMLpOnANqR/lSsCr3ZUsPxs3yO/944IVtslYyLEe2W5+sLsteCVy83aKKgl9Nuxdqb3Ww97jadjlcN+UR384jruoZPJwZIyJX/X6V1VtpAJ08OsNgBjY4HsXcqzLTWLlPKeqmGzN7fugsmoh4zp6fUXWz9Lph6SzsjdEhG/i4Y4xy1bEGUIAeR8k2FzctwI1uc/Mrdsgw0rcCDzGawInGVnckEKgoGbHH0tFvjK27XeS27XDaZ/hyJS+yELjn6F3xa3JearJEyDRLIm4dNdIN0auD4dDaCPvjpoJj/ETgA+clVJnsCZoacHexHMU6ntkwSFxc9/iuXbVpkDaLdqdlLrK00dmSEXWcr70oYefoOXNF0DOf6Rnc8E3dz/uEFywaXs9mfM4eRQXf2SAz4KRkVZ4tNu16y542aVCUTVANM+Qi+miC3nq/1nVR95ZaqBPRbKMim848RbSO9wgyw9lwn9SulRD0MiaxGOMt79Is9OEgILp/U0JRzgHYLTZuMJqLEyOwKyReb8RRMQaypxgnuZSUpQpNgs+tEp2b80I2eoxDuXUnZrMqp3G92EpGB4NNUVNe05aZeVf3urwcl0fCjdcYtjxaiKGSJ6kGbdqYbYSdYxw2m7le94W6Ex18f/EplzxTx6rrXAd37Z23wfmRWPFZPRetoFVsbIcdlYNjjddgnm5nZzKaKajnXtkbp9ySeEwCmWx6orqq3hCvComIBRLFRhhd+JuUdpoleVrbNr/JZ901POdFdVqmFsUGu/B89VT3rJCZxOoCN3c9VBx3m2uMX0iUyMrSlU6ef9HaLCPy5XL5z5dPL9O59PN0+W9+Pp7O+v6fHTk+Tgffvjjdj5bBruHLndeXvyvYL59eSjsEYj2OWKu48Z9Hkf/lgPXzv/e1YqIxPL7OTh/J+vrtWL42/elXjV7C1Gmquhy+VVnc3A96P71YTTX9zkP17Xmg/XJXMMmn0/EfFfp+ZAqUyc3JrPcvj4kLdsj34enRf547f3pxBuCu0K6+4RT5zS3zSdvn5w+gJPaKvKIvv/9vwDd6KMglAAA= -->
