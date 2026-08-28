---
name: "rar-cowork-cookbook-eco-impact-analysis"
description: "For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/eco_impact_analysis", "rar_sha256": "503e63243305285b3497148f79213a057c3ef9ef02f8f0abafadfe0ee86083bb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/eco_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `eco_impact_analysis_agent.py` and in the RCI capsule.

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

Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eco_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 503e63243305285b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eco_impact_analysis_agent.py` first:

```bash
python3 eco_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eco_impact_analysis_agent.py   # or on stdin
python3 eco_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/eco_impact_analysis',
    "version": '2.0.1',
    "display_name": 'Engineering Change Order Impact Analysis',
    "description": 'For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'eco-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/eco-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '517aedd76241ae96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/eco-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class EcoImpactAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EcoImpactAnalysis'
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
    print(EcoImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
