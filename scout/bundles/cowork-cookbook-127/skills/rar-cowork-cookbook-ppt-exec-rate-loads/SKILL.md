---
name: "rar-cowork-cookbook-ppt-exec-rate-loads"
description: "Generates an executive-ready PowerPoint deck on rate loads status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_rate_loads", "rar_sha256": "5c899635d3b6006dc74bfe8e105a6ee4608954dc5a940c3109c4a52d77f2669f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_rate_loads_agent.py` and embedded as the fenced Python below (sha256 5c899635d3b6006d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_rate_loads_agent.py` first:

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
    "version": '2.0.0',
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
