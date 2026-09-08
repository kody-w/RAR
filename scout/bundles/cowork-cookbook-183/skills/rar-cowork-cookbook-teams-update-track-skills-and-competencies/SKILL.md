---
name: "rar-cowork-cookbook-teams-update-track-skills-and-competencies"
description: "Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_skills_and_competencies", "rar_sha256": "b495bc4b8606d0c67d86226ee47ead9f9c732d56d8abbac7bab8fb4d61933c6f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_track_skills_and_competencies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_track_skills_and_competencies_agent.py` and in the RCI capsule.

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

Track skills and competencies Teams Channel Update — Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
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
    "card_filename": {
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 b495bc4b8606d0c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_skills_and_competencies_agent.py` first:

```bash
python3 teams_update_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_track_skills_and_competencies_agent.py   # or on stdin
python3 teams_update_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Teams Channel Update — Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_track_skills_and_competencies',
    "version": '3.0.3',
    "display_name": 'Track skills and competencies Teams Channel Update',
    "description": 'Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e65c1b68d2b99ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of track skills and competencies. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-track-skills-and-competencies-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track skills and competencies, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;', 'example_request': "Draft a Teams update on track skills and competencies for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on track skills and competencies status from D365 ERP data, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTrackSkillsAndCompetencies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTrackSkillsAndCompetencies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(TeamsUpdateTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOi2LrmX7H3jejKumZu5sE8URGNTCoICohIZUUWoyDzLNSt/94L3TnUqTqnz7ndn9qMTBXWeuf3ed6V+NuL07VRUb98fNEDJ1+ITprGUVAvnNxfsMVQ1Al4KxIX/F14Rd7Wsdu1Rd28vH/xg8ar47KNi3ze3mWZU8dT0Cza2vGSRZPEado8BHlFVgZtkHsxuBvWRbbgxtzJYq9ZYCSxEP6nzu4XYQG0LtLg6qSLIG/jdnzsbZwebHIWRuBkzcKLnDwP0kVZNO3iHVCY+MWQ/7go025WtWB8BxjUBwvWqf3FTleVxRC30UI6bJv3i6Z1WrAuzv3Yc2Yv3j9UVF3sJR8cb/ZkAdxri7x5mFMHfRwMfwO+BncnK9Ogefn48y/vX2Lw+eXjby9e6jTg0svDtlPpO21gzL7rD9eZ3Ge/cxxISZ38CpaXIwh5Dr6XQQ3UZOCSH4SLt2/vmiAN3y/+8z+TwamvzY8fP+WLt9enl/mP1uWLNgoWbeE0bQCi65SOG6cgYK8LJh2csQGGt12dz2FrQMby6+tz5zdJRbn4ab737qnk9Rq07z69FMAEZ47Cp5cfF8D/Ty91N39+naWU7358TYshqN/9+E1O07m3wGtnYcDq189v39/EgoXflsbh4rN+4Nk3XXXgxWUAhH/n3/x6mv4m7i0kn5+L3xXl+8VfS579+QnY+6xJF8j9a7EgBmDny+utiPN3bzrqog9yJ/eCdz/+I7FeFHhJGjftvyT356fgKHB8EK23kPz4/pG+XxbLN9++yvzHaktQMP+OJ2D5F3VfA/WPZD8y+3ei0zgHvfYll38p7q82LH9a/PwPfftnG94vwk8vXJCChq0dNw0+Ln57lMjPP/jfLv7wy+9A9P9RjF50tfeQ8Dlz8jgMmvbz559/aB6Xf/jl5x+6ElQxaNTPXZ3+lcy/iutDzx8i+Lbq3R/3Av2nPMkBFC2+9tDit6L8H/XvrwvTSWP/2/Xm4+L7Tpxfy8XsxBelzxB8140NsPW7OP748juAoBx40z0ga0ag//iPxT726qIpwnahe0XXLkCC2zgLZuONKAao1zxQA2BaUDcxCOzbOlD/c4Zni4tw8ev/8h6o/8F7Q32oncHtc/dAt88PaP/8hPbPADs/fw/tv74uDKChqONrnAMU15jD4VPuXAGaz9rLOmiCugeI5Y5t8AE09of5A4Djxa//upLPD3mv5fjrA7vjJxZq7HbGwaZLg9fZ43MU5G/+eYAWgnvgdUBVWnjArjAGSP4eRKIpUkAV7Rydh7aFHwOkAcTwpB4QwY+zsF9//dV1muhT/gRubPHkvQYCC76as/jwATgYpvE1aj/lgRcVix9++/2HxX8t/tmuh/BZxwEwyVt+gIUP4gL91mVg2UxYAOgd/5Gf335/CzMQkwOiBtmMw5lX582gXpPA/xJzfcN8QAly4QYg1iDOWVnULWCDRdy+Lrbh4qu9QOl8a+aLaCZWPyiD3AfxHoFUB7jzNZJ50QJGbuMmHN8vuiZ4aP3VrZ2HiRlofKf9dbFnD4CdihT8M5v5WAQ2Fzmg3fRrRTyvAyH1D81i/UXE60KZK3RROrVTRrXzpiN0nnmZh4S37UC4s8iD4VM+83Ewh+rRLs/wgEUgMt5bSj/MOZ/nEIANfvNF92ONM3Oo8eDS+lPevLWCU8+p8AA1AKXXLvZngvjbW0k1UdGl/iN+wNJZ0lsW/LesPGrQ+Kdj0HOeYd/mmefwsPjUoTCCL/4/nqXmwDCiqPEiY/DcglcM7fJM2Dxdzol9DqSzyfO2R3N+m3C+oNgXMP+UpzGovnr823PlI81va54A2dUgKxqjPeSDGgMJm+U+WmAu6bqeA+l8yr+wBvBj8YBI4ADAC9BPcxl/UTjf/WJpBEBh/v5tgniUDAgWiAQo80XZuSkowTAIfHdOYxvVcxu/ZRn0QzC39BDFXvQHr+acgbID8hfAiBg0JkjM61ckf979YvofNj4HpXnLY4jsQBfXDwHAjmA2cM7RnEVgXvsc5oGfHx9CgBtZ2c6+u6CPgKfPi0EdgKQ2cTtj5jOuQQmQ+8P8/vR0vhrcS9A6IFigQcoORPfRUjPaZGAMAjYAVAEdlsU5GAtAUN6C8BDoZDM+APx9m1ufEh+X3xwKHn0489mXjY9eAHvmEeHZB04+fg8jxl+VCZCXzSseev++0r5qm2XPUNoAOAQav9x9zhKvz3HgOW8svsj9+KfT0rt/70D1IPjTHwvg4yJq27L5CEFPUv7Cya8ABKCnrc2Tnz88qfPDAy4+POHiA1D54Xu4+IOGp/MfF/+elX8Q8dYlHxfIK/wKz7fktyp7e4GgsB/Wlw/4fPdTrgXfABeoLzJQZnMKRzAQfGXHL0sARV5rAGBg8ZMtm5lkB8DrD3oA+fiUf1/2c9vNiHady7QpvoODx5gAWuCZvq8sBm7lLdDtz4PmNXidz2ez+U3w8jHv0vT9C4DV4N843c2Mlc013sxnQ9BNYH5r51vzSRFA6OfZmqfM3/7u8Cy83flaan/G3veL4PX6uvjXs/0BhVHyA0x8QPEPs/rXWwO4EdjZjuXs1vNkOM+SDzy7t382S318cNLXBRcA7Eyb75vkjQTnIeC7Xn5mAmTAA+6/X8xmNjNpA9/nyMw44DTJgxL+0pYHZ31+ctafDeJmivsDrQFobr6w5VuITvpe+EvZXwfqPws+g7llluUXH2cKf/8GhuAdHILeL76eZ4BHbyfMWUOQd+Dw/vN8lprz/9gyfwB7wNvXTV//r8QNXn75k13AsAfCAp6aZX0z8tvS4nEGm10Aotvnfxn89gJqzQHxdd6q7W2IB8sBIH1o5kEFAo0JlIPvzxYC9/4vxvs3SU3kgKESiHLxFeF6uEuTMOnDHkn5NImiZBDgFGC5VbjyKAz1CdKnHRfQH+U6Lh26uE8iKwzzyBDIe7bkrCWLZ+tm00BQQGEHwbfb4JL/5tbTjTlmX08Ts/tv3v324pI4WLnBmy3zfLHQCnEhTHbvtbXM4eVdO3vdaDv8Rgp3mCJbYH7Rc0tw1Tsl63pw8zombdgjxlyFhDlFmWLX5RE67pajgamoZ20Zlk1Vbb+M90FwOrIdGh7yEgpVtx8PIjRgzW04dbqlFsS0tZVtpCbZCTelY4WMtEntDJ1QkWm3M9lxOek7WzpsDj204vJd4N4Mg3TvkbGRzoOipmIuwkbnC5F8oyD62t/pHFINZCnb54oXZMEZzbgoFU5IuzCjr5VRCg3uM23umOSW1xz6psi1zY5jJ+npXVa2dnFenrrdKUtuNB2OrrLcOQLa30sq6Oki37JIes15PN54RaxYEa9D9wvZr0epUdgSTy8pf9Z2t2y6rHTTbP3DulByC4NWVGNZ04qE1PW+x+o7uAD3WEWbbWleT/j5aLuCyhnCPsErZF3SYzI0PjwptDSx+HSQ2Quz5M7scq8oTe53a/1OFgD9hfS800QtkP0G8/dWV/Ki7tQssqSlhLuIOyneiPekKL1KppiN55h7o5k2jhXv0JPpyLDfSxNl7VPIWAGV5lhpuhMPw8QKBcsKjE1aMRJvLlV6allGEbL2GAsxpdugK3RKWJnVhlzZS13wM506CqLCCGEK51DGDXlu5xhyolvSjmwbLrOKi4mTftKd494YPDlOr7fJ5rp1vS1uW9tp9rwNDxyUkePV0FdJ4QrCEmHs9QnLupQj7vvUsP2D4CcVFFx6+LTB9qYQMbqY2jZ75pc30gwc0Uj92zY+XDX+NJnuRo9p45Zgxv7eXTairY2ct7wW4zFETpRnri8OylzvdoRy3B2LievWtUnxPAoerZhMJSqtw3fpZX2OGmfgW5RyyiA+3TZqne/vRi04reUeWESp2DW19SiiIONiarQyKFEH1IUk30Ncht2c7ahRCW+GM8SBtHE2iZINuMoXlxVHtxV2z8yrpdnuwUgINo9iMjBIGvKOY1bSJ0K2jKQ58KkKNO0dQTIdT+kU1htEirZTXNyuFLbBI7vbThCxgVgRWlLSJEEXhTGq8NAT0JKL6Q210qTBg5Pz8Xw2bsEgtbJnxiO6vS6Vqajpcl3oo2JJWz6K9hzBCnIWugFvBVtE0I9LrixQw0c2x3MpaESWc+Q5oWx1dXYm1tzxiZwEinnKuJIVNvtaWivcJBA8o5vdEKwDtgR5Pu7kAbL2a7/f3YZbg04Stbtf7yuK75Ngb1pXCtqXlSNU5SgVaSMWuzOLrs1Tw9SFlJ0LR03X++IUNt62R+kgosrDtk+VKj4H+Q2t2KSU0AobYxrPkSPVZq6aYeixMMOJpXJpH7Yxy9hSpgzoqKgXfKkN28KR90k4joc9gxsy72Jlth39lZMWTGiuagZut8xwxEJpm6sVP1Ss3GothwnGxCSXpXdnlO1BYDKRxn2TYPlzZWY61FaTlBFQLZ7SdcAdwYSiEjohaXu6OtqDyHkVh2ij5ncuMji6dD7ukFuxWlF4XE0rexTGDRKdVgpkWHiG+ng+3YfgDG0VeRi6LYcxUOdwW47qHYOPJpR1mylX9hqKM+eS0MT+5lDZljfLVMEv+XUHp/Im7ZwY2Qi8ZPBjkOb4lG1shBZp/7yu19aJHsIDVqa6gRkNdWhZTTANOb6EFD4WObWODhN90++cMeiM1htVnfBL7d45O2I1QHV/Njqrx6Klo2DFyT3hiXHc7I/4lgrHKt+tJ6yLCzsgjalh2ErrTl0wiAV8qYvLdlRXTVmRV2GcspVwpCGEuPIA2ZGVfFmzTNm38REuGOJyD9PtzUEQEgqW98tRjcZ0x7GX1GcGH40K+Goy6w0YdNXhmkcFRulYzZdHNrwekyLTtkZs7smQ2WrrivJtiOnLfWHmF2EtkgLmrAw9CwRMuaiE1W2FnVkUBzM6Lpu6FvDurDTE0EKS5i4NmLggOTvF/kZgM/WWTORKtaiBCOHN+j5eeXeLXLoDDFfRsCY8D9YNnxI2VcP7l9wgAehfaWLbrdthoBz6ctqT5Yaki35o6LMF3ZuV1U/LFSqa+GpIapyyDgflNmgOTzOufYoGRhlXKQATqckrAhF5ezvV6ipRRo6zzFWUMRWR4gzJqgrR6NUxiVIu6hNecc5o4phF2EuejKV7CZuO5EliJONYCpwejyfBsQU1N+2Lj1+0fZbbw/2UeuumLJNx3FzduOGaKu4MKwrrZLnvDmJoJjksmNrF9itZ8bggQUU3cQo0Mft2tSsahKQMBYXVmHVuKS+tV4fxKET+2u6idNSiHTeKt/VyWiJLvWuacri0Ccth5qldbju3OJ7EmtGKHcyg8XUrn9TxfOv60o8lNVE4ni6gu2UYWcFJcJQdCA74gPuCKBe91OeQYh6Lo5VsnOnQVD28ZcvrVoiJ0CH2JzgSNhl3daJNJVc2Lo+NV6XxfRtxewYr3NisiFyp+piwmoZ1JLQ4NoiU4AFz2uCKrhp3B10n9Knmm2RiW2e/SeFYI7mtz0xjKKDn5IQJeuF4hqfhMcnyW9StTcTPLXIyMoexN/erpPJXjxp6ieryLrJ54eKdNlEWY2vKzhmLuS1pNEnFeGvVKerUS0sg1REpK1Dg2Xo490J11o2TzzUXjl/D91xpi/Otjq/OyFtgvnEux2mZa3usGE/rFRf5010tMOksI7uY8Mptv5UvCIPv9XMdKyiYVtBhW59OxwvDCrTFjzs3jNZDdilUXrteEKxA03Ay+PIuFgf1ZkFNW22v9mlD8aUz3c19myEaa8cmuoyGvq72BYrCy8YQ8vU1uneUa9I0PxIrjV1bgl9ifmRVAhc6BpiIGce6Qioqw0N/4PowM0guiXthnhVop1quKa5P7ldHOVeBJlFplCS3NDvu1mSBMPlEVGZzalzz2m+Tkmt4t13bpd6eoAtxgNcevEkxgXGY/bUq5PwEApGaYs5RSisGJYQgRjOWcgTSWGLctMNFnumU4LrndlTRXhJcnpKbGENBr53QS8bVhHzUbiEkbq+X011lknx1dr07eul6nrnyYrTeXczTKpVoOCREpeLuyzts+FcigpqMOtDh1EoDtmOjbqnRl36zG48+uYTReLreC0BFS9zeyYbPhgSzTzQivbcr/SiREXQ4B6e1sTNTI0h2PJv6ZSboO+4UF4MG1xGMJyWGh1Kp8JGkNPzVOho8e0tsN6jSJXLvbYr28uMtrbH7HaIHNAyngrZDQ0NW+w206vRrM+aquFK5NctiEGe78T60hGx/JqfloHsmKcFHq2oyVEXd627JseIx1pkOZ0mRYMpwqrJ61yuyXOwIyaEky5duK//Kn8kTWeRl4B85b1PTqxDC9BK0rXq87SbFPZp91UplJZxXIWNO226jkxu9YwojtlRduh0yZ2lKhdPJBLe+EHCvu6LEevawwenEjvlR03pJg2+CpZ7WFm6cWiJlRYG3k8Y3eMJKbyhsbM3IWu+JtkQc/VBf9gnbMZv0Oi2nwPGIMx5vzzfn0im9IPTNYYD2+s3nL26m4gEL1ZSiuzu+qk3nQgA0vwSIeyISlVB9zRDXDaeLp7hdb1Ci2yzhaQmuXsWtpsCeDuqwwCm8zHwOvVWk3pDhBkbu2l1jqjuxaY0NrHrrI8dcMsSqkBvEQuMOlWBxDRXHAYGKhj6MttiDOfvgoo4ysmKULpdwB46VnGrDiblxd6Jgcplo2mMSHcZGTG/XOzdJruxw5rmx5YDpEZy8lxm/7ZsL0aZneKvKsSgazQ6hlMauR2l/r+qdftxs5fVNS8AbgraXxqrhQXZb7sjIU0psV/3yTG992fFu0sFdhz2PwcdAVhxz26gei1/ueX/eq4FfqxAyRu6xpzcIg6J7ditubzsplbTpXAi+c5VSrrSGXZ54zd5JLWXKAhQPEpxRmXUcIzKqxOM+2VieLSX5wDruZvItpFn1KxrdT655gJDTSWvhtRZ53nDlsRGOFJic9iVC78mVd/JxB+0lzO1oJQzyzjrWtWfLvCTx28qsdpiWm+Zkp8h5kkWVuhy6SKctdSqaZNhlHLIV4JjiJQxR+ssl95ith7STXxnQdTPIx+jkOWezrZM9ZR+WSCCZcTWgrttkEyMTJiZ2JqJk6eEWHlkKhsrjfkX1tsTcNIbk5CgpljW+xU3M9PMpIxvCdNYxX8ls0FTFLR5i7LIVz81S3e5G3QKM4MUrr4ZZJlfx5Lo5uFuvzoPVXTwkgtY4tHUYGH1t8F63gR1ZKImRO929RrjDCuOSVeL6uRzXh1zHhtj3yCoobb4cEOFmuULjtPjBo7mN2ULGspYQDQviFM37ds/RYbav6wB2S0OfjB0ZsLQY4QpnhrZSDU7PAYwXdLdFCITrOjvCE4si3IFqsFOBEPklUAL/jpyU3DnktaeqyxtqdrnWZa4U9F6+ZPfSbowMtBYDSOkL7E6QlSkHyCHs6zqfHHyJ5XLlk52ans4cfWegY3MSgmXoG9CxgjV+O+miBocGOEcJbCTtKqmLah4zh37az0d9YuVomG/3KnqXrGAUD5vy4qLruudRu6W6jQzmB2VzcacMW7ln1MPxTV1C+IRB9MZYxXUg7X3RgaA0pBVeslla73QsImQPrlz8CNO1Kbe6tT9AsnfmmcON5DehyymXkOSZmwyrJSLITaNNFQsnutVdoOt2t/cTisCxVZKF6PnmZZVj+Z3dGLSFugWxUpdX2t1bhRIyvSDWGGFE/X4f7KJ7PLmrG9EfVvIpF24Al3yOO0O742F36Tj0gN183/YD5ZJOSDicueZguGWz78L1XVd2uG0DnsIrObAh2DIgQylVeukMtRzV6ErKCh80q2qW4Y60yCA0b+1yI9+21KgBEtJ3PB0c4laZT5MF0cfbhD2C8j94klQFKddk8qHeWG3LTaFAFr5J5gysNXCbKZu2928mlLRpv9kOPNRSuwTTRgRpQp3v9qJ65jPJFLXdxHibsl6mHnUuFKbgg+YyHCysju8dG+Bk1zYBbazRKJk253GXsAUs8QCs7Qt9uLAmPTblFm932GpQMqPYhcF52Dm31jB6wjlsbsiSOnRL6MStQ3zDjqFDNmjZXzMxRmC1obLB924sNNAq7Yz1PlypUZUa2v0sdNDWwmTpaAgyvnG0vuV8xI/lDGdt1BtwR0btTRAqODz2FTpqVLYfN/sKR12MPR+XLklwbTF251wRJ2ctJmcPNs38KvftdRPebjVLsvUAJWq7tzZV3hFdGx4u92o6oyq9ZzzQRGh2s4aKzhW5Jl3bxoo28w+yk46iWHgeJeJBHNvBDRnv+FQP22NhoWQ7lTW1vp6PB6qACK6yhaMhXuiNP92kvoqCnb0hSbXYdPRWoRgx692uveJYb5z7sCEmEyZqy8YptSKJQwxqElVD6kR1XoAZtsYdAL8RiJ3h1Qldcipd0teVGMQGEpFKfQ4w2NBWdwDUpr/R3NNK2lGwomd03cPdXko7y1iZXiQEzem+9h2mRPNObgtUbg7ouTWXd+kWnTt1e/LVnUlDJV5pd5qKJhO6Xm9V2SnGQI+mty35Uhd0udZNaQV62vWcdr1na6oCmE7hTQH1ynDV1KHWruro+0dBzEJIxTcX6xCd9eKED/Q1uuBkeN9dqx1/yy+WKwM6kpBDXnSJr6o7ZpnvG6Ugl4cxwTbawV4ZtYAi6KBwl6obVUKK3amGLhXVyTUWkSTrr4Oi7HYqOEOkHnrEjhheOERi4JNvwD6ayq17VPONj4WZjfkiirhZuwq8XNZ9zLFsBsUO151GOfAZJwnElXzKUzK4nrSbrI5tiyKRSUID4p3KUnTuE0d7HmqHG7u9OAin27Qb9ZfzeqjpJSw6QUDTJrdvPQrZXTK8sT1qj3sn7YrYm+0RujmDe+/x7KpeW8Rrbr2esw4rpgVgYQ6xcEHQJMIiN3TUWufIPlpXkbrfRxGwx+TdbmbuLBEjqajWNQ7mJrsdiDGaam+PjXWKh15HhmoDDocn1DabpcOM7Hhfl1ww3qeB1TtOu/YQ1cN9766OPgEttyBw2QplxsSqeXHdozSaqo2H3wnfDRpo1Ac/pQ/xaFUEJW40WLfayhsgoa921IAJ+/zEovtx8sDQnnAWfPclHMVHCAAQStPxFj1Ma7u2+iPdlpYU4IB8QFSuB+Mo8uOFPNTWPsZLGkNQ7eAB+Np3Schu5dC7wUxyVpdHdldumr0nMFu/42yqT1DMmcyWqjlZWkqswCF7MtwieVqrHQqdxBWvXotVGleb5sQNHWCxaYDHusJp3cLavIObriOzKWColgtJbFrVLb00WoxLl7cQ7RnKOFDY9XS4Nxi15gcs8PWWsmU52la3Lktat5Ubc3DAuYES1bZYRcQSaU7klIFAYAOGEnVndjhSB8N+HKg7CykeXK/hwIO5RqEg+4puukiCit6OpBUZd4Th9FCjGbooHngoZupxt2acyF0amsqjg6CpYikXMq3KaAbjCiVglgL4nY2Og3en0OOEWkclXrdHZbOG7MPIaJw9gUmMYKiouCEkdMFsvzDcVQCRwrJdF5cQJ0riXiK9p0PKcLqlLHlmFYTqrMEVT4ENwGlaSYVOxGiUH9PkwC0twvcoiF4StJYPbsKVk0A6q2uhQ07Jk+zAZgpEar0vLyeIEsL7pSQ7Jzw7dMBBg5dTh+tpDfMMw/z008v7l2/PF1/+G7+nmp+3/D97tPN8QvPlZxGPZ2Rg48eHro//HeN+ef9SezEw7flIq0m769sjob97oPXhX39COssZnz9b+vIE9Pngt3Wu8y99X+Lc75q2Hj83Rfr4oQTY4XbN/KPAZv7dqAfev3/w971j4GsEBq7PbfG5Dlrw6WX+0d78C4jAj5/356/Xt4d971/8t5/xfMZI4nNQl7PLb0/YgafYK/yKvfz+vwG+Peq9sC0AAA== -->
