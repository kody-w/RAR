---
name: "rar-cowork-cookbook-ppt-exec-report-production-quality-non-conformance"
description: "Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_production_quality_non_conformance", "rar_sha256": "b926c0be09901c9ab225192ee9293f70a255b10660f69cdfdb0923dba8e3bdcc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_report_production_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_report_production_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report production quality non-conformance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 b926c0be09901c9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_production_quality_non_conformance_agent.py` first:

```bash
python3 ppt_exec_report_production_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_report_production_quality_non_conformance_agent.py   # or on stdin
python3 ppt_exec_report_production_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production quality non-conformance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_report_production_quality_non_conformance',
    "version": '2.0.0',
    "display_name": 'Report production quality non-conformance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-report-production-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '467cef525f410442',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-production-quality-non-conformance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-report-production-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecReportProductionQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReportProductionQualityNonConformance'
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
    print(PptExecReportProductionQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2Jb2X6GjP1RVkxkIokDeddd6FVEGQUFEoLJWFDPIPMlQb/3396BGZNa9dbu7VveH1xxC9Jw9PHvvZ+8D8duL1TZhXr18eTl5VgbtrCSJQq+CrMyF6LzLqxj8yGMb/IOcPGuqyG6bvKpfPr24Xu1UUdFEeQa277zMq6zGq8FWyOs9p22im/e58ix3gI5551XHPMoayPWcGMozqPKKvGqgosrd1plkQGVrJVEzQFmefQaq/LxKrczxoLqxmrb+BNSnReI1HtRFTQg5oVU19d3OxkriKAs+F3cFWQ6MeAX2eb01bahfvvz8y6eXCLx/+fLbi5NYNfjo5Vg0DLBSuZtx/LBCfhgh5Rn9zQQgLLGyAOwqBoBWBq4Lr5q+BR+5ng89r36svcT/BP3Hf8SdVQX1T1++ZtDz9fVl+qO0GdSEHtTkVt14LuRYhWVHk8JXaJV01lADXJq2yoBjwO8KePX62PlNUl5Af5+++/Gh5DXwmh+/vuTFhD5w4OvLT1BeAX1VO71/naQUP/70mkwh+PGnb3Lq1r56TjMJA1a/vj2vn2LBwm9LI/+u9e9A6iPotvf15TvnptfD7slPsPPl9Qpi8eNDMAjxzcsmHH/86V+JdUKQFklUN/8tuT8/BIcgt4BPT8N/+nQH+RcIfjr0IfNfqy1AWP+KJ2D5u7pP0BOofyX7jv8/iE6iDBTIO+J/Ku7PNsB/h37+l779Zxs+Qf7Xl42XgEqsLDvxvkC/vZ2ODP3zD+63D3/45Xcg+r8Uc8rbyrlLeANFEfle3by9/fxDff/4h19+/qEtQK55VvrWVsmfyfwzXO96/oDgc9WPf9wL9J+zOMu7DPrIdOi3vPi36vdXSAMl6377vP4CfV8v0wuGJifelT4g+K5mamDrdzj+9PI74IsMePPghIku/v3fITFyqrzO/QY6OXnbQCDATZR6k/FqGNUQ+DvVduUBXOsIAPtcB/J/ivBkce5Dv/4f506rgOIetIoURfM2EebbgxLfvlHi25MS3wAlvn1Hib++QirQlFdREGVWAimr4/FrZgUeoD9gRVF5tVfdAL/YQ+N9Brs+T2+gKIN+/evK3u5yX4vh1zvZRg8GU2huYq+6TbzXCYFL6GVPf52PBuBBSe4A+/wI0PAngEydJzfAfhNadRwlCeRGFYAmr4a7bIDol0nYr7/+alt1+DV70O0cejSaGgELPsyBPn8GjvpJFITN18xzwhz64bfff4D+L/Sf7boLn3QcQRt4xgtYyJ8OEgTqr03BMhBKEHxALvd4/fb7E24gBrQ4CEQ38iPvsRnkb+y579if2NVnbLGEbA+AB/BOJ4gBh0NR8wpxPvRh77P7TSwf5vXUFAsvc73MGYBUC7jzgSToZlANkrT2h09QW3t3rb/alXU3MQVEYDW/QiJ9BD0lT8B/k5n3RWBznkUA/o/MeHwOhFQ/1ND6XcQrJE0ZCxVWZRVhZT11+NYjLqCXvG8Hwi0o87qv2dRMvQmqe/k84AmmASByniH9PMV8atkgh9z6XXfwHBJcSL13wOprVj9Lw6qmUDigVQClQRu5U+797ZlSdZi3iXvHD1g6SXpGwX1G5Z6Dyn97pGDe55PvJ5PNNJl8bbEZikP/n00zk3er3U5hdiuV2UCMpCrGA/VpJpui8xjjJoVA06PCvg0X79T0ztBfsyQCKVQNf3usvMfquebBem0FoFVWyl0+SBSA+iT3nsdTXlbVVAHW1+y9FXwCqXHnPeA6KHpQFFMuviucvn23NASVPV1/Gwvuca/cyXuQq1DR2gnII9/zXNsC8DbhBPt7ZACe3lSXXRg54R+8goB0kDtA/hSRCMAJ2sUdOikHboIy9Ks8/bY8moatR8SAtWDo9V6hCyinKaVqUMNgYprWABR+uIuCUg9gDEz8QLgOreJhzDQnPw20pljkKUie7yPw/PJbAdxtmcwHUi3XagCW3UTRrtc/Ivth5zNWwNh0Ktn7pj+G++kr9H3P+tvX7G7jR1cATJBM7f47cCBQgekj6yYiqwEZpd4zgUAm3Dv766M5P7r/hy1f/ulw8ONfOz/c2+35j5H7AoVNU9RfEOTRIt875CuoFQTkSFR49dQtP08F+flRcp+/ldznZ8l9/oeS+4OmB3BfoL9m7R9EPNP8C4S+zl5n01f7yPGmPH6+ADj057XxGZ++nWjpW9SfqTHRcjKA9vzRo96XgEYVVF4wLX70rHpqdR3orneSBnH5mn1kxrNuAHlkwdRg6/y7er43axDnRxg/egn4KmuAbnca/wJvOiglk/m19/Ila5Pk00tmpd5fPyBN7QOkMsBmOmWBqIDhqom8+9XHoDVd/PHYeC84wBRu/mWqu0/QNBQDdnyfbz9B7yeO+5Eua8GR6+dptp5UgqXgx8fajzOp7b2AE18zFJMfj2PUNNI9R+1/NmIqN2Cx400jQf5Rv5PGfxIC3gSBV/2zkMP9jZU8SQTw/MToUfNe+jWw0wXj0icIRBKUJKgygB1A80/UAD2VV7agk7qTu9/w++ZW/vDl9zsMzeMs+tvLO5k8Y/CcO8FyULWf66mXIiBrgUJw/cgv8N3/wkT6lAgIEcw/QKRNYUtnZnszipqhDmXZGLZAKczzKIya+8QMLFvY6Gy5nPlLynF9155R2BzwPenNbddxgLxH3r5NI0Q0WYlZlkM6BIq7FGEtHW8+s+eOh2KoS8y92QKIJUkPB4B9bAVt1H26/nB1wvVjOJ4geiLw24u9xMFKFq+51eNFI5RmEfre7kOdGpe+wV3JnD8peYvjo4x6rrDf115kYrrUNHwrdfHq0vEbh65VuovFvpT4Azusj+lJr9q5c2ZlrcRmcyslnQALXYzyEBfO2FsbxIx83S7LrlAuW0Hjl6RSxng7b5xhNjcqZyEdmQXTqHZ68gSWhdXogqKmK9w2a73M+tDdEVtuoTmRRMGwdibPdlwW2kWL94k8ukpRXk5L4kRxlrzFBJVazslCuKCOGpuhFJ/SqucvmLXY1eYlKWpUMVJtnvubc+NxR0fmkk7aFBTZqglsHlUU9o79MRvRgUJoUa8aQ5DndCXGleamCwHrRoKusnPCJBl32YsCLKKRk6DnbeAb1w3nJsTeOWaymoyFOiqKGBwLtNT2PXmTk2gBODGleyy3o9LQg7pR4nTNHAreK+tQDHvrXApjgZkFt6/2Vjo3FrvdONfrpFIJYqMWTmWypSaofHYazi6u156p1sqpVE+XWujdmNRNjqCvTGoUwPDlxYMdZbYe2pNuLlaxJC7KiqVNws5o2Kcvl8JNZvF8ezpwN2q9metlcgphFm+q07W6rYV+qDttdNi+H3rOXit1ii+sDjWrixpK6iGlFXNPjbIdzipnebV6cidoB9rlLDyVy0rp3c4rFmWDL1TCXoJJZzXIqEhQw7BEF4hc9hiR780Sd65ojLWDWNXIaVBFZbQvZ8XQLgsn2p2Xt+WVwdLhfO1dfN4oSZ6uUE4j+h61lFYNRl+SR2NYRMhaY6v+NOBBis32K//U9wfO8PRDbppDmxviDe6Xy3Zx2Ta2djya+8NuG2mkzkVNGq1Ct9wVly1rCqXqooOqN3F6K2OsXp4EAlbqReog26K9GQnM015E3MLMXx2UitAiS5ApnQrS/bGQRkokMFHupOMCi70NH7m1Yneapu3LLrFGM85jbdmcqks49PSy6lJhP4hGJ0UacpUKnDzG60AMdboKlVQjrFnGcjdnQZBsfritV1qYCftKkwKtSmmtk1b4EAlpfpK4jImq2J1FwlpA82hm0Ev6HNrbRLqYuKOue26eOaXYHW6E5V0qq+Uqh1lsCa71vJIFxkoztVNRZRzR657i7KRUPY4SsRGV3K2ZMWKFJH7HiheKFWBnfYPn5I7Ascs+NfnuDO+x1KISqxZKChZXpw7FU8fWTlZ1cpFe4cZrGwgXrdcWQs0i1KrzJVxPQJm6yCZVvctJcpdppKCrCylsTxurRm9LKpAjkpg7fHEo0+g4IriY8ImoLfBE2Yv6IhlOuF9Wl0Sz4/3Wqs9sSM0w18Cz0VBONwtFS6vgFqY7a2K9mp259fEmMo0ReWuUUhFxEV28jOE1PSjmeKpXasKHMgJr+blQqoXJUjQX7fqhFBi3atBZ6XvybCEWfKw3OVMfWMC6helS6YFdKvIi0fpVI53MuM/0Q1wXccOf9tg8P+PwuK1LQmPlcEZzm6wiW2vUi74ZyZPgH86bW3GQlj66VBWO5Q6jMO6vtO0FdUYpBkrlUVlphNrOcHaZ74OjhbCEQB7XG73G3b3HymNXcMvhlh1nVrIhO/W6n51DZNDygt4gnuqRvmQz1Vw8iTZrnRLFiIJ6PPajTNLpnB74wU5atsIoVudUoQ9XZGcUkX1sMonhpc2O21xW3DVMihu8xZqjTPfGtTJEjuU5epvsSCvf3Qz53JznK7IYmJJjTo3Acd0ZPy7SC78PxXIhq9c64OUTbmLZTj6YlkgKLr4giKRfn9bYuBvaFUYWVwzu657ExsPm2F9FfAkjdoH52ajBThw3vWOZPQojbRwHXTVfZI59NGJ2FYyH26lOFQTWV2xkZ+VhLp/lqNgQG2IhoMf93kPJlqBgykEQ+KiQuZ+wcn7d3fyds+C5tV/TYnKolMV+LwmMMZYLjctc2cZTmLrakam0RbuKlhtN33SsQNpcUdkxygUzAo+rWKCtotLx4+oMq13qs76p7oxQMLAOLSp+3W5g1GyqACm5eYRV+/wcj/tYTg8Lmqlx6jh2GpE6XGlF1a7lnBrHCMMOmkNuLYbGT5zT/pbmxm5365yW21u0bNX77KLNiLbpVyEMCCXcx+vrxrzu7BwT983hSuoWN5iEv6NSuO0X3NwYkZWsMKWaF4NZZe1M37YupUuK1EVycbjYhHgctHA1NNetWnPageXF8OLpTprazBEWsX5nzHiuL+ODmxTnIPHoGq+YVhgbkCTeASOGBhRhIvKxXPtshIdVw6Uh0LdWSjutsmO04IrVWpnzRH4oilPIcWW6Vhh/1e0EFBeuvLkgM2vAD8nGKMxcleS55mFqdVZq3PBG51SttytNZQd/ebxZJaHz1qrlddHY6aEwrnd7TzdJW5jFpOqchjXvXBdIPZ4X8Fk+UiVWgEKmtUonC9sbWcorzaIEp8SV387ba65FSuZeGeNK8/PxEpjOvNNnGHeTd7DlzCn6ep7nwzmI2i4vskhaiLndUPaKJhbYhZdyJzmc3RkNG41ZaqVg8VyAutuZtkvq6OysWaOzVBZu+WbvY6Fw2hxlnlojMC41jnotDk2lDKvLUZJXZbvvqzBwqAo0Ak1xt8rV4RcCe0Pm9hJLKE48CLFrxQERrzIiaS5r0T3wI1FI7q3fxi1yu24KN8tRY6B2aumfsLl12/V+3ofM1dghx3ZR7+XLStqe1rWz01ejjiUJf1wjIV2c7JVIqYyjWJSX8ZQSjZcLb4XBCs2kvcwmwlVi1strdgIM2i1L+lo26trxiEuPlluiyitdtCpYOZm6TBlbrHQclNoIxjoYtiSK8KeAUhV1E7iiiQmrbCvNIqd2DmnK1UF/HCV0CPhDiltbL2xjeVkt4nnJZuxpoZqOUOylgSYj/zSrED+RGCEh+CiPx4hNQBHTgsc1aAioHt/aeBRyg7re51a5702BIXBDZHWUMbV1glaZTNZNXdDO0iw2p0ZS7Wsfg/TA1UKDNz0zVm3CzQt1yIXVrBwKV9wzqFfedgqfaEQiZiIWW/MdVqeweqlpZMahttwtGClHde1YYcGww0mL25GIgaK8OeRYxSdnF1l2pxPpXm+sflq6yzpS9t5gwkKRzVkQIhFhzxrON9apWK+usVafEgZnvPIkB06B3+RDqQ+BWwlKXkSVlaf8/Dhb7Ihwk++JIzybuctzk7qCeMO1DJwvRF7pO8vKKj5MvKQpZGbYHrX1TWYsHo2DXdSBCerQ5HtSK+3A36U8b5RbNQrHk5BmgntBF6ahw8fDvNRX+SmW+rQlt0pKWAND25GIGXzSwmswSY6bOpyRcTzNS3w5z8D0FocKxyxH3MXQMfZ6vwCtj5dDcukIlUavV4IfFbqoXKwyMG/MuEnSlhr57SysRZeErx2dyuxWh4nENg+1Q/h6yOXyuAqRKtVSGdkJxNy2QnsJl7qbh1G7RHB6q5+FbOnsVlTvXVItUwBNRgMasut9pBcawu9klHf22y2PU3tnCY4ruWoYahjg5NqIDWdkdtctLHblWRzkq3pQqyFfEjqORUrZjmmwchVYqhC+oevlIcuobHXuCnrtRv0trJfwZlOgO2Ybm0kWGgcGy+qUQcSzxJF5v6+X7WXfNXs0tpvaa3Y05pKu2KnrY9vguLbVdXa+3XBCEHupAAty4y+XHbMIZoAsglVuknvd6443v3Rs8nIdqS3ms7mv6IRXep6EuiRxttS5x64bbUR2N1Yi2nXUsvsMTbGu3jiYLjp4adIl6hDJadMc1qbW7lcz4ri41uNsZXD8oW77dkkEa4LYljc3bQXaMNWeacpFqPrMICDw3tuSRpLL/Li5tDq6aKTgtsyQa4h3HOt3t6V/qDwt0FFe53wjRtyl4Fzoa9qJGHV1R8GF4UYxvEN1mJOlsR/WlXrFiU1mhvPaduxKdIBrGgIjZx3h1qSphSasIQizganN0fWobiTxoKA0Sd+7tIBtZ2u6YQo2MOG9Gtmy54CDo7ey9siSySKOX5cjdU4NNJdPjtuemHARwmueZRcSHhxWBJ+RukI6+HDT5Woxr9t1MOqmt9gp+IE9UDSqXYWtTGGL28GgFkrknlRmLtd5HRBwoGzJ8TzHx+DIblVXtAuWlMJb3QaYoRhIFa1z9jhgxJK+pXZyc81dLCbeIee9W7JBwchyWEdlUGukRS8tN+OiS4g0F5zA0HnaIJUPO47Dmeetjp+9bsOclKN+Xar6imx4zJ6Pomq4Xot2uBHNAxrD87FGLiiF8NF8GbZ6K9J7DDkf8KXdgoNhQ9Y6RlvBakONJeyv5awL51G34axFz2XG6ab6KBdaV2rokZl/khl2HWzqmyotdzhfEsnCK3lzjsmbvM+yjI1lfGeKwlqaH2bujvZDFJsfmJYkxuuiY6PQGODV1lGY27IFDa9euh7i0yIr++WKYNIo6W4jkpIRTa9IoVzduhN/WFK0YhzcbSDKuI4Sg3s+U9iOEtWj3x8cPpOJ7oSsdfZok9TMrpWNHtnuOIvrXholAxy31pi9bDBLok1j32HtWUEiXTCulKMQNda6C1OCcXU7E5ycvK3XRwpb7Y7sChMl1r/2/c7qnHXquC6p41Irel7bE62xGoLLxjy7LkZ17RJwdjsU86JNWkq3mmGzObekFB3YcmTga4NzTGd3q9xjEj+3VvNFg/GMvDtfYfaotC5bmZsrTjEsk+q+xiAFangZelmyFilv5KohMPyyIYa5jXj2+radX3wYnS2JKgUsHTFrpIV94pR7xvpmIyE1miRq6wSqDPDF2l3c+Dj3kf7UN+hw9NTUpPxbpyM4b2474UASLTfXZ6FLg5aouLhcRCuDlEy9JOqMRGfiQWnOsFEps1Gbz1rNd/0+stY5z8teVeGt5xO9xjS7ueQ7UViShEowRStg8CUKm/oWWrFdkophFBTbbK4zDj/mIpsLDJgVjXbHXrV82Cqq3TcD5qq2f7NPbuRKx96qVpdtsZOwY+tQKk/QbEc6bG+fUfx8HDZXke1WvE4zpI4F/OhtDpEQwoW0OFgrc7YQeFH0hbCWBoMSDilVHfTgciHCg3gLzrp/xOQtgiCciu8FXDP2RNWYZMTMWt3x9r4Z2vPdYp008JiYFDg9qyxCg1l/F1+1ZLDxmExo6YyYlq0SWYyy2Ppw63t806ylTWi5NwtUpHRo6BVD+BeGR0p+s7wOwk064oe+YbO5gjh9h2HuvPXa/UCw15mNt6ClaCshWK1ePr1Mt6yfN57/B4+op3t//2u3IB93C98fUt1vO3uW++Wu68v/xMhfPr1UTgRMfNyKrZM2eN6m/IcbsZ//+sOOSd7weDI8PW/rm/e7+o0VTL8J9QJO523dVMNbnSft/ebwpxe7raffw6jfnjfBX+6Op8V0R/3d0ef99rcmf/o6qYqy6QmS50ZW834ZPO9Uf3pxBxBQMM2+zZeLN68qJr+fz06m27nTw5OX3/8fNTDh+4EmAAA= -->
