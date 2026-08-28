---
name: "rar-cowork-cookbook-ppt-exec-define-product-attributes"
description: "Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_attributes", "rar_sha256": "54e46639febdae042ba1009d5bd9af2eaabfd3735df080ab39f17e2b9528fa0f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_attributes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_attributes_agent.py` and in the RCI capsule.

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

Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 54e46639febdae04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_attributes_agent.py` first:

```bash
python3 ppt_exec_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_attributes_agent.py   # or on stdin
python3 ppt_exec_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_attributes',
    "version": '2.0.0',
    "display_name": 'Define product attributes Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6265b2a16e5b4e48',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineProductAttributes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductAttributes'
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
    print(PptExecDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
