---
name: "rar-cowork-cookbook-adaptive-card-recognize-employees"
description: "Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recognize_employees", "rar_sha256": "854f79ff4bcf1cfaf3272123c171b55ca84e551f3e11b6858e2b41ba36bea4f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recognize_employees`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recognize_employees_agent.py` and in the RCI capsule.

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

Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 854f79ff4bcf1cfa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recognize_employees_agent.py` first:

```bash
python3 adaptive_card_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recognize_employees_agent.py   # or on stdin
python3 adaptive_card_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recognize_employees',
    "version": '2.0.0',
    "display_name": 'Recognize employees Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c48a376936c7297',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardRecognizeEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecognizeEmployees'
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
    print(AdaptiveCardRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
