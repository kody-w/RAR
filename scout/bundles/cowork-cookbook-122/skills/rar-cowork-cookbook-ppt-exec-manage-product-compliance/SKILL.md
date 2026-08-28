---
name: "rar-cowork-cookbook-ppt-exec-manage-product-compliance"
description: "Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_product_compliance", "rar_sha256": "809f9a62622f21229c84e2781f23e0412d8f9e44ac7bcf6bcf6a1f35576e2632", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_product_compliance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_product_compliance_agent.py` and in the RCI capsule.

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

Manage product compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 809f9a62622f2122…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_product_compliance_agent.py` first:

```bash
python3 ppt_exec_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_product_compliance_agent.py   # or on stdin
python3 ppt_exec_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_product_compliance',
    "version": '2.0.1',
    "display_name": 'Manage product compliance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e75bbfa794280dab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageProductCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProductCompliance'
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
    print(PptExecManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
