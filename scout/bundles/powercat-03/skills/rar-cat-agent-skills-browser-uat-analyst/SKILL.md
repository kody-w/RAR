---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "1c9fbb8d48aaf02473498265789011da312ac8431035b97dbb21a8d021a8f256", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
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
