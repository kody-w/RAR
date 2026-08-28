---
name: "rar-cowork-cookbook-teams-update-analyze-and-reconcile-compensation-and-benefits"
description: "Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "4ad772f55a98a6f5ea356dbd30b2590b378f5643856f500961ea205cb768cf35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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

Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 4ad772f55a98a6f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits',
    "version": '2.0.0',
    "display_name": 'Analyze and reconcile compensation and benefits Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7d197ccf89fd467',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits'
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
    print(TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjSJLtX9G78yGzmswr9iXb2mwQSCCJTQIEqLIsix3EKhZJUFP//QWS7s2sqe55r637wygXARHh4XHc/bhHoN9e3L5Lqubly4seuuVMcPM8TcJm5pbBjKuuVZOBryrzwL+ZX5Vdk3p9VzXty6eXIGz9Jq27tCrBcL5xo66duTMjdIt25iduWYb5rK7ablaVQJ6bD2N4l9uEQJKf5iGQWNRh2bqTjHuTF5ZhlAI5bed2fTu7pl0CGmZp2YWN63fpJZyxgVvfLzi3CWZR1czOfepnM6CbG4evQLPw5hZ1HrYvX37+5dNLCq5fvvz24uduCx693BU068DtQvahFVsG+zeduB9UAs8XT4WA1NwtYzC8HgBgJbivwwZMXoBHQRjNnncf2zCPPs3+8pfs6jZx+9OXr+Xs+fn6Mv3Z9+WsS8JZV7ltFwYz361dL83TbnidsfnVHVqAT9c35YRlC9ZUxq+Pkd8lVfXsb1Pbx8ckr3HYffz6UgEV7mp/fflpBlD5+tL00/XrJKX++NNrXl3D5uNP3+W0vXcK/W4SBrR+/fa8f4oFHb93TaP7rH8DUh9298KvLz8sbvo89J7WCUa+vJ6qtPz4EFw31SUs3dIPP/70j8T6Sehnedp2/19yf34ITkI3AGt6Kv7TpzvIv8yg54LeZf7jaWtg1n9mJaD723SfZk+g/pHsO/7/TXSelmH7jvjfFff3BkB/m/38D9f2Pw34NIu+vvBhDgKmcb08/DL77ZuuLbmfPwTfH3745Xcg+v8pRq/6xr9L+Fa4ZRqFbfft288f2vvjD7/8/KGvga+B8PrWN/nfk/n3cL3P8wcEn70+/nEsmN8ss7K6lrN3T5/9VtX/p/n9dXZw8zT4/rz9MvsxXqYPNJsW8TbpA4IfYqYFuv6A408vvwPiKMFqev/eDKL8P/5jJqd+U7VV1M10v+q7GTBwlxbhpLyRpO0M/J1iuwkBrm0KgH32A/4/WXjSuIpmv/6nf2fWz/6TWefdREnf+jsnfXtSJfgOvr1T5bcfqfLe9EaVv77ODDBn1aRxCkbO9qymfS0BE5bdpE/dhG3YXADTeEMXfgYc9Xm6AIw6+/VfmfbbfYbXevj1Ttzpg9X23HpitLbPw9cJFSsJyycGPqDx8Bb6PZg8r3ygaQQmaD8BtNoqB3TeTQi2WZrnsyAFGoA0MzzyRV9+mYT9+uuvntsmX8sHBWOzR/5p56DDuzqzz5/BkqM8jZPuaxn6STX78NvvH2b/NfufRt2FT3NoIEc8bQg03OiqMgMx2RegGzAvcAhAOHcb/vb7E3ggpgQJE1g8jdLwMRj4dBYGb1bQRfYzSpAguQH0AfJFXTUd4PVZ2r3O1tHsXV8w6dQ0MX8y5c0gBNgHYekPQKoLlvOOZFl1s8kobTR8mvVteJ/1V69x7yoWgBzc7teZzGkgz1Q5+G9S894JDK7KFMD/7iOP50BI86GdLd5EvM6UyYtntdu4ddK4zzki92EXkF/ehgPh7qwMr1/LKdOGE1R3d3nAAzoBZPynST9Hz7QP+CNo3+a+93GnbGjcs2LztWyf4eI24b1eAKoMs7hPgymJ/PXpUm1S9Xlwxw9oOkl6WiF4WuXug+w/WXo8ChjuWcA8CoXZ1x6FEXz2v6bKuS9MEPZLgTWW/GypGHvnAfhUpU2GeRR2oK64D74H1/da442p3gj7a5mnwHua4a+PnnczPfs8SLBvAKp7dn+XD3wEAD7Jvbvw5JJNMzm/+7V8ywyfAEp3GgSLBvEO4mFyw7cJp9Y3TRMQ1NP99yrhDh5YNgALuOms7r0cuFAUhoHnThgkzRSGT5sAfw6nkLwmqZ/8YVUzIB24DZA/GWcCHGSPO3RKBZYJIjBqquJ793SqvYAWQe8DbUEZHL7OLBBJkze1wGqggJr6ABQ+3EXNihBgDFR8R7hN3PqhzFQ5PxV0J1tUxeRGP1jg2fjd9++6TOoDqS5wOoDldeLpILw9LPuu59NWQNliitb7oD+a+7nW2Y8p7K9fy7uO76kBkEA+Zf8fwJkBBwR+PTnpxGEt4KEifDoQ8IR7on995OpHMfCuy5c/bRc+/nM7inv2Nf9ouS+zpOvq9st8/siYbwnzFYTUHPhIWoftI3l+fmSxz88IBN/B5/cI/PxjBN6b3iLwD3M+IPwy++f0/oOIp8N/mSGv8Cs8NUmpH04e/fwAmLjPC+czPrV+Lffhd/s/nWTi5nwA2fo9Ub11AdkqbsJ46vxIXO2U764gxd6ZGljoa/nuI88ImhgqnrJsW/0Q2feMPfHPw4ZvCQU0lR2YO5jqwsdWKp/Ub8OXL2Wf559eSrcI/4Ut1JRMgHcDkKYNGYg0UH51aXi/ey/Fpps/7i3vMQjII6i+TKH4aTaVzZ9m7xXwp9nbnuS++yt7sCn7eaq+pylBV/D13vd94+qFL2Bz2A31tKDHRmsq+p7F+J+VmCIQaOyHU4FQvYf0NOOfhICLOA6bPwtR7xdu/uQVwP9Tuk+7NzZogZ4BKJ4+zYBJQZSCwAN82oMBf54GzNOEICkAYp6W+x2/78uqHmv5/Q5D99it/vbyxi9PGzwrU9AdBPLndsqsc+C+YEJw/3A00PZvrVmfsgFbgroICMfdgKLQiCBchnbJiAhdjCADL8BgDyUY2MMoOiJIHKMJ0AjDDImELgoTvkeRtB9hBJD3cOVpyiKd9EVd16d9CsEDhnJJPwSiMD9EUCSgsBAmGCyi6RAH0L0PzQDVPkF4LHpC+L18nsB6YvHbi0fioKeIt2v28eHmzMH1rLm3TySoyaHbDSN3mFmbcH9B9l7mk6dElTLOWGQEuT8ut9Rm4+uHzthIioTmS4Wdw/u5YzObKJIpbbPK1TXq7iB8UeCdjwblEYqQwhW49SINCF7y5md9Oa6U5LCSstQnTX1dK2d73WwRLLss9MbmEOToH6SNEVjllsjLcydHK7VocylFCGa+3EGKLWyCsGqWJqGvmt1uDL1g9DirQauqsV30thb34VZXDT2nz/5R2mYnyNdrdXu0xCWJVOWKXA/WmTDVxTnQRIKOLh5OqPZxh4kopdpEQK7w3nXHK6deku3QBNYK7kKrQw41b63KrSVEMC8yh/WWkKxb7h83Ro0u0/ES+ut80OHNdbUoDzpiuhmujXnJ5FI5nBae7dipvrOFWxGvGueKyl0gHd12o4h6fdqa0hE+DHGAHOA9IZ5x1HfR0mbEoE6z/jCMt33DJ77gVC5uZ8FxrPY6aeuWIiEIxO3aFBvWeZha63PTmZSlzv09LgzobdPLuwo4SrmtqFWxgCCzaQ1jVaeaYDgYB1lFsJNJRE4rEyOJfGMOgcXE5y1JrhedH8mDejODRacW1cFlwiHYrE2i2qwy0pg7mRLCjEw27i0OK60871WuZh2K24VGNXSVZs4PAhptDifiIrIpEYfnwLI9hUShNeYTvin1jIJKR5y77OS8nQ/oTr5ijruMWFTlV8Rx643ccLFu5pGIcDFPmSojhIS7qJzW6IvRPzTXgwlJeCoJESRViSNRWuvshUt9OmWyLjenvRzsU4pf4VGjNGcqdw7AiASlHK9Ja1wGZknLY7z0ajPIj3t4iTR8G9an0aaNc9A1S4xqgQMZ7oicMMMFLo1lVKNdjQtmK1eFwvdYq20PRrIjmjktro6IKmJXbL7TpQrTDlaAUYl+HL2lRa8M59afx7bhhA0h1DmyPq/XoxvyfttFi1FSN7tWRivmCvvboysc2kR1mkXEBgtMlX0C54zNwdwVUg0ggfV8SMnVcpmy89N5W3EBXC0v0Ypx4n4ZJBl/pCUiXV/bdCglGZeVK154J9QWcPtAHyP12GmCKxO7zFBMgkVXGFqaQtqcBfxsC5mqaLZ6cXppLusFER6Js4UeB2G0xPmtIC4gDkq+pPuIxlCP3I9j1qfRsW+6S9tAxtYBGViONjKvR+6+8dZuvYG1hXjqpeOaCo6CvnY2USePkTKYKxs7o4QB2UV/qs5nVtc7ukoDunKQbeeG8QUJBKUfDckciuXtwswDZb6XzyaOW/Y2FpkziCmwj7oYwwUhkVqfV9dzE516WOOK8SJka4Pdoidpu0/P81ptO6vUuGVapsvO2pRxEGXJXHOKHMGrdUNvd1GqBh27a1Y8hZN7NxfslTlfb9mds3XgTCAx/1LtLrK/SEt+HHkvTuyTf3bdYriucceoVx5n2g7gL6I8CZ1P6PT5YpKCeYASPiPX9lVK9WBF7Y5sy0RFXiv96SCKUGlurQrYKaKCJbzjjyPYHx06Od3SG/OCKaNNptYNkNspEmFQlNzKeXe6zfediYciUIfBuqPuFMM5Vq1tZNTx2rc4PwzPmWYZ7EpcL6RMLkXeMIfuduYJI4/Ou4NGbxvDnIuxiq94lfWzvX+GmIuxGQj+ZlXyUVgFcjqO3tgL+bDcra6xuR6K6846QYl0MuNEKcG9qdqbrS9sqKDfEl1rqtLmdnXdnpWdlSalySYwd4C+e8tyNv6Yimy9OFxlmyc0GT3wejxXbEt0fB+6bkeudka32vuEBwEmVhn4BnGjmpaJEBAIw4QGTCmFJKPrjbUKnJPX9RhON/WIEXWbSuOeFNkrIeYEjjCqoK2K8lIXkYO5e05M13MdYiD6UOgSP587dQ7RfV5iuUjX54UCN+No+GYfH6+CdpCuO6IW5UbdmuculACRH+F0Q89hulwWJuN7yTqLkRUNsaUnDGe9HdxM1xkmPXCrWjkKmFqmm9IY8rInNiyiL4e9s2Qrq+Zqa+GuDkrEJQ6zPlf4Ak0KYz/0417PBi32VOxio6vhmvpFWZ3d5YkN62M37A9Krztk2rgCwubUxm1RBDtGt1O602jpsG8kTLey3bm/XYvWskbB3vJLQTlLlqGWTX3NjWDJ12pxYu1IQ1L90rShvjRIb4G5krm56QeJ3OrDPqBLR8KycSnpVziNriQ0wCGHsUeVCAY/81WMZ5HK9QR6nMd27LLNbluhQcJ7hyqPTXnh0+bJs66IEXJ9k+aErfdjvb+OO/d41ovOrxh/2bZwfUJiJIBNS0NCMxylnBt323rrOayuUAtnZ9L8hm3FOJXzshyCZtxRrHkW+3ysONVG9sg5bm8uzZuGdFtnssClFj1EB4XudHxQs42blGm4vMpbtu+C7HZthii+5bGjrOyCu4xycmGNAUWLk1Bs7UbEDt7cXjkqWm+6TWrtyupC2IfUjGOycGChEutSCwbx4iq767ziJLjmEHWzmBtVsiFlZNMt8+MBT1sHM9FUEW/2+lZEQsUrqdHiO8w5EgVd691+v69ZcVH1p/W5uG7Y62ptKI0ZMeMePtEp52Rcs7MZNGdal/aYJoHD03EcD6w9rOAxDIItv+iKGlGOeREsnTgdYcpjNPtS14siTDve2VIsCdMeFSW21gKKN+yzH3qUiAw4qA5M8nIsxtUg59lFoDCrLBaHBIfYM481i47i5CZZsqK8uMhCGd8cYDetq4J1ejU8k/d4MzJSKMjqwDqcXId1C9iwTou4OiS53Gd7Kmm4pZLWB7g8IOdigSu3DadrFt3RRI3553woUtSU8h2OSDTHskuu0qimt/LFBT/pSRxoNbpdloSCcZHsq/kaD/V4xCvyuHNKjDUTYZuJu1OaFSeoVvBks2JaONO5Yw4om8lvOsT2pcA55dKFMsqumvVGPlyP5XZrNoXLDkvgRUkNZzvAXUnUSbsSJN1zBZ8rxLWlLHDVQUBVXbXrJBJNFy9diF4DJ2MhkFxRvWjgjjYue+Y61F4vVY2zLbVNub2FlXHFT35i2T1CXVddVp/q3fnsRetIWah1QB8D3FUqze3XWsqcDHR1OOpwaHBOf8H3xMEMeEztKpw6BVdXhARjvkXXlHDpfcsuNgiyxs5O6qk+vXRCnYfJZZ8a4s5h8d6Uz+I5LZvtriKKutnJyWqAStbebQ4RQ9QILVSIN0Y8s1Z0SVDnyWA15VnvIS3Or7ZyWKbNAT7aq4W+thiThFjjqNLFro2XvWt0LB9ugpVuiwbezk3jBu/q1TI+3TZnH+86aly45E45mUoIagYjkpkDfZaQla076nrcB7JpKEeEx/eKXmeDHuZKuZBEnNpGwy7Ot/SI0yhzymAHgc0gWda2XxRSqfuLbLtI60jem6F11ULOTYZRlxNNdsb2vNRqPGQ1NV7mZXfDWFCEbWDAR+ul4kucS+SHyj4tcHKFViSDkTG6ENl1BkusRPM7RmA3EFRnh+2tqrd100LnTOx8Ed7cAC+CdINCp6LVQaGt4NnGcBypix15dczw3RW3MAE6JuL6CJ9E6yhcJAVBNYpY8gel7FjWjzfEEbIoAff6gD9webW87n2a0rqUDCCZ28KgeB7XmuhYgB/2263qZfBIxlk/bzbVIAMu3xrnWqZBuAxokWkaJBEsTocn6nwm4a5esjvFR6JgAzaBwcKK6Ow6rpLUvNULMWJ9KSCZHYNfYEhCM7Gah4dOvQRDDclj0BrE2EoxXUQadiS2l+DmH64ETdFew9260fNvVG6u7VM3nvXcdkNdR7Vd3MFJod6MK7/cWYTpKSsE020M7Cc91NXWutGU10rSnYwONG5BneYoei7xuIA99XSmxvCy6mp3wXHsjfM7qdVbPVIb/XAqEcXeRw5+sZiDavO7cbcMoHEVDWeVPrQK78yPKFbuVMvRaJI/+b5NlSF1UcPTOLgaZdsYJfDQ4pjUmDWfFzakFqu+CckbFNsHKIU9bp5xUR2u+TAtjGqrcQhZmny5MXwmti4KtFBJkDQdXKulIrBMqeDgNe3TCy3bWwvSCB0tVrk9lWeRqDIXGO5RnyIyEIAZ2h/agN9TPSFxSJZmMtlT+SakN7d54S5AtbCRrwPEhVvmdDiRh5C/SSTuemeRWc0XtHLLYWFMJQnC41Abu7qHdiKxpMej4tAZOwSESGLMGoJwNsePbbuJNcQ8ZAwESUjmUcVZG4MD2cxJhMGAg1nBxp/vUpfVL/qC0KKFDFjEKMmyrqoAQlzK4QaOL67NKR4spKO2wxzNw6YSEgWPzloY7MecKjF/u58nxZr154rRlbEv0ccV3u2GZS+7Cro8wVbnjtZ6DNsLQsCoxV13S5c4B5dduVJI+TIie1Vj6WWgHsn9jVhhC98TdAFLvX7O9Wwxv2KqGyodwiRaGTtbhN/ghnoRWqpkIowqR9oPEkGqtAMbpKPL4Ri8GsM9v2AtF12o62Ujdk28Nnlhf+QPqEhAV/FwkPzEuIhwg28NsEWy5xtzgcwp1NOCrSTvEeBcPrOUZHPnSqCiqVHEn4fEab0RuYu9HxOMjlumQ5Bu2xskqCvxkbhWzm0M+Cymt8ANRYc2FW8XS3SEslcUqGdQfbvWVMjpbl5zjNudlCStClUuiR35honClZcbhhFhKGOmNSmG+fpiwG4b7FHa5qmEyHCO8+dnYdGgAoXiMk8ucF6k20CkTPmUQeIFESp1aMi4YOS5iKM1cuVtiHWx8DKW/O1ioZSNDk7HXEiPJHosCGgVXspzGVT/DE3m/BCvxjl9rULR8S7RXBWP3GgRAlHt6K71lWtI3SBs13Qor83jIBf5NYX2zimKdAYGll6ssHylxbyduJZyUODLgBlXgkRsSnBVwRWultWKcD4/ra/8jjNKxbBvO3qOcf2aVCCX84vECUGxn1oYcr6s/PaixLByhm6VtfcKjcUqB+2XC2URBxs2BWm9uvpXhldH/oAorWDzHtIlEBMoI1MnwOd33FVZn3qIGcWzpTkDrYkLpkBAtsGgBSIAU0k2t6RtIZZGVeS5bUMbTXZE2DEel0JYqwv+6HV70lypHmx2C4gZOPp4XMQQZVmpDWktb6a6fXNhH1tFC6LVfELeIBcl0Xz84in+iQ6pZlgsI57YJBGx2QdWRR8Q2CbAtp9l9tCR9PaU14d8qciXxQ3nA9lYVJ1sJ4ukFipm50xx4q/CYFkEe2KJCSW9INQTszk1orPXCioSMdtng9Mcl5Z8KtWufGZZ9m8vn16mk+7nefW/5UX3dFL4bzuwfJwtvr3vuh9Xh27w5T7Xl3+Pur98emn8FCj7OMxt8z5+Hm/+t6Pcz//KG5RJ8vB45zy9zrt1b68KOjeefoD1kpZB33bN8K2t8v5+0Pzpxevb6Vcf7bfngfrLHYyink7nf1w8uE3SJvzWVWDpHbh6mX6VMb2jCoP00T7dxs+D708vwQAsnvrtN4wkvoVNPYHwfCcznQlPL2Vefv+/eEo1E/UmAAA= -->
