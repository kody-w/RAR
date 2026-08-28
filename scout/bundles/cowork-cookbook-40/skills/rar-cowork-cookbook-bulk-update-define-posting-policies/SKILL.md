---
name: "rar-cowork-cookbook-bulk-update-define-posting-policies"
description: "Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_posting_policies", "rar_sha256": "eb25aa1f15d6fd6e350446947d21d4a6f3b4885c375f5a54441874a823f8320d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_posting_policies_agent.py` and in the RCI capsule.

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

Define posting policies Bulk Field Update — Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 eb25aa1f15d6fd6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_posting_policies_agent.py` first:

```bash
python3 bulk_update_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_posting_policies_agent.py   # or on stdin
python3 bulk_update_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Bulk Field Update — Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_posting_policies',
    "version": '2.0.0',
    "display_name": 'Define posting policies Bulk Field Update',
    "description": 'Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a68cbf2335ff09cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefinePostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefinePostingPolicies'
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
    print(BulkUpdateDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bOjRrbmv8Lc94Ptp6qSWASoOjpikIQAIbEvQq6OMjuIfRd4/L9PIqlu2c/tN90TEzGquvcKkXnOye8s38lEv77ZXRsV9dvnN9W3c4ix0zSO/Bqycw/aFUNRJ+BPkTjgB3KLvK1jp2uLunn78Ob5jVvHZRsXOZhOlWUa+w1kQ06XJlAQ+6kHdaVntz5ku3XRNJDnB3HuQ2XRtHEegr9p7M5Tat8taq+BgrrIgGIozsuuhdK4aT9AQ9xGkFePH+suh8ra72N/gBw/KGof2JNlcfsJmOLf7axM/ebt88//+PAWg/dvn399c1O7AR+9bYFB+sOS/cMC6WmA9NIP5qd2HoKB5QiwyMF16ddAQwY+AjZDr6sfGz8NPkD/+Z/JYNdh89PnLzn0en15m/8pwMQ28qG2sJvW9yDXLm0nTuN2/ARR6WCP81Lbrs5nlBoAZR5+es78Lqkoob/P9358KvkU+u2PX94KYII9A/3l7SeoqIE+AAd4/2mWUv7406e0GPz6x5++y2k65+a77SwMWP3p6+v6JRYM/D40Dh5a/w6kPl3q+F/efre4+fW0e14nmPn26VbE+Y9PwWVd9H5u567/409/JdaNfDeZ/fkvyf35KTjybQ+s6WX4Tx8eIP8DWrwW9C7zr9WWwK3/zkrA8G/qPkAvoP5K9gP//yI6BbHVvCP+T8X9swmLv0M//+Xa/rsJH6Dgy9veT+MeRIeT+p+hX7+qEr37+Qfv+4c//OM3IPr/KEYtutp9SPia2Xkc+E379evPPzSPj3/4x88/dCWINd/OvnZ1+s9k/jNcH3r+gOBr1I9/nAv063mSF0MOvUc69GtR/o/6t0+QYaex9/3z5jP0+3yZXwtoXsQ3pU8IfpczDbD1dzj+9PYbKBE5WE3nPm6DLP+P/4DO8VykiqCFVLcA5Qc4uI0zfzZei+IGAv/n3AYVyK+bGAD7Ggfif/bwbHERQL/8T/dRND+6r6K5nKvh12cd/PosgF9fBfDrtwL4yydIA6KLOg7j3E4hhZKkL7kd+nk7qwVVr/HrHhQUZ2z9j6AUfZzfgDIJ/fIvSP/6EPSpHH95FPX4WaOUHTfXp6ZL/U/zGs3Iz18rckEJ9u++2wEdaeECg4IY1NYPYO1Nkfagvs14NEmcppAXg+IN+GB8yAaYfZ6F/fLLL47dRF/yZ0FFoSdRNEsw4N0c6ONHsLIgjcOo/ZL7blRAP/z62w/Q/4L+u1kP4bMOCdT2l0eAhUdVFCCQYV0GhgFnAfeC8vHwyK+/vfAFYnLAbMB/cTDTzjwZRGjie9/AVlnqI7LGv/EL4JGiflAVYBmIC6B3e4HS+dZcxyMAN2C20s89P3dHINUGy3lHMi9aqAFh2ATjB6hr/IfWX5zafpiYgVS321+g804CrFGk4Nds5mMQmFzkMYD/PRSenwMh9Q8NtP0m4hMkzDEJlXZtl1Ftv3QE9tMvgC2+TQfCbSj3hy/5zJD+DNUjQZ7wgEEAGffl0o+zzx8MCxzbfNP9GGPP3KY9OK7+kjev4Ldr/0HkwJQRCrvYmynhb6+QaqKiA+3AjB+wdJb08oL38sojBvd/0R/M/A0dHg3Fk8ahLx2ygjHo/1/PMZtLMYxCM5RG7yFa0BTrCePcJM1wP/sqwP0QmPdMme/9wLdq8q2ofsnTGMREPf7tOfIB/mvMs1B1NcBKoZSHfOB5AOMs9xGYc6DV9QOIL/m36v0BoPIoVcA3IItBlM/B9U3hfPebpRFI1fn6O5O/0JlzGgQfVHYOQA0KfN9zbDcBVtVzcr2cAKLUnxNtiGI3+sOqICAdBAOQDwEjYpAuoMI/oBMKsEzgjgf678Pj2S3ACq9zgbWgC/U/QSbIjzlGGuAA0OTMYwAKPzxEQZkPMAYmviPcRHb5NGZuXF8G2rMvimwOit954HXze0Q/bJnNB1JtEEIAy2Eusp5/f3r23c6Xr4Cx2ZyDj0l/dPdrrdDvaeZvX/KHje91HaR2OjP078CBQEplzaOWzpWpAdUl818BBCLhQcafnnz6JOx3Wz7/qVv/8d9r6B8Mqf/Rc5+hqG3L5vNy+WS1b6T2CWTBEsRIXPrNg+A+PpPu4zPbPr6y7eO3bPuD6CdSn6F/z7w/iHjF9WcI/rT6tJpvnWLXnwP39QJo7D5urY/YfPdLrvjf3fyKhbmwpiNg1HeW+TYEUE1Y++E8+Mk6zUxWA+DHR5kFjviSv4fCK1FAFc/DmSKb4ncJ/KBb4Nin397ZANzKW6Dbm1u00J/3L+lsfuO/fc67NP3wltuZ/y/tW+aaD8IVwDHvd0DqgJ6nnW+Bq/f+Z774417tkVSgGnjF5zm3PkBzr/oBem87P0DfNgKPzVXegZ3Qz3PLO6sEQ8Gf97HvG0HHfwN7r3YsZ9Ofu5u503p1wH82Yk4pYLHrzzxevOforPFPQsCbMPTrPwsRH2/s9FUomtaeWTluv6V3A+z0QI/zAQLOA2kHMgkUyA5M+LMaoKf2qw7Qnzcv9zt+35dVPNfy2wOG9rlF/PXtW8F4+eDVDoLhIDM/NjMBLkGgAoXg+hlS4N7/TaP4EgGqHOhSgAzfQda2DQfw2sMDD/fR9QrD8A1GeAjsYTYeoA5GkmsXJdbB2l5jGAaTBGaTCBqQKLLygLxnbH590hoQidi2S7oEjHkbwsZdH105qOvDQB6B+qv1Bswkfcz/3dQElMjXWp9rm4F871lnTF5L/vXNwTEwksUajnq+dsuNYRMm4SiRs6lx37pelpwT65XmBF5dH32YZVyB3mnbBMcVn+aJI+WqhqAdz01Um6FAoQgnZUxwPS825+WoEzvFO20tAT3U2SSMa3daitLFLaalwGgbRS1XdZKpKdw1p16hPZsJGEytCFrHEdVkx8udOOpY7wXBXcz9KyFXWzm6qZt1fzrdznExWiuFjMjtTjEShSHopikQufK25aXU4xWALuZXHTxyndeKsZoYfsV0bRsf9RG/yxwYzMAoXmzYskHcy5rciOh6WNK+26PwRGJcg9r3UlTXpimnTirG7apTBOvoVrAQ82on32G5WQ4Glh8Nk+DlJhd44RBxVu9xU3uvFMHQSIbm46qWm0uM9erurnduiezuK/pMnkYG44WQLzD4vDFOCm2rmFFcFFOt1NOp3uG3Y91WkmI2C1hgelwcF6O9vgAVJ/Fcb4/S+TTxhba9H/hSPGrK4aLuomMs5Ig92ISlI4QpwjU67eiw82LFkamDh7UuErmpf72FQX6mEGe81m7oIDe84fxqDdRP96VRmVRroWe2Ux0zEW+3TSab/M0SWgze3syaMTrBzXgevgpJj0x7y9jeF8WqSbmBLQnWCHOV6biES2yxrbc4U3UoXIpC0GBrneX2K7hDNwJaa8XNgNPV0KHJymrRJK6mM5qQKuPy91o36MqqBE4Xbrelxsesiejq2sekrOFj7lAN+T27kUjcTAfTvbKS243Vfb+Mbemyi1lyf2gLhCPTfeXLw9B4QzweRMs5E8tqkRUtbPrXTCrbQ7/fjjg60YthUIqLkF5LJdHXrQ9+Lvrau6ymqu9Kvk18Jx7WWq3m1F3a+sEiXJLb+22tJD5vtdomHC9iWWyWmYQZIX4+wVp96YyFBl/cGKUS7aAV/WSPPt3cjCql6iwahxs2BsR9zzNnO1tzW4UeqI6zeVg7BLwm7q5aSaiuGwdwCg/uusxKjbLUpG1Ys+NMkhHYZtseKAWOQnsrbmmUmyr6inMgJjtnhy9kX1unnmlhjebfMTx3eW4Ue4LvMs9eWBeShqPFdqMH4XLL6ssoJBgXV4+iFSHOccFmnXZEuQvMdqSwxBCqlOFakRbLlZSYMe14tnaKSMPrHVznMclIESGULZ1DKD1TxwJH0TC+Z4e0OA13SqbqIdvgUbFw+pN6u+lSoaFdXJyHHXW4m+RW9XRAFOapWW8kl6f9PLlPLSYnbrYQx9M0CMZaFA/62O+WB5BpYhTmmikg9UZPEqrjTxfgG8GoIkXCw+ywqC5qpPFbtVqWAdczoZPs8OqSUGjdBbqhiFSXrq4HYe9uhKUek3ZV0Sd0PR5VlRMcPl5S2ULJC92X2XbRXQQ/sJTy7qt3OXfkrT1WRjDGN5ttXGEVNyNXx1sbbzR+v+uEkOKZe2H4RTg5W/HkhksOKczBEqRMWCMLXk1Q+6w1y9WJho3dorz3/YS3g6WcF9vMMJXVWSGKk0pUp6tkHY+VAmiSgkmpzpdoGy0ojPJQ/LxnyzuKYXRytBz+fqhqZXGmsNHbU+EgLeIDs8XM7YidYn+vKIaFxaR1Xjl9wVmi1mg3lJQRTtHEpoxv5XCZNktMO7LVuUHS4Filo4mLGSUqVGpZyfEahyttLSAlfQm86203tLS4kw9HnltNhawZYpfdj91OvwnceaszKUPr91TmyXpkLcZpnQ44mS63MofdFCEN6BpZVNOAErdbfzdpY8cSk7zfGSGxvWbupieJ3ZFqc09wrgK5lKZ0sZBqX6bQTZWzF/SOq+rtwC8m79g0YxDJh0kpzAAOpA3IzB1BaDGyv9M6F/CnEy4Mi2A3TdM6OEVLUrJKtzhFh0shrnvp2I4qvY04zuOvZjQZ4pWhDaq6eifW0I8Ugy9ueHVUuKylRpwyculO57LBrbvqyLtMKeWWonIhu80K27D2w+FMkUeZQiiOtC6wfD2kJYDBOfFHYUSmKmFRJdMtEMe7JtObNaMb1zSwRye/XoR43bA6rW8v+pGR/MhqJ5Fn3fVxBTvJtThPmbkuK3qTe9iJjvfcwNwyNXaPuQ9n7PkgIaZzjnT1bF1j+YZOCyHlj61+bVegDjSmIk6ifUBkoaGr8zk1xl4VL4R0oQj60sSs2EacTuwXo9xwjNBgIxt3UWJF9CH1WStKEd1rI/K+GdyUb+hW6K6yCQs8va8HxdtFQ6lpu9MhU4OhT9US2W4pbaDv3trl+F5JCq5lzImP1/UlwBDlOBzPtaG2cqVZtCSb1qntTvezECf+DlNN+6IgTbovGbeQAd3KeyFIYbM5T0wdu/C5p69J6hG0YJpd7I1dg6lIco4kR6QS11zlcAsC2GbU4+WM7gziMOXXvKxsGvG6lRAix3hjd9Q+QKzutJJbSXcOCY+clgpsl1wgXhFhW27x43Qx62vOXGLWHeJN4Yf6bZErvLa68pZiXoriYm9lLTKckb9whRSTfLsNm1Gr4ou27V0qik7WEeTh6jBcD8qocKKcIIFwijboGU+DSTuU9zzEJaUOCGq7PIpIoIyCI+10xqXYU0YS0+qwt3W44hPfGHUpCFAUv+eX5W3HgS4I58TNHul6TB68Q+2PvjfdHNfy04sBZ2SGrHPifKHwVMaQBQ73Id+eEI7OxTb1V6twx+0iqpCFRS51JQerRugQMqlcI8ag9hdS79k1HCROOxmhybEUzAt6K/p6RU7FKek8ToXjm7FPPIN0+VvtXXg6LjXQ1ywOYn9au1Vh4GTL54wXyCVCnc9Rv/VGpBH4xJpOV+fAJZ6bLOXjDp7sSo5GwLwjn1nbcqPQazpiutt2KzaqLeEZOtKZg2xAq0kS/CneLk9xvok0/ayNrtFuOORc7bVdYEb8ggNGmLp2ZpXIblSpOCfHGIMTczGuKGk5ksulUhnC0ZPhVc9yTuUmInCw7oA+mhsIrs1curoG4QWW8FOkCZVFVD7Se7mCJ5bBHDy3Gf3I4COhpjdpUfNosyDkrAFdG3q5D2Dnoe4IcnSM++midOh5M3hRU5rbQ87d7JVfhuXSSA/HOyKSrXcqk6oS6ZY45laVBW7Tlsnkoso+7Mb4mLWpdectPVLELREhUXhX737f6tJhPyF0tB15cxpouWMEi9lEuwIJJLMrLRAI9n5dDL7ucG2CTKfjeNwjS/1CsuhVtHKPLRl7ddEP5iV18ONJ3R6zJit3AXVe3LY7SqyT22kwGLADqE+ifbbFIh3DhAeJxLV54+mbq0VcOqqBd9qp0G7I3czww1SWcCOLyG3T3DsVW++bMne5LT1xXUZXcKUcY+00oTs0S7cUs1Q3YWYuU1MRKrKWJH2rBO4lq2ia19mDo8pqyZSDYNHaqc+Qu0Xeb9JY6d1wHKkVJzmn3h27FZp2m3UpZxZ3xQIG1ugy6EXbSRE7qrA9oM3SDfEh3m06kLfinvfZbr8WGuXqjXG3Zk7GJWTLy+LIBLpwPjLsekWeTlydetZwl4k9ZTZsVBRkzlEIv7oORnGIo2x0r2LOr5gcJVcrWdPvBXUeqL0Nj5Oci7cUX7SrvbqXM5lbyFUiDs1wiujdZodVZ0UZEKa6qSt0F6UNnnl6eYAPgClX3kQgbhcbV8vv2X1C2nHX8bjorzdG7DBmIOzNe9+2ZbcUtmagrfPuHq58TMdNfMvWm32/ZIu6KTcrvK83muFwaK+yd8JNWbMnY4IIsT4aW8xAzG10RUbs1h9UTj0IBFLdGDvYqbXPME5vZYtJCk+icsLNDeKkZXgBhRQvM3vJkcNYxVxDZIezrnENiwWDlNMwsxdlv1erXojIw3KSz41mbkOn6an8VqNpYWxUE0mRo7RSxp4NLbjbb24WaveHgA1Mk70V05ngkckK+dWwFPsrYZnrW31fNPdRYpHLckkYARlycmoyuZujCz5frVURJ0HS4LCibVKxSYUt6BV9zjdxN5rcDav47BBo201DkXawOrQ0Wuw2F7JLuGxHrTC8cbdL7Tbux0yYat91FwvtvBQ7rF2tOsKtidwqtq1hK4i3VzCEFuv2yt1ZppbWmtbzZ9fSuPpKG8cMD1b7KIgZJpBSih8uLWpKtLTUmAVObMTycBPGkznIixPRt3yndLqPjwJn8aSgaxtpx9YMiTb7bdKfDdLe4baXczETLVsTIxAYydJlHSwaNxiuOnZBdH/Y06oiXW54fXHJ9oh4YLuiWUYQ2IN/VsyRclzzigQ3279kdweWiRq1t8kUVOw5EInjkiV67tj2dDGclw1eZyh9XHAjrud3ChbvNB6na0O8M8fVfXm8eCp5pOQga/b3DY41jpUqYl1imBMG5cBGGb1yu8Px1lNtTZfr1R4bNXJsWhuriBtBSXlo8fDmgCkYuou1HG/Y2x1bCHs0CLotnuyKzI+QBSJ3e5IjuPOUWEcmtHM3y/ZL2dLo88Gzlxm8hT2lGelbsFzdOgE/2rsLrjnHOrh1q+5O732lQSVd1WhiBTdNl7DXnumv1rQ5RNK+IocbusvUO4vjtz6BO7/rmYt/BNtCYSWBja/TY3fvNgxwu9sSq02zDbsLmuZEUq57wbeF+6Zwtrtbvr9aXuvDU4PvNT3wDCdBwbaFgMGGeYBP+cm6xThBGfgZDcOJAWEXE4U/9Cu4LjZnlafIll2KnlTqqpQs2NvqlmhXYWNMfoVG2UnzMNm5h8IWbI4vEcb2p0W1JNYkMhK3LvE3gXFaSgduTzTkEkllcrXxb8GeQDRsrPploMQLy2YZT5fQUJp2oONCJJ8zy8UGJYgleS2sZSq5LXq+1rjRWHLhcCLJ6Qol+tfEhjfIpRPvCVsgRXBWKvwaL0m3jxcHlrSz0N6pOlvh3YllF6ShsEq1sVG2UHtphci1R9rX+4VyJs/fw+Le4OojmQ/eSjxpKYWEg5nU4XGTmSIrsjLcjIYXOFk6mRvHdnpH81QPkSKzpEymZDaIVJGtzBPifiD1w13TYSwlpv1EMcOwvexWlpkN28m/8TfeX9RCyVyp60DwR+oc8G0Hq/KG70oRZvfTSVLuOa7BJTG1DiZu/DA8uofe45vDQs7CxX20ndo/0ZKL9cTJvY0icR1pDGewY+SXltxprspn47RUh8Nuoy6uoBfYOJ21n8TMpEh3izS5X9T6Jd1GZReGkcW7/d49BB4de9viMDH58oZ1kddOGhuUqDzpVi7Upqgsye2K6mk3T0qKov7+9uFtPo5+HSr/O0+M50O+/2dnjc9jwW+PmB4Hyr7tfX7o+vxvWfWPD2+1GwObnqeqTdqFrwPI/3Km+vFfeDYxCxifj2Ln52H39tshfGuH8/eJ3uLc65q2Hr82Rdo9DnY/ABCb+asNzdfXAfbbY2lZ2T7uvS9lPq99PCD42hZfn4+M3+bvHsxPeXwvfo6YL8PXSfOHN28Eford5iuKr7/6dTkv9vW4Yz6dnZ93vP32vwGJqw63tiUAAA== -->
