---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "16e1403a1f0863adf1bb25718efd284fb7ff0d47691a8a8a03966fd450a14530", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/phi_deidentifier`. The original RAPP
agent is preserved byte-for-byte in `phi_deidentifier_agent.py` and in the RCI capsule.

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

PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `phi_deidentifier_agent.py` and embedded as the fenced Python below (sha256 16e1403a1f0863ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `phi_deidentifier_agent.py` first:

```bash
python3 phi_deidentifier_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 phi_deidentifier_agent.py   # or on stdin
python3 phi_deidentifier_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/phi_deidentifier_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/phi_deidentifier_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/phi_deidentifier/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/phi_deidentifier',
    "version": '3.0.2',
    "display_name": 'PHI De-identifier',
    "description": 'Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.',
    "author": 'Rafael Lopez Alcaraz',
    "tags": ['healthcare', 'hls', 'phi', 'privacy', 'redaction', 'hipaa', 'compliance', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'phi-deidentifier',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#phi-deidentifier',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4c6bd1961fad5f45',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PhiDeidentifier(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PhiDeidentifier'
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
    print(PhiDeidentifier().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
