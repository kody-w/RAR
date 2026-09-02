---
name: "rar-cowork-cookbook-run-deep-research-with-a-citation-map"
description: "Read a full folder of source documents and produce a brief you can act on - key findings, conflicts, and the strongest insights surfaced, each traceable to its source."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/run_deep_research_with_a_citation_map", "rar_sha256": "4fa6475f40c9acc7235e456544efc1dfb33b1926371ea452b70941035e17a563", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "run_deep_research_with_a_citation_map_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/run-deep-research-with-a-citation-map:57a591accc94b4dc22cec74a122b6ef2d877bb7b0d29b392739c9e8d31707075", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/run_deep_research_with_a_citation_map`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `run_deep_research_with_a_citation_map_agent.py` is
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
