---
name: "rar-cowork-cookbook-adaptive-card-develop-financial-period-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_financial_period_strategy", "rar_sha256": "849e19dcd80e3aa4812464e8fb04cd76ea3400500014ad87ce58bf116fb1580f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_financial_period_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_financial_period_strategy_agent.py` and in the RCI capsule.

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

Develop financial period strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 849e19dcd80e3aa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_financial_period_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_financial_period_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_financial_period_strategy',
    "version": '2.0.0',
    "display_name": 'Develop financial period strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '264ce1edbd9bb07c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDevelopFinancialPeriodStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFinancialPeriodStrategy'
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
    print(AdaptiveCardDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejxpbtX9HL/mC7qUpAIEB1112rEaABEBoYJZdXmiEYxDwJgZ//+wskZZarfW/3c3d/aFVlphARJ86494lAv73YbRPm1cuXFxXY2WRlJ0kUgmpiZ96Ey7u8iuGfPHbgz8TNs6aKnLbJq/rl04sHareKiibKMzh9X+Ve64J6Yk8q0Na2k4AJ69nw9hVMOLvyJqK6UyZ1Zhd1mDeT3J944AqSvJj4UWZnbmQnkwJUUe5N6qayGxD08I3dtPXEz6sJSB3geVEWTKJs4tl16ORQaP0J3rCjBP6FYzRgp/UrVA3c7LRIQP3y5edfPr1E8P3Ll99e3MSu4Ucv72qNWvEPHZbvKuzvGqhPBaCoxM4COKfooZsyeA1VhOqk8CMP+JPn1Y81SPxPk3/917izq6D+6cvXbPJ8fX0Z/x3bbNKEYNLkdt0Ab+Lahe1ESdT0rxM26ey+hl5r2iob/QfNh3a+PmZ+kwQ99ffx3o+PRV4D0Pz49SWHKthjDL6+/DT64OtL1Y7vX0cpxY8/vSZ5B6off/omp26dC3CbURjU+vXtef0UCwd+Gxr591X/DqU+ou2Ary9/MG58PfQe7YQzX14veZT9+BBcVPkVjH4FP/70z8S6IXDjJKqb/y+5Pz8Eh8D2oE1PxX/6dHfyLxPkadCHzH++bAHD+lcsgcPfl/s0eTrqn8m++//fiU6iDJbGu8f/obh/NAH5++Tnf2rbfzTh08T/+sKDBGZ5NZbil8lvb+pe4H7+wfv24Q+//A5F/6di1Lyt3LuEt9TOIh/Uzdvbzz/U949/+OXnH9oC5hosvbe2Sv6RzH/k1/s633nwOerH7+fC9fUszvIum3xk+uS3vPg/1e+vE8NOIu/b5/WXyR/rZXwhk9GI90UfLvhDzdRQ1z/48aeX3yFaZNCa1r3fhlX+L/8y2UZulde530xUN2+bCQxwE6VgVF4Lo3oC/4+1XUEoqepoBL7HOJj/Y4RHjSHa/fpv7h1PP7tPPEXtJw69uRCI3p5o+PaBhm8PNHx7R8NfXycaXCavogAOSSZHdr//mtkByJpRhaICNaiuEFycvgGfISx9Ht+McPnrX1zp7S70teh/vfNA9MCuI7cZcatuE/A62m6GIHta6kLqADfgtnC9JHehcn4E4fcT9EmdJ5AAmtFPdRwlycSLKuiUvOrvsqEvv4zCfv31VweC+tfsAbTE5MEtNQoHfKgz+fwZWuknURA2XzPghvnkh99+/2Hyfyf/0ay78HGNPYT/Z6Sghnc6gpXXpnAYDCIMO4SVe6R++/3paygmg2QI4xr5EXhMhpkbA+/d8eqa/TydURMHQIdDZ6dFXjV3lmpeJxt/8qEvXHS8NeJ7mNcNJL8CZB7I3B5KtaE5H57MIDvWMD1rv/80aWtwX/VXp7LvKqYQAuzm18mW20M2yRP4a1TzPghOzrMIuv8jLR6fQyHVD/Vk8S7idaKMuTop7Mouwsp+ruHbj7hAFnmfDoXbkwx0X7ORRMHoqnvhPNwDB0HPuM+Qfh5jDpuEFKKEV7+vfR9jj5yn3bmv+prVz6KwqzEULiQJuGjQRt5IFX97phRsEtrEu/sPajpKekbBe0blnoP8f9pCqI8W4vtW5Gs7xXBy8r+nZxltYVero7BiNYGfCIp2PD18PDZdYywefRpsGO6S7/X0rYl4h6B3JP6aJRFMmKr/22PkPTLPMQ90ayvoyCN7vMuHaQF9PMq9Z+2YhVU15rv9NXuH/E/QSXd8g4GDJQ5LYMy89wXHu++ahtDQ8fob/d+jDL0J8wJm5qRonQRmjQ+A59huDLWqxsp7BgWmMBg93YWRG35n1QRKh5kC5U+gEhGsJUgLd9cpOTQTutmv8vTb8GhsqopHjL0J7GrB68SExTMmUA0rFnZG4xjohR/uoiYpgD6GKn54uA7t4qHM2Ag/FbTHWOQpjPYfI/C8+S3d77qM6kOpEH8b6MtuRGMP3B6R/dDzGSuobDoW6H3S9+F+2jr5Izf97Wt21/GDAGDdJ/cU/uacCay3tL4D7QhbNYSeFDwTCGbCncFfHyT8YPkPXb78qfv/8a9tEO60qn8fuS+TsGmK+guKPqjwnQlfIWigMEeiAtQfrPh55KrPz3r7/FFvnx/19vm93r5b5uG1L5O/pup3Ip45/mWCv2Kv2HhLjlwwJvHzBT3DfV6cPpPj3a/ZEXwL+TMvRgROekjDH3T0PgRyUlCBYBz8oKd6ZLUOEukdj2FQvmYfafEsGgj3WTByaZ3/oZjvvAyD/IjhB23AW1kD1/bGHi8A414oGdWvwcuXrE2STy+ZnYK/ugcaeQJmMfTMuI2CFQVj0ETgfvXRS40X328J77UGQcLLv4wl92ky9r2fJh8t7KfJ+6bivmfLWrir+nlsn8cl4VD452Psx37TAS9wS9f0xWjFY6c0dm3PbvrPSoyVBjWGKF+PuryX7rjin4TAN0EAqj8L2d3f2MkTPyDEj0weNe9VX0M9PdgXQWS/jtUICwziZgsn/HkZuE4FyhZSpjea+81/38zKH7b8fndD89hu/vbyjiPPGDxbSzgcFuzneiRNFOYsXBBeP7IL3vvvNp1PcRAIYZcD5THkHOBzz/UYDBC2TTL4lKRIwPgORroeTQGbIDFshmHQLbbH0C6YMY6P45Tv4DMG86G8R8q+jY1CNKo4tW2XcWmc9Oa0TbmAwBzCBfgU92gCYLM54TMMIKG3PqbGEEWfdj/sHJ360f+O/nma/9uLQ5Fw5JqsN+zjxaFzw6Yt2bmF1nyg/NPmwuSiesyLaUwVoNktl8mUOMXeBTlMY1wge1Y8xWG7MBeBrK5OeFon/IzNBpEnCDrYCIdluSNAsiWJZcR50RwM6H5v+eKGDVfaXMX7uAuTS2kBW0zEoDDsYiuZM7PXy7ZppTA2jOYW12WENZ6UbfN+6aAIumlI41xiWnEw9EItm4u8w1e8se8pxFeTWg5aWin0Tp2tkPmgVVrS2noZKpUi6rO+Dd3ZUmpJUgmVXLTiyCMNpIaRiW+5fcHcdDgjXjZgMwB/Hc/93M8Ixo8arxKPkmb05TWU+qpRE7wxzRluFE7shtztUl7OaNR0rUQFi81BYQrM2hY9wgSNtSpPs7MXHM647tmJ6lqzfmilZEgs8ZTpRtS6xkIEiViCrXKRLXVqVtzxhlV6WWkq2cf4LfSmlk0iYZMjrn1s5OvRTNullWw6ZycGqpdkOd1dN+SQnaJET+M67q/5go3blZyJSysjz+VU81wGsG6WJOlBliS2Qtc7rZvqVx70vDsDyRR0ZjcX1aVK9aURVXpuRS1t1sdllhm1uiGCaRP4yWUZHaZcNVOOFH6hjdzUQkWzqmUZX29XJQ+vOHLFzqUV7PnbPjtKseJqorE89x67u86ohKJ6+Uy1gGd787iQY1kdEIaI5dprV9wUmV4EUKcGckwuGWW6Dt3uuU1pmGS9OxbZbOmZ1RZfIdZtMRNwD+YMEBCJ86edkZ4araNssMq2BjnMb560jOWCDjmWQGtXC4WgIEtzRxaOto732d4vh/SU4EZ4JvbnILlq+x7Z8itnpYnckql2BYfgkrZpM7+S0so2FMs0FBMrS6KV3Hno+mIUWYcYyRA/OvlB4G9YgkBCQXdoao/yEuVrFU15PrmzcmuHcbShLGBWTjexsxApvZUuTZXEx75RKyMKz+s1xzjLpI0Vg77obLUqBWxl3QbRbE/VQue6ItkNZ5Ze4rm+27jzIRD5ZUkPHKYmrkGRByxg892mjIqkvKh8Zzb9tt9UvLhKY3MQjENfSqf6kg/m4rYl9o3rhBq4VPP+dM6nrllcBHxZb0LEKTe4MlttNMURzoDIQNlrvYuKFTMMRlNfYiWtdshwOTilXswIBcWuzP7Cu1J7PcSERtaH83WeGLczLZMuiy3KUlaVapuUdeYyAtiRTb2o7X4XrLf9dM52qJOXkt8Wy0tIketNXQqdYGluKnvCLMiNjXKaXX2D5t1stmgFNfKmu2hvoWShp/rNyi5LIZN2kuPFZurtSzRyzHAzPRaG6fC05Bv7DCibWlJMxyx86RiVqBjUlqMH8sJZCPLi6Kyz25LTWrnwTLGkZFZGp8K0Ol/lck1iFgCSouf5rlhHbSCtCv9QNYzh29icjAvBspJwxYQct269uumNHUadtGQp9EdD0Onj+ZwMlcxZuaa380oQfRvvU12hjSxuhWVQdegaIhmTtbDAfMo7zMrEQ0kUxzUQb5nWZ/uq2to7Yc4pg4fvg6xO0nmeYT63rddnB/fD07xmA29PUfyu6+iSkaTtScGoYTBZv2XnvbeQfTXcScecYmNksdZAxbrHkhfXmSMYsj9j6YLyIwphlny7jDRskFa+FSGgPawMX5uf47MmTAHcwW+ONqccjBXLznRnqXAoZp7sVb2Mzjs9YOOzWkYimnYq7vjedXVaX7YdFrL+sjh6eH6VsgUj9DdRC4ftkd3t+mFhLofMtk+bXjhW0nQzo+tjv1CX+MCvMFYGxo12zraKruohGJjTrc4sArKHVs9c8xxQMmeyuNPcmCwxjzpTEuJgnvddLrgbSskGv+rEDsIxUgtNwHiEvENQTjzyzFLBaFRgTltUHGZHVLKDo7kHiAN3Kuyi705znWz4tHT7ehPwRk8ZOyoYWGU+X0+xPlIHV1xiq6q1AnGe10RKl1Eu2DHQPTfwZL2RbstZlB6AXm1oGcJSvNBXyf68dXRlQVga5Lv5jGOonopm62WHqzer1GI8iYuAqmZsiDGbgOt4sUYhS9QSvoqOOr5WRea4UG5VjeOOE3BNjleV7XJ42lCeCfwQ2S6Pi5LUcbpwdltHJj2xi4LpqZ8xZHBbL+xBIgqs0wpC0Sj0usBlsV3Xfqeu7CUnLZLzrei3NB2gR0LX3A0maUGK9HMmOR221WmmD9xe83p+Y1gJIZ4VO5tzJ8Y5LWuj3V5X66KMpSAD3DIvs7ZSjWYrIOCShheAS5UrbEKF1b1tSN6qy0mo3AW96u12Rok+DQQ5hFTlned8otwOy8U8OLsiwlsbiYC0GMaZ6lVyhxonhUO4YrqI8JFDSyXlTczmTm28vhnb/XLIxbnjzE9p3m9jOwzWQMi2HBm6NOKczG0qRSu2VpmOWa696/a2mi32lWODrS3ATZXvKy3qmhhFmmlhns+cH6G4ZxYqFOtcDvYBRBBt5QMoZZ9UG87pw+Lm+Ri1UcFF0ZzjwjQAu6LSKNlW2Px4bpOzaUrqSYdFLtcKc7MrXYyj6KKejMXBM896I0CADvRUhi0g3fjqOslVjC23LOrs0TrFpAvhatT0EscwEVkuEnzer/n0fJrhorPEjJXS6XoOUMS/yrY1BB0mHfFS5dtO0pojvomPU1TNMnVFWZFcGXMvtQ709ZxAoNtlOpLM28FrOGxw+sW6a86ATrtksWExY7O6daLL8y1uST1YkJFyiKeso3OYf7zZ7aDPyuhWbQTEbLuyipf5ski0Nuzm7C1RDzteqkM3U3OBaAg7lw7U1Lhmc4WWCrfIUWnultbq6h/KFXtyQ9/zezPfrzA9X9/6VBGj27wLJMuJUnW9qwedcmuSPeA1lxwu6+M6IMSN4iMxUW5SyyRg+7cuKqVbRS1Q+4Qhb+ii16/LlVk6UqCo21uDGczZknZ6lSonmIrFSuBF5dQqR4HYJvxpiero8rjK+/h8xEl64wgzfaakXn0+3iBfFuRUcfeddF3j3C2mz4k320F4y1X6JAt4Y1jVNi5xMBvE2/oM2Q9m6hWbJYcrzivTrdjUW9JDtiXDm92qQYXgJkLmXN7WMWeu9ivy0uQzVI+T5eyytndtgklzJ+ZENK5gL0ygEildFHR1sDo5qiOnJzVXvSQbwZFsLHeXm4u2o7Q00J2NlhcRXQbJ8ipvZ8QQXISFlhFgvVMki9hdQBbtWkP39uLtdrZ3l1VA3EgdKSU1WBhlU2BZwFUxNaTYGUwDahe0hV60y8Le5YnJniW2jVZJVvo6fj47RMs3TncN9Q21IiPNV8nBbcR0UR+59VZLW2STy7RDcQXCUoJoUPrUF9L9pV6iosQdRNwib43oy3A3fcDxuRpoN0xobHmW4ZKfJsbWcR3ztKq5KhmG8IAB8pYsh4W/Fwj2JOyvidXo0wLi2Bmb5oujwRwczjSPpsTRFGNrPkWXDjhdI/zIo8HJ8He2lXck3GGdV2fT24KMkkq8tS+HlT+XOjPIg7qGLU3XDjBPVt0lCrZrVsy5Wx6EWb6dStg5MXKxC9dTN7XwtPcqxF7Ia+GypAJquj8YFkkGYHpirNohhWLRLtihSz1ncaOQC7fZylE1OOvFSV3t12AqreL2dFZM3pKP1/RYawrR53PncAklxOaXM3K3bjG7RBDzcGQxIcH4jFYb2HbhQSGmwWKOXWeLK3Ggp7OYvNJXJ2TMueVpN8qgEIS2rH52pdq96aj+MCW99goEg55aPbXaEY3lbHZKZkEkOfVHLjVKcHND2mrKwjp4tnbpOvOILowNaxjqDFC8szaiPeHwxjomZh3kCUvIlGwt0ofqYKFTJvS5jc3ugG5k6RzR+I0zlOimO21vl2tO4PuMSOxOnmbW2j/FvtkTuzV/IA6Cj+AtmaxQ2wyYfTDPzsDx5H5RyReS5q3apoldnVEo7ATRo++j8dnHVvS27TG08f2bN9/5fpsDZDb3Tluxz5wy4y7N0mAPh7l4JBUvCoMEs65sJ9DRMSJQThEFgaVniOzs7C0rLnaEzB36Dg3q8MKlzGG9cfUBkfNW9hR5TuwQg9qw7hJPnZbImTW/zrgm0bujvgIWTveXNbcdJNgRxbwsk9I8H2h/G6vMWpAp0qZsbr5CF4xyS7DVLdovUXfjL2dTHLc2FkIw0WxP4roYXvMTi3YhTdf8mh3OJ16AVrXm3iLraXhpAEnvcCJt0Mq/uaYt1OWionuFXJTyZk0PjHwJAFJTDU1HYi3VfnPY7zY5zV5bWXJW+yanh5NHFQ5Oamx/a/BhLVQIapP6QPPbg5AgUubsD4xJXpRbe+iFdmMs6WKrc4Wg1cdofkLb6pyVQsAqlSlSCMfoDaN2VwNjGLh1xk78bbhwO5+re441iejkeoG5lfxCS/bXbev6gGUw2KJ16jXaGLQOwblcdAyCDt32gLr8/LSEHRjRaLXjruNjdxCDpuPwBanMzqfdkg0ZvTOMC+rEAk6Y+Ea7DlSPsHFu1SJawX2LY3rT5VQKnVC5ioim5ekscZcRphPSvNid96o4Uu51n6PdehbU80bB8b0vOibqt0LjcuvVrgpcGd25C7B2GVc5dYGMeFO2m8r5XiM0d4EsZhciPtfe1GVnJ3nRlHuvg+6itsPBPxtE1WTeDDXnPc/rrYNHO7mqRauimZizlY7VM2VnbZDLhRGJJSTx8oayWY7uLkZ9uTEgmIeOfC1bHzud3AwHlGAiB17PrkR/PG2J+dVEMXpxVQgTPUPAywil6TRhw6Mug06bA4PxSA1RhcpClaKRZEqTWm6tpgfCQ/fr9XY3Q6ibsN9fp+QCRRN8QLncuV0FzQEqjuKQCFfEcZVuFtcOX0Z4268HC+3IdGnRkbJWFctfGj0/TfyLh/GHgyYUKnFzUdRSrxtTzG1kxvEJ3mfpgXDTdm723R4nulCVFbBhNjoy9EFHCd6a4dja3gon89xGvELs5MNFx6ao44YJNkVoXL+u9yad1kagcMKVp9b0xj9jVHDE3P2FzKsWE+mZQqR8zC6rkAdydVCKCx/elgZywqktFZ8xMeW3dbYI58WUnEt83NCiGdC2G6Br83Deexlwdwh/tbKOsxYOoWa83xX5vnZTgyKiGw+1QgZiw1xahAnaXdhyJwsxBTklVlHSaKgkCLlfWsNapcCUzlhmKJpgv2ctWw4Ya2fhi6jYJbtww3nXfCoAcXXc5Uy0HjTEr2F7OB+89cZTHMfL9tnZ8C4Dxd9kE4L4SgpY9uXTy3hq/Tx7/q8+jR4PAP/HziEfR4bvT6juB8/A9r7c1/ryX9bwl08vlRtB/R4nsXXSBs+Dyn93Dvv5Lz7mGIX1j8e/42O2W/N+nt/Ywfg1p5co81o4uH+r86S9Hwx/enHaevyaRf32PAB/uZucFuNp+ncmjqe896cNb03+9nhQ/TJ+E2J8fAS8CGrwvAyeZ9WfXrweRjNy6zeCmr2BqhhNfz47Gc90x4cnL7//P3WqgLtfJgAA -->
