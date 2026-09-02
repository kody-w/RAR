---
name: "rar-cowork-cookbook-ppt-exec-develop-new-products"
description: "Generates an executive-ready PowerPoint deck on develop new products status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_new_products", "rar_sha256": "b53d85de14db24d2f3e86def3d863f5a4e954e04c34fd762b8ba27fc5605fcdb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-new-products:dc8eefa5ecabcea505a3254ce290e21788f3e543ad9e840b28454cd288cb8819", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_new_products_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
