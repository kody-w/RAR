---
name: "rar-cowork-cookbook-ppt-exec-develop-procurement-policies"
description: "Generates an executive-ready PowerPoint deck on develop procurement policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_procurement_policies", "rar_sha256": "2d46fe53edfe9c15518c14ea7878ecb87f3620d6e7f4d7368e4f924aae201d4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 2d46fe53edfe9c15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_procurement_policies_agent.py` first:

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
    "version": '2.0.0',
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
