---
name: "rar-cowork-cookbook-ppt-exec-develop-new-products"
description: "Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_new_products", "rar_sha256": "b53d85de14db24d2f3e86def3d863f5a4e954e04c34fd762b8ba27fc5605fcdb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_new_products`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_new_products_agent.py` and in the RCI capsule.

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

Develop new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 b53d85de14db24d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_new_products_agent.py` first:

```bash
python3 ppt_exec_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_new_products_agent.py   # or on stdin
python3 ppt_exec_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_new_products',
    "version": '2.0.0',
    "display_name": 'Develop new products Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4453f7c3748daa62',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopNewProducts'
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
    print(PptExecDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
