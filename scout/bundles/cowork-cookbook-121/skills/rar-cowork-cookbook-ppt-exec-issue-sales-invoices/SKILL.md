---
name: "rar-cowork-cookbook-ppt-exec-issue-sales-invoices"
description: "Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_sales_invoices", "rar_sha256": "26f50d1a0f6cd7bcbed79a2c824dabe89bfec11e13d36392b5417f282998534a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_sales_invoices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_sales_invoices_agent.py` and in the RCI capsule.

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

Issue sales invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 26f50d1a0f6cd7bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_sales_invoices_agent.py` first:

```bash
python3 ppt_exec_issue_sales_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_sales_invoices_agent.py   # or on stdin
python3 ppt_exec_issue_sales_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue sales invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_sales_invoices',
    "version": '2.0.0',
    "display_name": 'Issue sales invoices Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-issue-sales-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e9dfce03a79d933',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-sales-invoices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-issue-sales-invoices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecIssueSalesInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueSalesInvoices'
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
    print(PptExecIssueSalesInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZPiSJLuv8Lm/lDVS1UiobvGxuwhIXSAkEAX0NVWrftAF7qlfv2/vxCQWdXbPbMzZmv2KKtMCUV4uH/u/rlHKH97sZo6zMuXLy+qZ2UzzkqSKPTKmZW5Mybv8vIKfuVXG/yfOXlWl5Hd1HlZvXx6cb3KKaOijvIMTOe8zCut2qvA1JnXe05TR633ufQsd5gpeeeVSh5l9cz1nOssz2ZRVTXerLISMCPK2jxywEVVW3VTfQIrpUXi1d6si+pw5oRWWVd3lWoruUZZ8Lm4y8pysN4rUMXrrWlC9fLl518+vUTg+uXLby9OYlXgqxelqFmgkDCtqE4LCs/1wMzEygIwpBgAChm4L7zSz8sUfOV6/ux597HyEv/T7L/+69pZZVD99OVrNnt+vr5M/45NNqtDb1bnVlV77syxCsuOkqgeXmerpLOGalZ6dVNmwApgZAlMeH3M/C4pL2Z/n559fCzyGnj1x68veTGhCiD++vLTLC/BemUzXb9OUoqPP70mE7Qff/oup2rs2HPqSRjQ+vXb8/4pFgz8PjTy76v+HUh9ONP2vr78YNz0eeg92QlmvrzGAPiPD8FFmbdeZmWO9/GnfyTWCYG7k6iq/yW5Pz8EhyBmgE1PxX/6dAf5l9n8adC7zH+8bAHc+u9YAoa/Lfdp9gTqH8m+4//fRCdRBqL3DfG/FPdXE+Z/n/38D237ZxM+zfyvL2svARlWWnbifZn99k1VWObnD+73Lz/88jsQ/T+KUfOmdO4SvqVWFvleVX/79vOH6v71h19+/tAUINY8K/3WlMlfyfwrXO/r/AHB56iPf5wL1teza5Z32ew90me/5cV/lL+/zgwridzv31dfZj/my/SZzyYj3hZ9QPBDzlRA1x9w/Onld0AOGbCmce6PQZb/53/OpMgp8yr365nq5E09Aw6uo9SblNfCCLBTdc/t0gO4VhEA9jkOxP/k4Unj3J/9+n+cO11+dp50uSiK+ttEhN/uVPftTnXf3qju19eZBoTmZRREmZXMjitF+ZpZgQdoDSxYlF7llS2gEnuovc+AhD5PF4ApZ7/+U7nf7iJei+HXO19GD146MsLESVWTeK+TXWboZU8rnHe69mZJ7gBV/AgI/ATsrfKkBZw2YVBdoySZuVEJDM7L4S4b4PRlEvbrr7/aVhV+zR4kisweZaFagAHv6sw+fwY2+UkUhPXXzHPCfPbht98/zP7v7J/Nuguf1lAAkz+9ADQUVXk/A1nVpGDYVD4A6Vru3Qu//f5EFogBBWkGfBb5kfeYDKLy6rlvMKv86vMSw2e2B+AF0KZFXtaAmWdR/ToT/Nm7vmDR6dHE3WFeTSWs8DLXy5wBSLWAOe9IgoIESlodVf7wadZU3n3VX+3SuquYgvS26l9nEqOASpEn4Mek5n0QmJxnEYD/PQge3wMh5YdqRr+JeJ3tpzicFVZpFWFpPdfwrYdfQIV4mw6EW7PM675mUz30JqjuSfGAJ5jKdeQ8Xfp58vlUdQEDuNXb2sGzpLsz7V7Xyq9Z9Qx4q5xc4YACABYNmsidysDfniFVhXmTuHf8gKaTpKcX3KdX7jEo/FUDwL41Dj+2DOupZfjaLCEYnf3/azMmnVccd2S5lcauZ+xeO54fWE590YT5o5UCRX8GAuqRN98bgTcaeWPTr1kSgcAoh789Rt498BzzYKimBIAdV8e7fOB+gOUk9x6dU7SV5RTX1tfsjbY/AYffOQrYDVIZhPoUYW8LTk/fNA1Bvk7330v43ZulO1kPInBWNHYCosP3PNe2AJJ1OCH85gQQqt6UbV0YOeEfrJoB6SAigPw7+ABOQO136PY5MBMkl1/m6ffh0dQYAS3cxgHagsbTe52ZIEmmQKlAZoLuZhoDUPhwFzVLPYAxUPEd4Sq0iocyU6/6VNCafJGnIE5+9MDz4fewvusyqQ+kWq5VAyy7iWNdr3949l3Pp6+AsumUiPdJf3T309bZj/Xlb1+zu47vtA7yO5lK8w/gzEBepY+om+ipAhSTes8AApFwr8Kvj0L6qNTvunz5U4P+8d/r4e+lUf+j577Mwrouqi+LxaOcvVWzV5ArCxAjUeFVU2X7POXe53t2fb5n1+e37PqD0AdGX2b/nmJ/EPGM6C8z+BV6haZHO7DMFLLPD8CB+UyfP6PT06/Z0fvu4GcUTLyaDKCUvheZtyGg0gSlF0yDH0WnmmpVB8rjnWWBC75m70HwTBHAE1kwVcgq/yF179UWuPThsfdiAB5lNVjbnbqywJs2K8mkfuW9fMmaJPn0klmp9z9sUiayByEKgJi2NSBdQINTR9797r3ZmW7+uCW7JxJgADf/MuXTp9nUmALWe+sxP83euv77HiprwLbn56m/nZYEQ8Gv97Hv+z3bewFbrHooJqUfW5mprXq2u39WYkojoDEwpJp0ecvLacU/CQEXQeCVfxYi3y+s5EkOgL8npo7qt5SugJ4uaG4+zYDbQKqB7AGk2IAJf14GrFN6twbUPXcy9zt+383KH7b8foehfuwHf3t5I4mnD569HxgOsvFzNVW+BQhRsCC4fwQTePbvdYXPyYDTQGMCZi9xH4Nc2IJ83HEJ27E9l6CspUMuUdeyPZKyfc+BYQ9GXARHqKWNoTDhL8klRZEYglpA3iMev021PZoUWlqWQzoEjLoUYeGOh0A24njwEnYJxIMwCvFJ0kMBNu9TQSV0n1Y+rJogfG9QJzSexv72YuMoGMmjlbB6fJgFZVgLbGfX5Wl+gub0sGh4N2lEfIz2Msw1xFIdl3bkWcZWIVxM7muzY1eJOGwE9oAyhJG5SzGYH8X5oFHril+xyZGMyyLTagRPMtsMBFReB4u2lVydTVVtg1nLoQgvVlpBe7OGtOv8tKNOntdC5XHbjiJ8O4WJK/scPKQLVkEI3LT7Q2Lert3YX5ijmY1hlUQLuDvo7E5jTtBNXVZXHIcljLNPBnQrSNUFNhzt5SlWOTTMmL51d+YFHoZSqoM207vmRPSo7yMR2SAwPN/hDeG1LbTYLPElc5XyYhS39RIrAADwOYUstLTPUUIYDn7Zeqjm8YMJ1/xJczX9RlmpOi5IUTnJtdqr6RmSrcY2DuEpmc8v7UZFqVVllLXe8ocDslYte72+DPqtTU76KDhmbd1GLtUbDVkysETByz1dwgh7Iwp3Ufb1cFMTC2NzZKsZymFQXRS5Ydvs3MB6ZWy7PGxU8pKgsJfq1bbqXdjEqGZNdqFgt+drikKyhN0IJrKJsaFJWLcqjlBKcS5fY2c3P17q9YjDN4Mp51VhyHsOTnr9ZmA5kaJKqG2i45Ipz7VYwCFh2OYpVLT5Ljpc+Pl4WB6kUkfjtF/1oeExtXBGTT3IRMTrvMTMKQrXshNBywY90NSeqPsB32Pd4UYsiTNvE/35CF/7ZpCyZrGT9W3cQLVQ9Dc3Jlg1QVxzx8Jyf4roC4rYF6k02aWwXwy9vjyEZdD5lHM7p/1pHpUSwgRZt0rqfCmQSXzzDl3fUEFytbwOv/gjAcG6WGVWW6ONEGGogZmiE20H9MDahUndtg1yGQZbwrC97JBp5ZBcVUJYkgon3Dd1disg+QkV+aWqVLzAEyx/NH101dfOaC9wv0WJNYt5NwqvO5+ziB10AjZ2nrUvL8MiSti+2eeIBcmq1JqK5uVk0MerpejuFbn2eGO1Mg262kQ7Or1uNxCvbK9uf3BOK9YKJeOA2TS8Uo+3fUYHq3SwL5tMGtVOG8kTFa7w45Ifdjmbm0KaXE8OdckOjSOLGUbqZbNhreyE3LJxuz8NtHTxVDHWlloVqT1+DguT7hs12LrX3o9IaHduMA3fQRnpkvxFTXZutZT5xRq9xYeYyFXR9TfIpW8vkh1Rp7YIGHoTcN2Id4U5lr7LWOmNOjMujuyDzfEAu8Lo70cjjsmNT9HZUehvUuoN/D7crvHVjU0gg2sssV1SwW1gsKUkHeXSvxQkOR/go6ZhLp0fx3GP2xcIYzlrvG38ZZegRpnWshh3IMBKQz/2fQuf8cqmBetmN0kwkNhYH3ayoaVbOoaV9qblDRyKN0T22Wt6nheLyDCck95yiL5Wh0Mk2ch+fqCv0a5I8QDhNjSDZiNtOcY1OghLiDVbvj5gYj53CX7tC7g0cGRgNqU6wAPcRF1+Dm7OeNNDR4uzfNcrorxY7G6LfsEh2i25LrDGzdLcSvOlavHVfJdq7DbtpXGJW9foPF9hCH2sWSodkMsa77ENLEqlQhDhDtqVV0LgA4UXV2sa1a8ZahGwIbRbj5OoiKUJImcZNzQU0XIlNB1FlCm41vQ8OVFXTXkjWIMid7a0w1KsYfL5yU6WlCZetz3HK3RWNDeEIQ+XbnUI0BUvrQ8EJtm+fqAi13R6qE2rfmCLNc3ZaYcvzwnfMKWZcRc2CwQKyoPI0FZtdPFyijwmrePx4WojWDQHG4nQ7/O4KpW143ocuha85VYxLdrAqpXRuye6xylTNFJX32StH8cD3pYEhTlXKO5EU4LHslzAuKquGd9PybKKI9WJmACnWNPJFlgQGJWyIh2vC8TNsFZgz+Zl+LJXMI9c7EZiQe2lw5bbHKGArUpkbGVGXanlKi7UOTTXLdMI2SXeGha2RAqqVjbShTHZRofopONKK1aVU4bbCnGtFpk2LmOuzE5XROhliaZtYQFBGroI5M5HxyAhFavTutTbSw4m31ShK6S5m2rydde5440LHA3l19tgXZxkC7MOnLwVZAwqHd0InaxCeFG76fkQ7W5a53eSvOQRm0hjOSk1zJvXp6PNxYWOqVIXKLpJlwLSRGMhKr7G71DAoNfTehWMdqXzBFehO7uYZ3irmsPOImuEMtY75GK3DEpntwPKRygRClcXV9IFFoohesz1bMeTjTIYIaPeIla++LtRlLe4Ta+UShuO14N/kiLalRfV7Uhw6mmF6qzWxyZepXNHkB2K9dPeqAaPH/OIo3mu3OTQ2eQ2G5NbG13h4It9d/Tz9XG+hg9FrG2U7njhNvpVWXXM1sC3enkx2gAZztywxhOlZKtxiM1qZzvHjbiWTmiwjIbBHCGB28TtprGg0jpE4r7SuUPPmW7EEf7BwnVxc06MUqBZVVmE416jMXHtj41SRJt+rtk6UmGeJlpzWNOMUlyumLFw23PJXmg0vXYpu8uC+ry8BshBxgVfBbwNaSeKi1UkH/Rz1C7zpIWOpslkSLwnoxgtiwLamJ0ozwW/4qIA3zOlrnO720jX0rza1m7HSiVWCkpLImizsNhi60CrneUv4sAhEH7hUehNiw6kd0Fp2uEz/5LjgNQpdUldYFWDcM8LWp8ISQ4uqLBgGUJD2MwL+8MoC+g6zh3TW+8zC+4pobWhoc8oyq1oZyxhSbP5Vse6EmrOwRHaIu08ruiDFkgbla5goR+Xy8Eg492Zx4VOvlghtTU1QlqW+NDerK01rE7ejqQ1woaKU5EdPADdMSgZTh911+idbdz6iKhrzXwe1jd9s3IJ2hS1kzfewJ6O2rcHRgwkQWuNGrtVa8ZiLCcugvoo4Jg4z7tN2cI6vc7SBD/XpkQnNrPI3UArdC6eF3s0FhG40YlalqNmESgDVrSHExKvyMxQyStmXXZFCKkWkoVRJJKopW7cCAPaRRdLY/udniJXyPQKYe4tLsQtY24Fax3jq7tsBo3e+LKylJJIWuLrC+9uUx5do/EyRkniksrcNY8vAYdUeKutylufN7IXintMr1odvhYEv6zChZa2zMIo+VpYuYyMLlZVUzgmKXaIFHZHIlTbaBSODUYebL7GA8+Qx9xD8eVJi11V0gu0QFa3tD1ndlQnnIozgbzWV8LOd9Q+0tGSSfX1Oq5pOsoiSsfz4AZCvuDGzcbW6OMWG5DAnrNMbEVLVju2N5XzkdxCYnPta1AXcnzYoP4gXJD4ZOm0FGrw4QStuchNUDpnWdGy61XdXbkUy8ZCZuRt6KCFA0VF0plGDarIBtVGF0+67bXQQDV0af2SNFW4OqH+Pl2xRJsQ6sbpCIGS6YhQibo4NNBebLEzpNJyFfJ27WBcJeO21FxSVuC12LAOB4HW5sat1w2ubphrkJ6dqj2JSCRd5mp/XWN+QESr1porZHxOcXLX7i1AQGuFyeD60iQqcHWj2ymX2/OcahJ3t+nlrmIXeR4HF1JmQawdQCtAaa6EFM1hhWSLQymrykDTlO0qonFeYvpG5wT+fF4fA6/Z8ClKr10zBjm7qnRpaQcQ7NiqdZ6P6nkl4IXA6Yp/vFnlIfDWlbUXlE3FgG6XDvtj6BMxTIZrbQuJy1xK1itHFfeKn1yki8aCLGZ8GyYNrcHhOaCY0WXpDcnxWWwalHjgCwm0GSLZXzAYoHVy9C2oAIwyJMjWgNEsWnDBfIXuiIW6Tq9QxuPlhupALNW44RpiFpJyrOKL0HcHoiP5xJNP9NF1c9Skq1ZAjzrDioTDUkfNlYvLFiTSQOwvV3dEmfVVVeQTpTgUvCIpH1br0cBSlFWvBnOm9VMTc0G9aKCVF50jhVdWt1vpLrRiFWMnd4Pg3DIkzjF1xDZypIj+6ewPWnHCoY04XnCZ42OHTUySNc6XOddLnVPyi9vKXvMUse4ohl/5HurTXoyKO6XzlcWc5SnmxkZ1PVdOPpp6h7Hiy8AAJLPdrKtchsSqwFdov2YR1Qx3Wa67awimhkrc4Ql6XeSbVrz2ktte3KsqSnRxgTE0apKM5ROZuC5VEtNI8zJ3+WHULIIaHO8YrbjRNngMkrICDTZ7W3RZNESkzXjwt5KHq+cMZ5PNNVugp8gjSWe+h4RcdJSrr58WoGulYChzjlxM+QIdOIsdn5+3odcc1/DVOnTQGeclCL95FTGC2s6pGth8VLuiXC6A/j5/rGS38A0cwduFqSjQ+WYRN0PJ94kglFXnSv61lXvCH8ngchWaDgfkLp771fpsFMMls+brBANS2tOYBw3TSlkg82DvdsrIXbnY7IPrZi4afqtHJlr6EaLlRzREs3PkHxvyHJzjDOsU8VRpDRvQ+9EUsTkgJqqyQHtFkkyG7qHzuhujnXRgqr5fmUh0JTnaATt+e67XpMXH/ErJovMW1hL0OHRRlLVz2Pd3V9yVIM2H+FsglaN3XC6VZPCOa5ExuSWdSazi10Fw02P+Ysc6x1NhdzVuVHOOUA0jsN0uk1F3vl6iNlzxbVZlSSPM14gt00OWXgZ7h2mrvOmd7EgM2XDceOHYRa1EnfncL7H9KqU6vyyuSnTIw9GNG4vdEpB0Os+l2j4D2nSWQmeWhVwuQohAYKmS8wXsduJhF15reV7ZaEoAknTmxu6KgCbAd5fhJrzxNHHU1pDdrA8yyWnoEaO36+v+hNTBBqWoweXozWpexOT5dIHhQ0UoYk+JCbfXWktDNufNet4jDXsgBcInNmyHzWt57Gx/GZnjhdz5YK/ShtwpH6NuJBenuDSVLXfatcMQqvN+XS7kLnNSeDs2OGcpCK6hc7xqmy2EUXw7tIs+Omo3kxo8NHZ9NRki9sTwLbORDutTeCvlou0k8bS9YhwMdvcur+1Pcx4zSGKxjw97WpSZ/V7bIIsxvTFMdERBd2o5jaSCLTqRIp06mObSm5Ogk9/leUdprMLxdD52/uGsqLrAIMXO2a6462HYeHUtil6PBPiYEBeCb5s+OebHpIrzRXLbKIrO0GNI+onoGL00FxsScrpV5Qi64G7ZUto6iICXA6iwqR7LkTS4yTXfKIkH51AB2LwKLa0gEvaMj1pJNPZIEyhNeVYnOklObck91Zr50A+WX7r8VXLIlt858UAT5y1LEhy6iV1DODQnR916sLI4dnuG0sDWkz0tEAbj0rVU0Si7pkRZu5hku13zR3dlMB1L+AuBW+Aigw/lLtgrBN7vU95e2jKExVvkaCu+sXW1BSqiIZNSmlOsVqu/v3x6mY6inwfK/9pr4umY73/ttPFxMPj2Sul+mOxZ7pf7Wl/+RX1++fRSOhHQ5nGWWiVN8Dx8/G8nqZ//6VuIaerweOc6vfPq67fj9toKpj8Teokyt6nqcvhW5UlzP8j99GI31fR3C9W354H1y92ctJhOv9/UB5d56Xrltzr/5lhV+DL9ScH0DsdzI6v2nrfB80z504s7AH9ETvUNwbFvXllMBj5faUyQT+80Xn7/f31jTu6HJQAA -->
