---
name: "rar-cowork-cookbook-configure-analyze-sourcing-market"
description: "Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_sourcing_market", "rar_sha256": "acf25fd6c825035dd577f572fce9f0b1511fdc62cf739e2495b2da31e7515e7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_sourcing_market_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-sourcing-market:f9e319fe4427432962778c8053870b6d81653d9cc3166ce89781854b91ad17ae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_sourcing_market`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_sourcing_market_agent.py` is
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

Analyze sourcing market Configuration Bulk Setup — Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 acf25fd6c825035d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_sourcing_market_agent.py` first:

```bash
python3 configure_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_sourcing_market_agent.py   # or on stdin
python3 configure_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Configuration Bulk Setup — Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_sourcing_market',
    "version": '2.0.0',
    "display_name": 'Analyze sourcing market Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cda691b2232747e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeSourcingMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSourcingMarket'
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
    print(ConfigureAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e5ObSJbvV2Fr/+juVdkCAQI8MREXkJAECBCSAKk9YfN+iPcb+vZ3v4mkKtvb0zvTERtxcVQVj8zzPr9zMtO/vZhNHWTly6eXo2um0MaM4zBwS8hMHYjNuqy8gT/ZzQI/kJ2ldRlaTZ2V1cvri+NWdhnmdZilYDqd53HoVpAJWU18H+uFflOa02fIDszUd6E6A3TNeBhdqMqa0g5TH0rM8ubWkFdmCfgIhWne1NC6t90Y8sLYfYW6sA6g1oxD50FrkqzM4tgy7RtUNXmelfVHII7bm0keu9XLp1//8foSgvuXT7+92LFZgVcv7FMel34IcHzy39/Zg+kxkBCMywdgjhQ8527pZWUCXjmuBz2ffq7c2HuF/uu/bp1Z+tUvnz6n0PP6/DL9U5sUqoNJU7OqXQeyzdy0wjish48QHXfmUEGlWzdlOhmqAtZM/Y+Pmd8oZTn09+nbzw8mH323/vnzSwZEuBvg88svUFYCfmUz3X+cqOQ///Ixzjq3/PmXb3Sqxopcu56IAak/fnk+P8mCgd+Ght6d698B1YdXLffzy3fKTddD7klPMPPlY5SF6c8PwnmZtW5qprb78y9/RtYOXPsWh1X9b9H99UE4cE0H6PQU/JfXu5H/Ac2eCr3T/HO2OXDrX9EEDH9j9wo9DfVntO/2/2+k4zAFOfBm8X9K7p9NmP0d+vVPdfufJrxC3ueXlRuHLYgOK3Y/Qb99OSpr9tefnG8vf/rH74D0vyRzT4k7hS+JmYaeW9Vfvvz60z1TAY1ff2pyEGuumXxpyvif0fxndr3z+cGCz1E//zgX8D+ntzTrUug90qHfsvw/yt8/QtqU/d/eV5+g7/NlumbQpMQb04cJvsuZCsj6nR1/efkdIEQKtGns+2eQ5f/5n9A+tMusyrwaOtoZQCHg4DpM3En4UxBW0OmZ1F+Pwk4UPybOVwi8ndIdQITZxDW0Kc0whkA+TB6fNMg86Ov/se84+sF+4uj8DRvdL080/PKGhl8eaPj1I3QKAN+sDP0QDIFUWlEg03fTeuJ4j42qST60E1MgUPgAHZXdTYBTNbH7N+jrv+Ty5U7wYz5ManxOgV9M4CwHqt0EYKpZhvEAmXdAH2r3A4BXgCXvwDv9avKPk230wE2fFrMBgru9aze1C8WZbT4wvHoFTq+yuAW4ONmxuoVxDDlhCYyUlcMD0Zv000Ts69evllkFn9MHEKPQo8ZUczDgXWDow4e8dL049IP6c+raQQb99NvvP0H/F/qfZt2JTzwUUBLuBgPBHEP8UZYgkJlNAoZV0BQWAHbunvvt94cnJulSUBRBPoXeVOTqyTvfhcGkwcM9b74BOk8iuuWT0492g7oA2AUKa2AtkOPV6+d0IpGBoWUXVu6bER+TH6Z/c/aDz+ST6mlD4Kd7+ZzG3iNwcqadlc5HaOdB75YC6k61cvJokFU1CNrcTR03tQcw06y/uTDNaqgCeVN5wyvUVEDVifJXC5CejJMAcDLrr9CeVUCdy+KprJfPugdmZ2k4Of4ZrY/XgEj5E4gx5o3ER0hygTWh3CzNPCjNyr2P88xHRID69jZ/6hmg1O2gqaK7k4/uGX2PPPpPmgn2h+aDmfqRI0CdHPrcLGAEg/7/9ip3yTcbdb2hT+sVtJZO6uURZlODNWn96MlA0wCBpuORM98aiTfMeUPjz2kcAteUw98eI717ZD3GPBAOYIADIES9059yvLzTDWsQH5PDy/JujM/pG+y/AssA71STCiCNbxMoZO8Mp69vkgYgV6fnby0A9Ai9SXUQ1FDeWHFoQ57rOncj1EE5ZdfTESBY3CnTQDrYwQ9aQYA6CARAHwJChCBqQWm4m04CWTI54+6F9+Hh1FgBKZzGBtKCNHI/QvoU1SAyK8hyQXc0jQFW+OlOCkpcYGMg4ruFq8DMH8JMTe9TQHPyRZaYtfu9B54fQYRO9QXwe08/QNUEvge27IATQHb1D8++y/n0FRA2mVLhPulHdz91hb6vT3+bUhDI+K0EgD59Ku3fGQfgdplU95ADRfdWgSRP3GcAPWPY/fgoxI9K/y7Lpz90+j//tcXAvbSef/TcJyio67z6NJ8/yt9b9ftoZ8kcxEiYu9W3SvjhmWsf3nLtwyPXfiD8sNMn6K8J9wOJZ1R/gpCP8Ed4+iSGtjuF7fMCtmA/MJcP2PT1c6q635z8jIQJ3QDiWsN7kXkbAiqNX7r+NPhRdKqpVnWgPN6x7l403gPhmSYPtAHVosq+S99Jp8mtD6+9YzL4lE5o70ydne9Oq554Er9yXz6lTRy/vqRm4v47q50Jd0GsAmtMiySQN6BTqkP3/vTeNU0PPy7y7hkFoMDJPk2JBWoc6HBfofdm9RV6Wz7cV2RpA9ZPv06N8sQSDAV/3se+ryAt9wUs2OohnyR/rImm/uzZN/9RiCmfgMS2O1Xx7D1BJ45/IAJufN8t/0hEvt+Y8RMlqtqcKiMoyM/croCcTjNhOvAdyDmQRgAdGzDhj2wAn9ItGlCLnUndb/b7plb20OX3uxnqx8Lyt5c3tJjuH43BI27AhH+/e5ts+lZ1v0yUzWn+vce6m/jemX4B6oVTdf3ukz+1Cl8ecfjyCWCN+/oyGbIMQQEb7wvpl4c4QI9vPS2gAFDjQzV1C3OQRoASqOH5pMMNIN53DKbXoXMfP918+vNG+M/S/5NHuShCeS6GLQgMXVDLBUGQNgnjKEnA1tIhkSWOOpRto8hyabskRZAIiWMWhZgOQpgukGLyZGI+pZgjkw+A/O+G/uvd+cuDAKgXC3wJKJi2t8A9Z2mTCxxGccfBCcLDiYVnu5QHWwiOIJ5jLxe2R6CUu8Ao3Fo4Joq4BI7gLmFO9J49wkOqL2+t+JtXHjDwBSBnEk4yL0zTJm0CwRyKMIHaKGyhtossEIdAXRinUI8kXQzMf5/69MzkuIfiU9CCzhD0Ze3E57enp6dAXGJg5BardvTjYueUZs5x0VIZcYbCZM/PiU6sg4FlOhtPRe4aJ5jGc/TVkLbnSy1GwrFXzKFaq1m+IWREO3XrExmeUMmm9sSukvuWRZyzVlwMxEzzpduWKTIg2/PpsBQWej/XbrxJZUt4pgnWRqVKNe+tqoiNUkcs8ZD3rrxoGNMokltJOlXbYsVYhAVc3QQhZsxBcfJKtBttncEqGelkTBjXC7fNqiSzbG9dnDHtsrzxUr9DGqQRYnF7atz9beCIcx7GaoKQwkLTjYIPltJYEiTZply8sFsxwgyOpFxFIRsunOthpWaadNstTtfyPKsTATcTrkJMHd/yx8JcZhsPKzqu16kk0dLdKKSqOaAlURz3t/1hx7NSUZl6o4UzJx3xhEIEvUhMpLm0mxvtysvrbbGXSvF8XOgWa52Gc63rPUvtnQx1zuszFsXmKt3UOTJXUe3aGEWuxvntWO9jJXVkWE1LJ89Ocq+xZTobndLeR1daOOfxiRFtS9EXRtkqvmAvB7TnAoaW5gFyhvl47MaG6eWOiOoQFVVdXlHtngxxrdSF3nLKxSVciiay03SuCWnL2I77qNK2B+tEFNymNapUOCZKYapX+eYRshqBxizVrjpblSuS6viDJqzSyzHHXX+jh9RI2fm1yhVl0zmsVTDLK36lyHlmXUp75Ci1UfpFb215Tk+sksO0/cUJHfV2jJYZEs+HHHZ1lFskw5nqvbaic3M9E44KarIjs754kjZelvhpzjqyGGj27AyAy1zP8ci/7S6KIWeaaaaVkLZzs6Y0u+TB2q1VrqIsS4lDGtfFZfRhLzvW8TVcrRFKWyMr8ONoWw2f1WeJcVoeKTx/7vmNAX4H9Lzb54YcK7fMwzxqS888b3So9b6K8mWZ6glFnozcY9tjaTHX0mw3o8/zu9gt9WKxkzdrcWFFZpdv+mgt8XNTkecrzDbWZr+mwphbavDWEpJ9b+4N3kzW6lW8XuTI7pCF0Pv9Ib9Y/DnZjcNBjchTHbKYutA7qcfKZFfksXZGrikTN9s1QIzwhrJFG414H+TVepAX1Q0Ncr5aW2G52i62YueGdryCExVLk9riDMEKGMWVfAT1+NOpHOfRHG8uPrKS5+fQrVGFrsSZKmCtoy3kW8CYTbXTFiFuydvzfC1v4LoqWYT1eD2o5/CKIVHtLHty1R62JIbcqsstdsYjjSBHVKjtbo6y6NCk2zYbUXLnyqXCM/2ckjQOkTQcC0/ioYQHKj+1CJUejnNKFY6pxGe94W3wDWGeK5I9HJFZkWq1JfBCPD8iqunMjwXXck5SMRkVjVh0wocYbsp9cPZuR4dUUVRFdsFlPmOFI84UKux19J7cLBxNWzUtzOKYkp07rGd2fVr761aVVBc2a9S+dKc8ltYqepGQeGdEiWcuQyEV+dJws5gldsIuPoyBodH4ahaE2z3lIcLCJCSTPBunhhPPhi5LqyagA5q08UOd6oy6dW/wSCQYP1vHDSwMnrAZxQp2kFZpVfQ6Z6P5tuJxBXHpZBP6qTA4TsYvvGgnt9vDEUX3XJQWItaLfVBtzURVpYMl4kOPBojlb2deirUcSmdOx2/s5Lqk8FmjciNN59zm1uCcdOLqCp/TcDdUq57W0mJ1EW9X6rg7K/o10nt7LstHfEd0sMuu67DVjQOHkqziMzP2HAXnWNjJt/gaF8c+lUxtgfU03UjXAR3pOr50JWxzzsWihhH18/0iP9bXfINrEd6PNoGWq1xkcUVeCsuxxJe2MQ5Ey7J6x203Zt0jM1Do1hm1aSMhXqh9J8u85sjxNdtR83od+M6IrojC3pI5o1RxP6P2KbG05e12HMnZXlZiwz63Q1qcQ7T1JL07DjRxuJDnPl8lLBJf1HN8FHF7aXbVrZ7HgRrCt2PSdw2tHkf7PPqcXllSsYn44oBvlDa0Iztc4SBE0SEFM09hijdlLwunZR7paZWsCzaca/llaZ7hwKY2RWYGw3Hcimy4l/TzwDAg0nxQTKPW92do3gyz1IIbkXEqwxBSXjoypNEfTK9fVksYc1ILKegWoOG11OvCIFL7xnhsd+YbCrlpDEd0zpVgz4vLgEc7v9d4ZWjBwlHGz+tcI5wo1KIL8ALHz/xTc8gOPmIIuLjwgtY+2QcmJCyBte1+jR/reranQxHhV7vcpW8NHOrEGffJrhLyQO3O6+OFERYReQuu51Y7Cx5aqqjvIBFO7a/IHF13uWYN1BExVpeAkoiA8A26DDcLKg4i5BbS54RxyYveWCdFWrOzZuUluebp+q3u1sWJPy8tlXO65KIju7BalM0y0mZWGOGcDfKrVs2TvRbV9rI5sG14PTIheT6cq3Ax1q67NVfnLLueG5o/t8loGWrVsXze8EPX5RJfYnUtoN3JKc8UrcKR2JB4d0l6ZkAJgyuuO+kAU1caKY7NPCPOSKMdDIxYmVng1KlJY4FsYCOeJlko2fXmoMycco2vu0RCM2q9O8kuiXScjsAGvOeVw6YTbli0puRin+4wwy+YsucEpMkceu8tuMMqJIpNAh9tVNgsNouLQ9xgDW5Unskz8RbLJVvoe4buBvNYKqZN6G2+5Vecmu1nvoG5ouFwy3oDInRQUmWHMHRm8KAzHDNWWwihsRvPoScqp1oBvcxMuXE8ubdnh1MVRaemrWTOnnUIkUuuheNN5emjiUttPtpjnYjhVSgoy5+ZDrZNtieMHZWgkmb+QVsffDr3Jd7vSJZgBFnFqxW+sVZSc6BcXrXbVOpPCWJupCuNsZuIKTZsNvbs1V0a2xlT7Q6LTWyojqE3l62PMmt+R1kDKuqpMxTnwuTLQ8MxkajQ3Jqhz0zrOANum4urnV2ME+awWDFbaX06rlb5UeZumDzbb1B5tccONF4JnR1IcRiP43V+FsjjLVwszMN1tR8S2HcHLJ/vtNOKl0/hyjvu434rI8xBJOBQkc6Yat+OysXq+iORSPs55+PZFq7Z1WxDnVNOY7wj5USlulCTXgxuy2BvOyq6H3kiww9zuqA67NDIC02bpY0w+HRmgYVxV6g6cpxdb9S5RNgiXTspX6BI5O7me03oCk7L0n0wu9lkbMQ5ErDLUEpGrrE0JRbyosLtq6ZQTaIsiypz675ODbsBiwql2qUzrVIXjgdAr2VHwjy0cgNCzhhVpheUyFcBtHdb+ri7jU2SZVt2vOXCuSBw6RDiyMp3mnVFu/tuGx0PVFYxJteYG/zoIvJ0brlVTjeqcpiChCUOC1KHOBe7bMeej/Wy7gm/HhzuHF060YS3V1+ATXzfO9tTp83Oqxua+ZrR8YJtts44MMVMESNWnuldNVbZSh1iCZTiTDPWF3+ebPhFuAzELM3XxfXqLhLxEAWkEyu4dT7GskrZW1MdtL291HddL6gor4Y4bNAX1j8XRphoW6dijUORORV62p3GzZ4Q/NXSUnxrPIRsp2RRuCaAvJK5OTIrg22T+iqJGwxfx2pNcQZoaoTF/hAGt2glluM43/j0bBOnF+0CH+IDPBh61+2oPc9U0YG2UhM9jfXKMgq/y0MQzmx3WeVZVhn0KhFIQhdpEV/JCbaXDQFOYCWDG3i/1RgWphlTXGrW8to5CNpaGF0wrs7HK2kGQJ/vd47m364ipxKrlS+VxJY5DMUtVgSZJYQ83XCXXCEXS4pbLUDne70hSE+p5zEsRLpXjf6oebMuVAsJ9i/anr30aL5doqA7aJ2S9IIZaZsRQhnZgoCFbWayW7fl5y3vV7XtKRxRi8NyI8+dxL3IUmsZgVItJbbhMgq7dOip0M583m+iayetkpsv3FTxsrAODtrc2tNFumwdWFfBsG0XOuN+uNgps/X6+YAjJ1jdofKwpJXEquEWydwdcdgzvMt7w4o84nV3sO0614KDJHuEKmxXaUZkoTw/HDoQJ14+2wR7oyII9CIvLiKJr04uiYqpO29lNyqHpTKgBjpnVjNG96+oPp8n6UxOuVp0lz01GtIstC12tmDt3N1RTSCfCl5hkWWMhVtkfmJqrSRZDVlzPtLJrSuxG/JC2Ic+grkZWGakVwnL5Azl09rglw62aI0DgXd2ohZ5vaSEOvIvCoWLml7dbCY1UDIX0UDe7087AedUPtl4sHP1Qr3yttqOO7fEbYfeFDLa5Esi2u+SsW5EefRnFtGW7ExNlWJ+kvhrsZOkLZbk/UlpQT1zN5Z4vKwojbvuSNCv45sALyISNa5FO6s9p0MucQpKAbxO/HUJ0O6Ewnp6oGB8li9NYevV+myxq3xfrAQM20e15Q5Vu8qNYrnb8YpIqcRYyHZLzoj8hNrrfr1KicapZlEAQsFg4Win4/1uvBxbLUJEBsTSYpzz6RG4nl0HbZo3SGSvc2LwFGO9G+tOxfBU3G5D47JVxViwXJFCL86wNigaP1ljI2cuT8IRo98sby0RXcngFDriGKkwwXbvNTSlM9pK2ROGtzYYfO3sjtfyAnpmR3U3i1V/2FkczGmXeYrTgZstGPbozsNsOSx8twOrBOPUWhUFlvi7yBrlCl9i+iXDOj0k8JOTzLhVxSipvaGodLP2kGSUtycDtnDZar1F5LV0cBLlwa4Y36AAlhgn3xI2TDtS3cbsbDVxCAI/dIosurrbo2ZHdzd9ZR1dQi1BJyc3DgUbbqFf0J5qjV3hBmh9FGBqCzprCQ1hz1bYo79cxVSPiW7lUs2Knvnurp9LYkYur6ENssBds+G2SHNWXKzJ2/aSovud16U0uVA4fzHHjfXMcuqWIMq0RQMTxMWOmzeyu9Ux96jOD0nokD5pMOWcqAhl3QR1riczmUBufF16djbtezjZfD7ow6m/SXNjz7Rtrs/2LH8LiTBMO6btEC5EEtD3EBhpU2a5iqQtI508s1isCLXt8wuT0XyU5CXWtm1aH9bSJguu6bZyt4lurKMaTOoNgMwXiV42JMsiewfLaDdIrxhNo5tVIK4D6xaM0riCaXwfGJnVbfSsnqNZ7u7dwMAq7aDQ62DlUEtdOZNuF2OOEhFiaVaCNWOQ7ermiwa7Jg3ZF0Zlu2KFkjyVtytCj/7IbdxcZqLrqckoNkyRpaBnqIszs32VkRRakYiDNaSi8JzNtc5gc/Mk8anx1rUG6e668Yg2yLAaiVkqrPFuf1tIuKHxi+Wp11G+LMTxTCPWPN+MOoGjl9mwSim7oftuh2F6M8LMkdskYPkcS1EuwMuOA+veGE7DyLa81SnGO2xMJJroUR4dQXboS9efY1xRuixZ0DT995fXl/sx8MsnBCYo6vVlOjt4ngD8pf1jfwzzL09SKEHAry//e5ubj43Gt9PB+3GAazqf7tw//QUp//H6Aj4AiR5bzlXc+M8Nzf+2gfvhX+4qT9OHx0H2dIzZ12+nJ7Xp33e9w9RpqrocgDRxc9/zBpZuqum/slRfnkcPL3e1knyi9s7x24ZrnX3Jzcm2YTqdy7lOaNbu89F/Hg+8vjgDcFdoV1/QJf7FLfNJy+cR1bTNO51Rvfz+/wDz+B1EpCcAAA== -->
