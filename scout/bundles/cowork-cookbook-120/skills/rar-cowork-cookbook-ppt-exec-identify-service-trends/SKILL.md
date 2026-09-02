---
name: "rar-cowork-cookbook-ppt-exec-identify-service-trends"
description: "Generates an executive-ready PowerPoint deck on identify service trends status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_service_trends", "rar_sha256": "e55565cb2232dd098b3d9ece984b88620d44fb4bf7af63c7bcacaf6ff3c8d41b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_identify_service_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-identify-service-trends:8dbba69b600f32b272c5b3567a7ed932302d8014d48e059dfd1695305a88bfe4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_identify_service_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_identify_service_trends_agent.py` is
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
