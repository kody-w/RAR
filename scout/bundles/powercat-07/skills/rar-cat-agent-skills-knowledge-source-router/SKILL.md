---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "28de060ce9e856846c1ed608ec2cee0367fb8584d3b8b16ad583db18d97fe305", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "4.0.2", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "sharepoint", "metadata", "grounding"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/knowledge_source_router`. The original RAPP
agent is preserved byte-for-byte in `knowledge_source_router_agent.py` and in the RCI capsule.

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

Knowledge Source Router — Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_source_router_agent.py` and embedded as the fenced Python below (sha256 28de060ce9e85684…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_source_router_agent.py` first:

```bash
python3 knowledge_source_router_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_source_router_agent.py   # or on stdin
python3 knowledge_source_router_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/knowledge_source_router_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/knowledge_source_router_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/knowledge_source_router/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Knowledge Source Router — Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_source_router',
    "version": '4.0.2',
    "display_name": 'Knowledge Source Router',
    "description": 'Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.',
    "author": 'Adi Leibowitz',
    "tags": ['knowledge', 'routing', 'sharepoint', 'metadata', 'grounding'],
    "category": 'integrations',
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
        "upstream_slug": 'knowledge-source-router',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-source-router',
        "upstream_version": '2.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '222db16ad4565ae2',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class KnowledgeSourceRouter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeSourceRouter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(KnowledgeSourceRouter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjVtLmX2Fuf3D5VdVF7FAdHTEIoQUhsQmQ5Oqw2fdF7ODxf5+DdO8tu8fufidiPowqokqIPJl5nsx8Mg/Ury9W24RF9fL1hXUjSPQiu+ijZnr5/OJ6tVNFZRMVObirFm3jQU7R5k01fqlLz4n8yIG00Ko8uYjyBrq3Xj0L11ATVkUbhBD3lIYyr7Fcq7EgP6rq5jO47+VQ7VmVE0JFno7zD0B1VqYesFF7DVT4UGY1ThjlAeQWTpt5eVO/Aqe8wZrF6pevP/3z80sEvr98/fXFSa0a/PRyyIs+9dzA04q2cryHzxVYlVp5AG6XI9hqDq5Lr/KLKgM/uZ4PvV19qr3U/wz9138lvVUF9Y9fv+XQ2+fby/xHbfOHp01h1Y3nQo5VWnaURs34CrFpb401VHlNWwEELKhuKuD863Pld01FCf1jvvfpaeQ18JpP314K4II1Y/ft5UeoqIC9qp2/v85ayk8/vqZF71Wffvyup27t2HOaWRnw+vXnt+s3tUDwu2jkQz9rMs+92apA5EoPKP/d/ubP0/U3dW+Q/PwU/lSUn6E/1zzv5x/A32ey2EDvn6sFGICVL68xSJVPbzaqovNyK3e8Tz/+lVon9Jwkjermv6X3p6fi0LNcgNYbJD9+foTvn9DibW8fOv/abAkS5v9mJ0D83dwHUH+l+xHZf1GdRrlXf8TyT9X92YLFP6Cf/nJv/27BZ8j/9rL20qgDeWen3lfo10eK/PSD+/3HH/75G1D9H9U8S23W8HNm5ZEPSODnn3/6oX78/MM/f/qhLUEWe1b2c1ulf6bzz3B92PkDgm9Sn/64FtjX8wRUfQ591BD0a1H+j+q3V8iw0sj9/nv9Ffp9Jc6fBTRv4t3oE4LfVWMNfP0djj++/AYoJwe7aZ3HbcAff/sbdIycqqgLv4E0QI8NBALcRJk3O38OoxqK6gdrVB7AtY4AsG9yIP/nCM8eA7r75X86VvPFCgDRfamTKE1rOHlns5+fYP5cPfjsl1foDPQVVRREuZVCKivL3/LHytlWWXm1V3WAn+yx8b6AMv4yf4GiHPrlLzT+/Fj8Wo6/QFbuzpKzwyq3nymublPvdd6MObP203XHyiFv8Jy5JaSFA5zwI0DKn8Em6yLtAEXOG39sA3IjQCJNAdrArBuA83VW9ssvv9hWHX7Ln5yMQc9eU8NA4MMd6MsXsBs/jYKw+ZZ7TlhAP/z62w/Q/4L+3aqH8tmGDJrCG/TAQ0GTThAopWcvgeY4Ap54QP/rb2+YAjW5V0EgUKC5ec/FIBUTz30HWNuxX1CChGwPAAtAzcqiauYuFTWv0N6HPvwFRudbcysIi7qBXK/0ctfLnbnbWWA7H0jmRQPVIN9qf/wMtbX3sPqLXVkPFzNQ01bzC3TkZNB4ihT8Nbv5bJlWXuQRgP8j/M/fgZLqhxpavat4hU5z8kGlVVllWFlvNnzrGRfQcN6XA+UWlHv9t3xurd4M1aMSnvAAIYCM8xbSL3PM57YNyt6t320/ZKy5PZ4fbbL6ltdvWQ4mBYCKA1gfGA3ayJ25/+9vKVWHRZu6D/yAp7Omtyi4b1F55OBHg4eetAM9Wzz0rUWXCA79/zCkzG6y263Kb9kzv4b401m9PuFziryZYX5OXGBsgEAOPUvl+yjxThfvrPktTyOQC9X496fkA/Q3mScTtRXASGXVh34QcQDHrPeRkHOCVdWcyta3/J2eP4MYP7gIxARUL8juOaneDc533z0NQYnO199b9SOAlTvXMkg6qGztFADse55rW04ygzoX1Vs4QHZ6M0p9GAEQf78ryHtgDvQDbIGr4J8+f0B3KpoHoH5VZN/Fo3m0Al64rQO8Db3Ke4VMUBdzbtSgGMF8NMsAFH54qJqjGRbAxQ+E69Aqn84UVfLuoPWWrunvA/B273siP1yZvX9PkW95P/Op6w3PwH64+RYq4Gs2l95j0R+j/bZV6Pdt5O/f8oeLHxQOKjqdO/DvsIFAlmf1g0JnQqoBqWTeW/6ARHgUw+uzX75VxrsvXyGOPUPsk70ejQX6lL23rEd30/8YlK9Q2DRl/RWGP8Reg6gJW/s1KuD/o0v97aOpfHm68eXZVP6g+QnCV+gPZ4w/SLwl5FcIfV2+LudbYuR4c8a9fb5Cbf5BCZ9+9/0tXo94eO5nQF8z14F0mXOzDj33MUeo3veAAm8KULkzc4K6tsePNvIuAnpJUHnBLPxsK/XcjXrACA/dAPJv+UfQ3yoC0HQezD2wLn5XqY9+CkL4hOaD7sGtvAG23XnYCrz5ZJPO2629l695m6afX3Ir8/7NiWamcpCOALT5/AMqA8wsTeQ9rj7ml/nij6e4R82AYneLr3PpfIbmWfMz9DE2fobeB/nHYStvwRnpp3lknU0CUfDPh+zHEdH2XsBZrBnL2eHnuWeelN4m2L92wirLB63+kf+aYjb9L9qAusq7t6DvuLND33f43XDxtPbbw9Hmebz79eW9ZN9Qehu4gDiojS/13Hlg5HUJDILrZ6jBvf/2KPa2DnALmAnAQpR2vSW5dDzGowmSxkkH8VxySXsO6njeEiMp36YJGncxm7YR0nIJGnNthHYZyvewJQH0vemf22o0+2I7Sx8hGYQGHMvYKIrN6pY+xgBdFulhqOfSy+XS/r40AZXwtsHnhmb0PqbCGYi3ff76YpM4kNzh9Z59fjh4YVjURbSH8MLEpH/tY2bfhCDtlktKYdxmc3QF+aKfY08BVccTIhvUmq4EgdS3Z1G6Szm6l7OtX0q+d7n0WiqpiVSeJFm9i2xud1i19AmCpMbRjzAYJgWM4gk/34TnleBypxPjhDU/YqamFRu/cFFVjNTslomycIo6GhvIbjwt166QFUUC4L2sKPl0JHBT4nkZzkN5EFpEkrSULwx925zWvnaKvUg4is2ejnkjKiPxuK7OnnSAt2dd0W/pyUKz0Uj5vW16ATGsl+Kwde7n9Z5G9/mwbRcZv5I2pHGu+zau7kxuC1wNd6u1L2wyh4INx9/JiBselE3axFGX1kMhYe3Zni4TxiC2fDMKq0SvBZ4iZdJe+cyLaKNyznCRHlI8G5uKoUafXa5OWEpLp3qX0Wo9IqZCrI/GptZvlqpld0OZmDFXTHiD1UqFbKqDt1oIwE4Wwzo5xBtWuw7nY+XIWN2i0npzHUwmrx1La24TG5wXkoxI0wjvhOxG04tYF6ahhGX00JBuKacL5LzdUrlO83SSjkUXG6q4CxV9hW1NEKhjkJrpqI9VJHukvcIJXFkIdXyHewofF852b61qq76dLHzCCPOmWObkrMJuSfM7OJEHTgidcZufr0YkSGJFwh6Iqth2eqhw6LniopM8uAuePS8wpUULQth4d7ZQxzNR7+7qDanI5nSojqv6VjjlUZXTdoNaw6Y9KZR0Odxzf3HrBJs2dY6itHgzHhCOvrEXfs0sFHnrU5N7Y9ZlYuQIDOfxwqY62MbHvAojHE/FU0nhzATDtzPMZaiRIdLmuJmEA5IkSVVZYRI6hJ40tDGKHV8obKGXnl0BulLRk7VWw51QKJYVLFk2k6ZCM4vrHWXXC55n9TN7N/aCayvBSaDXDjssz7ZwSjj5fhpUIdA8F6bSlPC6bhpgBi4n2r9XLuHC6zhui6mfttya4yPuzucnVopae7HZXMNDnZSmJxD55aCEddoT6EVIAsS9xOrK7EHv2qQ3vtiIvOnUlzgR2GF1LTcHPMA0caPcWWvc7Oo9ZeqdZYyxtyeEkA2Ek5KJwdnWnc7Clhh7wEiJ4QiPSTfZVS2Ng34fAnZ7afDLndDQ3bW52f2hGJqtZbJEq23ja7CrKNER4pPvxQRICDrani0+9dvllEljhYnsDRkr/3SVBh3VurE9jkFJ2HdjhXb3na4eiXt9E8ru7gyoTO5XN15usLxGrraBUlyfted7mOriShXUe7xqtgTioUdnS1KsVO4Ug3dJ77rOzB3ZxxZsOjYJUGw4hcA0hpyuBcd1gjmouDgNZqxsVrUsn0+baVXhyGolCURJ55LJSdTSPNgUqYibKfL6gdjyiL419tVxsLrJXRwcwaAHZB8PYpHqVSchmbmmd1TTWgeu2jUGV43y1UvFGClzA3emyEjbHvMZJz96gse1Z8Mm5OkEWywCAmzwSt7fZNq7NXySHMTO7cS6OF4JDnOOJs7cMmfYkGBzbJqnp15fre/Vtc/z3Cm3A8PF6khkt9WwRgWEX5eaduVJQ0FWV7coWmu3apJbec9dilgPYliiDFrTLbXh9brAdH2KgvSKJcLuYDdKbBzbvbK902NAGjHCLpDAdvZtNaV1Xa0J40BvRMej3PiyVK+qujVFT9GqI1absmzmTL40qejsxSHhavytLaojMvnLTSWjtBfieZvE657aaz4raORip5n1QljEW9Y+mNb67Gv38NQjZn22Y9W7FMxdwdHsmqjbII5JkPxlUGpZN1YNKR+3BXW4hhHqHDehb+cCUpz0XjFxRaXOglXturFcK7dtomlqRfTC9ihTHablxEWI2EAjMkYgdbO5pCsHFRNW4Ky8a309jI/9qj2PRyuj8OuCVx1ky4KjYE+WKbbl6rUKh/pSzclS4S67zbqtLG5HregrUriOgCYHM8ece5RFZ47L3Jw7YsXqLq4FUR8N1NSGQjWO/l4Lj8j2uHdOqeiotoGchSHyOkRK87XdXUQlY7aVHi8qlXbYuy53/Slm9VwIt36o9Y1j6Ke0uzenUSlXUnCa4nwxTgtiezStrb7EUZfS+ZK9N6m0NnvQA0KTmtZjNK0N23GXCn6/eD5OX2KMuqkxjJcn3w/FA5fI7b2IkigI+qMVStKE6CSzS21O1Yx8WB0utFlaW7RUlkWhEPrCCvx7JoyGVnAetkKQ3fLk1Jga3WgGuaBBkFuJX56KJCPtk7ebLLRIsCJYiuKpIBfqIMH6XST2+n03pGMcC4PSy9lqfRxWRjDJ4XlAFKemxJNI2SxmVplwMk66Iy2NeL9E1mjHcodWp25UmQqnqnFz0Jr2F1FFSEO0I2pb3gdsNd2w3FPZiWA2RxUZBSvbctrutqmKCY9XxHDO41EZFXEP42xXqofjoei448Y74AYJqL8mb7VAM1VXA9IX7Hu+2hlltTXJMGkVpzmCg5V/MmXAOv3eCjRh2+GEjyRruL5v1Dzz14OnhWDWcI/iqowwMjR3zF0ik1uGqWWIeE25Di5iQcQRK/WCucKRtjDQBbLe4Qg7HWhADfWg5tg1athrag2HvqWFa6BpaepcKoRxF5iFd1iwahDrkGOblLxTKkGMUq7x++xy4oqt5AZ2pC0bQWCC2jha8fa2cs8HUJiKSuAVqw/BsDXUbSKFah9yKpKXdsUHhwEkd5houNqpkqYsmPaehOuh5lOJVC9Ks5OaEUHCaBI25IA7m1si2Q4HWw5LTVHplold9w5BbDVB26LU0lPkoLnVCYtdPMCk1n7Dhecb2fAkkOXsntszUaaKeXEzBMaXSMCRUSGH8YI44kl8aKL17SjtzNv5XB632vaqi45+7ns/Q9Zdv67y0Brux1Oyvig8o15uaWNd2HWVLc2enJL7gPBW2avYqVWp0vG1OlaIcrz126Uib9J9IzQT33uxRO5lPtLN23qLXHfZYRfqR2KzP1XskVzyFS0noBuCEfF0QfyKd6nDhGb1DUa4RijW7HBIVZNp2lUFaNGVz6yJoaJvBMdyL03ibXlLrhecU8+uYJRn7bBMgqIke4RVB29b5kw3CSIa92O6v7sFnF12XYgwR8tpj1y4rSu+RdaRxCnens92VRDteaLH95suEtdNORncTbinRIVOuutOl87cRMuK4p2sOBkXbBWtl6OmY9yZWVZCs6uaPIFXLWWES90Wy2yBTvIlNofCiunFVVvfjON4pgG04IB3OvhwRfDRiiPNKKo9a5F2NxuJw5Z1D8GOLAhiU0j56VLeLgd7t3Hg0rBJ9uDTQSfaQcOiabHcbtQGL28i1uBbCgRY0UoGu8iu7VOJ2bYjfYFvmbu6s1jtm62Mw9NayDp371gIyHfAGSWx6BEfK2g2UljJxOsjRTR8SUwNZSwlDI59Ht+tNlIk+BEcFqD2eY7Fl0NGeFR8PZy4a9/5MXs9+cKgE5PmrPcRvaW4FTk0ERUgdw7WTtitJJBePUbeLtZcVpDD2sZMzvL2VNpKIK76VHbyCSbP0ZialXTAKQGTppWy0ytCCWAbMP1eSGMMX25W8Lkh/a2OJlZUyb2AcdPoLabcv0VmeiB6tAkO62lFrwX+LJU2CuspC0fTNqHJ5W2L5FPBOBWnrYocqxiVQI+souyOUuimjEQTt3G9a5Nsh6zH+8RcUI9oxUtdFp4cTfUh4fYb3CdPGMJglOGdt+v64vbhkOf2xShiKlToXLwiF666BMK1ihJZdwlKTNENfFwsrOiqMX7UlLuBsGLmJtWpzLgwEzarY5hsjvUgsif1xtKe37ryorImHGmyfTaVXoaxJpfiK7c9HCkZbXx5xMEx202nlI182UKxXdxO7QCOfcdxinWcg+tKzuFEpM+bsfO1TVtrJ5QPEVIKeZGiz0uOMHbHiDTCPbc6an3XKh0vqnwkTN6N7nRB653tcbH0W2QVYIFa8DRjbembtOCnk9mKuluQK4fkgkpeiodukJBjC6f8wpdz2lvtd0y/V6Krtxcajrx35+2BwxjW3GG4q1WroMQlwNlFLVNNeLjfzwSdt/LuAucpf1FJf2Aar5BMyqJ4pSG2k8OA/nHutMs4WYqR+YKKDHyoh51YIliIDeKeWiNeZxHidbIZJdsUCo7DHsNeSQlv0ORGjgt2YGR5V5wRmKzKThj9yepAnSxNYw0G0qV9gpGTbO0MOlcNO5nO+d5dVk7QI1K12F7JVsI3Xjf0e7q/s9Ee0daT2lFqoCpycvWFOkftwDyWKb4ez4fayj10fUKJykVDo+PZ5YGSrtV6KBaZa9Em0ZlLpsmvnS/ds15Wox6m4F14v2CSb9e7enXlF0Xa0FrCNIcV7dP4lrHPVbO77C4UjMudxAuL7rAo86bOkhaTNMEhbMtXzufAulJmRRGjkzug/DZIvAqQi1m7Ac7eJ9yVlION8Eo8XMUyYKOLvmpCJEt8wBKLfNw4x5IrtY12tA+bw7o+kV170oOVcGGQA0nGqK7LE+HhbH8UTrghLNCK402yROTd/jC2vtZujjLO64uIoHtHDcuCWOaJe2Gq3kDgu5mfUXZP47pPOtEdi1uPMbIFPqEX0sbR5Tqt71GdYNW2lAkDcwyXcZfN3l2w9pRsPD8KdGHPEFmPadhS0RwiFHc7wokkp/V8Y4dzLnrE/GHVSIThH0CXm5qipTox2qMnWbmplLVEipi+7q/W0rAXMDhP65dJMtx0d4srqUTgck+UmMIhd3On41QEDt492Q/3kB6SY6X0khjAm1N11MnF3tsdcLnlUHklYWRe6qkR3uNNgUp6CpvMCFwEvcPdU9bqmi86cK4+WGZJToGP3uT1IuMTGzfSW7BorL6QhRMWhpNQDkfyaBywxPEaaieIfrCSy7JDu/VZvyYLqbC13bGEbXEEB4o9CZOtETIEXkTdDi5r9E4T9FmoZM5MzuR9tw8Esgfn55OYjIwoqrAHMxUcZsQdzF6Ey7ooN+aXgrB4HEWxlNj7yn1Patj+hHmi2zKTJTMOFtdVQOsoc+HhA6x34/KaLsKt7G/Fbe5RoMiRg3P1NmZy2NyFkxOnaDnB9xNzr6yiLuL1elmaJEEeuw0YcS8oQwgiLR2P/rjaUyF7tZIp2V1AuK7oqT0I4BwGzqbkit8EjDhu97t9LeMlz6xWi3g/aHC5IOHlVuEF0HoX0mDbMVEIoXntRSlYYBtyyXTabbojCUwp1xWsnktrBc6SW0ff9d59TU59P1X3BW52sLOwFxSXkejgJzEWyEtZuZY3dbEht+uFPYJzSKchBt+zt16l7T6I3IGetiypWfKCQt3O2GuAEZH2iIr5GONUwoRZfT45C/WWLtpli6Q5vbX6DgVnhJBxUKSx4ASsFWii3t3oabUdcphaRnuL2I7B5O0SL5JPy91ALuleYPbOxhNgdmNwJsceYn9hqy2P9jtVXukn0AazFi6Zdq2ejaVNTfdlss/jm7AeW6WyBEtpDm3BdFHk74VdQ8Z9AZpTJ5V7zF+vbdWOM3hL4LXCm14CWm8st7l6lcd4cA0whbqiuNsyo+gisOCzEyd6pKGvnQFTygIldypeRZ1nTAx82QXJ0i/7jel0nSL4DJ8l6Ei4PBWLi/EULhaRAGaUtX3B0+kmCgwBs9y90XXfP/Ys+/L5ZX6G//Yk/j+9O58fwP4/ew78fGT7/tLt8Qzes9yvD1tf/6Mn//z8UjkR8OP5aLtO2+DtgfC/Ptj+8hcvb+ZV4/Pt8/wqcGjeX0s0VjD/36vvaMyPwMGS+Sn9A4D5tXeUzy8HPh69f34JgEjuzjLAtbc3PcAj/HX5ir789r8BeTFaVIQmAAA= -->
