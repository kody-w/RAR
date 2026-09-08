---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "e65f1661b81bf0103d70144a51f6b3ac3d022e795400f9e8c93ea1780eed398c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/gantt_chart_generator`. The original RAPP
agent is preserved byte-for-byte in `gantt_chart_generator_agent.py` and in the RCI capsule.

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

Gantt Chart Builder — Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator
  Upstream author: Nazish Qasim
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gantt_chart_generator_agent.py` and embedded as the fenced Python below (sha256 e65f1661b81bf010…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gantt_chart_generator_agent.py` first:

```bash
python3 gantt_chart_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gantt_chart_generator_agent.py   # or on stdin
python3 gantt_chart_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gantt Chart Builder — Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/gantt_chart_generator',
    "version": '3.0.2',
    "display_name": 'Gantt Chart Builder',
    "description": 'Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.',
    "author": 'Nazish Qasim',
    "tags": ['gantt', 'timeline', 'project_management', 'matplotlib', 'charts', 'scripts'],
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
        "upstream_slug": 'gantt-chart-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fe66d46e3035d79c',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:scripts', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class GanttChartGenerator(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GanttChartGenerator'
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
    print(GanttChartGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjyJblX2HifcisJjNYJLZ89swGISEhECCEkERlWRb7IvZFLNX138eRFJFZXVWve8zmwyjTIgS4X7/Lueded+K3F6ttwrx6+fIiW2NUh9DeqqP05dOL69VOFRVNlGfg4drLvMpqPMhJPCv7BDl5Vkd142VNMnyumyHxXCi1miLJmySyobWVNQ3khFbV1JBf5SlkQbUTem6beBB3MKC8gpZWY/GVlXrQ1xZHsTnURU0IBVXeFkB8krdVPa2TFok3KQHlN69KrAHctDIXyGty1xqgJMq8V6Cu11vTyPrly8+/fHqJwPeXL7+9OIlV15P6kz7cpM7TEGDxp5fEygLwsBiABzJwXXiVn1cpuOV6PvS8+lh7if8J+o//uHZWFdQ/ffmaQc/P15fpn9ZmUBN6QB8LOMSFHKuw7CiJmuEVYpMOaAxVXtNWWT05oamiLHh9zPwuKS+gf03PPj4WeQ285uPXl7yYVAW2f335afLY15eqnb6/TlKKjz+9JnnnVR9/+i6nbu3Yc5pJGND69dvz+ikWDPw+NPKhbwd1xT3XqjwnKjwg/Af7ps9D9ae4p0u+PQZ/zItP0F9Lnuz5F9D3ASIbyP1rscAHYObLa5xH2cfnGhUIdGZljvfxp78TC5DkXBOAv/+R3J8fgkPPcoG3ni756dM9fL9A8NO2d5l/v2wBAPN/YwkY/rbcu6P+TvY9sv9F9ITt+j2WfynurybA/4J+/lvb/t2ET5D/9WXpJRHINMtOvC/Qb3eI/PzB/X7zwy+/A9H/rZgDyF/nLuFbamWR79XNt28/f6jvtz/88vOHtgAo9qz0W1slfyXzr/x6X+cPHnyO+vjHuWD9Y3bN8g6wxlsOQb/lxf+qfn+FDCuJ3O/36y/Qj5k4fWBoMuJt0YcLfsjGGuj6gx9/evkdEE4GrGmd+2PAH//4B7SLnCqvc7+BDk7eNhAIcBOl3qS8HkY1BP5PrFF5wK91BBz7HAfwP0X4zng+9Ov/dqzmsxUAov1cX6MkqZFg4rJvd279Fryx2a+vkA6k5VUURJmVQBqrql+z+7xppaLyaq+6AXayh8b7DJL48/QFijLo17+U9+0+9bUYfr2zbfSgOI0TJnqrAYu/ToacQi97qu1YGeT1ntMCqUnuABX8CNDxJ2BgnSc3QI+T0XcTIDcCBAIWGe6ygWO+TMJ+/fVX26rDr9mDj2fQo/7UCBjwrg70+TOwxU+iIGy+Zp4T5tCH337/AP0n9O9m3YVPa6igHDzdDjTcHhQZAmnUpmAYiAiIIeCIu9t/+/3pUSAGuAQCQYr8yHtMBjC8eu6bew8b9jNOkJDtAbcCl6ZFXjWA5KGoeYUEH3rXFyw6PZrKQJjXDeR6hZe5XuYMQKoFzHn3ZJY3UA2wVvvDJ6itvfuqv9qVdVcxnYLV/ArtOBUUnTwBPyY174PA5DyLgPvfg/+4D4RUH2po8SbiFZIn4EGFVVlFWFnPNXzrERdQbN6mA+EWlHnd12wqqt7kqnsWPNxzB0zkPEP6eYr5VLNByrv129pPUAHw6fcSWX3N6ifCrWoKhTOV9gEK2sideP+fT0jVYd4m7t1/QNNJ0jMK7jMqdww+Wo17bYcWbZQAjn9rKP7/blom5dn1WlutWX21hFayrl0eTgV6TkpCj9YMNBIQQNYjgb43F28E8sajXzNgQ2VVwz8fI++heI55cFNbAXs1VrvLBzgAjprk3mE6wa6qJoBbX7M3wgZKQ3d2AoaAnAaYn6D2tuD09E3TECTudP29eN/DWrmT2QCKUNHaCYCJ73mubTlXoFU1pdrTiQCz3pR2XRg54R+sgoB0AA0gHwJKRCAwgNTvrpNzYCbIsnug3odHU7MFtHBbB2gbepX3Cp1AtkyIqUGKgo5pGgO88OEuCko94GOg4ruH69AqHsrk1fVNQWuKRZ7esfQ9As+H3/F912VSH0i1XACVr1k3kazr9Y/Ivuv5jBVQNp0y8j7pj+F+2gr9WFn++TW76/jO6yDRk6ko/+AcCCRYWt/hNvFUDbgGoPVhHkDCvf6+Pkroo0a/6/IF4lgdYh+kdq810Mf0rYrdC97xj1H5AoVNU9RfEOR92GsA8qG1X6Mc+VPh+se90ny+J9jn90rzB7kPF3yBftyL/GHAE45fIOwVfUWnR1LkeBPenp8vUJu908THH74/g3UPhud+ApQ28R8Ay4TMGmT5va/QvO/RfIZ8YtNkAIXzvbS8DQH1Jai8YBr8KDX1VKE6UBTvsoG/v2bvEX/mA7A+C6a6WOc/5Om9xoL4PcLzXgLAo4mrALsCecF9n5NM5tbey5esTZJPLxmgor/d30zkDpAIXDbthUBWgA6mibz71Xs3M138ca93zxeQ6G7+ZUqbT9DUeQJWe2siP0Fvbf1945W1YMf089TATkuCoeDX+9j3jaTtvYB9WTMUk7qPXdDUNz372T8rMWUL0NjxpoKdv6fftOKfhIAvQeBVfxai3L9YyZMD6uZO7VHzBoY3dv8EgYAB1IMkAdzXggl/XgasU3llC+qcO5n73X/fzcoftvx+d0Pz2Er+9vLGBc8YPJs7MBwk3ed6qnQIADNYEFw/YASe/Q/bvucswFmgAwHTPJLwMZLEbBqzfRRDZy4F7JxbBOaT9sxyZi6K4x7FEHMU9RmPdpiZZ2EUjQJenjG0A+Q9IPhtKuLRpAnBUD7KMLg/x3DUBRtjfO66NEmTDkHhqMXYFmETjGV/n3oFOfY072HO5Lv3DnRyw9PK315scg5Gbua1wD4+HMIYFoJTsRxK8AxFFkcE7mZ6JTYVjisK0uR2xoT7U0sZ5IDB4n4dzRtUv9gnQ9uKCeGvRFZFD359ZbrZljOkuuivzRDvpUCsJXOznDvdbMfA+7jc5vRWyrBKzCxy3sC4U9SYljPtTb1R3FkA28UTvT7o6oLuQtFY42k9rIEOI48n8/Ro20GzS49je1p4+mobLfmmbE5rJz3tGzQWdErJ+AbtCybvbeQqjfGZlWzRcGvCOJn7jZkeSiw/HnHtYNXGMtExdJv5grdRV3Q4iuWRwoLU6VfqInVuZ2KO+LMMJ27XkbmNlQz7SOymdnNgjYOOrA9UczqBzuKEb42WsNZbeww4ItN2s2Fc892pT6uF3Ml5RWWe6l+WSS+RYbS6HDkLx+S4gN2UWNFwf8vMqLjMTBEeLtaA85fz0M3txOFSJdwJahvGllZ6e7Em8TIhlVliEpXd2OjNXV7sHTVqS7ZZlYaO3wR2pBt+Gyo4z21dWtmLypXnyHw4l1jXNSfdbo7jqfLR7iBfqGuNB4Gwn2FLazPYxAnnYZiuyGKBK9kpXTLNaggIrMhXtnrDmm44e9ZaOh7SJt6v8Z4m96cuvsgNelzcTtUmC2VjQw5lth58opyT3NiMJXPaG0JhzLdoCLoctrgsJavzClJsGFJvztRCMRYDy8hUQ+nuemYJuEu4O6kh1A1H0pph4ucrMiABFzeYHfJpKNNmyBERuUuHJli1iHQOPGfVCZbQu60AY0Ki4ozSycpMOUgkcU3CK47X4UoklZObjz2CZ9TFqU5YaIKWurDieXHeb0giEo+kbgeMY5TemvMrRtgZvbveRqSiXzg4SXGJoUq/tpA5Yrl2PWNGQfdlJpDJo691SBQi4WgzVyEIrbkLHxMd+EE8rTaoJY/wPiQ6UdOToKW3Q7DXWJRT1P6yYVsmmO+kwrziGmZTi2V1Cu1TxptLIhswNN3yAey24XBp3Zyr6O02JFabhmAXpL0sfG5/oI8X7LJlYW2kemm+y2mDuJg3cbvreWHrHNq5eBXaNT1mhqYrBNxt2z7bx5Eq7vva04306hn8PCAQTpU3qxsNa9fbAoeV00IhuhlRz22aye1uZJvTtkj9oLB9TGB08lhcpSxN3Mhb8rXKu0S7dzpfUdzTOrvNr/ZWZnnzJhk0+FE7Sr2Tt3ifE0drz6rlTlWV+MCNBMfb3oW/oa5Eh3BrzvYEzeW5NQqLm7I6gD0IpeFiSTbHIi2wG14QWy0hkouIRji3O0szxR7P89I9WOkmFSo6RU4WhuzrxaA422McMDE1v4bbrq1Ff9WNF3E/MkEF1/XG3vn7oPSLXhQanWbLnGular9C5VuBCypVX3ZwsBhW9oGVzJQ0NhKuSmTfBdE+uEatQMTSuAud1aYuQvEonfpg40gRGdxYj3IxwfVmMawVblRnSNbTdHLTCpzVaXrDR2G7veFebp2UUtEoQu/SVChTGpONkhCOKT1Q21mvXhuE3iz72FjMLPtIiKJKW8UgM02KmjRHe7mnSbMwTa9E0c2TleScs4x0EcToabiN9ZERbkhxWQW2Y6zLRBTq5mKIg0wedmwS7RqhbQceE2xqKcV94VEZWoYutpcBGIzQcfnSuq6H7ShEC16P0ZG2L9edsJzN5QtbEpwsEFRmCjm2oWJj2GU3fpdQ6aBXwr7vcibZG6tiI0vpYB5qQ6Edrg95Gb9a8UErZPbcSS5eEoZ2bTp2Ho/qKhykUrVqy/U5eh0ucUeqknU5mEk4Ygd48DdpsRTk6Hg7CQagQep6xFxLQeuxuSw5NhWvNuUrRYUNsr9bXouEOw5KqkVzb+FtW6GrxBuvGC4qdueyHnUCK+ND3GxnN53iXNWiyORS3xKHCKXESrVVk2vSak3qaWjJDK4Wmw7fWnutXCPYDJZEK2JXWKPlO5Uf6nlulgxBGrpWHpfLMz0MrUFdSbygyaszMg6MzzaU0PEb0dmH5D7d+y2NHWpxtsIomRUv5zmb2nIsJBrRVqYlXfNKXi+iRaFmPAm7qjTsEHWbM2FSV/2RAZCW/HMpSxorx2wXuKvLmd2vjNiN1quCiBVp6A3O0MblItTFhqr3i7maLczVWjAdAZ5Z58N6ze1EcVArLlz3YJ9/cAgmMNYCbSyO/LkIxD0toJuubBfEUsyY+eWmHS877FZ2EZpZ3KBh8sJi6aLwD6SmroPrnJXpQpwv+mtLSbQsqAuP7TfxkXL3kpJmRzs3eZFBU1o7j6TC+d5hzCV1vtrXonbsliNoaeRtf0Bn1TUKuYWIzLk6whvLjlvQti/34cqxV9Fic9l7hnQ4nHRJ3edIK46ceY7jdXChLtTOvZqDg3pzkSBBPncseZ1x/NAeRzZrmFo3Qa048vtCwJlNmhr5Jbdgd8vJZ8WhSzMRCkma1S1xWPtlHlx5OZur3YbSOnc4h57XX2qMWmkjHZy6Fsfm64UiK25q7XLe0Xwru7bMOS4wNzSE2aoIjVGv16hfeYuLJaY7VzfV08pei8UVvZBLbs+iIXnz1FBytNwmdeJy9Q4ya5KHVqvnS2dRxqdGXGw91leLZiuVCefZcLnJaGnbiAp2ZqOLweyNK8rNLHGfa/32lHc6tgi5i3mN5CgsrZjQ9S6JCkdeJoiQN/rKXG37KmZunTBU/NjOBC2Il3kNh5zUbwU/57SzfOzZkWIvfGSf9BG3x/Wm4txU26IpIZobPfT9wUA6UdxnhZpr6cb02hxmYbZsheUy4kISXZ2iYF8KXVOynOnkihGYEUZierfeIYJ/WB+ziDcLS1qTI7kuac6Fq2NqbPtAi8PZqKtXlL2dG3ev7xlUt1GeW+5FQVKGpYJiFKohJIkOzYZLs7pTc/N4UwXvWiknZVvVo4kGa9mtqD15ra7GcTss691a7Jx2sbnOj/NSEQvWyfblam1v++ImGrmLemF4sQ6HevSCFczuhCLaIYddxvX2FWZFDeyjLsdKbjKlIIT9caaiRCTEuequeC/hNEdPEg+g+1T4hoFKBF9WSX9arGG0sg+Rb7F4VdpkpMOFRYo1vTU5cXd254YykkNDRLNDrIyOQFMyXyjL8FScGEu2+1I7NcQVsSs9vZn2xrnhA5PNzLTRq91Y++tWoeFkL2zYHYme8hmhFqZASq3hrI+ootFcEbG3SiEH2z8QuGWfenmTXcxjMVcxQ9+37UrkKKwzQJmu2FId231Ujc6Nb9bVUFJFJ7QYPB/h+Yp0cZvcoxlFbOiAPOPS3mG4ZkTxJegEyay64PXWNUcznbXzxekkza3FMMsVvMc6G2CfvcAWjCBChzThxTSLqmOOCHgWX+fqmW1LGCe35k4gua2AzcOKXIXrqxFKamkcFIu3sC6aYSShw0F8LeMlJjKEkQhDIMvrcxbt5gdF2GxlKscD5zrCEmoHmH6gmFFJFxHBHw/EjGrmqtJh1voUtF5X8vAZ3YxhBuwjthESoEUNzIzzLTUnkvl2yFQ7uAbaxU7pBaO5DJYYK2xYnwucgznKsl05NPobjFh54fNiMF/BF9Mb1bbdIDU71qcAp8xSCmOM6NLc3xilghUuIZ4JH0HCppeGgCWPmsTKmsnSM2R5sVx8lvWjv9OktKLso3fBNoZLmcPVyMAWJiTcNDyqJDHsTXZmrcdNjI+3nkSGlWltOWWhIl5fyOudXztN0suB7LYHRxN8fO9otbPWSQstA9EPwMjDzvGlq+30bbS88u1ZOCiL4SrQDoXFrHjccDRfprLvjpfdxo7i/MRsL0RDjIueCQ+16YP2anXcM55O0c0aNBfkds6ESL4su6tAgYYoNzCXcLzTQovHhR5wOHcNUbmWorgjO4m3XGRHcqCLA0x72tDm+XBChXTVYsvBPt2WoN2v+5Q8XBTvujptYXN5sOUjb2azq7dbkC7LE80mXCtC6m2cBY7aZ0lPY7dehb6oiGo15osOEczZfE72bUDQirQpdL5f64h3Nrx5fTEKyt7QKaucorHStVu0brejRhJgV+gxaj3ClGVkWlFu+APhSpq5v+WMU3sp72zFZZnBY0sumuq2ZqPAE3rEWAo+dpTWc3rFBOdtXiY+nNZRb1IIt/RZ1lJgNZY2fYBnTUnxhWphRJTdsptStdHs3M1N2tdbrNw0K6yqkHgX+LOupXbhoji2RdBRNbXNxhXjltgOhxHNpoYwlm7DLd/YM34g45NGByBMGSugoLkfLhmTrNt56mE8li75sm0u8zrYGRnYpWDXWTkfqwi3KVMrigUVV0qOjDtmyAZ+rxRRovPDpgSbbMaiMNuxwgVL6DRWwsRy7Rz9uHdW7LDT7XkZM83pqLl5Vl7c7Yln1uegSmBO3uWeqszQ/cVqTcGkby0iuFnqLjBJL4kQdRzxzCx6x9To7GYUVbNrErS6yWh2gPGxDpBKiTwKYcoqlG9aMGIoyDfiNNuIVJSusMXIubG/XyBYcp7PGWnlwsYyqgpE0EOC7nQFkZtyJkrjwQjxZRMsG+PGqbi8OvBgf7lCUk7flcNsXmPA223p8B2cSwe5tqozrM9VPb0u5FzbHAWq4/X00uwvmKDvPGZAd8uQwvburcfYOsoCsmWoUCa8fn3uyGp1beWjs0s1OLkFSItHFg2Dsgg24tvVjaAXVloQI1tpameg/HrIDhnsWNLtWJdSF1cDlXCqQ14OmlGEKRFcq5CJoj3DrfxoiA7XumFuQZecrWFcqiSn6W55RfrKmHtuCwtCPiJZbFVj4SnprpOsflkEdLlIVRbPd7NdZZZnrRkQBAeMp+E4ekUkUqLwRSK0YYduQ6ZppejsOaVAOjNBnumx37rdoMTyOXCqgDZOzHnli7NjS+a9OrI7D67TXnKp3Il6Sak37NIUA4vOhMs+nZW3WFfx1DT4ZTbfO0k5s1ThBHopLHZHgxB88xa4p5OwtES2T/Vq31hHmt/IjLfaXjYOs1gOwYXfWpv1Jdite3Rk3Vk0kicXRcEGD5DfXnLWY0eBrmwz4qWRyFGVN/IMEUUuxmZxKXvt+nxiOBW0V+nV2TFaxrcDSH3MntvaDJsBBKK2yiBeCpN475UNFatoW/TOXPej2fwGyMH2T8vbPBc8lpuZ6v7mLbWbGmlhWKexncLnM3w+buTTBmv7NX9GNFrGZ+pWLZA4i6odhqUNVu/UEHaWul0xHdOqFiJyQTdSAjJeeNAzKotoAyhqv5IjUszb1mEQkd+MO3KQXNics+dYCqhCqXnXxo6RyPKYQiBr+yLdAi5gsCO2z8RrM9PmdCsmFVHVJ+msrxy3l+CjwNuaeliER7Bh6PLNsNZGr3JEeH6RxnKPzegOp4kORhQKqQ3ypAT9zcVNx/PQlvdT2toOIXmIVYO6nQNzljjDxpRiM9OkcluaLntGKXnbuUx8VEuKQWK1Q/PNojPMHm66HkEPZqIW9Kagrn6SU6RU3TaOeTStlld9YVAWYCfb8mx3ZuieZdl/vXx6mU7en+fn//4d+HS0+f/shPVxGPr2mux+cu5Z7pf7Wl/+Gz1++fRSORHQ4nFgXCdt8Dxo/a/HxZ//8l3LNGd4vEGeXtz1zdtrhMYKpr+cevhhOvuOUm96Sfny6e3IevorDrDA9PoX3Pz+1vR+2D8dq0+yH+9HJjWf72mAdrNX9BV/+f3/AGHXiMtpJgAA -->
