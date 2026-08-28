---
name: "rar-cowork-cookbook-ppt-exec-define-security-approach"
description: "Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_security_approach", "rar_sha256": "fbdd7ef23d5ebe6be6b248f5095d41d5ec437ecefa7c9a159ba260d21998a4b0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_security_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_security_approach_agent.py` and in the RCI capsule.

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

Define security approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 fbdd7ef23d5ebe6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_security_approach_agent.py` first:

```bash
python3 ppt_exec_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_security_approach_agent.py   # or on stdin
python3 ppt_exec_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_security_approach',
    "version": '2.0.1',
    "display_name": 'Define security approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc49bdd666c5b170',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineSecurityApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineSecurityApproach'
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
    print(PptExecDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
