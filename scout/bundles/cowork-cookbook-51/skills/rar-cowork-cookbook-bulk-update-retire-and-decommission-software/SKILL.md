---
name: "rar-cowork-cookbook-bulk-update-retire-and-decommission-software"
description: "Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_and_decommission_software", "rar_sha256": "03ff91685db98437596ed46ecd224b2f0b0e38b35d60ffd43c1942a9948882c5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_and_decommission_software_agent.py` and in the RCI capsule.

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

Retire and decommission software Bulk Field Update — Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 03ff91685db98437…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_and_decommission_software_agent.py` first:

```bash
python3 bulk_update_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_and_decommission_software_agent.py   # or on stdin
python3 bulk_update_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Bulk Field Update — Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_and_decommission_software',
    "version": '2.0.1',
    "display_name": 'Retire and decommission software Bulk Field Update',
    "description": 'Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca606ba475434478',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateRetireAndDecommissionSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireAndDecommissionSoftware'
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
    print(BulkUpdateRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816Z5ej1pruX+HWfLA9VBc59VlnrREIRQSIJITbq00OIokghHz93+9GUlW3x+fMXM/Mh6GSYO/9hueNe1O/vbh9l1TNy+cXPXRLaOnmeZqEDeSWASRUQ9WcwJ/q5IEfyK/Krkm9vqua9uX1JQhbv0nrLq1KsHxW13katpALeX1+gqI0zAOorwO3CyHXb6q2hZqwS5vwTjoI/aoo0rYFi6G2irrBBSMNeNoELRQ1VQGmQWlZ9x2Up233Cg1pl0BBM35q+hKqm/CShgPkhVEF1t1pdW9ApvDqFnUeti+ff/7l9SUFn18+//bi524LHr3wQDLzLpJ2F2VWBvPvBNGfcgA6uVvGYEE9AnBKcF+HDeBUgEdBGEHPux/bMI9eoX/91xNYFbc/ff5SQs/ry8v0pQFRuySEusptuzCAfLd2vTRPu/ENmuWDO94x6Ztygq0F2Jbx22PlN0pVDf19GvvxweQtDrsfv7xUQAR3Qv7Ly09Q1QB+ABbw+W2iUv/401teDWHz40/f6LS9l4V+NxEDUr99fd4/yYKJ36am0Z3r3wHVh4298MvLd8pN10PuSU+w8uUtq9LyxwfhuqkuYemWfvjjT/+MrJ+E/mmy6/8X3Z8fhJPQDYBOT8F/er2D/AsEPxX6oPnP2dbArH9FEzD9nd0r9ATqn9G+4//vSOdpCSLiHfF/SO4fLYD/Dv38T3X7jxa8QtGXl3mYpxfgHV4efoZ++6qrovDzD8G3hz/88jsg/Z+S0au+8e8UvhZumUZh2339+vMP7f3xD7/8/ENfA18L3eJr3+T/iOY/wvXO5w8IPmf9+Me1gL9ZnspqKKEPT4d+q+r/0/z+Bllungbfnrefoe/jZbpgaFLinekDgu9ipgWyfofjTy+/g1RRAm16/z4Movxf/gXapVPWAikB0v0KpCFg4C4twkl4I0lbCHxPsQ0yUdi0KQD2OQ/4/2ThSeIqgn79N/+eRT/5zyyKTOnx6yMxfn1kxK8gI379PiN+fc+Iv75BBuBRNWmclm4OaTNV/VK6cVh2E3+QBtuwuYDM4o1d+AnkpE/TB5A3oV//Cpuvd4pv9fjrPTmnj6ylCespY7V9Hr5NWh+SsHzq6IPkHF5DvwfM8soHkkUpyLqvAI22yi8g400Itac0z6EAsPZByRjvtAGKnydiv/76q+e2yZfykWIJ6FFLWgRM+BAH+vQJqBjlaZx0X8rQTyroh99+/wH6v9B/tOpOfOKhgqz/tBGQcKMrMgRiri/ANGA+YHCQUO42+u33J9CATAmKH7BoGk3FbFoMfPYUBu+o66vZJ5yi3ysPqDBV04G8DYH6A60j6ENewHQamjJ7UrUdqHh1WAZh6Y+AqgvU+UCyrDqoBY7ZRuMr1LfhneuvXuPeRSxA8Lvdr9BOUEEdqXLwaxLzPgksrsoUwP/hE4/ngEjzQwvx7yTeIHnyUqh2G7dOGvfJI3IfdgH14305IO5CZTh8KafaGU5Q3UPmAQ+YBJDxnyb9NNn8XnuBYdt33vc57lTtjHvVa76U7TMc3ks8EGWE4j4NpiLxt6dLtUnVg45hwg9IOlF6WiF4WuXug9p/1kJMJR5a3JuPR6WHvvQ4ipHQ/4L+ZFJgtlxq4nJmiHNIlA3t+AB26qwmAzyaMdAfQGDdI4i+9QzvGec98X4p8xR4STP+7THzbo7nnEcy6xuAnjbT7vSBLwBgJ7p3V51cr2nuiHwp3zP8K4Dnns6A1iCugd9P7vbOcBp9lzQBwTvdf6v2T3Qm+IA7QnXv5cBVojAMPNc/AamaKdye1gB+G06hNySpn/xBKwhQB+4B6ENAiBQEEKgCd+jkCqgJIu2O/sf0dLIbkCLofSAtaF3DN+gAImbymhYYADRC0xyAwg93UlARAoyBiB8It4lbP4SZut2ngO5ki6qYvOM7CzwHv/n4XZZJfEDVBb4EsBym/BuE14dlP+R82goIW0xReV/0R3M/dYW+L0V/+1LeZfxI+SDY86mKfwcOBIKsaO9uO+WqFuSbInw6EPCEe8F+e9TcR1H/kOXzn1r8H//aLuBeRc0/Wu4zlHRd3X5GkEfley98byAKEOAjaR229yL46RF9nx5h9wnw+vR92H16D7s/8HhA9hn6a3L+gcTTwT9D2Bv6hk5DUuqHkwc/LwCL8Ik/fiKn0SnnfLP30ymmnJuPoOp+FKD3KaAKxU0YT5MfBamd6tgASuc9AwOLfCk/fOIZMSDBl/FUPdvqu0i+V2Jg4YcBPwoFGCo7wDuY+rk4nDY9+SR+G758Lvs8f30p3SL8S5udqSwA/wWwTJslEEugUerS8H730TRNN3/c8d2jDKSHoPo8BdsrNDW4r9BHr/oKve8e7juzsgfbp5+nPnliCaaCPx9zP7aTXvgCNm7dWE8qPLZEU3v2bJv/LMQUY0BiP5xKffURtBPHPxEBH+I4bP5MRLl/cPNn5mg7dyrcafce7y2QMwBt0CsEjAjiEIQWyJg9WPBnNoBPE557AHgwqfsNv29qVQ9dfr/D0D32lb+9vGeQpw2ePSSYDkL1UzvVSAQ4LGAI7h+uBcb+W93lkxbIf6CjAcRQIoo4jGapwONYkmAojg4Dkg79AMdJD49QDw0J1iOogEajKCAJH+NI3OU4kmVZ3KcAvYezfn0UPEAyRKOQ4DDcDwgapyiSwxiwIHBJxnUDlGUZlIkCUCK+LT2B5PlU+qHkhOhHozuB89T9txePJsHMFdmuZ49LQDjLpXHG0xIPbujw6Njc2iutDc5owVbpFrYfbfgi09ciTWwXI6+M2grt9mYCH/ZWoy9jgxJLhlfbjqV2zLg26/GUDgc8ti5SuTndHJbJFY51tnEqDHpn0af1ptDN1PRWjifpGF4YQlEcqFzLqPp0vlw1pUNPGluO4WgpEmETrOEQBYj9w2LBL2WJKFi/341SNWKgk7Op2UZNWX3rHES8EBw0z8Ncl8zuim+bkbHWaYefzvOttoDr5ZnG15i8iVd+e65JlccDpWxGOiwbHA6FobebK8yFsnlZMIa/cM8Nr49b0AyiiqUcN2aFceftQTmOaHriBozNN3lISfs2l0nZ1EizDSrEv24txTLQhUifyWZ2ttJFUDZYymKb0/kg3FBxx20FgdzKbRCvbwpnrfbi9kCZgx4ohj3KmGvV3VnVDi2MdcsLrYzILvPr06ILD+tgJ7PSuDUTXKqtzWajyA09228Eu0121El30gJ3r/gFuGK2lsrj6TDwvK1vbK7dbUBV9CWqpQ630JC9kxSOkTVfofa2EwzfVF3stD3IiMBsSwdNBj9iU+EqenzXFvHOvQYjd62PVd1YJ1xHfHxJnhdZoNXOVovV21Up+eVJ9rVtsh4C7zDHJIy/lKN5RJjrUPXHVV1aF5wIOzWVbcU2BCYytJgI9W2zA/JgO2fwlp1m6nVaEflSxLCgIBZ4MZrZFURNri2a5Qxb6wx1pNW1vRk8tT9Tu8DXkETJdNLcR1XVycptJV46Y1SWi6wQDkNNzahLxFzqsxRYZRFktHf1hoHr+yJVfWd9ksqxJSt8PPY38DPo3tHtNnIrFsFRRrtSsguyVVBGbIbBGOwSJSOD52Jq0QbboT4gA1soDseysHpa711+e8btSLtWuwunaPMuIVGprB3CMtEtdUiss+bI86B2Ayq7iPLavW7tPEVFXbiRV1LyFKstFPK8UYaAv46NuvOQDZbXyf6wx4pNo+1kX7+Qu2Hez/3tYHTmsNhGaXASVsJyZLVqWPhX0dy1bNnsyN1mYJZeNhpL0tbIIFI0SnX1cDyi81MRrMlNZTLHwLweFdyrErswTs1NPcqaSsPhpitP5wBfcvgxyAJB3igHlbEjUjWly+E2M0/byErWVnGRYHt7vNiWuEq0tZHg7ZJyUXO5Ot6Wu23cr7vsKJ53Nmn4yOA7iu01xnURofWJJJRKYs9DtxU3fRjXs2UgGmOlrSLYLlZ7j5JaUpgFODK/SQy7thxRXWA0sVRlu+4yjTbqZtlhyFnXk6OVnK/aMUaxvVN2e0O4WBKvI0dzaRLBLlmQLOXPNPq2FOkTxa7sxfZw0xeg9+X2G0TW1euuL0rxtrgQYydoIKCEEuF9NouOZzZeeUwQCAx3XZYrStoIXDdbNJuuuR0P3pHKEvYkFpoc7RnDPDs7x9KaJAmSjdBg4sU+bq7NaUNZhNBbScUmiGpfQ2vZBJlX0pWIh9XF3Xurlm5M+mjvT0FhnaytCCM8odApntGJ4bZWE7X79Zw80zLBINfVTmVqi8f940XqDfO0udL49UAioeY72yTWgpW60eNwp+aUvElUrSfPpLuzV7qY9FXstox6BcYQiptQaLSXLNUa9lTbxB07OFrlIptdD97ZWw8NP+xnyaIcS1zgMaTCz2a+Wy5SWUoGltzMzHrd+IoRdCZ89mgFpvTTAO9L8WgOjs8XO7MgrouNH5P7eRbHtcmvHbQ4MxtDv9zIZjUvW2W1XqwtW5w32qyrzVXXlVRZyaV5OKdLB8O4Hr+xZGvnV/8kpsbusMZvzIU+grSnjZlf7Kh2Lpi+kM1I7gwHasS4s87rlSMS8DEiq9GljEc0hhHlLCUUi0RqZtkEHsOixc/YA8ueiM16v9rFCVr37koWqdzVAqHO0TawxlPsEfS6pXPRdMm5VGkHHxEFg/ezgq5ONeme4IBfretZoLh5bcXqRkTnYyLMHdKgrViaDXWjzbfJqSNFbrujT3zELR2ds3PGkkvLYrYuZ55W3nq0gnVqBbBTxhd8V1nWYRFuAA13LrcOpTOltKwai1L1Xr/Z8krzLwM3n6/TBXNecliRb2uGDK6lkOH7kWKrOGF497rTmfAq1FhwrrqoNJl8N+J41Ax6lemnM+hyrVtMz+aEAie9NKPEkG8W+3xeE6mVzLR8vhjJ64Jr9utTdR6ZnQR4N2eVXvdDvT9ftztnqaiyOea8uBNn+4O3LQYq1ZbbJiPI2pIW2YXP5rx+HnFQNMN2To36eKRHtx+2m3IkEv1cs75pXVFqb4tLnSDnMT8nlTAt/DS3zEPDoOxmveFvfo0JHUUfLHcjF5sDSi+dfj3yRrs6dkQPqwEOgqD29O3+Il8EvZgN++zAeJiZgWp7ilqQk7qMvXVGt0NSF3PNxL+oR6tnRBulibI4H9MgNloCzs6WsBeCuX+cCzx6K9pAI3TzcpL1RGZOdZotZMSosg25W4jrRmKtW7cV6n2t0tcZX0tkJaj7TvIrqlqwg1eIjWlW++QUz9io0Ky+0uf7mbScu2PUrdR6heIOGo/76FJjipyZMafgOw3d2apg8l0s5ozPeS5nBbqL5YfIpbZihJQrHO/YZieRp4V9vmUkiWESc9NW81YOjMxoWZ/x5igNIGEEz1va7TWYVxbRHFeGZ81MEj3OzJxBLWomgG7gPOOTi0+DXlNv8o3KI4mwST1xt7FFWhC4yK6vxuWmm7yWRHNrgbUoTI0nYz+E/gJNpMN2YSlX7rCJezWg9lf9nCicy0fV4iT2FthERX2uZ/6lFSmg+OyW9NSRWHaj7LRSnSq5OFO4I1zHC6nDTH5eFjXtbA+7mdNpJHWqV+5yq82rS2GEleIHUi4Hg3JqibU0bjhJL5FkvlMN3T903W5UB48z3OJqawtr64ypEwd7yb7BxXyzPfayIWJtLqwXlMlh2tbQ4yA7X3GtWN+c1MJycuz6NfBwLU9g3l4DmRQFXxhwqWyJtTBnlKwdTtphYfjtGIKuK5dLMSirM0W0MLEvzoovDA267feIq0SCdQjlI33RSRheHXaXDWZenZHEz6vGBVXTuumslnSlrdPIts6SVTTW9KYmiAWyzWWEAk2GdAI7Op3UW71ckIu0Wg6Vv1lnRoie8xl10DNNW9riUTIUbSQPt3heLVy1gDt6zHS3YxoqjLU6qEbZamFRK93GZhc3KgxOTNaJbgh6AmQ9dp2QU/vTuFQtXh2OLk+X8Wq2161KmVUqa41eGS3PoEk4b7K0uOnrrhSCA0sdSTuctdjZXrfpOUqlebsu/QFtXaXKjGhXij1Mc2tnNZ8VJFuRTeZYeqlvOYJUtHS35kqclptym4833TkcgtqgSVJ19DW5rxQ39TVLX3sz87zB565sISE5X4Ynk+PCDF32+1VjX5lT4BA7n4nsYl2Zt1mqNrjlGq2Z2/AeFQiCM3FkL2LdaWGVx4096isR3UQj7BSJFXBpQfuEJcZW58K14pvObr0gMJQ9xwM2npv9sQqSWD3Mq8EMjXhRY+6OoAfhur85ytx2xm5TzxFZtlY8psdqzIcJkoecj8ysXUAuT4erGWvsHlvLKBWqy83ivG1MtyjTCDOXt7pYzFdHbAdXmtrRQs1UUnXzF4Hs5Nmt93eaBLqjlRcQ2NXYr+P87J9hJKsz6cChm87k2CbLFTjKOrfP+hx8FQkM1xQxH7qshnssymmsZ50KuSLl/IKcMcYkUkxlsqrhRsaD245Z3zDstoC3qV4RXuu4vlvf5G1eL5c2D6vzpT2D2XOALlCFkJyZau+Rgyfi2jAXpK1Y7srthjY2+yOCI3GkX8++EsRWXmCwx4+mtBNA63s8y/3ob+fK5WCn5mLjKXvyhASLrV/oWT/ucK4LRsGCOVkDxZpRbuyZlMdZY2hjZFxsnmg9P2oEf36DeQSBMRtZC3ptJTXicEhac4pf9pcQo+BM1wLcpHWRwzn+QoPep1pEKUMX5PySK8XcZSNSvJ1lRUmusNY7Vrzf+3KzFhwuheM4NdiU29uzcWMjRUUpnGM3tdWSqj27Dc2x2WV7ip4jwd6lsdOsCoHflLLCVtdNLadepZuHvYPs8SXsRBSL7dXL1QLtpq4hc6RhpEqmRV2lyJjmb+yl7+OG2lIhcdDqOR9kzdZo6CPnEMtbfGzbRUpkvm0YLbc44uo8xVYw3LfmhfMQJsmMpaVw8Cw7zNx05EkW0UmSDi7KLYSPqcc3BN6tMtFu4yWxKIKSxMuO8g+JKdMcHjs+ASRY3YIBybhLLuKDYa6FqOfs21EQQSsUSft14pXrNNAEbnE5ZgtSICSbc4MNgKvw1ZGTMZPgpTlbShi+2nH6LFrumPYIW6DNirtKpDh8Xo0Gy7eYQxbEKvT3ypo1m6U9nJIUxJdNm4gdD4cwMtzA4MjVeb/VHXjlMk5KqussTm+KE+cu33soPrgmvNIMzjyoXL/vbKvxuR2ijg0pjIUydPAx5FyiYi5NqwnEzgtvpVheg9vuKK0qvrBv596d8Zp5HYo+0pCY2K4vcx+4FQ5ruMfhg44Na988Epd9Ccv71dIomyWdXQbkmMseLIKtI4zMdzyxUtXlEca4Wb2XwrZbeoYaSEqGYkh77minZpAGb3yQN6TSOWYpjccX1Lnw60L2ZwtpTBk02uvICr+u49nYRvUNdcoKBQ2fD1LtMR/dbV1yM0bc4WdiGIl05q6CS98Iwx4+MDbcHWWypRmK6ssgQCyUR4+tyiHXwbWQW7xgTuys9S/x3EM4EuwMgv2a6ZMDuoAVWO0vCXUdGfXCwQKCzLx1JyAXhUlljNsS6lHfnVahuD3GS3VuHTovKJGmjTRaPYtz0e17t0cIibwkGrKsq2V8ynm6v6TXKxstRA31VLMbJVFCJRndEtGhANXiwOJ2EhgVpm92URvPleTmsnsRXQpoXmydQqdGaqDFoHCbxjPRniYa72YxLtMY/XWUrPU4YBXS1ixRnvmVM8CKXvXbY3ERL6EfHmcHZbYlw1wwcUHxUMekDAJzcsmobvLKcbZ8RtkdftZWGw+3Om3gxhvqO9cT6/UscoDnF7uqBJv3CL3ko+umIVq/yGmCvworRYJHYs1mPc4m8jKy57smk4V8dNKrS2wQbDszVcyosxoYq6NAx0xTPn+LV87YLrOO181lkVKiIGe1gpbD4orpDr6qSt+JcD7lGJqQR09TwE58blJBuiFVZCZdMSlBmO1+Nnt5fZnOrZ+nz/+l18/TKeD/2GHk49zw/e3U/eg5dIPPd16f/2vi/fL60vgpEO5xENvmffw8qvx3x7Cf/sr7jYnS+HjTO71cu3bvB/mdG0//yPSSlkHfds0IJMr7+6HwK8C3nf6Xov36PPx+uStb1N197EM5cOcGRVqm05vYr1319XEePT1Py+m9URik327j51H160swAjumfvuVoKmvYVNPqj/fmwCN8Tf0DXv5/f8BPWY30D0mAAA= -->
