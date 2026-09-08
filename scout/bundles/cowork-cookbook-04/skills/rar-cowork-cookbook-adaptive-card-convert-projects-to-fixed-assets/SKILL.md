---
name: "rar-cowork-cookbook-adaptive-card-convert-projects-to-fixed-assets"
description: "Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets", "rar_sha256": "ee4a756223f52d0df8b0cb65483d93f07db34abde4cabc0df95d33a1410d3953", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_convert_projects_to_fixed_assets_agent.py` and in the RCI capsule.

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

Convert projects to fixed assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
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
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    },
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 ee4a756223f52d0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_projects_to_fixed_assets_agent.py` first:

```bash
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_convert_projects_to_fixed_assets_agent.py   # or on stdin
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert projects to fixed assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets',
    "version": '3.0.2',
    "display_name": 'Convert projects to fixed assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-convert-projects-to-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46720b175723b1f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/convert-projects-to-fixed-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-convert-projects-to-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical convert projects to fixed assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-convert-projects-to-fixed-assets-2026-05-24-card.json' that visualizes the current state of convert projects to fixed assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current convert projects to fixed assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing convert projects to fixed assets status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of convert projects to fixed assets status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConvertProjectsToFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConvertProjectsToFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardConvertProjectsToFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOjxpbnV9HcjhjbTVWJXag6OmIQuwRCLBKL60WZHcQqFkng9nefRNKtst/z6x73zD+je6sEZObZz++cvMmvb97Qp3X79vnNiLxqIXhFkaVRu/CqcMHUt7rNwVed++DfIqirvs38oa/b7u3DWxh1QZs1fVZXYLkQVVHr9VG38BZt5IUf66oYF3TogQnXaMF4bbjYGup+EWdFtOjS+pZVyUzyGrX9x6atz1HQdx/7+mOc3aPwo9d1Ud8tut7rh24Rt3W5YMfKK7OgW2AkseD/p8Eoix+LKPGKRVT1WT8ujobC//Rhccv6dLE7SIsesOo+LHRaWLT17cNDKS+YBV4ALfq66j4BPaK7VzZg4tvnn//24S0D12+ff30LCiAB0Otdg1kB5int4SWsWfOzqPRDUkCo8KoErGhGYNEK3DdRG9dtCR6FUbx43f3YRUX8YfGv/5rfvDbpfvr8pVq8Pl/e5h99qBZ9Gi362uv6KFwEXuP5WQH0+7Sgi5s3dsC+/dBWs6U74JAq+fRc+Z1S3Sz+fR778cnkUxL1P355q5vZQ0D7L28/LeoW8GuH+frTTKX58adPRX2L2h9/+k6nG/xZ05kYkPrT19f9iyyY+H1qFi++GgeOefFqoyBrIkD8d/rNn6foL3Ivk3x9Tv6xbj4s/pzyrM+/A3mfIecDun9OFtgArHz7dK6z6scXj7a+RpVXBdGPP/0zskEaBXmRdf3/Ed2fn4RTEOTAWi+TgLCbXfC3BfTS7RvNf862AQHzVzQB09/ZfTPUP6P98OzfkS6yCqTnuy//lNyfLYD+ffHzP9XtP1vwYRF/eWOjAmRP6/lF9Hnx6yNEfv4h/P7wh7/9Bkj/l2SMemiDB4WvpVdlcdT1X7/+/EP3ePzD337+YWhAFEde+XVoiz+j+Wd2ffD5gwVfs37841rA/1jlVX2rFt9yaPFr3fyP9rdPi5NXZOH3593nxe8zcf5Ai1mJd6ZPE/wuGzsg6+/s+NPbbwCFKqDN8ICqGYT+5V8WSha0dVfH/cII6qFfAAf3WRnNwptp1i3A74wabQTs2mXAsK95L2SdJa7jxS//K3iA+sfgBepL74VvXwMAcF9fePz1HY+/9vXXBx5/feLxL58WJuBSt1mSVQB4dfpw+FJ5CQDgWYKmjbqovQLU8sc++giS++N8sciqxS9/jdHXB81PzfjLA7WzJybqjDTjYTcU0adZcyuNqpeeAahe0T0KBsCuqAMgW/xEfyBSXYAK1M9W6vKsKBZhBhAHVLHxQRtY8vNM7JdffvG9Lv1SPQEcWzzLW7cEE76Js/gIalUUF1mS9l+qKEjrxQ+//vbD4j8W/9mqB/GZxwFo9/ITkPBRD0HeDSWYBlwInA5A5eGnX397mRqQAYV1AYyVxVn0XAziNo/Cd7sbIv0RJciFHwF7A1uXTd32c3HN+k8LKV58kxcwnYfmupHWXb8IoyaqwqgKRkDVA+p8s2RV94sOBGcXjx8WQxc9uP7it95DxBIAgNf/slCYA6hSdQH+m8V8TAKL6yoD5v8WFc/ngEj7Q7fYvJP4tNjPkbpovNZr0tZ78Yi9p19AdXpfDoh7iyq6fanm0hzNpnqkzdM8ydx2ZMHLpR8fzUVQlwAjwu6dd/JqTcKF+aip7Zeqe6WE186uCECJAEyTIQvnQvFvr5ACTcpQhA/7AUlnSi8vhC+vPGLw1RS8J1o3W+MRyYtXC2M8W5g/tkJfBhRG8MX/p13TrDctCDon0CbHLri9qTtPf8w94uy3Z1s5kwdB+cy9743MO1i9Y/aXqshAcLXjvz1nPpR9zXni4NACe+q0/qAPQgj4Y6b7iPA5Ytt2zg3vS/VeHIDYiwcSAqkBHIB0mf3yznAefZc0BTk/339vFB4RAQwPFAdRvGgGvwARFkdR6HtBDqSaPfXuQRDu0ZyxtzQL0j9oNdsXRBWgvwBCZMAtoIB8+gbYz9F30f+w8NkPzUseveIAkrR9EAByRLOAs0tmfwHx+mdLDvT8/CAC1CibftbdB2kCNH0+jNroMmRd1s+ufdo1agA4f5y/n5rOT6N7AwIKGAvEfzMA6z4yZo65EnQ7QAYAGiCByqwC1R8Y5WWEB0GvnNMfwOurPX1SfDx+KRQ90mwuW+8LZ0XmNXMn8AxXrxp/jxLmn4UJoFfOMx58/z7SvnGbac9I2QG0AxzfR58tw6dn1X+2FYt3up//Yc/z41/bFj3q+PGPAfB5kfZ9031eLp+19730fgI4tXzK2n0rwx/n6vjxv0rwP3B5GuDz4q9J+gcSr0z5vEA+wZ/geUh+RdrrAwzDfNw4H/F59EulR98xFbCvSxBqsxtHUPe/FcD3KaAKJi0AnH4u7jOod3MdvYHS/agAwCdfqt+H/px6oMBUyRyqXf07SHh0AjO8Pb32XqjAUNUD3uHcUybRvKd7JEoXvX2uhqL48AYQMPpre7m5LpVzqHfzZhD4AXRrfRY97rzuax1/DYFC890ft8FGBdqTFEg1D89V71vvMjv2EfsAnMtHyr2S7KHbLOEseD82s6TPfd3cCT5g6t7/Iyf1ceEVnxZsBCCx6H4f+6/SNZfu36Xo07jAqAFQ58NDxG4utUCAWdM5vb0O5AtIlT+V5VE2vj7Lxj8KxM4F5g+VBSDuZQAp/2ERfUo+PQrNn9L91gr/I1ELdBoznbD+PBfdDy98A99g+/Jh8W0nArR57Q0fW/pqANvun+dd0OzLx5L5AqwBX98Wffsjhh+9/e3P5Hr45+u7f/5Ruv0MbgD8Z+P+s6INhAcChEPwZ/4FTB7ADMrbLO93Q3wXp37s0GZxgPj98w8Kv76B2ASQ0Xuv6Hy1+GA6wLGP3dy+LEEuA4bg/pl1YOz/svl/UetSD7SbgFwU4d6KIFEUiwk0hMOY8uHAJwmcwsI1FsOr0Mdwzw8jPPD8AIyviRDDPARH4BBbExig98zkr3PHls0SzuIBw3wEYBB9HwaPwpdqT1Vmu33bazxS8qnhr28+iYOZIt5J9PPDLNeIT2KyP25taCLjWvcaRsm49DyhEerJtjUe5GK5Hfxdl5unrckknZAY3pbT0gSWNkWbN6fISSjHJfIrppLCFDH1YG632xInNtI23FJQbKziwTblwJ02httQeZWn3XlaHzWP5/Ljpej5StCaeOdUVwI/xQVXBylGWPoWytWDOB0PUy9j1MlHtSxYQZpxTbICw3HT3ePovcIOUBBj9T6QpZPXrEO9S3cbu1xfEKKzSNe0S6JFCp64ll7gU/bOh7ZdfVTl7R5e8uQaiqrVzayRbFjyZ6mRsl0bn6HlHmupox7o1MlbqsvGQvhkZx51lwqv+paITNyInc16w3nW1trqfG74O1EbVWx1I6KlXUKqfDKW4mUZ2C5LkrjF9VlLb064G/Nqh24hVt7rvqAW9Jma+DWnmBjb33bsCN9O6GFfclwkYwqETUudxi65myR8cdxqxFYs0Fjx86WWGM5qq+POBdto5yo6aowoTNSWb3YnZ1PQcV7j51RNxquS5nIXXE2LaisUcS+QRjCxq0pV4mhWkurMnXTEiMcHPEs0Y6zYVF8HiREaXNkNhq408MXC7TzeDO0xzssB2oY1w3K6pmOXUBM0u2ev6+kqB2XtnWp4Mjab/Lolt4rWVFMo00lmnoyNUDT4JuTFnLNRlVE8h12aJ19r0hDiLEGGLqJCHNdFs9sx611V7PxD45yHAlvd+ShLlu5EZwyT9xk5ckdmbdj3U+7eu+VWJLgdPbg+KeW3QaVDasktaRhedcFdlSKVO1t11Vx6g2Xg1MRS5ghny7KkrjgjoKa/dpk+Ini6EfZNzUGNt7HS3qPpK+pboM06ZuIx3ha63PK7q9uPdU/BG2ad7wIKDtNLsOIM+xISRYwXJ7yneEiZLlacsXEiIw1LccZdxU0lTayYKGul7CFsb+ImScoSok71TmW2iVtVm6EqDVa9nKvpjCIHR2OTNaFUez02SxfapjHrNMIucjJvGegQfr4eSrYzpomFJaL0V7gT14idrFRCudBHOJWbe+/wZXHd3V2/diRqTBrElUJ8WV5ONKLdhA2VssOptJaJYJd7He6sxIvi3AlEz0TcvGSaXmWJPkXvkXdblXmmN5KuR1vNsthMIGLa2qs1GyZR6BbLgKJOU8AKiXlOWkvZFNW2mYJpJTUdpnKi2ZlLnbjtDjwKbTEL7o3L5bTb62R7Pws1dblfrgaLWGcvPCmTmZ95ZounqrT2+bWYO5dsifYuEa/qbKNz7t7DSy+10crp5Kte5Dc/cpMeXZb8Fdk5wFxK3jLcyYLXReAoKaVuBYbYpXqW8kI+3IQ12SSCcWito8+T+p7L1pCcKRFvHDmAB4q001ZxcNoKpMVIyO1An8Ucy9Fqc1Xp+h43cWmte885YiJ0hAqTORg74yBDiTb6SseZKk7rKhHvcoBw6LCjlHqjSBmd04EkHOwIkiAFsq7JhWlNUbX82qf0hg+QgAoFTs0gBRcmXkcS7sqsDkHFYAK2TApq6XiQwKZ9IvRsSu657WTnCntqUhW32Q1/PK+O3r2Ru7pms4pM7RKW+elcQJPh8KvVxfc45uzflox0JTwdaqgQzE94JJZPeETiaLf2Nr02dR1wR5WIFhtUVlzgu4yw9+o6ZfaETJ5p0b47Q5SGAMLMc1yB1L67u5FCmJhar+qU6+sJ7yUzSHrgoxRzYInv1MRfV+r57Pv0YAWYlNnXW9JJiXPxrdhbTdXBqhPP0lCHgK8NI/iYPGA8uVLpI3bZimhun5qdhh6NmssxguQofRJCs9mazbFejUSDb2nxMEqSVAUlofOkx9Nadg5QckLZytBT+apJtFXKGIloLOm7o7wPNk5x1rXDgU0H17ZkJOgU51SLmyI/sHUjHHUd73Bbv+tCZcLpKqjaNRlfR0kbS8tymjVdjtDZOGu7JaZ6zbYLmTNsCfGFj1FTHCbqIql8f7utPJVThHV8xLCJgPrD+YKScXyoyBESWqKivGFijOpWkhHkFwlzkxUN+GkDsWWvU61hJb7shvpRcekxzIe9EmpH1IrFNvOyOJammC+Pd+coTVh25bghua/F/W5kKKNIYq6+tZ2y2Wjw1SRFSdKOLo5OuTe69LS5nncbH2HxA8Ol2SE8Ofiu5McNQ6rstb1Xh5OsD76bs3KnddBNLPadgu1wvcnaK7ucstWJQCzxWoc0UyetceJDXdyDSMadDb9NhzQdy/uGZqwVnVtVKWF5V1DU4NdHfGcdCI0Vd5ftQYfNi4gFfrTzMwCVqaQrcWrG0lkQeUNAS4dheyYyKwQPVfzKoFfvCgneRiyCxN1m9bK9XJWtqNUNdVqNalCcFHqdnTe1ERuFtjypvXJkJi+Q6zo5EVKgq4zMnCq1ZTMCa3t+3Fnp0XJPRxPEmXwRmlK/kZDOOgMmXX15yyd+dGUEXuaGDN3lYxTywtFrADxskS2Hs/gGu23WYeNeLlB1Ce/JPacErnOY5D4VomUXsctAuV0I0sDsCneF+ocTT/E4v963VibZMo3mPmnwY9isRskrM1w2s2PfEg1vNPdhgyubTCHwFjwPNVs3BILrlcLYKtQVJP/9oFfShPMcKmZ2Wh47jIx58q4nS6Y9HA3pvvVQKep23e3SaHJtV7V751GTNe6mU7B39a4Zt3Nyb20HymPW5puNUCtQa6/gfMXRh04v17LgQHsJ0xg3ky+jlmEIdjp6/iW29fGemLflYe27YWDcFYJON1PjnzZYJ51szV8d/dOO5orVcoKRoCxqPFhRaKh15SlA7nK/1zd4up6EmhfbPavx+/xmHM3RlLgs5NSzqdvHS+kd9yRscZ7GWpfDJdn5rnvL/CvbJPKuH4UYEIUvOyeLmtvxiHd7f4z2mbxqdxRJaQfGuWOH4RRpt0DVCFhWdiDQmz4onXbKtyGPh7Zz2QvbhIQMmN1RcSjvaBjseC58iajh/noJa2VkYMkoN66iW/VehPJ7T0eHnW/tPfvADKTfHdbLeJsLhOMoWGAWEoF6IsCr/k4ZkCmJshun3EgSZ+a82i7zJPPUxGIohODki0hRrmPjpe+cWCPfWciORBNa3zZB4uSKf+Lu0cSQ+TkhlivhjqixahUG3lpRHm0rhEO3UbbR1DTFytTkdxB+uZkaVtHxiLpITy/Ho+rvic2JI297e6pWXdYEpG1h6LndSJlV8zvE6OUTvJMAunQKtw1u7DThORTze92k7vYJb7mJ6++ONTLCDhO3vXUpatEQaarU2rot8L6Sj5sSk1UFhkBDxZq3LbrNbTg/BOlmtHYyV+NpbTteMSoWguRgFyK49xNl37cTNUR+jklAbu4WbS72lr0mbcx5ikzTzegdUvq8ud+kyoDTiT1GjcCIhlnTnW4pftjAtUFqK1/s5KXs2LXScvscbUz/ZkQbatcqBUbQrWLay8K9I6Q8KKNfuIm47ah7Jw/rBo9hcwopQS3ldDqzotlztXlKVvYtzTboprXPXWK07NU47pVLe/IcglziV7JFhWowd+P2Zp5RYZDYCyQ2OBwdrkQORedmvWRPB1i0ODazYim3wzymJsWA6wCF7UIxzMP9NsqniDKdHc5KYueB3oFCRlkxGsVeCcxZKnClQrw9icGq3EUq7uPX44ZuwhpGKLhblV06eTrFBe4p9JPIJNbwgEzkVjJ7a1RkTpOwZGPgO/t4l2ILDTCbY5ADwXPldEtwZcdnU1Y4N7vbuEabF5uwrwfrWDUpq/JGbF/LeyVOOxcVmMpDG44j9S5Ecr5x2oZpV3tfn8YGRTyiS1EeoAx6SA+7E99EOlb46RLhQRLEvbm9GJTBHAPBvu46ZY17JtmFsMJgfuJTzHbSR/rKO62kuN6ZdTg+bDXpBBtB3gz6dBsve2KFT8JquzbTckrv2tXcV2F5xsxl5AddbbAW7cjwpYDGKTumlnHcWpv2pnMb1Ei6gGjKxq0h8eRdGcsThivTC+3E2pjKFmvaFVNXPlMb1assiiLXpLYz2XUgaLTX5UWX1AntILmckZrWsce2pVfKeVx2oqMPG0tVI6aDD6MLBWV4OQljr2JTvjcTzS/8cns3bjhXbTf3dioMmAg9fJ/IVxNKnQkZNocBPhyZpsJAgPPw6tCx7W6/3xEbgrbdPD3uLN9VGd0mAwdtFGl1mBxQ5gIS7CTYvYoL0YG9jmJ+seVNA/D7OjEejBQ9cWOPNCMiNu5WhrJrGtDyd/zR9II80FzYu57GvIXz9k6Ox+MJbsqlbAf6qMGdjTdMc578sr+wV6xyPGmEw+lqn9CaJAakN1loKeGiOrZDufb2fr7GL51V+noc4quy7CKpgFCbglYKci4CF5XPth1Ep6mAswvhEfflKRqbNRloo2vBq3wN6wUdMvK1xRtEaZcxdh9dPxsqt5LJSb64WBEP1XipI9/sbESBmWWKpSckdvVleiguGW01Z4Xk3fPRvVG1xNMFemwwqRzDC6Vkuya5tq64svZjIyyp6OapK1hAD5Jbm2OzOUhGvw0NFFJiFV33tXGDw3N/O+7QXPTFMxyVOwBIyxXJL29JhYO8Tab1+hTfYXxDJ5BQInaKrKKgRZwNo12ldjzZm5Hlz3lAr6q9rG3WSApgoN4lagUTq+Mm6KchuyFwp4fsBtoQwJdjJQrykE8CjvgwuSuqc+UffQGaLoeYPdcHa50N4zhOMrUnkqlUrcBw4k6JVte7nde1j9mrbiPHhKwXEp+p9hKFqgFaGZ2r4JOCXJ2Ypla+v80VoY5dWbjcp/vaL/HqEG6xSefDY7wrA4jEL9sUtKOykUer/HJAatI4Xsk7tGbd4EAqLW3spc1Fl8TzRCFpgbleLO4pncv2B8uqoZsz1GbuTY4y9qEwYocQty53JD8J4oW9Vz48HlxozVyW90lShTjbVmdkIi5nWibAPpyNHQ74AugDZ3GRTEvdVEGLMiIjoymU06RxOAw7QclP7H4ti3fuFgoK1qBB5tBZdExY/36yDixKV7ER7gxUjkI7YjvQB8gEoY977nCB3KWs41R0wNzwhFFJyBMcRu8kSEr9FYzc0qGCud3Vs+MumFTspqiQx1wPccgkfr5qifJeLEn9Job0xJ7GEOlXZDrA3Z2fok1uH7SA5dZwUx1K2HWxU+uOuj3Rqn8yW19xXZlo21xFzzvCC2B/3yorrZn0hsLpAOmYFeWEjn08RYdl1077O+lOxwIVCVo4WZ53gxian8wy9i4sLl4YBz4nvifvo+ziUFcUAc2GUAfImQts31Gudus6kGMlu3RX74ahozzV0cT8DJEHzwVokAGoixi6hsYdWcLG2EHlqqdbTKEjZ98irb7uYiH0ILQt221rXaXtREz3FeADrzhliRGYR4RjOo61rpBr1M9Bm0eU5HZ/L4lkOEAl2wtW2Po+Yu+xisON4U603r3mHMd2UXVgRLcOYl4J0EJYHRibYq8Mv09YO/N2lYL1GL/s++gSpsLZ6AOPIDRddK+IyPOq0EQndR3Ja8jV17nM3XCVmo6bLpcl1zpCGlnbiN8ZSIJuwBZcmcgex+rl2R5vg5KIp6bLIUj1eAlapjiPm5MBh6bkTHE+FjByKCeudi4BqbEgQKp7KyoXJIEP7kZc0cUy7WwBinP77nkrXfTW5lVAN10f1CuJuPuqM8lL70Kkcs+CyKBdOtaK6zbBOe3S7iW/8ylODccNqWAaIkaNQdQcm94nG5T4QIRBwwdZJxUPeAldp3Nd09bVTlNKCGHUTh0IP5sszOz7nRJgxbmxYL9b2Wp1V8/F1t8I1+A2bfm1at3L9gha53t5gO6uwA4ruDT96hKFVOCKytphPTg3A2IbI5qh7WrcVdYXb3kOR6yKz2VEyJHdcg5cUGXCXBCMCXgCP3JnYkd2e73WrKltGgdNozivDKEKAtPTN+TUXYV+uhb3nlgNmlvaayWAEJqM8dOAHFQzOjgX4RxDhtLuw9qEM5jSwF5VVwlpc/A2OQxdUXG9WsPLXBfpWBdPol6sNPcoF121OV99H2wuVZ0ho1VZBOQ4mAzAFCQ+BT1ybszBRnYhgFq2s1YNJirx0S+11Y2S9hKorhlDivf+VC53tusQvS+j8kQTexTzUQtZEevAXG58OAdbqURgGsUVEKxiu2Dte6tDBeo7NIm1mAgsJkp2csxu0xnX99K6WN0dWpRrJJIJuS9zrFk2nNuYd0FD4xtm4kJHwS6CYuTNhuNjIXbUSVsbCWhsa/F0TQk+tsP7NlbHZV2aPILsM8gUw01M3iYoZ5ZL2J32p3W53A8sqtqra1KBHcRE0p7hHYb2FAbNSQtOGtIGp30J0oPtsTXsQOdOxNUDeq3UDgHhm1HiMCkkYa3OVr8+mzJ75WTKS1trm1JTFp6vcRuZaVOaN0/GwqwP20GSbdW7akOllRJlQgKr5RlNkwUgHiqcrXH6gT/x+WaoEEwnAxXK2rrAWt/QOCq8+1RTSWWykiwUwPlhtYGOa8PSJvUaGSgR2KuQbX1qRDlvNWDL4xVpVH41qH5EeaFfcdcpRjaERuwidKCwFlZWycVdwwIOufDxku1KUeMR1TSC1dpB1viwXN5bfM9sMJxJ1XjS5Djkypoyp/Nexs3bHsQVjiqi09u81h76SFXvK+oAHbfsmASaRtNvH96+H1K9/TfftJrPW/6fHe08T2je36h4nMVFXvj5wevzf1fAv314a4MMiPc82uqKIXkdC/3dwdbHv3acPtMany82vZ+2Ps+Ney+ZXwt+y6pw6Pp2/NrVxeNdC7DCH7r59cFuljsA378/aPyDgs+BmfGsGbiMs3lOVs0vUkRhNp8jP2+T1+Hfh7fw9dLOV4wkvkZtM6v+OqQHGmOf4E/o22//G0c5QPG9LQAA -->
