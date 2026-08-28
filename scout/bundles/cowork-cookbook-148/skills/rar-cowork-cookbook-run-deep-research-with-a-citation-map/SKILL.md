---
name: "rar-cowork-cookbook-run-deep-research-with-a-citation-map"
description: "Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/run_deep_research_with_a_citation_map", "rar_sha256": "173222031f898c008f3f2293d343353185728ec99e78cb90e883a1c7d6a51aca", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/run_deep_research_with_a_citation_map`. The original RAPP
agent is preserved byte-for-byte in `run_deep_research_with_a_citation_map_agent.py` and in the RCI capsule.

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

Run deep research with a citation map — Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `run_deep_research_with_a_citation_map_agent.py` and embedded as the fenced Python below (sha256 173222031f898c00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `run_deep_research_with_a_citation_map_agent.py` first:

```bash
python3 run_deep_research_with_a_citation_map_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 run_deep_research_with_a_citation_map_agent.py   # or on stdin
python3 run_deep_research_with_a_citation_map_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run deep research with a citation map — Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/run_deep_research_with_a_citation_map',
    "version": '2.0.1',
    "display_name": 'Run deep research with a citation map',
    "description": 'Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'run-deep-research-with-a-citation-map',
        "upstream_url": 'https://coworkcookbook.com/recipes/run-deep-research-with-a-citation-map',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b41adf0669ecb48b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/conduct-deep-research'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/run-deep-research-with-a-citation-map', 'uses_skills': {'custom': [], 'ootb': ['Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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


class RunDeepResearchWithACitationMap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RunDeepResearchWithACitationMap'
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
    print(RunDeepResearchWithACitationMap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
