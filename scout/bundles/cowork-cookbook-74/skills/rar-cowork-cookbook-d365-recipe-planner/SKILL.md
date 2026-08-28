---
name: "rar-cowork-cookbook-d365-recipe-planner"
description: "A guided planning skill that turns \"I want to automate something in Dynamics 365\" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_recipe_planner", "rar_sha256": "61ecb24282af0c16b17b3bb194aaaa804461f11219b44fe0907644ccee8e8279", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_recipe_planner`. The original RAPP
agent is preserved byte-for-byte in `d365_recipe_planner_agent.py` and in the RCI capsule.

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

D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_recipe_planner_agent.py` and embedded as the fenced Python below (sha256 61ecb24282af0c16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_recipe_planner_agent.py` first:

```bash
python3 d365_recipe_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_recipe_planner_agent.py   # or on stdin
python3 d365_recipe_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_recipe_planner',
    "version": '2.0.1',
    "display_name": 'D365 Recipe Planner',
    "description": 'A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'beginner', 'read_only'],
    "category": 'general',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-recipe-planner',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-recipe-planner',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c36f119a3c6418a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': '2026-07-28', 'mutates_data': False, 'plugin': 'none', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-recipe-planner', 'uses_skills': {'custom': ['d365-recipe-planner'], 'ootb': [], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 0.5, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class D365RecipePlanner(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecipePlanner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(D365RecipePlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
