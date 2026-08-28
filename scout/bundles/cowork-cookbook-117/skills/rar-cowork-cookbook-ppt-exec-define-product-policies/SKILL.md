---
name: "rar-cowork-cookbook-ppt-exec-define-product-policies"
description: "Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_policies", "rar_sha256": "3ad51c0ca87484f2d4facdb761c50ad31c97536f3a8f7fac7f63fab8fdf8229c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 3ad51c0ca87484f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_policies_agent.py` first:

```bash
python3 ppt_exec_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_policies_agent.py   # or on stdin
python3 ppt_exec_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_policies',
    "version": '2.0.0',
    "display_name": 'Define product policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aded3d8b2f3781e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineProductPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductPolicies'
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
    print(PptExecDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
