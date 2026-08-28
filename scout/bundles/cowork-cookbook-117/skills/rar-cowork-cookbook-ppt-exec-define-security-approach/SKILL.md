---
name: "rar-cowork-cookbook-ppt-exec-define-security-approach"
description: "Generates an executive-ready PowerPoint deck on define security approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_security_approach", "rar_sha256": "9d0cf5aedd684816d266cec8eebc412ca814b3ea3226a3535d327e7153a12bc3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 9d0cf5aedd684816…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_security_approach_agent.py` first:

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
    "version": '2.0.0',
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
