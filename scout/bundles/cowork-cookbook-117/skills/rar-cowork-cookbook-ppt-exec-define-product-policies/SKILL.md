---
name: "rar-cowork-cookbook-ppt-exec-define-product-policies"
description: "Generates an executive-ready PowerPoint deck on define product policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_policies", "rar_sha256": "3ad51c0ca87484f2d4facdb761c50ad31c97536f3a8f7fac7f63fab8fdf8229c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_product_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-product-policies:6c28004f8a61bd2e17c00370abeab7a0e9f9f81a3b730778a8ad8841ca33d742", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_product_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_product_policies_agent.py` is
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
