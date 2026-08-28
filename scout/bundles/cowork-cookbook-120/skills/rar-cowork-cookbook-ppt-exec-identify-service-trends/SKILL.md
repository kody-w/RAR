---
name: "rar-cowork-cookbook-ppt-exec-identify-service-trends"
description: "Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_service_trends", "rar_sha256": "e55565cb2232dd098b3d9ece984b88620d44fb4bf7af63c7bcacaf6ff3c8d41b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 e55565cb2232dd09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_service_trends_agent.py` first:

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
    "version": '2.0.0',
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
