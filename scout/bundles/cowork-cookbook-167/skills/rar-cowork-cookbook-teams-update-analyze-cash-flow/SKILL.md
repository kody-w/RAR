---
name: "rar-cowork-cookbook-teams-update-analyze-cash-flow"
description: "Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_cash_flow", "rar_sha256": "08d4da8a274f3ddcb317f89e4c6fa7d36e1eaa607db55f2cfb6adb2a5fe93ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_cash_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-cash-flow:ba81d0b349d9d476050c6a1072d50c30309b52a53e19efcaae3de80b5b8887c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_cash_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_cash_flow_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Analyze cash flow Teams Channel Update — Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 08d4da8a274f3ddc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_cash_flow_agent.py` first:

```bash
python3 teams_update_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_cash_flow_agent.py   # or on stdin
python3 teams_update_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Teams Channel Update — Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_cash_flow',
    "version": '2.0.0',
    "display_name": 'Analyze cash flow Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22b3cd7c29aa3333',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateAnalyzeCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeCashFlow'
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
    print(TeamsUpdateAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eXOrSJbvV2E8f1TV4Gt2hNzREQ8h0AJIIIFAqtvhYl/EvgmoV9/9JZLte2uqqqc7YuLJYRnIzLOf3zmZ+Ncnq23CvHp6fTp6VgatrCSJQq+CrMyFuPyWV1fwJ7/a4Bdy8qypIrtt8qp+en5yvdqpoqKJ8gwsX1aW39SQBWmeldaQE1pZ5iVQkdcNlGeAnpUMowc5Vh1CfpLfoLqxmraGblETglEoyhqvspwm6jyIda3ifsFZlQv5eQWVbeRcIcDdCrwXwNvrrbRIvPrp9ed/PD9F4Prp9dcnJ7Fq8OjpLoJeuFbjsQ++HGArAK5gaWJlAZhTDEDvDNwXXgU4pOCR6/nQ+92PtZf4z9B//df1ZlVB/dPr1wx6/3x9mn4ObQY1oQc1uVU3ngv0Kiw7SqJmeIHY5GYNNVR5TVtlk0lqIHgWvDxWfqOUF9Dfp7EfH0xeAq/58etTDkSwJqN+ffoJAqp/fara6fplolL8+NMLUMOrfvzpG526tWPPaSZiQOqXt/f7d7Jg4repkX/n+ndA9eE+2/v69J1y0+ch96QnWPn0EudR9uODcFHlnZdZmeP9+NNfkXVCz7kmUd38S3R/fhAOPcsFOr0L/tPz3cj/gOB3hT5p/jXbArj139EETP9g9wy9G+qvaN/t/99IJ1Hm1Z8W/1Nyf7YA/jv081/q9s8WPEP+16ell4CsqCw78V6hX9+OCs/9/IP77eEP//gNkP4fyRzztnLuFN5SK4t8r27e3n7+ob4//uEfP//QFiDWQA69tVXyZzT/zK53Pr+z4PusH3+/FvDXs2uW3zLoM9KhX/PiP6rfXqCTlUTut+f1K/R9vkwfGJqU+GD6MMF3OVMDWb+z409PvwF0yIA2rXMfBln+n/8JyZFT5XXuN9DRydsGAg5uotSbhNfCqIa096T+5ShuJOkldX+BwNMp3QFEWG3SQKvKigC4Vfnk8UmD3Id++T/OHTC/OO+AiTQTDr21dyB6e0fAtwkB3yYE/OUF0kLANK+iIAKD0IFVFAgAXNZM7O6BUbfpl27iCKSJHohz4DYT2tRt4v0N+uWfs3i7U3sphkmBrxnwiAXc5EKNlxZ5ZVVRMkDWhFD20HhfAKgCFKnyJLEtgLbTV1u8TFYxQi97t5UDsNrrPadtPCjJHSC2HwEgfgburvMEYHYzWbC+RkkCuVEFzJNXw72cACu/TsR++eUXGwj4NXtAMAE9ykiNgAmfAkNfvhSV5ydREDZfM88Jc+iHX3/7Afq/0D9bdSc+8VBAIbhbC4RxAm2P+x0EcrJNwbQamgICAM7dZ7/+9nDDJF0G6h7IpMiPvPtiQO1bAEwaPHzz4Rig8ySiV71z+r3doFsI7AJFDbAWyO76+Ws2kcjB1OoW1d6HER+LH6b/8PSDz+ST+t2GwE9+laf3uffYm5zp5JX7Am186NNSQF3g13sZDqfC63qFl7le5gxgpdV8c2GWN1ANMqb2h2eorYGqE+VfbEB6Mk4KYMlqfoFkTgEVLk/A12SgO3uwOs+iyfHvofp4DIhUP4AYW3yQeIF2HrAmVFiVVYSVVXv3eb71iAhQ2T7WA+IWlHk3aKrj3uSjey7fI4/9Q9/w6C+49/7iUeWhry2OYiT0/7EJuQu3Wh34FavxS4jfaYfzI5KmNmlS7NFZgY7gvvieFt+6hA9A+YDar1kSAetXw98eM/178DzmPOCrrUBkHNjDnf6UxtWdbtSAEJh8WlVT2Fpfsw9MfwZ2AA6oJ3gCmXqd8j7/ZDiNfkgaAntM99/qO/SIrinqQdxCRWsnkQP5nufeQ7wJqymB3q0O4sGbkglEvBP+TisIUAe+BvQn80fANQD376bbgUQAPdEjqj+nR1PXBKRwWwdICzLFe4GMKXBB8NWQ7U0uA3OAFX64k4JSD9gYiPhp4Tq0iocwU+v6LqA1+SJPp0D5zgPvgyAIp+IB+H1mGKBqgbACtrwBJ4AE6h+e/ZTz3VdA2HSK9vui37v7XVfo++LztynLgIzfIB5021Pd/s44AJorELkTVICKeq1BHqfeewCBSLiX6JdHlX2U8U9ZXv/Qr//477X097qp/95zr1DYNEX9iiCP2vZR2l6cPEVAjESFVz/K3JdHDfrynmNfphz7MuXY76g+jPQK/XuS/Y7Ee0i/QtgL+oJOQ1LkeFPMvn+AIbgvi/MXchr9mh28bx5+D4MJvQCi2sNnEfmYAipJUHnBNPlRVOqpFt1A+btj2b0ofEbBe45MKBNMFbDOv8vdSafJpw+XfWIuGMomNHennu2xl0km8Wvv6TVrk+T5KbNS73/aw0yYCoIUWGLa9oCEAf1PE3n3u89eaLr5/R7tnkoAA9z8dcooUL9A3/oMfbagz9DHpuC+x8pasCv6eWp/J5ZgKvjzOfdzA2h7T2AL1gzFJPVjpzN1Xe/d8B+FmBIJSOx4U4XOPzNz4vgHIuAiCLzqj0T29wsreYcHAONT1QPF9j2payCnCzqkZwj4DSQbyB8Aiy1Y8Ec2gE/lAWwH+Dqp+81+39TKH7r8djdD89gu/vr0ARPT9aPoP2IGLPgX27LJoB/l9G0ia02L783T3b73ZvMN6BZNZfO7oWDqAd4eAfj0ChDGe36arAhqUxKN933x00MWoMS3NhVQAFjxpZ7aAATkD6AEinMxKXAFOPcdg+lx5N7nTxevf97b/mXSv9oWg7moTZBzd+6SMxqlUIe2MHSGu+CKQAl0blO4RREeNvd8x7I8wvUY1KZshmFmziTZ5MPUehcBwSbrA+E/TfxvdttPj9WgPuAUDZajjEu6FmPhM9InXNexCWzmM3OPdGjfmrkE7WGeZdHozLUpyscd36Yt1wYS+96ccDxyovfe8T1Eevvorj/88cj8N4CUaTQJjFuWwzgzjHTnM4t2PAKYx/EwHHNnhIdSc8JnGI8E6z+XvvtkctlD6ylWQbMHWq1u4vPru4+n+KNJMHNN1hv28eGQ+cmamZK9C+15RfuskyEbO9JLzfZd0zDm+tzt6yIp0HzQ7NKPQeCoIafpgsyrxYI4kdQVPmzhmzaTMjNn/TxUs5kza7Ul1m56hV14M7P1PI7Lt4G7rSRbaTU+T1FrtpbHDUZWnraKqj02rvenyIDFk3AREaUaJXjbixfvJLiSclQG+daEYiqMG0VP8Wtyavoz3mJhcNqXc1287ERzaPq0LjmFGrdyeJJ0MicanW4PwqlsT1JorTV6vs8E2FU0DPaU3k8lrPf90JOwVbXZXfbH03VtYLvSaEFJQ420dg79ecDC6/yGMadt4wmVnjvuRSvarZbMi5Xd7o4Xq7wEaoHprpUcHVOgb56YjIm5PWf6KUqd02LrAWkXs2a7osyosDWDW1rYyVpa6HjF+tA1TGtmROjec6ym5JBovnVKbEyjg5gcg15Psit962R6zNQouZZJfdQwjOLUujqNV7DHSdptWl0ULI5J7lrXzXC0RmsW88ReveFqvUR88WRsLymK4quiNDkkTV1y21cnq1B9qTWSY1wRm+J8teTbAi4V47I8i7sAX9vGqjGaS7vdn5m8VLZ1Bl+uux61ZTq2bnq88bNSq/nsUEVbfruJUyqYa/3JptAMR3YUBXPqioq91jDN7kQtq7XdBg1o4vuVv7R5TpwpRI2OK2fVZ/xZyFUq5tBdEHezbWRrttjfasaG8yHXWY0MT4jNMoOAe6uTho5UVK18WMoTXSKVWjdW3SWOHLmglMWxHxeSdWZChmpckyGEtszFPYXs+IQ+w+tTeI7P42GjtskWOyWCraXhrqWrXXFsrmhhjCVHmHh67ny3pOHFAoYdRNjC3IIJtqvOFTe5oqBKvGZxYNcZfWJue6lQsxM8p0b94nNdVNmLbXnuxLHIi+tpaI6VEQ2H1awnbUFIVvLZ6MUmhLGu8yiVjwY9O3MFcjgmOzU8jYVyc3aUHRWhfDmY+DIXvELlBVVQ7cVB0Mzt6qoFh2bYHTfVcrtK+NPIn9ShFM9MJqToMjq3iuDY4WHVYwxZoTe7GUPzIJOnq+kKB5HeDItT3M1v9vWoMtuljI/YronQvs1RmwlxoW6xnLoS1RZBfd3WZ8Etr3EERxdYOXSUXERzTz/Dp9kSc7tNWt7S0Dlr8pmqODLCdsEm3/qRmbXruCjjXJ8jw3zpRyp1OlzcmJ5vlhhuhTp8y9D5rVxQtJEZWOhuR5ueK4qySXSDJHXktJEoEdu1R4vw0s5WbbzYyovLyajWpSNSnlXoOEkbXKUXyYY6+VdClLAEF9hyTDgj5xUVhnMhsntXKnvuxJKiDxt2Xw8om/sdi22uOXauEJrVV8qWiyQ+9+3qxMDager5iE86id1dOCFz08LCDb10i3DP+8hW0A9SpqUXx8LHZL9JQ/Nyond7Xr4NaxfP4nO53J3jHjHdS4nmOAVfVmnu8wEoGzOGytHVRtsHlwRL3TXvzbiho6New4+jdzWrWeCrAdr5Hbxf5/5uQWoYA4vH9XK8FZvZgI0RuUND8hxT+Y1QXC6qN2JDSUArDFyplgqrwnpWJptzJNej0lOmw6UEa2wHsHNYZ/BsbW5G0Su6ZAiLwVaabMevqiW/2WuLg5Pv6lbOyPVcG5NUroSxVdGreOAPGU/QeOVsm4tpMXnErzYc14ibTamTuyI1ttJCti7mMlSDrXo8X9ostTfhxYxiEbsRsyppF0cBGzl6VEX8tKCJC36mpAshpGSYFfuuK3E3oyLMz7aLDT+cgp1pe4g25MuE6CunUi5Xgg0KPi4MTUZAFnOtR9FxgwqLkmyX8E65IsducPbIEbkWfjYEMH9acLM9w6SEsFEFJwjRIjBX1nYUx6hZHCTKoUt7V+6pWafi11TXaDvYNDexqeiboyjFjYHTccbEq0tN56WzoviVYvMCnyzHOXuBC3Lpi86qYwmfg60ALaptXAa1TDeK6Cgkm9s1dVpWeMEMli/JR11jm5OUXiP2uB+78+g4/L5QI3FV3/wlswgJHi+a4JRpgrfAO7W5SEaau3jcscx6Iy85tbuIlz4tnLjZk4thXJnKLlgetN4aw9RNajrs+aFwQmZzgD3b3ks5lkg4sr6W187oszTG2E4Pj3GU14ZlrpANTALbk4c0nzHbrPVj1rjCcpWPIUo18boVmGFWNLfDeHMOZR1e5gkr6ej1tl8seEY/mk2Rpxy/WOM7RC+b29G6DqyiE4sI79Czx/H742p5Mncm3C1mKh4dxROD6/YZvagyjx/aW5Jza/WACDK13u6viGGGM46gWUvQ8mVF9CfMuuLn5qxm24RMVE4L8qS7rcelJ8n4ykBDyZQ7icwkZbd2qnwlJ4ZmCHV9HNWzEMy9iyF4HDPs5c5INqYk4Y0dYUK/zymqTNNUT8iNhFd7etOvxvZQyodQpijpuK+K+W0OR2u0iBfJ1qavB9pHL6Lmbcsy79cyGl4SDkdinhUQZeg384XeDHEbGKMAjNCcjofter8zY/x6Mi98QHHeBUbP65kzWrqfhtJxuV0McOoitYhyWwyIsCgpUrzKPHttZ7NKVn0l11ZVlYNd6+HoKL7fdujcg1HcVY/u2lXnw0JofCIIon12uBBo20TkgBt+JiRoS6CX+uLFu+FyTBG70y5mLmNCvFnAnRe1C/YYyjnJns87L5OatKSO2s0n1VJPb8uNflvzRmcWtK9rzJhEBmmyO0Pzmx3t5PqIr9P9aaNiZairXlWe5HU/q3JedA2JiMvMObamWO7hlhCLvjYx7hgIy419M52mWp4uKxkW0H6tloFU176z4RKcLINwHGVsn0l7Vt/bbHHd9Oj+vEWPyxOip/DhOtBEeWozeWiJQBmoQlHNMWaZ7EyRmwEdzXFZxYtKEQ4rfQgTkUqXFdh8765b/siD8uAtwwvNr8kdXeBiKafXixqXFH7EtwN13CnCOerM7UwHfRVboQq7FbUm0Yl8jpqrhWf0WxcXopIpqiTVMC42WUM/4tT8tJ9nWFYkWxWU2+0GtI4uSyEXl6R3uXJpRSIEsWNUUbzhY2NjkW1D9vOTXgh0LF32+wRb77Q1tyfSxtpVJiFk4rhjONZGpKiJrAg91MeYJ3kjNngt3PBrv73u87UVnW3xXFJ5YZ2HtSnhDlsE6gae0WMV7YSSSJHjkZWHatsgrD43u8t+NjtwZpiS8SDmRGGRuXjhiDIgbpzLzgZ1eck3LUqIXBzKjXzzM02+5vqSwtRtIyyy8qTTxcU2W7ZBS3uVW8GuN1JYGErKMmTBPzD4maAcxsC1MV3fuEOiba/pvNTk6DgbCYdIk4W8YjSGARCRHdVZXtuSdFz0imOuUn7J6cvEgs9cDjeqG/CalKVDrzJ9rIBeD856msVIxZY6rW+vmd/Oi0LVz5sL6a2wUSzUbi9KiWmFFeGXkl3YR+rGC9l5m5Xntc4s/eXqkh5ct4lSco7oKL+zfHQ7pjGpoi1+jcd2eTDFdM5GB3S1ONTrPs+ZbMNTInOplEASlrsrKSOZeK3sGXwEe4dlGbM+y7qSJM4HX13rBDMG4lkPQa+5GSnctReRDtechEtD3C/Wom3g21WYyqsEtEoJ7p6Urlr07tjBizaQdwq/Nfbbwwkr5p06gG3ROjh20VUy6bZa7M+7BUHlCi347A6vASKW2Qrhc8T3ba2nBeIEm1bmxi5xoYnz4M1uJEvX/jgnWq0lV+LMaX3GkvbDbuk6vRiVV1BLqMGI16UZH0/WIuxvloYckptsi1cndKimR5kYQxHMoHZIat8O3HC9XOl+P6yiCIGJfIkelsZhHMSSIbobfl3Ny86SuaXEuPiecSlsdiMoX8fO8vxow4QSjmd6T7Oxj2JGXZgXCxdCZlZX9lixlbSai0rscD5nemOzaLt+UJTBJBBqZTOBESaG0SHZGhaJhEE8mqIac44Hl5k477jz0bsZuoqB4q9EFC3kXHbwnS44toO3VegFfDzLS7XCTwY/2Kylu3tvExeHfkFpe3IXtHsVEa7O2mNqFACmU82y83VRm96ldZcHsmV3ujWYB2PdzhE5mYW4ci3Oe4rXKlnugvXQMk0NSxKrq92syOGNgmXyridW2lFaiYzp3kLGzGxToThEyVKz0AQ9KPZevmGQyxongrMcroYxVQnl0GxlDfWLnCBEtGOoam4jWIzJccKartEjCzlcCPN2WbjMukfXl9av53Io4DMzbgJpv2FtrtuPO9sk6lbyrT3tnVGpk3rQFKCEgzl+w3RrnLMCdjkfS9hfqNmtlgpvwUu+Gm0xXurheSSb+dpp/F2HRovFcL4hEmoewzbSXao1q2h1wK8svL+o/UjpK87g8EDLEFUPI5tZ182FTIhyxipZcBaxpUAeR4SLtIru1mNPwktWVhFvQV+5OnVnuIfz7XLYkBv5ZpAbMrD2c7leL25hrd9OSswg50NZNq0aKzGVMEKhxs4BWUnOzt7MCQwXQzvcdVtcM/OSSh0hQlVEnDemuO74gic1U8qRmz3eDBjmQbMKoN2haecCk/x+45gqk8Jcg8QLsG9bnlBy42gps+ZA0wqKnpalZEPRs3WbBNyau9lSXOVGeyJUmiqIeD5ciqpb4DM9umHLrsurkF5vMnTXLVh87bHC4qa6c7BL8w+ZY21YuVozvBcz9M4YlHVPL/FtncLlBVHhG7XLG0ZuyGAVEjZuBe12NhAXn2AQG3wTh85rrflMjVCBaff+7Eg62RKOkqUEy6TRNoQHEwyHio1V223bgVJPtIe2PuzAbt8PEHjA51bI7yiT2TXd1oJPR+EaS7dY43mUFNO+rGqNmcP9fhGeYDI+oPEJ1FifnVMmeZuzKILOOIwxFKXJgfPjY1qBhJmDrdY83RFC0Ql1t5MxZqGniBktl4ISILkDcGUxXwTuVg0OvLvOpGydH/CL1RaNOtC213SK2VRtsc/W51gPJBaP4XFGeF7Oz7MlCYscCUofo82pkAoWZ5IF9tW39pmlOlBWEpZBdsXqwl5uM3HLyr7YtLujOhe9yK32Viwphz5baWNrx/qM3M99V906AtilO8KcTAO4Hyyz8iRecchuJjkxgEt74El6RW5Dnzqrre0cRQNTmFI9hnDly+4unzeIvKA6TQo8hyW8Q4C6VynswwJAd3gW3Y6tBb8QtX3OBLPYngeOqSmE0/f4/gAgwtsOdBWjJsPafXpajZuCZdm/Pz0/3d/SPr1iKEXSz0/T0f/7Af6/fgQcjFHx9k6HmBHY89P/3inl48Tw47Xe/Tjfs9zXO/fXf1XEfzw/VU4ExHkcGddJG7wfS/63M9gv//xUeFo7PF4vT28e++bjnUdjBfcj6yhz27qphrc6T9r7gTUwcFtP/1pSv72/NHi6K5QW0xuI7xUAt3nletVbk991eJr+82N6m+a50WN4ug3ez/afn9wBOCpy6jeCpt68qpi0fH+3NB3WTi+Xnn77fz9Y+eEgJwAA -->
