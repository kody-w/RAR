---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "c74fb9856ed7018e68218cddcd1930ac99ccd995855c5106c6feb4cab241d398", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/stoic_negotiator`. The original RAPP
agent is preserved byte-for-byte in `stoic_negotiator_agent.py` and in the RCI capsule.

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

Stoic Negotiator — A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#stoic-negotiator
  Upstream author: Faride Ilanda
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stoic_negotiator_agent.py` and embedded as the fenced Python below (sha256 c74fb9856ed7018e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stoic_negotiator_agent.py` first:

```bash
python3 stoic_negotiator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stoic_negotiator_agent.py   # or on stdin
python3 stoic_negotiator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/stoic_negotiator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/stoic_negotiator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/stoic_negotiator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Stoic Negotiator — A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#stoic-negotiator
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/stoic_negotiator',
    "version": '3.0.2',
    "display_name": 'Stoic Negotiator',
    "description": 'A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.',
    "author": 'Faride Ilanda',
    "tags": ['negotiation', 'decision_making', 'offers', 'salary', 'sales', 'commerce', 'batna', 'zopa'],
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
        "upstream_slug": 'stoic-negotiator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#stoic-negotiator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c1a8d265f7e75943',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.8, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:decision_making', 'word:analyze', 'word:research'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class StoicNegotiator(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StoicNegotiator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(StoicNegotiator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16abOjSJblX9G8+pCRTcRD7BBlZTaAQBJIgJAASRllkeyL2BexZOd/H0d6LyKyKrN7xqw/jsLCHov7vdfvcs51uX57sbs2KuqXzy+iXceev9imdu7ZLx9fPL9x67hs4yIHb9lFWce5G5ep7y1yPyza2J5fLeK89dM0Dv3c9RfNLU7TRRvZ7cItMifO/WZxbIvYXXi+GzfzeC9uZimPV33cRgv/DtSCyZ8c270B4bXf+HbtRou2WER+WgINXgzGdHbafFz4g+92bXz3wTUwFPy307FpFzYwoG2AkX5p1/7H5/PJfw56TvIXURxGnyogKG7HHxfRvC6OXVkWNZAwr6e23VnFonGLMs7DRV/UtyAteqBz5fvlQn83sSm62p1HfHDj9inqofDx3F8Y+q75+c3OzovbT7Vve+Oi6Nqya5tX4GR/sDPg0ubl8y///PgSg+uXz7+9uKndgEcvD9cpb3aCIH18AcEJwYtyBEHLwX3p10FRZ+CR5weLt7sPjZ8GHxf/8R+33q7D5ufPX/LF2+fLy/xP73IQJB942G5a4HLXLm0nnr3yumDT3h4bEIW2q+fVLJoWBD58fc78LqkoF/+Y3314KnkN/fbDl5cCmPDww5eXnxdFDfTV3Xz9OkspP/z8Crzo1x9+/i6n6ZzEd9tZGLD69evb/ZtYMPD70DhYfD1qAv+mqwYpVfpA+A/rmz9P09/Evbnk63Pwh6L8uPhzyfN6/gHsfaa9A+T+uVjgAzDz5TUp4vzDm466uPu5DXL4w89/JdaNfPeWxk37fyX3l6fgCKQL8NabS0AmzSH45wJ6W9s3mX+ttgQJ8/+yEjD8Xd03R/2V7Edk/0X0s67fY/mn4v5sAvSPxS9/ubb/asLHRfDlZeWnoFpr20n9z4vfHinyy0/e94c//fN3IPq/FXN8FO0s4Wtm53HgN+3Xr7/89Kzln/75y09dCbLYt7OvXZ3+mcw/8+tDzx88+Dbqwx/nAv1GfsuLPl98q6HFb0X5v+rfXxcmQCzv+/Pm8+LHSpw/0GJexLvSpwt+qMYG2PqDH39++R2ATQ5W07mP1wA//va3xT5266IpgnZxdAFGLUCA2zjzZ+NPUQygsXmgRu0DvzYxcOzbOJD/c4Rni4tg8ev/du320wOPPz34oIGbGce+5t+A7NfXxQkIKuo4jAFOL3RW077kjymzknKmgPoOgMkZW/8TqN9P8wWA5sWv/yrq62PWazn++oDZ+AlsOr+dQa3pUv91Nt+K/PzNWNfOv/FBWrhAexCnM5sApUUKQL+dl/okMi8GsAGUjA/ZwB2fZ2G//vqrYzfRl/yJwtjiyZMNDAZ8M2fx6RNYRgCIMWq/5L4bFYuffvv9p8V/Lv6rWQ/hsw4NEMCbs4GF0lFVFqB4uuxBcnPkADI8nP3b72/OBGJyv16A0MRB7D8ng+QDjPru2eOG/YQS5MLxgUeBN7OZ8GbyitvXxTZYfLMXKH1yob2ICsCtnl/6+czR44Pav+TfPJkX7aIBGdYE48dF1/gPrb86tf0wMQNVbLe/Lva8BqimSGdGr9+oB0wu8hi4/1vcn8+BkPqnZsG9i3hdKHO6LQCr22VU2286AvsZF0Ax79OBcBuQev8ln2nUn131yP2ne8Ag4Bn3LaSf5pjPLQoodK951/0YY8+EeHoQY/0lb97yGvQUwCsuwHmgNOxib0b7v7+lVBMVXeo9/AcsnSW9RcF7i8ojB5990Hc2X3zp0CWCL/5/Z/U/31nN/mbXa11YsydhtRCUk3555oFbACtAvjzb3tlaUAzPmv/eBb0j3Tvgf8nTGCR1Pf79OfKRPW9jniDa1cC/Oqs/5IPUBXkwy31U1lwpdT3XpP0lf2cWYPviAaMgcACG5vCAqLwrnN++WxoBrJnvv3cZj0ys5wjNtb0oOycFeRD4vjcHGlg1O+M9vUCZ+TNS9FE8R/6HVS2AdJDNQP5izjYQIcA+D9cpBVgm8H1QF9n34fHcFQIrvM4F1kZ+7b8urDkhQZI3AFVAGOcxwAs/PUQtMh/4GJj4zcNNZJdPY0DY3w203zPqxwC8vftekQ9TZuuBUNuzW+DKfmYEzx+egf1m5luogK3ZjCGPSX+M9ttSFz8y4N+/5A8Tv5EQgKZ0bh5+8M0C5G/2TMMZWRuAjpn/lj/+W2a+Pqn+2Ut8s+XzgmdPC/YJww9OXHzI3tn2QczGH4PyeRG1bdl8huFvw15DUNOd8xoX8L8R7N8etPjpOy3+QeRz9Z8Xf9jh/WHEWyZ+XiCvy9fl/GoXuw/ceft8XnT5N1D78MP1W6AegfC9j6D2Z7QGeTInZRP53qP30f3vkQTWFBmo6NnBI2D4b0T4PgSwYVj74Tz4SYzNzKc9oPCHbODrL/m3aL+VAiCaPJyRqyl+KNFHRwBi9wYa74QFXuUt0O3NDWLoz/uwdF5u4798zrs0/fiS25n/p/uvmYZABgJ3zfs0UAygw2pj/3E3Z+XXp6rH7R/2z+rjwk7nkgGV88iYd3yeER2gw5zisy3tWM7Kn/uuuVP71sb9u9hH/QHg8IrPcxl+XMwt98fFt+754+J9P/PYbeYd2Cr+Mnfu81rAUPDn29hve37Hf/nnn5jx1sj/uxFz+VUdALUZzGYazhuwyQOxaJ8BnxuJ9/d/skAguvarDhCzNxv3fbXfjSiemn9/GN0+d7y/vbxDwVso3npQMBzU3KdmpmYY5DNQCO6fmQTe/ffd6dsEAFagWwIzXAoPHIYmSN+jlgjtkzSK0K7nuR7CYEvbZRjX9RiGoAnCJZAl6ZKB7+Cu7aA44mEMDeQ9s+Lr3HDEsxEz/oG1fwI57H9/DR55b9Y/rZ1d860Znlf5tojfXhwSByM3eLNlnx8ehhAbxnbJUG6gfEkPEYyuroLEk5hxJKjk2kBnr7XVKrHRE5KLI180V/a218UwYfe9MqwNq9SEo78XmPEMu/sDywomUlCVUVfOrUPlNZ+VpAcHGoasJGh7h+G2hkNdJIOcoLfZ8oKOyFGlTsVwkezbEeIxj99k7T5pTr7tCF6JJYifXfcrT8qK4oaDeSp1V/cEbvk3QYPD0Y93qomqVioW5yPXqmlnCoOmC6iI3roLsbnE19U1aS8O4Vl4c4luSrVOKbOopctgRteUwwQ/gsRpJ+3VVaLHLb3G+f1V3EvoNilI+n5i8JsV5F0XhOjoS7SNOjFKNxhO8EtLbJ1JIFRfY0kFc9DRUzQtKa8ykdvtJZquxtGy0Chub/XpeO/vcm5UZdxO0MXJ132Mj77meVzrS9jV2zX7m8asR1m2bzdjOJUGTJcM3wxXWDTKArmulrvBZiaVPDOnmt8v2TJR9kNLyAioA3Vl+oNNBS6u7PFpLfE5ffAqLxdJ15eyHOut4+meToiGVsltUG5QrNt25xLtNoMa8d6ju/yaZHhM57gjHXH3VMQrn0BX8GgUsOyKFTQY+Mi4pGzzaIvyUUJLOC0vq9XkFYd+wtXhFNAcKt8NMYOz8cLfzhuI8U3HdeWYCrfb5ba5ycsC+OtwiDKxh4m+LRFLp+K4E04NR4nTLTMFrg704/W2r0HEJVlhmit3cfZXKa6Iq3r31Im2g3jsT5C9v9Q6VwRBJeARXE0cPTG80AUHKd1I7QqergwnsMfVkZJtSK7Q7J5QZ5jOTjcruo2DHEeHwkhvy/AKHdRjqQhEyBgRie02N7NO8Wx93TnxpTVTLrQ3o78uNb7enfoCWS+PSwiE53YRjEPoSWdrKZWDXVEnls/X/N4295NxLLyxqHaXnShsEhESoExF1frMLw+RKdfx+Q5JkLHujFSuJa1mAp3ihbqp65ukK1Fq6UeiLRysQE3h2IcnwrCO50vb1hljySbXblO8NC/x7nizVuEWKQY+kmtOE3lYmiSHJPy1tj439HjqBkMe8rsuEna5pSUO1047CqJ9DUtJ736u6VNdM4QPr6jbtEVGUuKi02ixZ0LtZCzm+mN1jMw+q1cwVNSHmkf3kZcoW4HkBVCZd3G4Ad4V06vQKPgonazVFOrrm8VP7OGK8WdkVXFH6MDy16phJe1gMX0s0mnJsua4Og3HneHd5Qk792JNdsyKqN3ixl0ky7ApSYUFdqLbNI64i6xbp4TKxkIjDtbaNHBta8opA6ACbvQlP2Kl2BxMYT1BJ2fFO5TcBNBFW5tTElC9F5aaDE/ddgwJpCzTfXmXDyOn3i6NeB02F2rFbA8NLzUyStssWov5rs9u/JlSqqaoorLdlNxxqwiWPKy6lj3eVDuRLTMcURNQIOPiZIMEKhRecIfNZX8J2x1GsmHGe3fjGDIbiqs2SsXnVyhzwwymwmUsyL0jYsq20hvgxXQNnTldC4dIAQl8NnQrbiZhZFQMLw/peZIucStk8Vnv6NLwLnCPOaeg6R3XR9xVwEIc0zchhR2Vu0HuHEgY6O3JGM/EmC5FHOXguMhwcdJYNMAb1JHWoHADJiuavpfSW0rv1wV9zegeup5NdWnmqWIY2vHaXupNSK9FNGk0uzs4BD9cvaNvqeiROoW1gWTF1u4qxGzdJSqZ58Nkkh1yVfdhT1cc1uADhux2TWavJGLbY5IKHe5JXxT9UsdXIpGKt2aFXY9QVDbbgPV3+tViY9zEtz6+blWN1dedsEpNV0rQZgrzvbCcXGg5dKKCqxuS5A4TvFoTtywA6KORnc8S0M5UcSt19U6xk41sufcdpMEkvYfvCWGU+UU6INeuNCYEbco6JLxzjzvrHr9dzPgqHhSE5TDAXMi1V7HluA8NFdStvBkEwkD4nRZD6XTUGUhU/FHduDV+CvtIInWywnfCrZacyRSTq16ub6y9n/AGg+5I4KVs67bm5robG6resztM0qAYUlYTvtrLNKcdvOWhVUesPxDQlqYqKFJl7X4Pm0txtJozI5TxZlJYK3J0b50Td009q3qEUBepcy+2bu7uF3dTr3hv22XxGo+to1/edk1zSw4pdBlZ1dqddqfzJUs3PkGmg3Xoff/OWGnWTUEXrHeRiCsdfCM1brhcre25OXfrIgEYqUMCYiyH1F1aUozej+b2PGDNBiY4M58G2Q3VW8ddlhxpGiI7ONeU5v3w0lS5y6XXyVBETF/FO3RYBmMKr6czPNDMJScJNYAhR9Xu7oqSQ7us2X2wM+pmuB90sT6ekb6WZIrYtrvNSZbOayKYsNLbUnILG7F41Tu+R8QjuTzx7J1LluowKlBbHPUqkIdEjOSVkGJnZ7uFVmfERd04tQyrdpY0lSkBW5pHU4p2POhGhsPN38sNIVxdveGti7+rU9IWKM9lLUgKQ5rYVWWuayLhyVZSoRYrcdr1SGm6FmwlyLEBSgmR3waXncFksmFn7WatasaWOBKbvl8LqwQ0l2MXqGKLb8WtUpwEPFfIQbv1hkrHppkMa4aHza0QBuX6bAWDbVPsPu2ObiPRfQUy0Iy74bDqnEKp1EQozy5LHR1zO3V3EdppaLI9rpXDOsvOuHuvQB4bO43vXVZMGjTd+tUgEccTVzYCF+T71rnkjjKKa4RCmCzhAuG0EVjvcFxylzxY1nRLippecSTrX6ShGfCsqGrvLDXVwd4b9vKg7GL6PgGSuLOrA5xN0CY83sUyL9ZBqwSFkUWaEq3VkyxES0kpEGFMN6s2u+MhnpCs7WLevtJDOALQcOHRLdWPpctXlMwcDqSf7BTJzdlsP5UcG1uj7CX8/tKvoZtiym7nCDUEsHC/zva3SOUuuHEL146pbBVS2GpsQhvW5mIPU7iXszgLXPu637kwdbK2gI6XumBWesDS1TZZGx4Bt6Q+8vsjkpgcb0M9traXRYBQfHSstpUQxSK/cavOy2XetaC8sGFCrjwhgm73w3g1EaM6kRCSiCZyul3yEFETfofHYLirb5w4OMmld0VZuXVtVXa45W6jjNQxrqghsFkZsXXMUke6kLfZvdlvdN0TT9JGsrpevqFJZR8Mva/O0WoreuMB07oo0lke8c82rwR7xDLkwEzHqCPaOC64pbwTSuKsQOdRhWOlrE13ZQ0TSjDGplQFnTlT7ibWRrPi+IIfd5i7PBO+j12T27rqKOrCDtO5vgj2Fs0TI07uUEfy13uCQ8lR0PvCDFfYzW43SARfkoZbX+oo09fwAR2uhCbnB2zouwGFikrTsHFzrNY3804GNEYl/WFKmIn0VqDl6NODhNoWINPLcO8cE5Bg3msbPdl4sMHXZhUfNzGPo0pJH6WGCvA6ORi363qZ+rCGc3sarU1PWsNcWBX7LYErSUgcMwjPqLOw53Qecs3bSS1WgShbLZstV7q+M7IiC2FZ29Pxclkc8ljY2mnf0528lezdaRUXrdPdkaVMXSvu5EUXQgtvIyc4dNitztcL1eV4TZ5WjFJtvBva4NgGixuPO5nIVVpRpxvS3xqEZS9ePwSSfr+LFOETSHvWChFpt7c05Ab8wLrVLr26As+EimQeZeXCG9ext1RjbZUMm9Waxw2weTD9Zbe62x4CJYG+mdJDqhQEnNqddasTuQtiqbdjysaPRaQQI3N1OJ0pi9RhIv06hbh5v3dWaQ3kjamtq4aSS+qE+iNXM8WdYNBrfbKXe2oz1EmnhQaQcRt3nRLcqwOnbwh1EnBNwg/hQSn4m3dGdiJEdVGBidpwgqpul1extbIKbBM4O6Jg75e16k5qB9mCsBFhtDPyIpQLJKPHplYiUiSTpUTFK+JA0PuwWwZ0cIGQIKAvLs5cLFKrkcbZQxhSpFEIrQu/ZTeejrKUQ7vcdMYYRyfdHS9xcDl2Kz0pqRWWWj6liGd0a9vG0qUEp+UVZB3q0C6OVLwiltLm2B62tBr0SpwUe1UI7Vt6OMiuku/4Q98HB/94oYqRv3DjUcPvercyWsvJrk2/P9uoucudDAtpaiXeyFY8xwfmfh+zxDcuVJ8OXu8Y2cWE2SrF96CzOeD9BNHlQVztTW0IDufAM01OAZztY6Pm+l7JGOOm27a015503z6cGB4TEIpSIYKBVPVwnizPcxV1EnlkQ5EKN7Yb8pj6VUAOEJaYrOWt2SnMjDDuJq6HoJXreaiTT6vT9jA5Noys940H70UrlzKkptAzgXtrz99XIhYRIX1FsX2CBm1fabQxsoczfpw8Smwm8USfTTlaxaukjaVpg7jxLgtH7TRhhh+6eskdBOaCRL4bQbJKyto5w0fcaZU0xGkiuvaEoHLW0Q5P58lAVxzaV8F6inabNt9v8xWa2oPlCtS5L1KKLs4TySjZtGcnj8N3zfUirUM/TQwfVW5mL2iutGe9rcTlt2XvyurqrnTVbgVNl2Mlp+tzDCeDSYulzi1hGt2cxelKeyOwKKZGr8Bt2b+uubtC7Mek3tPGCqv2SST6jhEAKLunUcdStlKn9aQ3qHzoo6mL0T3NBp668bq12tThPjhhAikgATfCS0a8B1XDlAlE4M4YWp5t7xnLBqzN1ee2KaklNGijV1pXLqpy9jZsRBRhawRCdS0TD6woYsdJpzwBGpYJG4dBD8EHHh+qra8NoAcQ1NPJzJxWvNyozKyjlcbzS2bpj6iWcK1mt6g9+kgCPOpDNJkRe0/drbQT5KKtQRds63u9ma0ycg/pRGWQetVjbuTx57SLKYy7kCiG7wP/fLt6ncmcTHosnHRpHHOwm2bSkyAs8XWm5tUInYLzOa0R3buEF8VE6s0249I9TJ6afcachYtryaTaGynHrZVhI/iE5UA3Xgr2V746ita+lr0t40pkC0lWOHAGlaoTmZCWEUw1fZDuF341lElUnQH0LhOyBN18FOgGLl9Og05E/EAs4ThZGZO0UZ171IcUJJmtH5OHPY3fEgJYjiZZCRtrhMzpDCWH4c6gfAkYhmplfMjOEGLCInY7eBTJOYAfiUGK8CLa6HvOu3sHnVmm5+XFR2IV4yNYvFGpBJ8CpwyZeGe3Y0Uv04N3d3QG84M119huNNYMIuWnTYIf+6koMYbGLmN4z+iEkNFJtJhTCY+74WSFm3pJ72sdFsDmJEa4xFxdk6mzhtDV1HDn+HaZLg+0avaBCyRDU8so9iDvVuZ6dW3c0qEVqm2y+73Ykv4SiYeA6fvhYNBtYoYh5BEuywjIFWrK+FLfjaba9ScFv7rRMThFIXlG+zhB4CtBXEmOIPbYaA4IfPeCuthcTZKg+mPtbG2Y7MyIwfEivotw2aBVQ7KJlGv8+nYii802lIhesVf7XTYycjFQPjzWeBoSNmm0ubdSSG5Mwf7IFnp0iaXI7i6Ja49zsjWVO0HH9JW6MrAcVBBtoCBlAhkiglsxaBO/933LWacookr6MVebDZuMIovcqi46UcYVZgT6cm3PlnuKuNGqvQuzxurtst0RgChTKFdF7LrNlHLV7PaQGtrLlnD2EzLo2pFMwrVmS6EhFv42Yq9KEmVsXfDWUUcPJo0FFM3dFL7tA2XVuCiuWt5FrFR+aiePObebGt7sbe+qdAjBassLmd3cPaPnYoRvKna8092WImFXOvf2nal9GyLRwfdOVKgt74dL5Ot38Tz25gQ5gcn022LbsVw3+lFA8xEg1ksP+7reUsHOSaQq6cqVja3PIgxFuHMPxuQoMTSkX1G0AziS3d0NFuIaEXTnrncsqjm72OVOoxxj+wl2i5lSDTYK329l3s+xHMV1tzzka9vpzqrPw4fNRaVOHberb4XAmjxGo7kr1aEaq3zpFDteUeAj5a6TjCoyrDaLra5t3COc0oO1PBmhY25OPSRLdCQc0ApT7wAPaVLgfJgWmzW0QQksYGLY6pdrhaSJdCCoI25CzlDct/7R8Ki7QjIrhTjvI8BNoP07VrGTbS4is/FlmgY8l28QBqFXeW8bq3QSSeuu0JzX7pubxUP0Eu52WbW5O9oBr005FO/YilB1it7hJzHixELpWfbl48t8JvN2svKXP+OYvw3/H/vi/fn9+fux6ePkw7e9zw9dn//ahH9+fKndGBjwPD1o0i58+1r+X88OPv3ruds8fHz+9GE+vh3a9xOl1g7nH/m9/HA2/jhveZ7df83s+TwAPCmCYD5cAmLs1K7H54U/P5gPD/z5bOnji2O3+fwTTYBt9mzt2/EdMBJ7Xb6iL7//HxtS21PXKQAA -->
