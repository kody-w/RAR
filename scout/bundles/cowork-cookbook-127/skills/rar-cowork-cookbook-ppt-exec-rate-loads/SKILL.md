---
name: "rar-cowork-cookbook-ppt-exec-rate-loads"
description: "Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_rate_loads", "rar_sha256": "ea06596ec94b54c2d96c10334a7f7a9f977efc3c03d92c058ab949bf9641d5e5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_rate_loads`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_rate_loads_agent.py` and in the RCI capsule.

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

Rate loads Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_rate_loads_agent.py` and embedded as the fenced Python below (sha256 ea06596ec94b54c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_rate_loads_agent.py` first:

```bash
python3 ppt_exec_rate_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_rate_loads_agent.py   # or on stdin
python3 ppt_exec_rate_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rate loads Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_rate_loads',
    "version": '2.0.1',
    "display_name": 'Rate loads Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-rate-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-rate-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd1d43a7ed71faee6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/rate-loads'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-rate-loads', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRateLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRateLoads'
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
    print(PptExecRateLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
