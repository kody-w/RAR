---
name: "rar-cowork-cookbook-run-deep-research-with-a-citation-map"
description: "Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/run_deep_research_with_a_citation_map", "rar_sha256": "4fa6475f40c9acc7235e456544efc1dfb33b1926371ea452b70941035e17a563", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `run_deep_research_with_a_citation_map_agent.py` and embedded as the fenced Python below (sha256 4fa6475f40c9acc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `run_deep_research_with_a_citation_map_agent.py` first:

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
    "version": '2.0.0',
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
