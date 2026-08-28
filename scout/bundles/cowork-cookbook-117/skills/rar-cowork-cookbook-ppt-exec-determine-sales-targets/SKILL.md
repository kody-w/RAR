---
name: "rar-cowork-cookbook-ppt-exec-determine-sales-targets"
description: "Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_determine_sales_targets", "rar_sha256": "da94dd28608ba34172b17f85f34ba5fb507e2342800e3664b7ec38a310e61df3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 da94dd28608ba341…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_determine_sales_targets_agent.py` first:

```bash
python3 ppt_exec_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_determine_sales_targets_agent.py   # or on stdin
python3 ppt_exec_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_determine_sales_targets',
    "version": '2.0.1',
    "display_name": 'Determine sales targets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on determine sales targets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5626997349275e3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDetermineSalesTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDetermineSalesTargets'
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
    print(PptExecDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
