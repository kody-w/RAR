---
name: "rar-cowork-cookbook-ppt-exec-establish-support-procedures-and-policies"
description: "Generates an executive-ready PowerPoint deck on establish support procedures and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies", "rar_sha256": "1f4c511827a033fec13155ed0fe33a92310bb8d653b5713b8257ac8aef452c20", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 1f4c511827a033fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_establish_support_procedures_and_policies_agent.py` first:

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
    "version": '2.0.0',
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
