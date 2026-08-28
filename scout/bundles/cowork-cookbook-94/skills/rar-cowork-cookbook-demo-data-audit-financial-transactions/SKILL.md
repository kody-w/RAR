---
name: "rar-cowork-cookbook-demo-data-audit-financial-transactions"
description: "Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_transactions", "rar_sha256": "0daf3a05c492836fe9c4ee7be4f23bb3f0f1d9f843ec5ad42633fd40e380e276", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Demo Data Generator — Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 0daf3a05c492836f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_transactions_agent.py` first:

```bash
python3 demo_data_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_transactions_agent.py   # or on stdin
python3 demo_data_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Demo Data Generator — Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_transactions',
    "version": '2.0.0',
    "display_name": 'Audit financial transactions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '771b798ab6e1987a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAuditFinancialTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialTransactions'
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
    print(DemoDataAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjSJblX6Fff4jIVsQTiFVRVmaDEFpAIBBCQmSkRbI4i9h3UE7+93EkvReRnVXVlWPzYRQWJgHu916/yznXnffbi9XUQVa+fHnRgJUiayuOwwCUiJW6CJd1WRnBryyy4X/EydK6DO2mzsrq5dOLCyqnDPM6zFI4fQ1SUFo1qO5TnRLcf8OvOKzq0EFckGTw0slKt0K8DGpo3LBGvDC1Uie0YqQurbSynFFchYQpYiEVlGRnPVIDOKa+T4KDwjRM/buSPIyzGqkc+LgMs+oV2gR6K8ljUL18+fmXTy8h/P3y5bcXJ7YqeOtlCW1YWrXFjqpXb5qPPyiGImIr9eHYfIB+SeF1DkqoOYG3XOAhz6uPFYi9T8h//VfUWaVf/fTla4o8P19fxn+HJkXqACB1ZlU1gA6xcssO47AeXhE27qxh9E3dlHCtcKHQran/+pj5XVKWI38fn318KHn1Qf3x60uWj36Gxn59+QmBLvn6Ujbj79dRSv7xp9c460D58afvcqrGvgKnHoVBq1+/Pa+fYuHA70ND767171DqI7w2+Pryw+LGz8PucZ1w5svrNQvTjw/BeZm1Y6wc8PGnfybWCYATjTnxb8n9+SE4AJYL1/Q0/KdPdyf/gkyeC3qX+c/V5jCsf2UlcPibuk/I01H/TPbd//9NdBymMP3fPP4Pxf2jCZO/Iz//07X9qwmfEO8rzO84bGF22DH4gvz2TVN47ucP7vebH375HYr+H8VoWVM6dwnfEisNPVDV3779/KG63/7wy88fmhzmGrCSb00Z/yOZ/8ivdz1/8OBz1Mc/zoX69TRKsy5F3jMd+S3L/6P8/RU5QTRxv9+vviA/1sv4mSDjIt6UPlzwQ81U0NYf/PjTy+8QJVK4muZZ/19e/vM/ESl0yqzKvBrRnKypERjgOkzAaPwxCCE6VffaLgH0axVCxz7HwfwfIzxanHnIr//LuQPoZ+cJoNMRA7+5EIC+3cHv2zv4ffsR/H59RY5QelaGPnweIwdWUb6mlg8gBkLNeQkqULYQU+yhBp8hGn0ef4yQ+eu/p+DbXdZrPvx6h9HwgVQHbjuiVNXE4HVc6TkA6XNdDmQG0AOngWrizIE2eSEE2U/QA1UWtxDlRq9UURjHiBtCkIcMMdxlQ899GYX9+uuvtlUFX9MHrOLIgzqqKRzwbg7y+TNcnBeHflB/TYETZMiH337/gPxv5F/NugsfdSgQ5J9xgRYK2l5GYJ01CRw2EgqEYcu9x+W3358uhmIgaSEwiqEXgsdkmKcRcN/8rW3YzzOSQmwA/Qx9nORZWY/8E9avyNZD3u2FSsdHI5oHWVVDustB6oLUGaBUCy7n3ZPpyFkwGStv+IQ0Fbhr/dUeiQ2amMCCt+pfEYlTIHdkkBaz0cz7IDg5S0Po/vdseNyHQsoPFbJ4E/GKyGNmIrlVWnlQWk8dnvWIy8i9z+lQuIWkoPuajlQJRlfdy+ThHn+k9JG67yH9PMYc9gAJxAS3etPtP2nfRY53piu/ptWzBKwS3AkfmjIgfhO6IzH87ZlSVZA1sXv3H7R0lPSMgvuMyj0H2X/VI4xsjox0jjx7j5EMmxmKEcj/B83I3fz1+sCv2SO/RHj5eLg83Dq2UaP7H50X7AgewsYS+t4lvGHMG9R+TeMQ5kg5/O0x8h6M55gHfDUl9N2BPdzlQ8OgW0e590QdE68sxxS3vqZvmP4JruoOYDBWsKph1o/J9qZwfPpmaQBLd7z+zu9P540rh8mI5I0dQ7d6ALi25UTQqnIstmc0YNaCsfC6IHSCP6wKgdJhckD5CDQihOUDcf/uOjmDy4Su9cos+T48HIMIrXAbB1oL+1TwipxhvYw5U8Eiha3POAZ64cNdFJIA6GNo4ruHq8DKH8aMre3TQGuMRZbAJPkxAs+H3zP8bstoPpRqjSj7Ne1G3HVB/4jsu53PWEFjk7Em75P+GO7nWpEfyedvX9O7je9QD0s9Hnn7B+fA/CuTR1qPSFVBtEnAM4FgJtwp+vXBsg8af7fly5/6+Y9/reW/86b+x8h9QYK6zqsv0+mD696o7hXixBTmSJiD6k57n0d/fb6X2ef3Mvv8Y5n9QfrDWV+Qv2bhH0Q8U/sLgr2ir+j4aBfC6oQeeX6gQ7jPi8tnYnz6NT2A75F+psOItfEAefadeN6GQPbxS+CPgx9EVI381UHKvCMvjMXX9D0bnrUCgT31R9assh9q+M7AMLaP0L0TBHyU1lC3O/ZuPhj3NvFofgVevqRNHH96Sa0E/Lt7mpEJYNJCj4zbIVhAsB+qQ3C/eu+Nxos/7unupQUxwc2+jBX2CRn72E/Ie0v6CXnbJNz3XmkDd0k/j+3wqBIOhV/vY983jDZ4gVuzeshH6x87n7ELe3bHfzZiLCxosQNGds/eK3XU+Cch8Ifvg/LPQvb3H1b8hIuqtkauhpD/LPIK2unCzucTAuMHiw/WE4TJBk74sxqopwRFA0nRHZf73X/fl5U91vL73Q31Y/v428sbbDxj8GwV4XBYn5+rkRanMFehQnj9yCr47P+yiXxKgXAH2xcoBnUtD7dQ0iHmMwanPDB3CABoGxDeDLdt3EM9zJ17DIEDh7RcYkbhuOcSKMAZFMxoCsp7ZOi3sQMIR8tmluUwDo0R7py2KAfgqI07AJthLo0DlJzjHsMAAjrpfWoEsfK53MfyRl++97OjW56r/u3Fpgg4ckNUW/bx4abzk0UbO1sO7HlJeWx1nUd1L57qXS0XVI9T13wvX2U5SdfDbJIQ6+ASbdUIO9gsv9Y9DIgXBdW8KpoM5GrCbUTpJDSldJsRvT10h84x+OntihqnBctnc4nCzNOFim9JaFpmwRfmmYz1WXM4K6utve1pQcuyVIxBXPJd7rVTrJ5cWvNiSDq51sPr9HqizDo/7A9omWuCZUrlKQgjuy9XJLoTtS7qgSUXi2Ny2nXbCNcapj+1enOVTtI2WXMUVoFV5iplNDgGGc1lgySm/MSTjdV8siHqkxU6x4hfrYJ+ltdajNWpFWJ1KB6CS48dqml3IgzBPfOltUNN85g1ph3PKe7SuJZliWagCtjJLeKDk66oDqzDWAusssBYptQ4YrfUzQutHZoTUZxRrMtqUNTL0Bv4fgjc88mywRXVbaW2D+WkrLLbuaJAITIEuOrb29ASXXc2tOLUX0XSjyg12m0NJ5fKi2mHoJgd5w5JLjjNOJPbOttyDbOvqIBJwJrslEU8O5u1LGONStHC9Mx5B6fAxBVRNljJH8zu1vRD1WE3Z9P3Q7+1F4cqIUirmxfYTuiSvOxDTDua+KxTV+msRJmrGKB0EXNcvdWphNvtDrI1gHxSyMxMK1Pc2cfyjZ1LRN1MaExgDgU5EGJBOFcsmjWDVFZTbThKh5t9Vo+LU0I6y7VDtbQQ2kdb7LuKsSfZoNucxXNT8kK1W0PoTKUpTOnk9NNA3uxIQ+oPcpWd+Wl8DR3VJ1pXHW6xcrlI7QSjqIY8r9zTBYDb2dnueJppjlKfBNlVDWzo0aLKk3MpcsdTzc9K60iFEwc2uY3nd1Mv07zFVek9vDNSX9nO55nArSvCmy7Wa+9Y0hNvGpyXWdeeJq678Tl7aaNn5uCJ56a4VqUQaYN7Lk5cY212a9teBRXvoJe+sCMf4232RqRRaUgnJt8TQg8TQegH0dhfpgs0DeTzhQvbanMutmdidexstsF4XdYj6wAEHt/eMn67krEsbC4cxemBvYrls0k4x0W/xVOnkLp9S4vg7FnN1nX5fLXbpqaA7bKIKuuIlk7EhRSjI5M4N0/WZ4N4nFFXk4zkQ2Oer6mwmW9aZrOHGkhfPMRK0enr2/mEC3Hl5cNyq2X84WgPQlEJlbHmb+u91dVqfb1wV84gjs60c06yPhdTjPfw4BrUJ8HfZYm5TSlhUFVRt+ZJOjGqFfRtQQWnOXopFEVp53Yu5WGrLETBDKdScz5f65ONDuXcGVBhIgqieCMoJ42PJH7Vjtz1dKP1Jr5g+jTP9/XsOj9zvr81B38iw5zqtXOFwf7ADhzOu+lXRtvVqcgTkeudCkHforNiwyQncRY4atm6UeO503x5W7rpNTijPjdJML2zd7si6TtcE0980mxXZXGTEskiZ3Eg1nlhuidquRejfiM2XX9TXTZRBGoqJhVGObYz5cP0FrP0+WiDdO5GQ7iYLauhGoguwf11O9XPsqeJNqbV1hynLgBb8g3uTaQ1O234SNEbGt9u9dRUjyesTnIWREtiOCx3Uz0oKS27GeytMTbOjbWI4rrijXI57Ex5kQuDG1qT6Wp+5YkLJuwNCigGepLSuOCuvjGxUqGaoE6kAtE0WS5bKvGiSQcOzTddF1yuYues95y6EsItFus7C0UDm2jobLjIdcdtLP3kWsRN366bZLYQLntX2gW9qOqhKDG3w3GxSkJFq539niIdVg9cZ2gqgutjHfQzN9lbM7c3m62ZGsbs5u5vzMRpbz3erSSzSDcG3VOaduWLiWSnJs1HBL/KUWoV3ZTpTWCrvAEE7S7UQoxYR6ErR2nbnuvzSTnB5hNGX1Kqst75gYkDcLbDSOL2rE7rkbBMGGeoiNLXw4mxL6JbJ/fMBqtuoVPai1XHl8AO9xe/OlxN7KCTmLZHr/yR2yuyihaEEYjnBaFdl5Uq0J0SFnIBhguVKcv6HMd5QHsrGstPvL6/5aVgwLI3MLVluvy0C6OItYbbnpYHwsrELIRxqERi2d+udnmzVnlHGWesYOhQxcxiPb8eaGM2sDu2LWda45rGcZvgPBeQqZzsG3EtyZxkTudTfhZKCTj3pWXIMykNej2VG2XLNrmWn9Zzg1/Nm8FtVjS4ELvBctiZtBN6yLukOySQluX55rbHFm6YDeUV1+tY1WwWi/Tl7Zxbs4TTdmveDD0LOzWig6bstkkulY6BYqIPLKyD2nAwjWaMlUKZTGkoruoeAb9TvYvVcop/OS1WzOkQVRV1rE2wAUs9Ewh604q974RystTPZmg6gsppl4lo72QiNSxSOawCwQz8GSOI9PGwTuj8ul7rBn/mnUpbqiY55BMTrFRuCmaopM4EbW5Nkp09u/glepRlvaI6npanBRWrkZ1u6XWG+q5Elms1m7eA7hcUj69WeGjhOapF8zWXrg6n/dZcVyspO50Ym+W25OwsTDM+3usuyk0udVIcCtHaboUF50yqsLDZaJMdSeXcqnO6sTWFzDTU71RHKTBlfuXmUWpsMnK9S/2C7cLFQLd7p2a7fa5YTegPVtUK6nw6Z6baiZ4QJocJ6HyxwDMRx6aHCXehQJ16KoXh4S4/zd3EUOnWpPrVsE/1SVw3c8/iSm0WLjZdPvFc+cL6660u8ks7a+n4WEdQOeiUyMz4AePILt6gTGWQa09vLljCXZdnHy2PTiy2Enq46akm1ZcLbAqMg7M8+vl1V4WqXmJZ6e0t9ybmTpFhsJyLlMc8uAx2KwWe7A21atVZHnf7ZGtdF/P+6G7T3WaZ5+FuKx2Zm+tk3DHnl0m3E7SFE2qs5683mGaT3HFXglwdgBufanYa99rEr9O1QO7FmNwNc/XECcEhoqPwEPOkykSOt6qJkmVMAlJdcYm3EWE0kD86mVwcVDTcbKnGjeAWc9CVY3Xelhe/3aITS5KUTlQ2OawfyHYeSh7OK3Zlm6ibrMIC5u1OSosVKISKCKq5e9rPY5TiUcIokujarHanRpW9xAb73LNl+WjrdGWIvh1VpHNZtBR+TbGDhnr8xTYxtMmE4pIdcKYAoeXOh9vg37yptGQ4osxip+FLPu/Bgs+Wqw3BLRapTAcTwSzXfZWHZVrF5nVLOjuzW6CcazgTSywzHrZ10lWB8D4xMWc28YVJmdZkI6FanBnVpmpirNBqkTtDIqlkmm36veSzs9kCrRdUzdZhfXQUC10suBj6Wz9QxxVKqgW+2e04upvPKpVY7fbBXsJxNtRx29J825GT49op23jO1Rbp781AE6JkXhyVcL+74RKexIvtmjkyxEyaxpRKZ4692WmQBxxjtboei5jttSapErlkuGqBUjQ58zWFuXQMJSg57/ibQgmGHdHYmDCjW83Uo2SxnmycuhoyfTeNxPyEZwWJUf7E1reZt+1Cao5ODz7bhnQnDRW1FWT0OEuzznDOc9Ejt8NaKoNLRsJo27EGVFmgl6xTbVZ+KV2X6wvsmcpDstKCZJAscziB87FsPMMS15DYLZat2S2VM3tifcs6zzuriyPEaSFZ8NMZvMOco1PmntTEcvuOUa19T+gSraI3yvebSS64Nxd1HclQtowttKA4TLR94+/KYnZRF1s0OjF+aqsx2puon5+TagE7DHLZtP7tTJ1IhZ4bV8YOIGzQ3onKG1eraScpjVCg26WPNe20wh0S0P6lDAaSJMtqx+JyfNusxUSNUzu9FFs3xwQxJrj15oBJ88RjSbiPHWp8h28OvmLYtb6rsIk5CVa79SG5pismO2S7Ke2pbcDL7HK/tW4DaOUgkue6FznSetvRlDw/kgypVdwkLzqSjloyq49hhwJ0sZ7WdmUe2jbOdksSN894ai/Omkzp3obQqaiZX+2la1+js5e30+lMxEm2uYlVrdCKwpyUHTWZYzccb8t8vZhBKNRn+twvsmCwc1FZ3FBn7+fDhIArdAbm7KE8GnUXrm1JuAVzfTbvUZLQ1skG3USSHeEQuZdM4vbubrgduak7tAkIuzXpmgmNwladUEm/NE8ScVrgu2JOHm/x+hLvpKvJDsNk2YqSg98Evl2Q3LxZzyi/Vb3OWHqmy1aXtgc4t+sgYtXGsJpOIAFrs3224KW56tTzQckbtnOXcnyVgokVWpqTZq1xaJtT5pG4QaXTcoMDSV+Y6NJA+QFl9dlln+KdvVHnDTk5ojcexgg0M6jMP1YiSkhY7YGBaecZXpBXvWEUYd2CPZHYberYNeMnKMe17K3GM7CT1JRItya3WS95en2klPN1RfOX9myQIWXSwZZdOlgIWh9fLT2+2GGuokj7pbtmGYfIrpuulIAPQTal227pCy2zGuL0ajuetWDQ5eLsX9pw4xK65kwxxWs8L8/XW7th5+fFeam4tOGtjQXJOzx32TlsrLpXkCTLQN16K2l1uExxkpPdU63xJTOVWl8WVzTcMmD0eMzSME2v7xxBpveaNl3hUu9XwN+YXgO3DgwUlnIW6W4mC+cSTrFuA3CLXJspbgeKwQb9NSYUofVtQMAAEB3m7pc0T7aLLjl1WInNSLyRAGh6uiLYwT8vTd11u3nXUIqhNkOO5w20ALfqYbmEbTcGMa6E+4bDjIFrkTtWN2QW54Efuxs3PLDL+DINj6gXH8TJkQCKtj/IEY6dZGoDNkItt8GiXbPongbyfuMDpp4Zk6Uymxkw1+d4mbTgdqkX3u6aTtBmk/geeswML/fYGJsQuKEE+8AtjaWLM8yl0lx6ikWLxjVsZjOdnPCdIwbtGu6CIU/iVKVKkQ146wJ3FLCjkg03UuL2fBikIsV5a59YzWRbEkotTtdxBrdeV2Lfhn0/bVe6iloM7vbUanerleqcULVMtLGZZ+1CTDcWql0uObOZL0OU6ORMWuYiv7aT5BrcrqhES7WhzwjTkdvzLKVnKK6nxytzKtSVbx1ad0m3is6BW8Aoq4VzxmQgAKZjukUlsaeu3q/qinXwbMiGtC1u1iFR185+CNXlZijtqx4pWpqV1i0m4mtF3K4CgclY71ZLr536fMPdmnjPTZgr7DZzeYdNV+Fmcjm7WKOSnluRmuMsHb5vmUww3GK7OoJkwleC2p4gIiTjCVzKMjfYuSgKa5dCZ4m3FaleLDvbbc9cSnfLhYEftqkODm6fT43JLlMACXf3UpLPm/kx7meby3TCDlqjBD0QVZZ9+fQyHkA/j5H/4pvj8Uzv/9nR4uMU8O3V0v0IGVjul7uuL3/VsF8+vZROCM16HKVWceM/jxz/20Hq53/vtcQoY3i8mB3fhvX12/l7bfnjnxm9hKnbVHU5fKuyuLkf6H56sZtq/HOH6tvz4PrlvsAkf5yCPxc0HtHe3wx8q7Nvj9fHL+NfI4xveADcEtfgeek/z5fh3AGGK3SqbzhFfgNlPq72+Z5jPJAdX3S8/P5/APNF8XrUJQAA -->
