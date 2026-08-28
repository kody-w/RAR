---
name: "rar-cowork-cookbook-ppt-exec-establish-support-procedures-and-policies"
description: "Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies", "rar_sha256": "55d5c4c892c18080d47a5fcda496c44e4d606ef90c944bece28445df06c3c77b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_establish_support_procedures_and_policies_agent.py` and in the RCI capsule.

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

Establish support procedures and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 55d5c4c892c18080…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 ppt_exec_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 ppt_exec_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies',
    "version": '2.0.1',
    "display_name": 'Establish support procedures and policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '963e5b46cb82d409',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecEstablishSupportProceduresAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEstablishSupportProceduresAndPolicies'
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
    print(PptExecEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
