---
name: "rar-cowork-cookbook-ppt-exec-define-product-policies"
description: "Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_policies", "rar_sha256": "a49ca8696711d6804638e7d377e6e88b993947dd7dc7a2ddd52fcb009a7c99ae", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 a49ca8696711d680…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_policies_agent.py` first:

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
    "version": '2.0.1',
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
