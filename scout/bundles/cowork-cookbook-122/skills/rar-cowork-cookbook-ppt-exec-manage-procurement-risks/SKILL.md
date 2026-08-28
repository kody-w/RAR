---
name: "rar-cowork-cookbook-ppt-exec-manage-procurement-risks"
description: "Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_procurement_risks", "rar_sha256": "63c86db0f6c81bb041bd4d5682a9a3a444930c53b5b84aa3b3062fd47968e50f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 63c86db0f6c81bb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_procurement_risks_agent.py` first:

```bash
python3 ppt_exec_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_procurement_risks_agent.py   # or on stdin
python3 ppt_exec_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_procurement_risks',
    "version": '2.0.1',
    "display_name": 'Manage procurement risks Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage procurement risks status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01670af81f1563c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecManageProcurementRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProcurementRisks'
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
    print(PptExecManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
