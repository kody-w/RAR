---
name: "rar-cowork-cookbook-ppt-exec-manage-product-compliance"
description: "Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_product_compliance", "rar_sha256": "303f7170bf374ac16e46c10fa3bb2efbdf6f42c024979b5da4fa14c98df592eb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 303f7170bf374ac1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_product_compliance_agent.py` first:

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
    "version": '2.0.0',
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
