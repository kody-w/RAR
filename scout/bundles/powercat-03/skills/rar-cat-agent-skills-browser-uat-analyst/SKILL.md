---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "1c9fbb8d48aaf02473498265789011da312ac8431035b97dbb21a8d021a8f256", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/browser_uat_analyst`. The original RAPP
agent is preserved byte-for-byte in `browser_uat_analyst_agent.py` and in the RCI capsule.

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

Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `browser_uat_analyst_agent.py` and embedded as the fenced Python below (sha256 1c9fbb8d48aaf024…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `browser_uat_analyst_agent.py` first:

```bash
python3 browser_uat_analyst_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 browser_uat_analyst_agent.py   # or on stdin
python3 browser_uat_analyst_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/browser_uat_analyst_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/browser_uat_analyst_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/browser_uat_analyst/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/browser_uat_analyst',
    "version": '3.0.2',
    "display_name": 'Browser UAT Analyst',
    "description": 'Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.',
    "author": 'Al Macey',
    "tags": ['testing', 'uat', 'playwright', 'quality', 'copilot_studio', 'power_platform', 'automation'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'browser-uat-analyst',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '09f0ebd3b94914ed',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.571, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BrowserUatAnalyst(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrowserUatAnalyst'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(BrowserUatAnalyst().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
