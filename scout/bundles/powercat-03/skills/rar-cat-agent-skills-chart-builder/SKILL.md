---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "f8c8b03dc4628aed2f0ddb36fee0bade66fb9ee1ceff7e2d407c92a7ff4dedf0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.1", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/chart_builder`. The original RAPP
agent is preserved byte-for-byte in `chart_builder_agent.py` and in the RCI capsule.

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

Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chart_builder_agent.py` and embedded as the fenced Python below (sha256 f8c8b03dc4628aed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chart_builder_agent.py` first:

```bash
python3 chart_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chart_builder_agent.py   # or on stdin
python3 chart_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/chart_builder',
    "version": '2.0.1',
    "display_name": 'Chart Builder',
    "description": 'Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.',
    "author": 'Adi Leibowitz',
    "tags": ['data', 'charts', 'matplotlib', 'scripts'],
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
        "upstream_slug": 'chart-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#chart-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f32fa164a482da33',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.4, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ChartBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ChartBuilder'
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
    print(ChartBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZPayJL/Ktp+f9iztBuB7n7xIlYggUAHQhIgmJ6wdZQOdJ8gzc533xLQbXvfzB4RG7G4w60jK+/8ZVbRvz9ZTR1k5dPrE+uGiARCO7uEdf/0/OSCyinDvA6zFL5dghSUVg0QJwZW+ow4WVqFVQ3SOu6+VHUXAxdJrDqPszoObcQJrLKukM+2VT4jcZiCZ6RyrLoG8DaA6zK/tJJnJA/BL4hXZgliIZxVWwv4FCBZicz1PQL1CJAshSKtOH6BGoGrleQxqJ5ef/3t+SmE10+vvz85sVXBR0/zQeSsCWMXlJA4tlIfPs07aF4K73NQelmZwEcu8JDH3ecKxN4z8q//Gl2s0q9+eX1Lkcfn7Wn4pzUpUgcAqTMLGutCVXLLDuOw7l4QNr5YXYWUoG7KtIIWVHUZpv7LfeV3TlmO/GN49/ku5MUH9ee3pywf/Amd+/b0y2Dx21PZDNcvA5f88y8vcXYB5edfvvOpGvsMnHpgBrV++fq4f7CFhN9JQ+8m9R+Q6z2MNnh7+sG44XPXe7ATrnx6OWdh+vnOOC+zFqRW6oDPv/wVWycAThTDSP6P+P56ZxwACwbn80PxX55vTv4NGT0M+uD512JzGNb/jSWQ/F3cM/Jw1F/xvvn/P7EeUrf68PifsvuzBaN/IL/+pW3/1YJnxHt74kActjA77Bi8Ir9/1VV+/usn9/vDT7/9AVn/t2z0rCmdG4eviZWGHqjqr19//VTdHn/67ddPTQ5zDVjJ16aM/4znn/n1JucnDz6oPv+8FsrfpVGaXVLkI9OR37P8X8o/XpC9FYfu9+fVK/JjvQyfETIY8S707oIfaqaCuv7gx1+e/oB4kEJrGuf2Glb53/6GyKFTZlXm1YjuZE2NwADXYQIG5Q0IQgj8GWq7BNCvVQgd+6CD+T9EeNA485Bv/waB64vlQ6j7UkVhHFfjG7p9te9Y8+0FMYIBtEI/TK0Y0VhVfUtv9IOEvAQVKFuIHXZXgy8Qdb4MF0iYIt9+4vP1tuQl774hVuoO7wfltPlqAJ2qicHLoPghAOlDTcdKEXAFTgO5xRkEScQLITo+Q4OqLG4haA1G3lRG3LCEFmVld+MNHfE6MPv27ZttVcFbekdJDLkjfjWGBB/qIF++QBu8OPSD+i0FTpAhn37/4xPy78h/terGfJChQnR+uBlquNY3CgLLpkkgGYwAjBnEhJubf//j4UnIBvYaBAYl9EJwXwzTLgLuu1t1gf0yJUjEBtCd0JVJnpU1hF4krF+QlYd86AuFDq8GcA6yqkZckIPUBanTQa4WNOfDk2lWIxXMrcrrnpGmAjep3+zSuqmYwPq16m+IPFdhK8hi+N+g5o0ILs7SELr/I+j355BJ+alCZu8sXhBlSDQkt0orD0rrIcOz7nGBLeB9OWRuISm4vKVDjwODq25Zf3ePP3Ti0HmE9MsQc9iNE1jibvUu2390axcxbo2rfEurR0Zb5RAKByI8FOo3oTvg/N8fKVUFWRO7N/9BTQdOjyi4j6jccvDWaZFHq0Xemik6wZH/9wFh0IxdLjV+yRo8h/CKoR3vHoOqDHog91EH9m4Eps29Or7383c0eAfFtxSqWVpl9/c75c3PD5o70DQlNEljtRt/GGToi4HvLQeHnCrLIXutt/QdfZ+hETeogWGABQsTesijd4HD23dNA1iVw/33TnyLWekO5QvzDMkbO4Y54AHg2pYTQa3KoY4esUgHp8CaugShE/xkFQK5w7hD/tBxUFX465LeXKdk0ExYQjdnf5CHw3wDtXAbB2obgBK8IAdYCkM6VLD+4JAy0EAvfLqxQhIAfQxV/PBwFVj5XZmsjN4VtKAdVtz14McAPN59z92bKoP2kKnlwui/pZcBOF1wvQf2Q81HqKCuyVBtt0U/R/thKvJjl/j7W3pT8QOrhzwaGuwPvkFgRibVDTUHDKogjsAEvFsHE+HWS1/u7fDebz90eUXmrIGwd8C69Q3kc/LekW7Na/dzUF6RoK7z6nU8/iB78WGKN/ZLmI3/qQn97VZCXx7d4yd+d9NfkZ9G+p8oHmn4ikxe0Bd0eCWFDhjy7PF5RZr0o/Y//3D9iNItCsB9hjg1gBpMkiEjqwC4t+FAA9/DCLXJYOUPEBl3sAt+9It3Etg0/BL4A/G9f1RD27nATnfjDR39ln6E+lEH0PjUH5pdlf1Qn7fGCQN3j8sHrsNXAwxByIT8fDDsJeLB3Ao8vaZNHD8/pRBW/nkPMUA1zD3oq2GjAcsAzh91CG53Qz5+vcu53f60W9rcLqx4KBZYM7dcAW3o3jwMwRriwpDcgyJ1lw+S73uHYY75GHL+me2t8iBkuNnrUIAQHuMb1L7Pls/I+7R/2y6lDdzu/DrMtYMtkBT++qD92OHZ4Om3P1HjMeb+sxJD4RUNhLMBxoZWlVaXAbWr+h7todm+v/8TAyHrEhQNbF7uoNx3a78rkd0l/3FTur7v2n5/egeBRygeExokh9X2pRra1xgmMxQI7+9pBN/9N7PbgxpiFBwnILlHO7SNYq6Dk1PaAu7UQ13XxkiIs6gN9y4k6dkMABMHeB4Fpi6OUg4ztSjPw13geoP0e0p8HTpyOGjgTkiGYjyKwTAGuChJTCaQl0OgDkZi3mRKk+4ERx3q+9II1tbDrLsZg88+xsjB/Id1vz/ZJA4pBbxasffPfMzsT9SRspXAZkrS84szU9VXQol8SwrsTU+BPsouAhmdphFlWmkQ1VItTzfSPImUFU4tRVZFda+KRh0RM3qa2sbpepC0VcQyqzQmABgRxJUQj5q/XFzrXG8FTC/AWm4kM8VorZ/oyXne7cOFHFdksqLpa3Egi8pQnbSuu1QMFvZBO+VmcSLFw6o7yntcdCa7nMuN3XRxPpyOojclL1JM281pKm6LZn1Yx7RIarjEt8SCH+271RQHaqJMN3G3Gq/kA52h56Pkj5Wk7zpP7WOaAXoHPDUt6LJetUqWOZlO89KqUKhUI/ZkVUkUv44DsxP3G1JLR+J5SYjJNY+Vy5JWFqsKG0frgkCLJsuTBbc4HfaXtGp7vT+2uM0EFVXIV1XWgwzTOj872ctDsqeLw+7a+1qQlDTaRcDslMnBBDYPzvWJti0DptNU6JaEuZYW9rzgfCw8zU58MyPq3XUiLU7ieledTFpOD7yPz67RYjUZrbGdLSQMQczmna268fKyYeNx6UnQntYhLu2BqrYKoVx3xebiQS60sDmfVyVfX+vTPFbifXjdJw2TcRk+PkZKWFw5e73051YPOmdNRUSeu9F4BvK28faclykSN234xOFGW7SUI77bEtO5UBwKzmmi44RSz97FObarhuzRalSpobJrDnhIepp+sbC1sgV2lJOxsyqYessafk3tdidcimrtYAvLoM9RKaTpkp9HvIGH5tiedafw2Pb7kehI9oieJJF4XDITWxDtks7WRDp2DVqRbbnoKkk10OnpULPWsZgeInqy2V22MQUO0mnSRII5v6T6xK1NU20mnHJNk/O1cSVJmJvXHQbmAXOVsdW40TznQpfJZrETxHHvGPvjkQDFQfMFIVXIw/JIjvTC8XdpIEdzIZ9mxHrNL7pCSZXLCnVr61LmZthj4vJwDhkRTGL54JTo1IqmxgK7oMvrnrostkSHBw26NEz/Okn72hb9wO4Mf6JbYXCSAm91PNlxbrPHVY5r4dEiFHO184vN/GqJTVvt5+kqtX0ed6apz2Grbc9r+Wkxp/T8EqgbwTwvYR1mpKJyY4m19mdcWfW0O2OCQ8uzsk14KjpCpb1ImIyRgKw/GYtVs6spdkxMOIuiHTgGxEIpFfhebKSt1WqxHmdkdNzsxtl+VIEx2F/ldUkF3mxTmpt+TTfrJkx7VTpMUBfs14v1MV6UWh/ydN+GmNB7hWsdlMpv9pjLJXRnLYPteltdQ16nx5zRJW2O1rkLenbRFrmA+yZnuUvcd9VmVfPs1Iu5C3tkl44IcUpV04jUOSK8sOsRVvuHOuNUM5Mv9n7vB4RsHOfTUZAk+W4KDHS32UUkt+2qgItqXiauE97cFlZYCf2ePOkoZsv9nsmWQaYcjYxMlcB35JmukafDujicKHqvmoYy6WfHaenalZkD6lxRtEHZNC55iusXRmfRlKjvDvWsM+J2szEW592ROBN70Zom+Hbkyecd2ciCiKXj/jKOLxRN6xtDELCGc3uTLFbJjEczNBZRZpIT0txbzRW8SKf1uVvzZOy6WOZappzm2b7hwpa2QcVxy0kf+cWB2/e6rI8F2yz2QrRjUdNn49BM3OnM5mUwSzciAQFtr53alsN8NXBMYC20drSOD/qOXJAufuEwei91Mk1mcj4hHMAt0elom9s6X6/maG/jsaFtey8sNnHUzoR5yu43YRSjp9GpCasYW1O7TF/0tGOZWiC3RNCmHLeQMJQhLy2uoQzM+i0nyb3tA3k0SVk8nkto7TTrM6i2MW/5WKXnIr3d7wyy8EOCSvanIy1vbSbWp4QtbaWTj+74cqeHuLlR1FKeijka6F2AF5YSrRPUGUXjJJA0jtvGo3ocHCV0y1+z64LdbraHXSMZpruPHIVYL6WCnIqrcKfoSUoypdrvJ5TIhtXWPc1bWXD5C5ZMWNxAFaVDM2ZzAF3PMFyuMiGgdigVX9o48pYXNVh3bMQq2+0q9uo8M49NpcwN/rjEA2URMAfxADi6W+qqfOxkYbuTFuQICOvZ2LxEnBdOsJlbBJuyH9XiZEXNG0FbhCInZkJU1bBRUtvgcM7iFN8dDkRWccu5mUtnDrej7cKKreBYTS6pf8DWnr3kPMmK5/h6nq23rbxo4rU1prZxLTlx6ZIrLV6kVsTNnTnctV3QSHAhpiwiviln4nQ+SUlldLSKqztZoiyljbOAWmWsdaKLPjY2IhxnJCEic5+0InfkV4sV11+bnaGoBD+yVaWQpt6B31ez4+iyUhbXjWcS6dkaGSG/WF5GiTC7JmE8Abm9c/CxOuepQBlRnAd2S3y1MhXWcfb+iYR7JDlZaHOFOPruOlpe9kLnbyNRQNe5HQe8NMG5bLUYXVfrVW4axQ6Cn4FqoY5xEg8E15ZMhscSiKHMwZdTj7ZO6FX3NOOMgvOmu0znZ9SLUp3Ix7vlZikrx/HOaqj2vN2U8mFz2Hb0DL8cx5xO7w9Te58YXbA3twS7yFLN6drR3O62UltHwWzczERVaKzV7MiO2QUz0mwFJ3WWD8fjPJqJmavuT76w22Cr+dJYUrjkRLhDsATsU/ODWJxNruhCsHbRNbkjK7dc7NTr8bBbnyS5IlOa1k59bzG03NjdLCCLbGYpJGsuVwrPjyma8Mmj0JdiuOhMWEdFuVr2V2tjSbok7uX5/tik82Tl7couzpWKZC7abIJvmG7VLhtshFd1gF20Yu1MhGg032X8vhXndGtJIgB51SmGKpy1Ws1FYycf94xsq4bj7uyOxbxVvbP4TaFrlUE2c/yshpNr67BewvnBNOfl6nIcZY6ZcbjEhb4Us+hCE+llJmfFxK/6TKk5etOArcgE2lJwugn0zWTEt1yzQZm2EPy42ZjN7IjZp4KzsJo1LDmcjdEAD1odBdSe3NuucTaL0XklYrXV2mnrlhKhKEcrGQNhBssAjrptwdEkxNvazGlh3tfBRXA3GzbMK2NKYzijbUi10JxxOScBLzPzfGs2SbNE1a4JJhMlZTy5qG24u0CNBa80V7LvARNdBG2tFoopTxQ9xrS65GJMTMrlCVIXlN1emYUgLLM1Q89dplP91chuz5Fhm+NKb+tsAnM1qW21K7N9AjeyZ93VuBpVAoGyjAvbmiY2JpYe7W9jsapVSlVpfWyEGMUJUQxKjMud9dTKMx4rTYsnR8q2p81Wt3cHRyDVVMd4FV9E2lRgxztRKaYrjpijlSGDo5cd16GH7kJeXl+FuLoGKqhatCumjmAZx0JadYlWKTOfodbSXouS8zZ1agpLl5vkdHScTo36eUmLRMlKerssLnzcj5jifOppSeub5lKWmtMrsNmz6clzXQ0LRVgtNXq0thfLV6+KSU9Vzb1W+LaEEw53lBcoSm2uinL28bM2bstyIY2n4w4/onqXqU51RLfLPPSBqqJNyl7PxOiEXaItjdJjKzpw2qhrNou9m0TTxiO8ONgpU3rjm8CsWeKctycVH9uErlT8VWIlpi8Ohm8KeFLu9TMv7Sheh/sXYtfLPuVU3kTw8gPnd7Numo/o0Nm1c9Rt99cVKI6b1j9ShHGGk8RhMZpPK4Pps8WVTymB1KVr3cgO3wBtUu5Ek5hntGhv2mLcYGZ7Wa2ykMHlDJBRMBq3mLY8dbyGX09+uzIOZ6G+no6KOgvUbCuOGLoupMzgjocV3DPt08pF9akTU0uCSN2rG9oJfjanDo6S6+aUBp6CL4a8o3kOTWbnCxlW4hg/NZ5/NrPZyJgyJLnbe3N+s5Hty9EYL6rizKPLi5YltOpKqSzM9+ZZ81IpOIynVbcPKB8/9fiBOzVrc90fpY1iG60TNBYDYVDFc3lLoOYmugr7fuoruCIcF7ixE4K1QApZgsItZjhnybNA8jZgnYMSyX48yibsZjs2Hc9TfAOcpg27A+wGmxp6tvHKeTXGF+kk7Mu20WiCKkkdx4+4LDPq5EIyXBfZhND4OMqMpPPaRKdTzSqmzIyUVXKOj5jjOS5Upl15Y8IEU2t5bkVSVybMClP0pVlwbbgQ2ZmBqc41LzHNw6XpBE73xnq5Yjxn3jEYO+65jtuuDFbMKbzyvPS85YXFDO5sCalyweg0TTdUgqlhF5UqVsp2aU50u8NjVnA5HUUvG5yTdH3Fl71wgDuL7DQ9FmVTUwe8VOu6xvK8oVTyVJ52LL3QRaps5cko7ZO5EHSu0Bs7Bre9Stg7m4w1G36BNwqLJaPlMdqbZIp112KWSknBoyItLafm0UML8YAVuXU+YYlwjZPFmWnNYI5dXYZ2/bhPKMrw1dRTg7qPJArrt0Rht30ztyXaEHsmUOeGQHHZGVbPVpxSPR7RS7/JIN4VkXcgUpam8trftKxbrnG7UxYEbOsSNl4txbSkjdXiOtFPeLMwrvmYn/WYWWlyVubkkqzTMsOTi03PAL9qrSt+Zln2H0/PT8NJ3OM87c+/4BqOOv7PTlzuhyPvx+S38y5gua83Wa9/If+356fSCaH0+4FRFTf+48DlPx8XffnpkHWg7e5fBw0H9df6/fiwtvzhrxJuh4K3Q7bhyw148f0Lj2Hp/dhzkP44foVCpy/oy+Tpj/8AA55uPIghAAA= -->
