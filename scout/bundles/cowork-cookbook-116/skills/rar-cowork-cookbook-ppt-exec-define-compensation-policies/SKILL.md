---
name: "rar-cowork-cookbook-ppt-exec-define-compensation-policies"
description: "Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_compensation_policies", "rar_sha256": "cb8611accad6f58cf6e50adf20054fd0890d29a10a9252c39b5e9119456fd10c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_compensation_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_compensation_policies_agent.py` and in the RCI capsule.

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

Define compensation policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 cb8611accad6f58c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_compensation_policies_agent.py` first:

```bash
python3 ppt_exec_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_compensation_policies_agent.py   # or on stdin
python3 ppt_exec_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_compensation_policies',
    "version": '2.0.0',
    "display_name": 'Define compensation policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1dac3e911bdeb58f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineCompensationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCompensationPolicies'
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
    print(PptExecDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
