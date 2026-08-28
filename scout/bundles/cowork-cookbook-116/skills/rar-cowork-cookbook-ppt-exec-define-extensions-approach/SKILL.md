---
name: "rar-cowork-cookbook-ppt-exec-define-extensions-approach"
description: "Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_extensions_approach", "rar_sha256": "bef26cc10d418cca363bdf3076898c3e564b78c61b8b6311bbe61373b2879f4b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 bef26cc10d418cca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_extensions_approach_agent.py` first:

```bash
python3 ppt_exec_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_extensions_approach_agent.py   # or on stdin
python3 ppt_exec_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_extensions_approach',
    "version": '2.0.1',
    "display_name": 'Define extensions approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define extensions approach status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa922bffff553dd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineExtensionsApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExtensionsApproach'
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
    print(PptExecDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
