---
name: "rar-cowork-cookbook-ppt-exec-develop-chart-of-accounts-strategy"
description: "Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy", "rar_sha256": "946735177c1aa2fe1f564bf862467969bbcf083e47455d93cd3cdbd521e64b3a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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

Develop chart of accounts strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 946735177c1aa2fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy',
    "version": '2.0.1',
    "display_name": 'Develop chart of accounts strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c821606c5f0028d9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecDevelopChartOfAccountsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopChartOfAccountsStrategy'
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
    print(PptExecDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfiRpfmX9Fkfyi7qUztW73H54wQIARaEQiByyetJbSANrQiPP7vEwKyym6/b/e4Zz6MckFLxN3vc2+E+O3FbZu4qF6+vFjAzRHJTdMkBhXi5gEiFn1RneFHcfbgH+IXeVMlXtsUVf3y+SUAtV8lZZMUOZwugRxUbgNqOBUBV+C3TdKB1wq4wYAYRQ8qo0jyBgmAf0aKHH52IC1KxI/dqkGKEHF9v2jzpkbqZqQTDfDEbdr6M+SblSloANInTfyYUN8FbNz0nOTRa3mnnBeQ+xsUDFzdcUL98uXnXz6/JPD85ctvL37q1vDWi1E2cyje7MFfHKnpofBkbj15Qyqpm0dweDlA++TwugRVWFQZvBWAEHle/VCDNPyM/Pu/n3u3iuofv3zNkefx9WX82bQ50sQAaQq3bkCA+G7pekmaNMMbIqS9O9RIBZq2yqFGo+ZQnbfHzO+UoJV+Gp/98GDyFoHmh68vRTnaGxr/68uPSFFBflU7nr+NVMoffnxLR6P/8ON3OnXrnYDfjMSg1G/vz+snWTjw+9AkvHP9CVJ9uNkDX1/+oNx4POQe9YQzX95O0Ak/PAiXVdGB3M198MOP/4qsH8NASJO6+T+i+/ODcAyjCer0FPzHz3cj/4JMngp9o/mv2ZbQrX9HEzj8g91n5Gmof0X7bv//QDpNcpgSHxb/p+T+2YTJT8jP/1K3/2zCZyT8+jIDKcy9yvVS8AX57d0y5uLPn4LvNz/98jsk/V+SsYq28u8U3jM3T0JQN+/vP3+q77c//fLzp7aEsQbc7L2t0n9G85/Z9c7nTxZ8jvrhz3Mh/11+zos+R75FOvJbUf6P6vc3xHbTJPh+v/6C/DFfxmOCjEp8MH2Y4A85U0NZ/2DHH19+h0CRQ21a//4YZvm//RuiJn5V1EXYIBaEhwaBDm6SDIzCb+OkRuDvmNsVhJKqTqBhn+Ng/I8eHiWGwPbr//TvQPrqP4EULcvmfYTI9ycIvt8x7b0I3z9A8P0DBH99Q7aQRVElUZK7KbIRDONr7kYAAh5kX1agBlUHgcUbGvAKIel1PEGSHPn1b3B5vxN8K4df77iaPDBrI8ojXtVtCt5GnfcxyJ8a+t9AHiBp4UPBwgQi7mdoi7pIO4h3o33qc5KmSJBU0BhFNdxpQxt+GYn9+uuvnlvHX/MHwJLIo5jUKBzwTRzk9RVqGKZJFDdfc+DHBfLpt98/If8L+c9m3YmPPAyI+E8PQQlXlq4hMOPaDIxlZnQ3hJO7h377/WlnSAaWMQT6MwkT8JgMI/YMgg+jW0vhlaAZxAPQ2NDQWVlUDURtJGneEDlEvskLmY6PRlyPi3osfCXIA5D7A6TqQnW+WRIWLqSGYVmHw2ekrcGd669e5d5FzEa/Nb8iqmjAKlKk8N8o5n0QnFzkCTT/t5B43IdEqk81Mv0g8YZoY4wipVu5ZVy5Tx6h+/ALrB4f0yFxF8lB/zUf6yYYTXVPmId5orHIJ/7Tpa+jz8fqDNEhqD94R89GIEC295pXfc3rZzK41egKHxYHyDRqk2AsEf94hlQdF20a3O0HJR0pPb0QPL1yj8HZf902zD+ajz+2HbOx7fjaEhhOIf+/tCqjPoIkbeaSsJ3PkLm23Rwedh47rdEfj+YMNgsIDLZHTn1vID7g5wOFv+ZpAoOmGv7xGHn3znPMA9naChpzI2zu9GFoQDuPdO+RO0ZiVY0x737NP+D+MwyGO7ZBK8A0h2kwRt8Hw/Hph6QxzOXx+nvpv3u6CkbtYXQiZeulMHJCAALPhXZt4tHeHy6BYQxGy/Zx4sd/0gqB1GG0QPqjKxJoTlgS7qbTCqgmTLywKrLvw5OxoYJSBK0PpYWtLHhD9jCBxiCqYdbCrmgcA63w6U4KyQC0MRTxm4Xr2C0fwozd71NAd/RFkUFv/9EDz4ffQ/4uyyg+pOoGbgNt2Y9oHIDrw7Pf5Hz6CgqbjUl6n/Rndz91Rf5Yl/7xNb/L+K0AwNxPx5L+B+MgMOeyR9SN0FVD+MnAM4BgJNyr99ujAD8q/DdZvvyl5f/h760K7iV192fPfUHipinrLyj6KIMfVfAN5goKYyQpQT1WxNcxE1+fufZ6T53XInz9yLXXj1z7E4uHxb4gf0/MP5F4xvcXBH/D3rDxkZL4YAzg5wGtIr5OD6/U+PRrvgHf3f2MiRGB0wGW4G/l6GMIrElRBaJx8KM81WNV62EhveMxdMjX/FtIPBMGqp5HYy2tiz8k8r0uj5DzcNlH2YCP8gbyDsbeLgLj8icdxa/By5e8TdPPL7mbgb+x7BlLBAxeaJRx0QQTCbZMTQLuV9/ap/Hiz8u/e4pBbAiKL2OmfUbGVhfi4UfX+hn5WEfcV2h5CxdSP48d88gSDoUf38Z+W1t64AUu4JqhHBV4LI7GRu3ZQP9ViDHBoMQ+GMt+8S1jR45/IQJPoghUfyWi30/c9AkbENlHDE+aj2SvoZwBbIk+I9CUMAlhXkG4bOGEv7KBfCpwaWG1DEZ1v9vvu1rFQ5ff72ZoHivM314+4OPpg2c3CYfDPH2tx3qJwnCFDOH1I7Dgs/+bPvNJCmIfbG4gLZ5iWJLGWdbHXZcIAR7SDOWFHEPABzzDe54fYhwJKJai6YAn/QD+egFN4ACOI11I7xGp72N/kIziASwEJI8TcChD0DTF4yzh8oFLsa4bYBzHYmwYwPLwfSqsmMFT54eOo0G/tbyjbZ6q//biMRQcuaRqWXgcIsrbLuso3jV2+BsTHooTV6wss2jZvafmuzxJBjYvzsFpghFnfE4xwupwjtvpfpqwZ/V60Vb6cpgameVUbRgJkaU2hFripTEv5wcn7NgOY3i+XxRD5Bqbo1Okgj3wLqed+0byuQE/biSVwC9evbkMHBsmbn/lzpc+nZQuLk5sRcBZRVkpfN0YBqvnRWxiu60G1FjKtlk35QgcNXeUYst5uOSvpkRQrrGXjkRqLVR5FVisRohE4uTTFDhqOWguUdOLVcyTEabnJMNrDo3xKklT6HFyqMmKZQzi2OLRamaJ6i052Vm1L4tmz1zczHN2iq7aW8Ke3lDR6YGV9cl8TlL9OgtcjszZcpXQqezLu60UDRhvJkeG1x08vzqqPLcvPaY6TSYrSbuy03OjS6kjlM2qGG5rfFGJZr1bV93cvRguu4+wfGlo/LGaVFmJr3YlOBZQzVTDt+XF4JTrSqSza7mZ0kO2sOrhuN3jYHeJN2cMtPhNO7CT01SuKv+c4X102B1xx1+dlesWW+NBvXcbTbtmLh4pLI0Rks/QC2WvEOSx8OwTSI9J7gcYfisM9iBmsicEXVbwbg9qrAquK7sdTvFxOcEjB2XtC9ikh0lITglxG+FXQwfSiaFjfis7LN3nBKrR9EQ0JfoE2r3jdDY9q5ZeGzU5ng4aq1VUssa7btHbBhWcdLkeZNBqYrWapeX+WDWb+cRppzQeWMdI2x0AgaFNBI71TUvtLb5lTsoinNyKZicwhrrbzzv3Ni+C7aBL+FaS9vuYn9Enngy3du4S6sU4oppa1T03aZKjulPn1rwq9oF9dN2dj+uhbeveaqHjuezWGezOmRaNTjM7z0lP7iIzHEiNUG7ManubDSe/n1/dCp1Srb/10EnYlflMpkHisysj6s97B1V2yYa1627NLLLDuZvZl/gAXXo9OJOMIpL1WT1ctWEjnbR4yh3Os9JPdoK0qHCudHayxzENtwxWB1F0zcGepl1urlNm6gSSqS4252KjbjcKkWiEasmpfCTa+X62yXc+ASvUxVApQ8J8S0vJ/qTOqslQpYWUX+fhOZcVKictQuHPlzidd4M1VSZqZ1273WZFLm8uv6DZfJf6C3I4xhXPicQaVyn31vJog0bhtDemEIeUlSHyYk92on1tL4rqi6f+KBGJfVyY/EVfEYOvxSVVOTsxVrs+o9mYYg4DXxrkcokT1HF3SE1Bt/fk0rfLKFajlBeuaMWI2IKmO8oCRwZsjBlEheLCSiI5yU76kDAJXuJ2t827tOn7szUf9AW+ucVjytOSxC0yztubbZAY63WwaLHq0s9lRVF3ElqA0LRjUNS0XWZKziUGujdYyfZ2mUJ4ON+d0z4J/AE9bw258C6XVZheS/JAqeS19K/CkT7YjSzUOnnJjOAYFoQ0X2tzZW7OLCc+6ketUmTPjKf61YDYpa6SWmerpRpjsizk1aSUbsvy2ty4jaaYYDWF0IPTsjOXzo4WHVPV0Yy5TupYJ3bHVaBJtatheWQspvoGBWgaCmgtBSCNT5xXoxdLiHCOTgRfNk6iH5tGyJ8ZjesnyzO2lA5b8zyJ69ixC33PitPsVrMHnOdunqRsdVynT+42v/HsPE0nCynj6X5h2VfH1SXBmqxFc+avDSBL6CTiZMuSVbunsNnUilfy4UI53u6wIEp+j3IB6HNMuFn5YrePyk3V67bdJNaBntz05aKcWjIzUzplZl7tMqD84HqjuEqUUou5cZq+aGht1QZsGJNpfLjkR6mtiQnIjwQKlmQ7X8fW/qw4rDvZWidZDZlg3QTZ1hfFiaWnx2yKohd5UTY3csme19LNozq24VlgyD1gBU73cnQT0s5yiCe7YJtUOEnfmsQUJGV6KreurmJbJ4unrZg5Fn3G4yDTabSO9uRsR2+mvbijF5tQOaO1UQ4Ho0RNHzvw6sHPaFHqtnP7HGuu6y8PK0rM1v78JrD4xRTOjb2COJhG+jrxpJODJwpaQG6Dn8/2yjQQtlfJutE7fCOoEQgPG8kr+9J0IZaaFxWw08GLPK3p1sd04VTNZVdV8RHjZ4DYUqv1MDV7qmJ28WHBOMXt1k6FZpN7SW1IEBYu20C8CmmJoQm1jT3NVo3T4naMPTIjtBnDndWFpDOZXaeWtmA7D6L8NpB3irUOuP2SXl+j6Sa0TprnXbXlVvV4Ma89JlFxCUzdabFBix7Ft5Q7Uw9rs07AgGeuK1tUkJFQhmWpHGZyvG6NRWkSrrmcmedoOkvYrErDhF6VwnRNrthCpVdWLMvYSbgkk75nxJK9woVAquXuQOnXhV86K7PrCQ1kg2snNSbKx7bHOylLEgCxVgmYzj4sPF/aDPxJsNg1F0kxDjumDALJ7TBkHQYyE2VJHTfws65MwLTRzVaC3ieDSsFaKj+37qV0pd50mn2AbRKzCk7nw0lckV6zOfaG73TcZpdpV4tipYYJ5qWxiZSrvcmJ5RQv5UC8GeelT7cBftqwkpWvdWbqqXvuKh4r+Xx2d/PqhlpFehJNIMzOV+90YlualyfZdWbOtuaMJ2K+Tjj9VJ254GTfeknYR1Hdsos8NNvtZQtbj4tYFaEs8DxPoVsNZdzeXGlkY4pUxGI4S202zqzmNbB1ojbwqiV2wVrbY0JHnXSL6womaeUFDDs/guw2F42Tm0yoSRQvDlQfmVoVybVIsItaWdUGHbX+pZ+tI+dEK47CocZlybnctTork6nNGFjpWFgezGLmFFtn+7zYlWtWnW5uHZtdChMkcGWelo6hp+v1qdQG1vZUnBcuh2k0LDgcva6j2ttshXCpu7WJDxv+EO1a0jbnOjg4lzprIs0wi2amzTQ5TlF3C2TgB0qq2b2NHWF5O88mTmqwquQfddjRAZ8gSvUSU+aBbJM8UfyDl6xAxHPU7tyck1Wya1bXFVYHUxkNjchZF3pSKO4OF3U2PyoRVq532Cw4qXyz5uyjki2pBX2i4sAN99mC3h6LzkyrTb5u9klXra1mMdjdUiAoQKzKo8bjzHmFDvVmEh89cdVZ8lbo9ry/V1e3JpYGIzNLZ5GfNI1hIkb0+N3eknBFoxhmu/XsRJ5X7RanLlm4rz3bZilriCJ9tt/I8pxYVPNyA6R54fVxsBIStulh7Ik7k2jPK2WXNv5xTkw4WrpF6U6DQGcx+u3cZMFa76hFvtUZf3s6xbtAa6ZaNbSlOz+bK2atXYTc1NtamFszLVgN8YHaztK1fTuC/X69OkTiIfInsXkj5Yvnt40DZriHG/FutZVYBUIvdbWaozS9xqK3P5Y1q+33irQE4vGsNx561IQdmVf1hKaBOHdvbCBdb5jNXPxVgMtmwzOqWG6SlbA2ktJZ2zt3ac7I+hgN1Z6v1MXJEHVjEm7omXiYJRXqD3xrVkudxClrPVd7OWRo+gD7VSJl/UZo+HBjdJhBX9r2IsQ2LtJoPo2M0DnLtosFBCjEZn/t7ZrHSvR8UsUtKV43x0veeMXuaAoxcxMKaTocxG7VC6bcKDPWk/GZepYxxXYpzPXacHu4UofzfHYxmiI42N2OEdi2G4LpVkhl/CrDwHP2vR8aBWY1MzHhVtc+m8enDUlb4uDE0tGO4OIntItjm3TDAovzTZ9NnJKmdl3n+tw6qS4Vvduk812s5Bdjn1f5pSticR2D62TXNTFoYqy+KbhIiqhIURxDOyesi0u+xo1pT+FBC1dWARn3ROCiC+92WNq9ak9o/2Jie752JWboBzGxcrI6C64PyliDhVNR2lPisepkStEyfeVvHLncWYbjGbZ3xjcHYb6bH9eVvnOwWI9atOFEnjIXhOJOFbXMOCIVlsNlIvfmPjp1Annr9Ny0IwdfOXP0cEaDwvX34onoVYKvgq718NgdMC6Qjh29x5yzQGTLK7nUuWV7yDhyL/PLvCRRrtOMibAM1tXUmtx4dHGb8LhxBDx9Y7n4EpwnTKovlkeLEMLsop8GlV+wV4hh1Urb6htXCeuVszP3M+fELCzOjSKfYv1odboteVFcG4OHb4LpsDWY9kTReOq36f7WBf5MnzZMs9ZO0cEIbtNKcSI9vl14VE3ZmNWorRDcZNI6HEOTXOg7b6CwblqLfCuQgWmwpKucOjW6KIpcdF68pIImbVBsNvFam0/roznbe4wokBxc5LCzTa8y++i6pC9KecKZ66IIWbvV+TJIZZQh0XxxuSqw351Qp73gJsOUJiYZjhmKFWSwj5sTS9gb+Lokt4fI29s3/7bHeVZJSOLU5vl0arPgsgZ6Bmvvie9Sn+i3u4MYtoFzc9X55HgNlUSZe65kBRudQ7vDacHMSMWh3HZuyvpNWQ60RKpeEQfASwdYMEEpGCfFUynusohaaxKdArJam1e4kKtvR7imuHiqkQv+Gj+tGAvcZglZYSapDX7HT5Zq2Ar8fmovKouYTGTPSSPMXMRttD5NJZz1KGUR3dQ6viySG88bl8UsiKvb/MZOZFgqYQEbWBCEOp9fyX7j1atOI255UdLZUUqwHbrWalLNa/+iUqZT1VxfccUeDEuGODmrk88y3JGnzmvZJ00802fhlJjVQBLrwlTRvInURcKc6gnDdyyBZooPoN3XvhIXtT4ULr31ph4JQBjK+T5jAHsN1nhxYBrc3W8ThhByLOimQib4QpKyG3tYFlMnyVVrLXCn5WTn58Nlag/h7MaYa6XOJsWxA7c+1KAHZY0ypZj0WCuaaMxA7jnzpjUpug3UgKEUsm+iCI37Gwqc2ZkD2Kb2JownORnbhLUjkRdYQNk2lm4oK9Ve4JJ4ScAVM2yAUM6vAWfPQEOKnrNrQlYSuE1AbcpEcLnFpoT4qE5cnl7KwyX0NwVzvLBErnc1yZGagM3PlLLDOccwmrpK9JPTR6Rc+J2GTdaux+7IhD00jYfJ5ezQJYuZbURo4e9Pyyk/jYKVGUF0acyCc6cz2WYyLEqZJeAr3WnyejepFruZECuHpYmmM9rIfQHMYi5caOE+FtCVzvW+ILSEmScMNnUPPV1v7DCXfbyxVEa4TYm9FZkTm93PrIhWYCNa6EwuL694KsE+y7uZLDXhQSCswkW+UXzYBGUmcR2YbQlY1fCpjFL23RmuYc6rDab1isgrZukThybTLh1tRviMT67+wNJsNTGnt0nrCD41bf1qW7CyPTuJmyC+ij2GAoMSeWtXHldUiWcdHVz55ZzU6uBq6Q3RYn7bH+gl2ttciWFrbjgLgvDTTy+fX8aN6+f283/nZfS4Efj/bD/ysXX48XLqvvkM3ODLndeX/5Z0v3x+qfwEyvbYia3TNnpuVv6HfdjXv/F2YyQ0PN76jm/Wrs3HNn7jRuMXml6SPGjh4OG9LtL2vin8+cVr6/FbFfX7c/P75a5qVo476R+qjRu89/cL703x/ng1/TJ+52F8WQSCBDJ/XkbPLerPL8EAnZf49TvJ0O+gKkeNn29LoKLEG/aGv/z+vwEiQe5bQiYAAA== -->
