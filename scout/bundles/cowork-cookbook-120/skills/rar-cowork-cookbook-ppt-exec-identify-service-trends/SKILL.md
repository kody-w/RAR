---
name: "rar-cowork-cookbook-ppt-exec-identify-service-trends"
description: "Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_service_trends", "rar_sha256": "38576df5bd55ce83a7d7b78bd08ca3262a2bf724b4961a556e5d5fe6f259b7e1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_service_trends`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_service_trends_agent.py` and in the RCI capsule.

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

Identify service trends Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 38576df5bd55ce83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_service_trends_agent.py` first:

```bash
python3 ppt_exec_identify_service_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_service_trends_agent.py   # or on stdin
python3 ppt_exec_identify_service_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify service trends Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_service_trends',
    "version": '2.0.1',
    "display_name": 'Identify service trends Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-service-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-service-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9933027d886468aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/identify-service-trends'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-identify-service-trends', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyServiceTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyServiceTrends'
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
    print(PptExecIdentifyServiceTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
