---
name: "rar-cowork-cookbook-ppt-exec-develop-procurement-policies"
description: "Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_procurement_policies", "rar_sha256": "048f09082eadc663f4ef4f367bd1fa7e5e351e7dbd3f9fae5b0ab083027adeb3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_procurement_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_procurement_policies_agent.py` and in the RCI capsule.

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

Develop procurement policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 048f09082eadc663…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_procurement_policies_agent.py` first:

```bash
python3 ppt_exec_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_procurement_policies_agent.py   # or on stdin
python3 ppt_exec_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_procurement_policies',
    "version": '2.0.1',
    "display_name": 'Develop procurement policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0d7e6475aaf4c76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopProcurementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProcurementPolicies'
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
    print(PptExecDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
