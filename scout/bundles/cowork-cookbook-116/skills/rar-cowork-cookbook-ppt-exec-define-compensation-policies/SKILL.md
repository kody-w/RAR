---
name: "rar-cowork-cookbook-ppt-exec-define-compensation-policies"
description: "Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_compensation_policies", "rar_sha256": "759faeb8f3e080424b03264cdd38f95f1670506e52f9d49ec599b7899a67c41d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 759faeb8f3e08042…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_compensation_policies_agent.py` first:

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
    "version": '2.0.1',
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
