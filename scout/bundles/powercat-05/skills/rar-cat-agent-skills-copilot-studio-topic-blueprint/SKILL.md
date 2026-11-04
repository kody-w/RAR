---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "e2024d790e12876be0154250bf26a90cee1e959d35146d58c5a4107b9f58ce36", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_topic_blueprint`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_topic_blueprint_agent.py` and in the RCI capsule.

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

Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_topic_blueprint_agent.py` and embedded as the fenced Python below (sha256 e2024d790e12876b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_topic_blueprint_agent.py` first:

```bash
python3 copilot_studio_topic_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_topic_blueprint_agent.py   # or on stdin
python3 copilot_studio_topic_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_topic_blueprint_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_topic_blueprint_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_topic_blueprint/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_topic_blueprint',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Topic Blueprint',
    "description": 'Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.',
    "author": 'Elliot Margot',
    "tags": ['agent', 'blueprint', 'topics', 'design', 'power_platform', 'orchestration', 'adaptive_card'],
    "category": 'creative',
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
        "upstream_slug": 'copilot-studio-topic-blueprint',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '05163d5246a491ef',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'tag:design', 'word:blueprint', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotStudioTopicBlueprint(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTopicBlueprint'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(CopilotStudioTopicBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6abPaSLrmX2FOfyjXxT7aQIs7OmIEAiS0oA2BVK5waV/QviGppv77pOD42NW3uu+9EfNtsIODpMw33/V53iT5/cXu2qioXz6/7NI0LtqFaNdh0b58fPH8xq3jso2LHDzVuzpf2Isi9z+lce4vusZfuDZ4i/O2AA+cLk69T7Vve+NCjN26aIqgXWyLMk6BUK3tvBgMC/28XThp55c1mPd5UftukWV+7vne28N2LP2FnXuLonYjv2lre1bg46IFktxm/luk4M8tL+6p74X+x0Vv17HtpD64ay/ufgok+gvas4Hmvb/Y2rX3cdH4blfH7fiQ/E2pbe17cdss8qJ9TAaP7EUQ1w3QAqy8KFM7fwWO8Ac7K4H8l8+//PrxJQafXz7//uKmdgNuvbxJe1qoz1puvtkH5gIRIRhUjsDJObgu/Too6gzc8vxg8Xb1ofHT4OPiP/7jdgfOb37+/CVfvL2+vMz/1C5ftJEPjLebFrjKtUvbiVNg0OuCTu/22ABPtiBCDbAA+CzOw9fnzO+SinLxj/nZh+cir6HffvjyUgAVHh7+8vIzcDlYr+7mz6+zlPLDz69pcffrDz9/l9N0TuK77SwMaP369e36TSwY+H1oHCy+avJu+7YWCHZc+kD4D/bNr6fqb+LeXPL1OfhDUYJY/6Xk2Z5/AH2faeoAuX8tFvgAzHx5TYo4//C2Rl30fm7nrv/h538lFiSfe0vjpv1vyf3lKTgC6Q+89eaSnz8+wvfrYvlm27vMf73snHP/E0vA8G/LvTvqX8l+RPafRM+13LzH8i/F/dWE5T8Wv/xL2/7dhI+L4MsL46egNOu5aD8vfn+kyC8/ed9v/vTrH0D0fylGK7rafUj4mtl5HICa/fr1l5+ax+2ffv3lp64EWezb2deuTv9K5l/59bHOnzz4NurDn+eC9c/5jEL54r2GFr8X5f+q/3hdGHYae9/vN58XP1bi/FouZiO+Lfp0wQ/V2ABdf/Djzy9/AODJgTWd+3gM8ONvf/sBZzW36NoFCHAbZ/6svB7FzQL8n1Gj9oFfmxg49m0cyP85wrPGRbD47X+7dvvpgb6fmlucpg3kPjHta/MAta8P7P36Dtu/vS50ILao4zDO7XSh0rL8JX/CN1iyrP3Gr3sAU87Y+p9ANX+aPwCiWPz27wV/fch4LcffHmAcP0FP3XIz4DVd6r/Opl0iP38zxLXzhT8AbAfi08IFugTxgwiACkUK0L+d3fAwauHFAFLaon5yAHDV51nYb7/95thN9CV/IjS2eHJeA4EB7+osPn0CRgVpHEbtl9x3o2Lx0+9//LT4P4t/N+shfF5DBkTxFgig4VE7SQtQWB2gPUA+c1QBajwC8fsfb64FYnK/XoCwxUHsPyeDxLz53jc/ayz9CV3jC8cH/gW+zcqibgHsL+L2dcEFi3d9waLzo5kYogKQmueXM93m7gik2sCcd08CGlw0IPuaYPz4oPd51d+c2n6omIEKt9vfFuJWfnAweJvVfAwCk4s8Bu5/z4LnfSCk/qlZbL6JeF1IcyouSru2y6i239YI7GdcAP18m/5oKXL//iWf6dafXfWoi6d7wCDgGfctpJ/mmC/mPgIEtvm29mOMPZOl/iDN+kvevOW8XfuPxgOoMi7CLvZmJvj7W0o1UdGl3sN/QNNZ0lsUvLeoPHLwn/qaB+0v3nl/8aVDYWS1+P+1Z5o9RB8O6u5A6ztmsZN01XxGzi3ydtb42XTOwkH6Pqv0e0/zDbe+wfeXPI1BGtbj358jH/F+G/OExA5oBWBIfcgHyQYiN8t91MKc23U9V5H9Jf/GE7PZD1AE6QCAAxTWnM/fFpyfftM0AugwX3/vGR4BqL3ZdpDvi7JzUhD8wPc9x3ZvQKs5oN9SABSGP9f2PYrd6E9WLYB0kH9APkiQxexTwCUP10kFMBOUclAX2ffh8dzjAS28zgXaRn7tvy4uoCTntGwADoBGbR4DvPDTQ9Qi84GPgYrvHm4iu3wqU9S3bwraABGaOMx/9P/bo+8l9NBkVh7ItD27BZ68z1ns+cMzru9avkUKqJrNRf+Y9Odgv1m6+JHO/v4lf2j4ziEAS9I5P39wDcivOmseGTdDYQPgDOTs0ziQBw/Sf33y9rMxeNfl82JL6wv6iZsPglt8yL6V24Nlz3+OyedF1LZl8xmC3oe9hnEbdc5rXED/iS3/9sZqn56s9ulRdp/eK/ZPCzx98Xnxp83Wn0a8peXnBfIKv8LzIyF2/Tnv3l6fF13+jkkffvj8FrZHWHxQwPkDbEHSzBnaRL73aGtU/3tcgTZFBsBidvcI6Pqdx74NAWQW1n44D37yWjPT4R0w8EM28PyX/D32b3UBeCIPZ3Boih/q9UHoIJLPQL3zDXiUt2Btb+79Qn/ebqWzuY3/8jnv0vTjS25n/n+5zZoZBeQmcN28NQNVAhqpNvYfV6CSZ0gEAx+Xf97Wnh4f7PR1wdqz7t/HfnOn0wHEBIABkK2ddyYfQcHY3oznH2fSKdN4BoVZ8RmGgcjn/mvu2N7buf+87qNyAeR4xee5gB/iwft7Fz2v8tzXPHageQe2jL/MHfxsLBgK/ryPfd+rO/7Lr3+hxltD/y+UiGfwmOHmiQO+9xemACG1X3WAbr1Zje92fV+ueK7xx0O99rnH/f3lG168ReWt6wTDQWF+ambChUCagwXB9TPBwLP/aT/6Nh3AG+iIwHwfhdGVR1Cwj6AkgTs+jKxX6Bp2AhS3Kdj1fcSn1pSHrZEV7q1Jd22vEJhwqAB89jEcyHtm6deZaONZJceFAwSnEBLAPOWgKIbDpA8HGIUTgY37GOp7JAzDzvepN1CGb3Y+7Zqd+N4az/54M/f3FwdfgZHsquHo52sLLQ2buArOeLxSCR4U0XWp6LtEoWJlagMV9ybFnkjVuK0m3u0E+5xG4g6N+XhH0/Ad5awsQ1Iz4HZL60i1k5Ocl9tbN1nG9mykZBWHJ8JplxDb+R5KrvMVikBQGEED0U2xEqmDz594PD0MiYmZA3fTllus3bJZC2dc1KTaEdIdpiJO2L2ddpomxOmR8lmubNOeh+90ilOiRxzbdTdsd3XrxoZUht1kojzO3Qqx3N/E6DiI6nmUvQ2+wu+2NBwinfdhT2ANLUz1Sro33Gm95wRCFW/EYG6Dw4EYHeV2L254bo4Bw47QTXaNchlsz8vhkJ0JF9kGQkKaKq/s2y4eN8F0UiDfqiwzkK9kNQRTbR2PjWqoZTFwzZ23MwHT2o0AbWGQV1J+uMoETd7hHXYAHYtjynUnxRccZ07Hts58d4JvYRZ7x4kab/cLtIPMGJP29dHfdBx20Q8JdMaHRKJ5c9JFx9dau26SyLjw9aVGT4xwEYdYOXq73O6djpAwdyrXEOuW8VBSObE/Twwhknp9jC2zGONaMkIdYhAAdoaNR0NRs5s+3UyMMPSQFF61GyxN9U2wl7aK4tIRruATFstX26nMkd3W2rTTo4yhlipyVguzCMM7wbU0dCQgZT9lfISgK0MJ7Xi97Nl7v46naipcujdrvd9OZBRsGU5m+iuxN1q30mnyTK6aimUgrpHcKk/ddXqKq52QiqpVd56+FZMhFRrEqyoPslAyheLlEC/txh3VTXHNisMqlCtBRaZhNHBTIc552VbQuoDyJbHGnAwuhDY7rBLMOrODjhoMSWgUtPcpgfHvEXtsUtHdimY8nofs4u5PzahXvGUkHB5L0KFw12Ibpzt9ogm91U8Xbevz+/J8CFmNEPv4tm1DjdNMZrPzIsva5zTLofzyEGTuMWjRG6qvVVi/0jjiVBd+pUe2e3bp243OmyRT3TPgAY2eDqJSO+xg7lIDrjx7uO43tnjRSbPeqrq6ScvQsna5GMIksZwIglpSy4BoIKvtB6sP+iuEYfd9fgVwtvFvtbai8ZhahfEQc0qZC541KSI07G1DzlAu1k7j8ngLZJzkS0c5hNymVKPzmUuNo4QJGyIsGE1QdV5o4QiurmcxO579XTz5yi6wyRgZt5oZ7/iApw/UeaRYR2vI1j3qyyk30ArhraiopHqU7XYV5Gu92sCTx6uXxsJyxlAOcITg3rkXOKkCPbKT9MTO2jbMqDihxnJpm/m6bBOM3Ao1aRwsos1E1uQhaWMZnKO4eAOPHc2CviuMon2dXlTiUMhtgoSKSKNo4kx2czBrF2+PZUaZEmjNLF+o2wMy+cVaORehK4hidRNXyjGWLO1AyaLalQlly+3VOUnGZlDxRHSJ+uQFjR5J+U3YJF4vH01x6AhCbm7FZdOgirwpWf9wv3eWi8q7NBTOTlguN8N42Camvio5CCmKZpBzy8fYwy0mLZxUVwZ6vWxOEoRBxjZcY0i1sUi2YzPx7rvivXNFGL9fLNRxgvzC0P1wBFy8FpG+dIjTKZTc7XZNC+WKnSA2i6bovD8IHQbzZ951dtkQ+gfHXd5wyAQu4LvmOG2jHa86kgG7+oRV+SE16AS9706jaLKNvgJYXqxUKmuiakNfsxbRTamtdfUc9J5jaVcG2xOtEwUkvyNK6XKBRqNYa84qJpA8P+/g1MrkOx+jd49WQ9jz7ofskLdIaaBOZMdeAKpf9JZ3p2gt6SyXYCfNlFMm+gHa+yW2zUj2ilSK2q2XLnE7njjhICMppY88c2Xqhq9v8n1qKW1IHf92g6puG1zOpwO0ucVngjNwUvAv2J3M6l03RNJgJymbHEa0FfMtTMC8S9FgK2yWOyYmltHRIntYEUqvppkJviQlcjuuqlMrsnBs7TZ2vrPOvry+aLsDZQxcdabMPcJfKZQgrnhlThs4NateM6iUuGAudNweKt6EWRmyV7V6skOUKzBsLXQR4ND9VSO3pOZd9b2lJsd7CYU6wV1vsEMMDr4f8N4XbspYrE2957jaR+M11YnRvZ4O9l3LQwbWj6d6dz9JjaBveXpjZL0eT6I+ti3cIHjdDJCMLVtNt1rM6+9V0san3lIcVlk2MO6yd0Vi4LOjjDtyixG2OWZmfVvr11rCmTtzX1FXCfZl08IJVYnww1LWwmhivKZVnGhzt5sqd82lhYi61EqYQidnl4IgXxAE/Bj00GSk0PEKQeutY030ciyWlWld7cvlMNK5PRy6vRZvlwWqBZF5g9soAdleUtx2jKKa52HmotDQdkeF1m6w6WBlJPtpjXNadXTzrXwyb7LmOG4dsGup9zzn5oYj43gnNpQyZkhyX6RFK1519/udQlpV5WF3T/i3TdswbdAVN8RHbsodu4a0iAdpJNTeoIYUPN2UjqeZU63v5PheIULelj5zOHqEEq2IBJPDdbhPUHO7tstyO+53vdhMVzPq8c0+j3l3GcUFaxRCeFSKMyl0jc6L2KUQ8War1svM2Ra9RZSMFUemOanhzTusjWa14W4rQckcS8oEGU045SApAppeSbevVjfzvBGhiZCjc6ZruyNVnE4nWFWTDU/g6OT7ru5U45241n1zsVx25yrqEAo389ggdo+zt2B7uO3MfCUREn4E8GLxF1XF2cjb9aq8256UVqhIn5WWa6+PoJ4zsH1Ryk2r3TiiO+SoRsjhLSw3RzFU8CwaOQ0/N/TFhuJtKBRqNbnwWJ4YmPX97bC/qbFaCvyOuuawffSGIfYmNzkwwT4cvUimnYidztfRLPbUGKaHeCpx/ebu+Vo/NveWgzdpesP1qiOp3dDcGc20/XA/qFx915Nc0VUsvJCqjuaWrWbZxUksOlLVPuXzyL7ba53F5NUxtPYVGdSHHX5bFoTCYz7JCG5tcyOqdTZKNaKj0WvbOqfOJB0lXbqobb8il7Ig1ESsHWEd324JjjsE0lAlJ8GIDGs1lL2FHKDx5nDUkG03GLG8hglMlUVSWvft/bq6M4m96chyXBspI5ksfhzNq7klEWm18caVu1S2+WXsfWOLI5h0cDtkLxhezSf42Oi0MBzgbNedDMPsgnpX34XgYu8PxqngRimODBHHTXaTqb0SVpYLDenpWLEu0lzPiLTzax7j+t41y8go6CHBlzc6kS681qmcpOjX0DH3oeBU5224tDlp1Ee975dK6oS6I2zgosFpKYZvFuQjpFtchpuWBfnoFMNV6xsSC7VID1XYU/yl75ibZHCIANVAS4d62ytpe8maO97PDsYadFQphl+lxvlInuJ2Y2MOF1q8tsFj+twweRdt2u2h5IjiamhNhHaJYu2as4OE3JAfRGYvXg6FKNOEpO3QYpNHmhhu16Q+iopGDfDWPVSyc4QlXzSm0/5qQ6rckfc0xYYQNTYZ3QUb1fF3CZGBDZzCrjY+JzWdoaCeuSw7zClEE3BY5RSuZZv2KkBRUq6bjcaLO4e9gB0icryJbbW2jcsmipHet9H4FE0G38pXXCRF6w73y8E5Xl3FaSmaVvbqetxsNgTkjAqXc+ZmdzVMVZHuMndfmY0rJKvraIy1yvOO01tOiCt0qoi4jGJSxZeYVNv4rhpqV3er9uKhYI+c4Suz6DOYzgYkby1kMqzGT6dhpa7ybR31rDaS9VlwBJA6m0lxfNutCATNhdRtnRHB0BzzcGQC/YFhUMvLKBOy3gdm1rYEsp52Bd9pGa4Df16bKqDUq+UP1wArSDq5scp23bDUhUXqVrUhFrricbutT+2aHmvvcjYvZT5ku/LYVowupSsGogIkLO0RMYU9jVBojljBJlKrsTncT6GcmmdGgUzGuBqk4/qUTRB9j7WOuBytnXa/B/rqeIKltiA4px/YE4lS2MoxjG06OJB+dI+1qmJ9zrjLzJbzJobPJWquOBg/82d7ia6aLhKCa7iXcFdjsjhZqkLeU1CyqhXF5E5s1Ao7g82Y1WHL5Z4Q3JbrE9iHZPJxjZSk65yum3F94bttUjGr2vMIVNx1HKOAHrO7wsSYsjtx4C9OcGM4B5ogTZdAN91iDHE6Uxsl1PTzFcKD4IoFiXEUnX6tw9sMD7x2uMZM7yTauU9SBWzwt2iX3uSLh6C0demXbrvD9neEgIz6LCcVyvJwUOJXfAnVrBOLNG5sSomzUkD8zd2Ve+icB15ukSM87vg92jNqLBQc1Q5Wai2pcu1f08Zgus4tDvqauKAm7KEUKl2X2uVCajk9LbEmcshzP6jXA7LkTsuRy896nsPEDk6agTUV6bjhz0zIHYZ6Sy6ZleLBqpZ7w2rM/VDYYNy4wgqUO29dJKUzLFHRZIPew0BDIj5vc1HMaTEF3XGwk6V7kRJQc52W0OkqcHTSbPDCwtdJuTvReA2Z2XKjm+ywOTigQYvdk75VHdgDzKqsrogzemfjKuOQqEk9JMgdx8b8iDl5bZHeeLms4jXshWuHv1jssmnT05jUDblKhEplor1/vThhMp6MoWNLL6MGZF1gtsGZioVNzmFJn9Bg08EAHbHVXi6niorVHuqF2301nBjVRwHQn1g3X/donZQJaJBr015X2DHJOntXZ+0+qtiLr+oMbJxz+NRdaXTv0xYDJdlKwRW+QvVdHMrcsGTFS7mU7PGgx7LFFQNu4fa4LLJ94Oz9lcLck3ZdheZhWtpIjfoXStfRwkcZEq/rFtkJE9GQy1MZuAjV3WK0RfsMP9h2TSQ0711O/dAyxiijRzFdwrZcexCVYyVgresNgktPtbeEF9PVespW1nmgJZ+r/EbIUC/wkxDZI8kmRK6Xxpu4gyusnNOad5BCHYfrElSPkkq0f8cnW24mkSzJ6MxUZnke3PAQt0pYy27tJGdOuZyh1u6785Dv5WHVu7R52FXiVUaNQNcSTdZIapPtKdDmlJG8y7OdIOf6UhAlXbydcWUZaHRPIhcEFyxummJVTie+Nk8Js6ylBLk1PYzeqeYgCMbesvqLpDlTvVxVRFnDNg1RdB+fDGTk1HsRUSTNuopHwQx5Mv1hODl8gnE3MrUgOjCRmNQS24srCE4VPwfMix2u6yNp+1GcYEhZK2x+1u5pUWMtipljL2RuR/An7HCRrjXE7BG9u+3qXSOXw7RPSSpCovzMlPnROkSRy24gXtCsEllppK/eA1dtL1rdUdKl6Nv2YFLaOJ5zHF3yy6sPup014yuOuIItKg+PpZ3X/BZawRRuS/olKCsTmeDqYuxXVkaKS6WQS/ju2nvxgOXuGOMYIvouMx2vFyNV4gleRy3nj/lQ94jfwOF1WZU+i127mBcdKE/sWs+RE9hA8vbAlgVZbXKBRgsRbeJsMA79dQUlwXIDFRl9RdfJZZ0SI5Paraa5AthbpUJVjFrVjMIVFrAxJNsWYqRphYci20LnEbrcZOF+Y9eoeZwS1NFY1GPFutGS/UG1uo2aVWp+R9wqQwFj2BagKr5oVhC/ubU+cRz33TVqTYwfiaM+yWSojYOCxqFopHeYvaQyc82ijjva17MdrteKuA3bZDhwzKkLxJD19vwUmzcjuFwhk94lxdQxaeNFKADYu8C1g94Fd6qroJLybibY3pQUHBZHMmZ9OIn6Sly1Ek1ZOyNI1yzkgKoMqNZdB7Z3xNotZbHQ3lXajVafpVW1vIQdhLN4le33m8Od9lBFFEB/JK3JbXYgxk6CnDIw+UbH4X3uWVBG2n3fMfqJL3xzReIY73lJUDPSSqTKQBp7lLGhjgr1KREwAWqGwTxNRBZLYR/k+90dGwM/XxM3jIA9c03nW4Pwdea0xXTCtkl9eeLr3W1HIyeKvNTusQ3F2OdBf7PdRg50QLS2THQDbCmnCr5xeWIdmbFTavtoKy3fFVSvxQF3ZFs8uRdEpPSnksMChnFUJ8mgw3rVKLuLfyt7OZG7XDXlMRk8Y4MrniCwB2oUKIQ5BnS9FdTl+cy4A6aUBYqzKlnHoNGtKcgN6OMK0kK7WQUX0YaqozR0abW2hkwg7kEXjsFmY2wRriPb+oaTwUq2e9q+CCFG0/Q/Xj6+zIc4b0cx/80fcczfhf8/+0r++e35tyPYx1mIb3ufH2t9/u8q9OvHl9qNgTrPM4cm7cK3r+j/+cTh078/0psnj88fRczHxEP77bCqtcP5Z4Jv3+1/fPlxxvM0/nlYE4ePg5z5t3Vf389LPr786fweXNtvJ/JfXbv2ZvXfDgeB1tgr/Iq+/PF/AUeabD/AKQAA -->
