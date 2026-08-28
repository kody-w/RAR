---
name: "rar-cowork-cookbook-scheduled-brief-analyze-cash-flow"
description: "Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_cash_flow", "rar_sha256": "5cad100794689bb9a0ff2a8f979a2ad257c0014d3f56f73a6777410bc6fac048", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_cash_flow_agent.py` and in the RCI capsule.

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

Analyze cash flow Scheduled Email Brief — Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 5cad100794689bb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_cash_flow_agent.py` first:

```bash
python3 scheduled_brief_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_cash_flow_agent.py   # or on stdin
python3 scheduled_brief_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Scheduled Email Brief — Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_cash_flow',
    "version": '2.0.0',
    "display_name": 'Analyze cash flow Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d5af45add3c1286',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAnalyzeCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeCashFlow'
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
    print(ScheduledBriefAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOi2Jb/v8Lk/FDVQ1WyClgvOmJEEUVZFASxq6Oa5bLIvonY3/7fvxc1s7pfvzfvdcREjFUZKXDu2c/nnHvJX1+cro2K+uXLiw6cHBGdNI0jUCNO7iPzoi/qBP4qEhf+IF6Rt3Xsdm1RNy+fXnzQeHVctnGRj8u9CPhd6rgpQLKizuM8/OzWMQgQkDlxijRdljl1fIP3IXMnHW4A8ZwmQoK06JGgqJE2AkgNmrLIm3jkUvQ5qP+GQDFxmAMfaQuk7nLEh9wGBNL3ACTp8Ao1AVcnK1PQvHz56edPLzH8/vLl1xcvdZrmu2bA50d1Zg/Zcyh6CSXD1amTh5CsHKAjcnhdghqqk8FbPtT+efWxAWnwCfmv/0p6pw6bH758zZHn5+vL+G8PVRstaAunaaG2nlM6bpzG7fCKzNLeGRpoXNvVeYM4SAP9mIevj5XfORUl8uP47ONDyGsI2o9fXwqogjN6+evLD6PdX1+gG+D315FL+fGHV2gGqD/+8J1P07ln4LUjM6j167fn9ZMtJPxOGgd3qT9Cro94uuDry++MGz8PvUc74cqX13MR5x8fjMu6uIDcyT3w8Yd/xhZ630vSuGn/Lb4/PRhHwPGhTU/Ff/h0d/LPCPo06J3nPxdbwrD+FUsg+Zu4T8jTUf+M993/f8c6jXPQvHv8H7L7RwvQH5Gf/qlt/9OCT0jw9WUB0vgCswOWyxfk12+6Jsx/+uB/v/nh598g63/JRi+62rtz+JY5eRyApv327acPzf32h59/+tCVMNeAk33r6vQf8fxHfr3L+YMHn1Qf/7gWyj/kSQ6rHXnPdOTXovyP+rdXxHTS2P9+v/mC/L5exg+KjEa8CX244Hc100Bdf+fHH15+gwCRQ2s67/4YVvl//icix15dNEXQIrpXdO2IM22cgVF5I4obBP5/oBP06wOcHnQw/8cIjxoXAfLLf3t3xPzsPRETa96g59sdCr89ge/bCHzfRuD75RUxIOOijsMYPkP2M037mjshyNtRaAnxENQXCCfu0ILPEIg+j1+QOEd++Ze8v93ZvJbDL3c0jx/4tJ+vR2xq4MrX0T4rAvnTGg82AHAFXgclpIUH1QliiKqfRlQu0gvEttEXTRKnKeLHNTS8qIc7b+ivLyOzX375xYXiv+YPMKWQR4doMEjwrg7y+TO0K0jjMGq/5sCLCuTDr799QP4f8j+tujMfZWgQ1Z/RgBpKuqogsLq6DJLBQMHQQui4R+PX357ehWxgJ0Fg7OIgBo/FMDsT4L+5Wl/NPpMTBnEBdDF0b1YWdTt2qrh9RdYB8q4vFDo+GjE8KpoWNqcS5D7IvQFydaA5757MixZpYAo2wfAJ6Rpwl/qLWzt3FTNY5k77CyLPNdgxivStuY1EcHGRx9D974nwuA+Z1B8ahH9j8YooYz4ipVM7ZVQ7TxmB84gL7BRvyyFzB8lB/zUfeyMYXXUvjod7IBH0jPcM6ecx5rDVw26d+82b7DuNM/Y1497f6q9580x8px5D4cFGAIWGXeyP7eBvz5RqoqJL/bv/wKPDP6PgP6Nyz8HZn+aB956NCPfp4d66ka8diRM08n82atx1FcW9IM4MYYEIirG3Hz4cR6PR149pCjb9pxhYL98HgTcYeUPTr3kaw4Soh789KO+ef9I8EKqroTL72f7OH4Yd+nDke8/KMcvqesxn52v+BtufYKDvGAUDA0s4edjyJnB8+qZpBB0yXn9v4fco1v5Y0DDzkLJzU5gVAQC+63gJ1KoeK+sZA5iiYKyyPoq96A9WIZA7zATIH4FKxLBWoHfvrlMKaCaMSVAX2XfyeByMoBZ+50Ft4ewJXhELFscYgQZW5BgzSAO98OHOCskA9DFU8d3DTeSUD2XGcfWpoDPGoshgzv4+As+H39P5rsuoPuTq+E4LfdmP+OqD6yOy73o+YwWVzcYCvC/6Y7iftiK/7y9/+5rfdXyHdFjXj8z97hwE1lPW3IF0hKUGQksG3vP00YVfH4300anfdfnypxn9418b4++t8fDHyH1BorYtmy8Y9mhnb93sFYICBnMkLkHzvbM9Ku/zs84+j3X2eayzPzB++OkL8teU+wOLZ1Z/QYhX/BUfH21jD4xp+/xAX8w/8/Znenz6Nd+D70F+ZsKIqbCe3eG9wbyRwC4T1iAciR8Npxn7VA9b4x1hYRi+5u+J8CwTCOB5OHbHpvhd+d47LQzrI2rvjQA+ylso2x8nsxCMm5Z0VL8BL1/yLk0/veROBv6NzcoI9jBVoTPGLQ4sGzjotDG4X70PPePFH3dn94KCSOAXX8a6+oSMA+on5H3W/IS8Tf/3/VTewe3PT+OcO4qEpPDXO+371s8FL3C71Q7lqPhjSzOOV8+x989KjOUENfbA2MCL9/ocJf6JCfwShqD+MxP1/sVJnyDRtM7YjuP2rbTfEvMTAkMHSw5WEQTHDi74sxgopwZVB/ueP5r73X/fzSoetvx2d0P72Bf++vIGFs8YPGdASA6r8nMzdj4MpikUCK8fCQWf/fXp8MkA4hscTiCHief4BI6zU5rhpq47dfAgIB0umLJTh3R8csJ6OPSBTwUTJmAph2FZliZw12PgUIDTHOT3yMtvY3+PR6VIx/E4j4WLpqzDeIDCXcoDBEn4LAXwyZQKOA7Q0D/vSxMIjk9LH5aNbnwfVEePPA3+9cVlaEi5opv17PGZY1PTwWjWvUYr9Iij11OA7Y56uT9H8ioy+2Nn3tTKFpKFNVA7MFvfJMnTT925mw3H6TKZrJT5auC1TA9qhZ1PpEOwPemmcFA8hjzXDaveGuxySbNKjzdSBNKtZmObyVLqrse6b4f1cppaE4uMvFwkErbY5VCf2rMuGFakZznGD6KUM+nmmFH5pqDLnMwdKmGPqOihS03asEptFm1SH4bUyVqpSjKp1Ql7uqyrG0iV+Co7UqdPlgsynYRYQegEd0DzpO8ul3OM+ofjckAvWuQfj+yUw1K8OSbS4dSUYmqTO9eVidZiySBS2sbi0gNB7WTsKqKsY7pWkfoTZV6yVjOlMf+6tcRVTm+ken/Cp+5uouVL72pf4ESSNG4lXV1ZDLPGI3fFhPRSvZ6Y7SnZbAimIslSj2UlI1Q8sM+Js8jTxg4p5uJcFCd1t/LAV6fqqNqbCcTHU2OpkVKXAdSzDXbzvTS0OVHqcODcWgyptg3IBX/m1XhO7tYbRnZ00xKHuqdUHkcbh9VqCVWT1tui4NTyN4asTH1AKa8SWXGyrJrIyNba2SCyHTnPbaWc4lENzTVSxVhRCvTwcJnm0j4kWyOWXR5oEQDMYb3BI6NzhuQku9aWkon9JR8ONMZe+yI+zarcbFQKtFqsHNWjMWcD4xpRQBdr+Qa2xGBPI3t/dkoqDQdF88p6w56ykq3CduO0cm/V80Cca5Sz2cpWSjsKEHPVpyuOBswy2bjsbBnVpE3n5w0weqvyep2ktHUgBxE7ceKMMsyVM7FEnZM1raabW7MswvVRz9hmLmhHm1WCg6tsHC1Ll8tF500EHVu5Jt9uOF7kljwmLtD1StRS/UQXMaGh/Epn85zCKewaLxIUVD5DUJfYcVncYpY3p/b9o70/xfogk5kZdU6+na/c5a0VvNC+VqcES/I8KDmVNB1LJM2ck5tQRxN6IlD5dhFPtgJ+3q7dDZ9ecrFbk564Fo5Sk+jeWZP4pXZVSWERifvD0RusoipSmJ0n6mCpKwH3UDWl5plsnKfEuUxWN8wAuhK6ceCLu3ayHvjW2HIrN7F3nCR04oTNSFNfUbp/jjRbpCyG8SyXKrBrcuApwuu3QnUZYNVcStGNr9ZlUsz5ZUEHk6l9YPf4RU1lQ9GsWQ5aw+YPYsDkJyymq2vNKNp6qR22u2pRlgutW6y6WOdSKhUz4Ri0XChecBHdT1BcShXtUicHZ1vBKXoAmWVfbisiT2jSUrQSM+V67jP6Pm5QzR9agqhT271aGntw/IQ4oKdabdGaM4d8djxlkd8ubsxS3vTCoaq9iWcme5SJsKVCEJNYPmiX3E66w2muLLhQmMxOvmnCuKvMJNdy2fIsrtltSVywhC4Lidacotlmhe5v5G1DR2I9IeVWsZa3jD/RrKG4K211oNmNOh0G2+TTaUljtdQRTh94mGwYB804GBPljILllY+WNzo7uSa1u66a3t+GBTkH173bRT7gBKJUa4qlStBrlB4kC0qL+pBvuEqfFW1DMzN7r53nXiSup9PE0Zq+zpOLmNmLgD8c6Ii75SUlzY5X75iU2qVVbV5RJ9wtWS3MQDs2J3ngNu0pr6fT4XA9MhKYKawcRpwsmUx0vU3EfajHZ3Kb2Phith/0PhKuYrHd+WeLqaad6u8MZ7aqdTjv7kUx53t8ICRqfzMjT11BatOvLOAsG2OVgFtYX4xdAEicX2fs9rhV+ZqG0Owd85A4mE622vMnguBQcBuYrjmaw06fyql9drUO5tYhaVdrhbHxbpAlidlsFjW+5lA52AaL2u0W9o6Kw7mWFMFgHFc3VAfBZD/tVguNwuIZd7jE54qbnMyLGNJSwWuNLiaye2I3fVzP9S0BGKZvswuBg91QRId9utiJx928qcCMA8FZwjjxjHL8SiG3B0U1QCT0N8FMosXNlxdzmeP7XJ7bdgDbXyS5h+u5JHahqNT5Gay42YGlPCYWV8L0FK2Gm5AKfU3o07IIhSxmVJlaLRfVYa2H28Gguchua8252KaEE8HZLeQ602+ls1y4Pr1Y6ItFn7CkFXnLFYjIrFkuT+cgRUORL5N8ksv91tGYlASUI5TGlnBcE98MF7cCumWIrrg9aYeFNBAbVWSubhmw3JHN3HgViY6ikSWQgLx0DJruYtyYD3HhHM9T43jbpjvOCVezc1QP6YIyKWOn32ascDBuZmtRmehsNS/IAis9XuaGlM2kyY6brq0yPB23s8SqlxXDFCAQ6Y2+u+Sb2KvSzf4AEZ6ZdfiOWyyLMi/SeZtZ5DRY79DeXlb+eomqzrZsSEKw2xnsoaEbzhNHPbHydLqlsquyM9v1ad6TnLSh8UibssfL1hTyYo0fKgfbRcuZht5kQ5e7WBM1J1sfVyeiDM63dCIXLKsritWIvXD0twWztHOPEvBM6COfSyvRPGBLvr8KzJJImeTE7QuuY+RUuHgQYO34slgferWpcr7jGdMPCsWMdQ/XMVtJokNPd1msM4S6CE6EbTq3cL08stY6SCfaJIAYp9unYt7ArrEKCVwCikQlJ1WaT1hxtmZDrqb5VWCZt0ona6ead3kw4Fsf66hzue0F+3Bc41jEU8XlQkR8znv+YnoLbcWt6xWeoBfDZQJquNkxnRtV4JAaqGa9c96H11NoLzGq7a35mk+qnRIXBgAiGdfpaTvD9iI9bAXZPM8DKSbRblvlWuYVTswr4SY3snTDylx0DY+xsLRtQjSPey/XG5pqyWS9OYi43YjhskQ70162sNPoN6urBY7fGzO7z736SDY7eVJIJdlWq3DObFeUOGv9blOsPa6/GJP4Fs7OWV9N5rIvonNfDomAkC6JJHctk+2lCWla+AI9LjVmTno27AkVlZy3Ez5IsrrIO31J4udoMew3sKnEG8FQdLuTHOF6yOc3co3hQ2pEx4OmbKNBLI7S9pSsow1jkdflbaZMxIZe9yQ2u4o+Ti4yFy+nhjlzcBuf5svBIaqcVZIqviSFdYvVG04c4ExolAbvRAdGgGOGv1Bph2tUzrNkvqWUti/KpjB5M99CP5VtQmDmMl1cSRX3/U152zXX/nyZHKYifqFUarNrsd3O4Oqoi52Y1gMzc+eGcZ3zfRIrMlteKt5pUlFP1115O2ReiOWuOlNDUE3ZDVVbyjJTwc1gZvvEWgSYatz8xWJPkcTyptfe4aRYrnUGh6UcucTuSC/U2F/afOMJpuO2/LHPrIy+3Epmrm8iji4SPN6fbpnZXSywpOKtv0mvm6w8e6YAokNZdmnEM3SgZHxPBbyY6teI2zfOwfLdDpcTKq+XqOSg5lo6U4yfp1KKiroElmu9ncrySjkf3DXEox16qCathfFEuJc7YG6X55soY5vIYAJtZ0UzVvFXAPYgH81JOJjtwyiPaAdvsjTm6Fl3dCvx4qOFIqbDdjtfb7ve0LiJXNJzTpmzapTdouWSgaBH8Zheo7rcSxdPWYoSPq09htrMhLqR+b5XF7w5UYV5u0zgrkTeLBdKQnNjYne55tEX3Nua/I6c8cz8ZLr0pPfz/fXKNRCWluvDcZMJ6HG9H6JtLejKnKk4Zd/ny9LY0yedL4P+LFRDNcH8224aoEHsFodmd90EYUT6Uz84pDJdxWt5b3JmesSIayrdeikIsoKXT5x6dIbdjNtw9cw2UMx0z+XEoklUc84hbTltcuvZFT/xzz1xGTeNi4oVN/20uyb2lie1s28PyrxJiwVDQ2uEqjju944ST3FwpfloUI5i7p29SbuYSgZBSIQ10Y7iYb0X3PR0CA0tVtmY6hnmNKxnSg+6TXvxXVpjDprgr63Zjo1XmC4RrM7Nr+WWrlZCzlzMY3wVTpRE3hp2qgyXs1ZvYfZPskV63KO7reMEueetdmASszfevg0A5AHGDCzWz9jStDdH4oJNAliROplffA9la5Haq365cPaidQmPZnFu6Fi7gqnOGNu47OxhC/exs9Tf83BzoJW15e6EObVwsr0MbKw47SXGAIxWaPMTZmZBznMXnKwIb1XDKVi5WOW+8888DWzFtHTDsLD0Cjh6OZy3aJLxTXTy3f2RmAvuJHEv14KfgqLzZ9rkyGjXS9cUW3F7OLZ4xK3yE2XOooDWBiVpz9XMvgX2OsNKA+4ebZiUA24VrLL3VaDxon+m6XaPXeoGhv4YoLTN6UMRXhqZCMWiCYGm4Z0aYe6twYNsnfXMlK8l+ro01nx7PeUn1C9ZcDQbc+FdOnmxzfpBpUkb5A2crmO/EQhxdmRrcyDDFIv3oNYhCORC7EebaR7sYrNUqa3GZf4a38E9hjpMFapxw1TpjilT5rl/mqln0cs8cFqEbtIVAsGpi7A3GunSnfqUyh3PRuG05S4s3AgEpR4KaYpSiyvNBfx5BdWY+frCNFab1coQjzwEWUG0a1k479qtl1mLm24bB3Xpn7BsOY+6gprEEoZt6nrNLJg5NRlYP3fDjvBjyaJvLuo3iSh1p3rvLGx1AJw/XFdUtVCXxDDXuIrGTM+N1EVGDIDlOzXeddEiymvcM7ANjl2byeoaFSynkdLNOkdqXTcUV98wzxo4IsLMfpEWrTg07GTPRrYMOh8m7cWYaj4dEadE5GvPOgvexSjWU5Ht9xIckNYVwK+eyQgmEZCSMFPNM7bR9hMTDmfaleOKiaAarilTVUofM5xEBYuzFzu2ne5pwK+Gng3YAWVPnkrtMdDNUexy1UOU0rRzaWnKGnb8Hp2e0dW25mZNH0j+3ACd6l5u9MnuWIKqZdYjI4rRMG7T2Jx5BhQqkMekDbrrbNj79L6MZw7EJZvwURnVp1G+HiqbMwpGqliyuoQo7nLUdIZjRD0nuAOUHFaxejb6glpV3kWJUUlkK5yK0YOVxdy8cvHtOrkSt5ksrpT6OjN2tqZba9wX9qfrpHcEkO1qXJkstgeSXJF4ftJ2Z9SqomU0t28dOt3m1V6me3V1S9ANk11mHXDAaUbO+Q2t53OC5FUXPx1OR4qQWulmn9Vc2kv8eWK2hSIZeMlsyGYCTidWlWkGrQeMRAc+oM7R/MifKP3CB7pSqZ6dpQxrEMZKrgFDreUmIOVSU3m4gaBSX6hLXNDbzgislVgYsNVvdyDAvG0CbHnoV3mo4QmjmO7AFbK/xBeH7cxoOSOssSLZlrLQcThWuUsywClF9a+66nfZ4HWNR+dY77ZLZmue9GQ2m/3448unl/FI+nmw/O+/Lh6P+v7XThwfh4Nvr5juh8rA8b/cZX35Czr9/Oml9mKo0eNctUm78HkI+Xenqp//5ZuJcfnweAc7vgu7tm9H8K0Tjn9C9BLnfte09fCtKdLufrD76cXtmvHvGZpvzwPsl7tZWTmehv+dGfBOUfug/tYWd0texr84GF/xAD92WvC8DJ9HzZ9e/AGGKPaabxQz+QbqcrT1+bZjPKAdX3e8/Pb/AZqhPv+pJQAA -->
