---
name: "rar-cowork-cookbook-ppt-exec-implement-process-governance"
description: "Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_process_governance", "rar_sha256": "309d410d60fa788e05eaf9f5c76376e92dcc4977b0b2ecfe01baf3ffcf231ec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_process_governance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_process_governance_agent.py` and in the RCI capsule.

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

Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 309d410d60fa788e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_process_governance_agent.py` first:

```bash
python3 ppt_exec_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_process_governance_agent.py   # or on stdin
python3 ppt_exec_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_process_governance',
    "version": '2.0.0',
    "display_name": 'Implement process governance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement process governance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac7a4fd00bf5dceb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementProcessGovernance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementProcessGovernance'
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
    print(PptExecImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
