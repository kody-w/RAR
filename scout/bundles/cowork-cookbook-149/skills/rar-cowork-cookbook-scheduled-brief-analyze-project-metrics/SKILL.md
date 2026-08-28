---
name: "rar-cowork-cookbook-scheduled-brief-analyze-project-metrics"
description: "Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_project_metrics", "rar_sha256": "be18761bce6bd2db2a894dd33c8541ecdabd370b58d701aa65ddc1d47df5a005", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_project_metrics`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_project_metrics_agent.py` and in the RCI capsule.

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

Analyze project metrics Scheduled Email Brief — Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 be18761bce6bd2db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_project_metrics_agent.py` first:

```bash
python3 scheduled_brief_analyze_project_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_project_metrics_agent.py   # or on stdin
python3 scheduled_brief_analyze_project_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze project metrics Scheduled Email Brief — Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_project_metrics',
    "version": '2.0.1',
    "display_name": 'Analyze project metrics Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-project-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02dff7dce92305f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/analyze-project-metrics'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-analyze-project-metrics', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefAnalyzeProjectMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeProjectMetrics'
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
    print(ScheduledBriefAnalyzeProjectMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjVpb2X9HkfKjyqCoFYpOqoyMGCRACgRAgkHA5yuyL2Hfw6//+XiRllt1uz7QnJmJUlZECzj37ec65l/zlxWzqICtfvrworpnOdmYch4FbzszUmW2zLitv4Fd2s8DPzM7Sugytps7K6uXTi+NWdhnmdZil03I7cJ0mNq3YnSVZmYap/9kqQ9ebuYkZxrOqSRKzDEdwHzA342F0Z3mZRa5dzxIX8LWrmZeVszpwZ6Vb5VlahROvrEvd8m8zICz0U9eZ1dmsbNKZA3gOM0Dfue4tHl6BPm5vJnnsVi9ffvzp00sIvr98+eXFjs2q+q6f62wmpciHBtJDAeEhH/CIzdQHxPkAnJKC69wtgVIJuOUAS55XHys39j7N/uM/bp1Z+tUPX76ms+fn68v0TwYKTnbUmVnVQGfbzE0rjMN6eJ2RcWcOFTCxbsq0mpmzCshO/dfHyu+csnz29+nZx4eQV9+tP359yYAK5uTxry8/TNZ/fQHOAN9fJy75xx9e46xzy48/fOdTNdbdx4AZ0Pr12/P6yRYQficNvbvUvwOuj9ha7teX3xg3fR56T3aClS+vURamHx+MQTBbNzVT2/34w5+xBTGwb3FY1f8S3x8fjAPXdIBNT8V/+HR38k+z+dOgd55/LjYHYf0rlgDyN3GfZk9H/Rnvu///gXUcpm717vF/yu6fLZj/ffbjn9r2Xy34NPO+vlBuHLYgO0DRfJn98k2R6O2PH5zvNz/89Ctg/d+yUbKmtO8cviVmGnpuVX/79uOH6n77w08/fmhykGuumXxryvif8fxnfr3L+Z0Hn1Qff78WyD+ntxTU/Ow902e/ZPm/lb++zjQzDp3v96svs9/Wy/SZzyYj3oQ+XPCbmqmArr/x4w8vvwKYSIE1jX1/DKr83/99JoR2mVWZV88UO2vqCW3qMHEn5dUgrGbg/wOjgF8fEPWge4LZpHHmzX7+T/uOnp/tJ3ouqjcA+naHxW9PEPz2XPftCYI/v85UwD4rQz8EFDOZlKSvqem7aT2JzgE2umULQMUaavczgKPP05dZmM5+/hclfLsze82Hn+8oHz6wSt7uJ5yqwPrXyVY9cNOnZTZoDG7v2g2QE2c2UMoLAc5+mnA6i1uAc5NfqlsYxzMnLIGorBzuvIHvvkzMfv75Z8usgq/pA1iR2aNzVAtA8K7O7PNnYJ0Xh35Qf01dO8hmH3759cPs/83+q1V35pMMCeD8MzJAQ045ijNQaU0CyEDQQJgBjNwj88uvTx8DNqC3zEAcQy90H4tBpt5c583hCkt+XmL4zHKBo4GTkzwr66mDhfXrbO/N3vUFQqdHE54HWVWDdpW7qeOm9gC4msCcd0+mWT2rQDpW3vBp1lTuXerPVmneVUxAyZv1zzNhK4HukcVv7W4iAouzNATuf0+Hx33ApPxQzTZvLF5n4pSbs9wszTwozacMz3zEBXSNt+WAuTlL3e5rOnVLd3LVvVAe7gFEwDP2M6Sfp5iDEQB08dSp3mTfacypx6n3Xld+TatnEZjlFAobNAUg1G9CZ2oNf3umVBVkTezc/ec+ev4zCs4zKvccJP9kTnjv5TP6PlvcW/rsa7OEYHT2fzyI3PXe7WR6R6o0NaNFVb4+/DmNT5PfHxMXGAaeYkDtfB8Q3uDlDWW/pnEIkqMc/vagvEfhSfNArqYEysikfOcPUgD4c+J7z9Ap48pyym3za/oG559A0O/YBYIEyvn2sOVN4PT0TdMA1Ox0/b213yNaOlNxgyyc5Y0VgwzxXNexTPsGtCqnKntGAqSrO1VcF4R28DurZoA7yArAfwaUCEHdAO/eXSdmwEwQGa/Mku/k4TQwAS2cxgbagvnUfZ3poFCmCFSgOsHUM9EAL3y4s5oCGWRAxXcPV4GZP5SZRtqnguYUiywB+fvbCDwffk/tuy6T+oCr6Zg18GU3Ia7j9o/Ivuv5jBVQNpmK8b7o9+F+2jr7bd/529f0ruM7yIMaf+Tvd+fMQG0l1R1UJ4iqAMwk7nuePrrz66PBPjr4uy5f/jDHf/xro/69ZZ5/H7kvs6Cu8+rLYvFoc29d7hUAxALkSJi71feO96i/z89q+/ysts/Pavsd+4e3vsz+moq/Y/HM7S8z+BV6haZHh9B2p+R9foBHtp8318/o9PRrKrvfQ/3MhwllQVVbw3vLeSMBfccvXX8ifrSgaupcHWiWd8wFwfiavqfDs1gApKf+1C+r7DdFfO+9ILiP2L23BvAorYFsZ5rbfHfa2MST+pX78iVt4vjTS2om7r+8oZmaAPAzcMm0GQKeB8NQHbr3q/fBaLr4/W7uXlwAFZzsy1Rjn2bTEPtp9j6Pfpq97RDuO6+0AVukH6dZeBIJSMGvd9r3raLlvoCNWT3kk/qPbc80gj1H4z8qMZUW0Nh2p8aevdfqJPEPTMAX33fLPzI53r+Y8RMwqtqc2nRYv5X5W5J+moEAgvIDFQWAsgEL/igGyCndogH90JnM/e6/72ZlD1t+vbuhfuwdf3l5A45nDJ5zIiAHFfq5mjriAiQrEAiuH2kFnv1PJ8gnG4B4YHQBfCwXXhE4bNkubjlLx1qaqzXqOAhirzAUdm3HtByEgCxs5RAQbJo45jg27KCE42EmBGGA3yNHv03dP5xUcyHPRdbw0nYQfIlh6BomlubaMVHCNB1otSIgwnNAU/i+9Abg8mnvw77Jme/D7OSXp9m/vFg4CihZtNqTj892sdZM4nKwxMBal7hHVtH6Vve8ltdtXZYHt3AFfGl3kGlbnFV4EdgonIKtemYE+mRsRg3FbnOZm3cqcUgvGellyQnBbeKoRuJxH0hkb1/WR8mxzzR9imhsTHR4cS722XhdFYUt7zRTO5ZsqJWMZhpDpmF9kwuLHQrvstxrESxeGnSf35QdLCXHeC1ee0yTRElPUKhan9fooTk5UO4mjKiZoXYwukbWb0M/pmY73M6hBpuVPYeNXcyem3MV2dtqWGhNVixRM4LcVM17L1WhtZciq3iM56u29RuGXwV8xGC5x/HDITcTmLvoxJyrQ14Orj0sV4tuN4cthrgWsTMIQrC8VHU3t4PjZZeWKG8EJw7WnFN+PEBdpR/GM2Qcdvi20sdtxh1YseOPTrm/bOdaqRhbkPRFLZa3fSRxsVqzVb8UxbRocg1RiZESdexykLZMyfGGcLVkKDg6cHqM6QOn8Vcstk+Ks1fEG9XYcVAWOnpp6lt7EVzSTuM4OR14niwV2GQGDb2m5GKuc0YCQchOOTfMwhFw38BKzcxP3qHRGSd1wjiIsbxMUCmImJva6FgNwZtSL5NLIFJszJhVMnhYsh9arR4LsdwoQjB38zPKQ0EUGsOtOJYJC0vMpU23jrWw+jHbnrY84jTLi95KA6MfEW9DSJYcsrrKE/vBHddj5+SGzCgFwviDKFn7Eu+vCQoX/po3m1t3LrcWzS+IKx/tLwZqSm5iCdp1WKBNqN3KGA1DCCIEWwlgaY+a+vFqWAp7k5IWMdai7JVFWFYeZRzcHRvCqM6BvD7RVn5yEtOyWMUQWw0TvccPbHgNRZ0vLG74F5SXUCJFRbY7SRW1h8dcZnhvTuF9L4LEQTxV2m16pxCIjeSfIP2Clmix7BQzOQwVbvIGY5fnAs6qmzxfJbtetoJox1TKDb3WZ9a/DZwxIENMkKqLu+eCvTorPO522tzFiqvKnBkswGGZQsiiofYbKBuCoooUvt8n6M6hAzI61LJvjLShDDxvVqPfpVRoNBJnW4HD9vEKXUOr6yI9r8L1Lb15MoelkOpyS6Ht4UaVqSUtqes6LTyTyVNbrqA526n7UqZi9dghc2pNOfxR20KMju+P24qJvcG4MHhV9R3P7I67LjIJ3qSixA1Zxtbn277W1W4jLVQBGW1mo613acRSBBfxN/EQ52WKG0N34s9m50Sr9sYL8xuiHLxua0OKt3Avo8JdGPfIwMq4WRh2VqcmjuT1Za0qEDcvOJ4nrmSVxiqGRIq6jbQELqmGY3lkvQ8YHCq33bkaN8KZSTPXo+P+eG1i+Bof4gpodQ5X1q5meZboAkXjRY+/zX2a87NTHvYHk5Cv6xTmpeNxd5Ji4rop+dNlbJjqOAy7qBbycVPY/kW2D6G6c2xc6WIDgvdtsd6mzM6OYtbOsYQPxou/8mBEN2tebLxEVvNl4NRc1VLzdjDkzXazvOqGbahWx16l5rBra1os6kt9RNdnz/UjceHO/WO/cMlG0jbB7YhJgx/WpSWe/bXA9rdkd2lyyrvFcjpnMrtR0OQErzT9uG93VK2PJqVTN4JG5wt6HdKrser5s3daLd32NBgnVWbTU7SCXct09guDrLpBITklQbabwPP5TOQHgN8Rn532R8Xcce4O2kKlxbRbpItyFFrQnJ6aQRkZtBkI0Fnv9msDaQNU2CuOoMFpYvFBrkKjlgYdwkrBUO0LXVqmJ90t1cEebWzpUc1B6CUJ54exxOZOaoEGekbDzjoKsBqV69bhODnRvJ0zVOtEtbfbJS5uRyMl0KzTr4h3tZuu0pgtLbGFdcBkJ89aYrk6CGw6zBerPRsy3bkmJYl3ep3dcCTvFMo5iAzJ2F010jTcQ6opRrfF5yqOG8GBqbsEBXAr9qfmpF/7Cs8Ke5eziXShmXPMqvXG5HKICnll158QebsofCgvuagIZBGK5QSPmDlk1OzGvXS1eOvwLtcO4S3xzeXYjNzQXfFY2RemHVFugMK9iLeg7rrVxYgBhIAIOplEqTJhIQMpktVhGTaOcVGFBKG3OZaKCQ9yRRD3gjF3tydVlBARwNEuNtc0Mj9eRJ3iA1D9FN/TvJLlhXZhjAyTbAJbWKEVsMHWEJGlsuB0YcPrwkWgicOw5Y5m1YwKkVRJGc1DpmIFPuGR3VVyzrq22dg0LMuSs0tK88r5DkCjBC40HeJP28s2469OT+kNdXFNmo4t8aKz9DieAwU3VuezJkPYyaB3Stvp0Jb1rzJjr2muqVb6pcYUUqf0+JJR5Ahrmp4us8A4oWKSsR6ZL6nQHUvPh/FWPQNA3546sd0qCXk6XV0Mh+KAw7cic6Bb6NCfyEU10mhwyCzcFc1zYFetqTXl+QLhY5oUpmkomr+AjUs+7OV03comqQQ2TBz4Y8u56NzeHqBcZRKuX6hZzOECfKhpxtBQKwx56HqbCzZlrgiOdla8km6P+MYT9ILZd3AYKRnwkLOTtTpTqLPUpQeL9BxEyikI4syTlUneEpHWgR5wx2beD+JF2pw3jU/HiCviOKBVTNjRmBss6WpAEGtsHpcekpJ7TtLzK4+S8HLk1qd9lC8b1+HK6CjUcYphhnOo12y5u2SDrRY6QmhESgmmiERn6nhpZUTd709JmJG7HbXOUcs2m/Ntxc5pPuYqsmcEuWdKGHdTmElF7hqfeGdT4GaUw31MNn633vT5Vq/PRUFFeKxuVi6624SpBpooCKas7Tm7yGBzbhfpLvCunE36u9MibDCtEsfbdUQvsjiezqeE1yT9SCnqWT9dESzB8xOTbves6OvKzcWsG4nn2G1RsJeDgqmGQ3LUcQgh3xvQfHE9jxS9ShlzHoNwCMgNWsdxJ+tmYmf66SiE6xV9uhlcxPTFNYlv6NkN2Hk8FPZgRl5u7xT43POWMKzzecJU8vlEu05h01fD801Zwg8bVSzOi3zwBV0I9THEBIu5YHGoychwHo2eNfCicQiphrjWbzXxGN2kxk9PopdY7nHUySWRFmh6HbSiC4d4U1/UZeecV0mAjqx5bNLzJrr2XdRi5/UOsgg/jY1koZMcGvfnXuxdri05cSPm8w2JKv3x5pxbhoT0UySrzAWW92pj+9iOCKiMp6TjvMJvpWKukQo9+rQBV8uFz7tl2hjNcZm7uIZTJZs7ALsUMk3Kpb/1yMNSpThSxG/R4aQlJ2KVnVNqVTeQ2kNkHNNhOhz4M16vx4FM5rIYnY+yDmVqe1yfhVjcDW22LWnDnuv8gdhAVCZKA+cPipuJ8xbh6XWUrm4Z56eJlyZws2p1zmHSq8GfJa4MMcj3DcW/FpdxhyyiC5heyBxGutpfOagcERDunTSXhNFFum8jrL2lVrPmYuV8pQ3U3S5HPlDa+b5ILm5UppeCRWo7DFfR9lCx6npH8nOh3Y38mG1uC1k2s2hTDzhULG7R/go1uzC6rdy40TiMhMpK2AydrYPdgCAY+kEOW9AL+J217/OU0zDj2GBrL8vMUugzkoK2XoEMrV8eo95ZGyQj8KesuArGqlHGYHvROQbfiWcsSX3hcNlFfspQW0IUhpIDk85yDYkrwZXbm4biURvZZ1uJysrCu+BGnxSJhz2O0zvN8RTnbMolclJoYa4d6iuXgi2pNldkfBGgRARpCDwHO+gk8hC7QFaDS3QoU9TewkEatUF3PGGDTY51OA4i5di9Gma3vF5icz1iC2NURFMMtM5VF3LcHVs+sQN7IfawH8FLBNYxkbY3XdgE+9EYQvd8ODOL+VKgUJm6BiPNNysk7a4E5WkIRlOb5nRctN65sWyboNuCrxQ3F9eWcMIqh23JviXMg6uXtWNtT0tvqdXYktTiaF4zfbORikNrLP0F2D5yKV4Si1W0WZ/KritLbwFTC1ZVlmPr2PNFiROy7MSuHxzr9nRoMo3Gt21vr6ndZvTrxiQPF6elU2cjc8KRqqylptNjRJpn5+gCpJT7DaYeUdFvjqcFc7NZd1VBUIPYJZFes01zcY3GoWS02YtXc9DUo6g4w7J1zyjeJxt53OOqILQ+sW334mquHkjdb628Pe4lmBXEHtmpCujF9KXugtUltSxtFXhl3cfmadCu/C3Fj1dJd9Y1ugOTe9ZiENNBhCvTNUWYdT/W5UI0F/pijaKoPGSHprmu/d3VD90FBS3nG9SkKqRd2klXYE7ZQx1T0ts60FKjqUtifmHamHVa4cpcajxz+g6xF/bKyh2pomGSvBCJVs2pwAvoyxal9jrW7dOr0rostA/M6IiZC4vK91vK74L5JV/ClE0fpMFuL7Q99vvN6joWYzRk9nbFrMlEaiBnt/UCZ6ke6dR2jH6FUr1SGR7ox3v74njceuFSmw51gt0hkzTSCcergiA9PLoytSH13ZLkKtqwqrGz+Q2V1UFxoOaLq1wUdXOKvQiLV0x+Sm11IVlObV3XCLzkAyvgWm6pXrICS2wmhE4Lfh1fBNYXChpVL4ds0VmQr8/nNL4sL9xo47htzFH6uLdbGRZW2xUtsNeVIFon311LFnk9ADnGeml6xHhIShtsuzohY7pBZy+aaBOND0NeW9SDkZetuiTOYQdTLYhfgLP7FBLbDblkXZLZdCdtvcxEz0auN5k0FAm9rncY5Na3oxRB+uo2lHie1qxFVfMEOaFISLq009rFtvM8nbAI9spgDT4u3CZ1HRuxvHG3pxbOypvHpxW6cZfettyVRLZsIYVy5uWZPBKZUy08fxERpe+CXj7i4KpddLg8huc1SIE+afOir7d95YMNjkyTGGoWRG4J7ZqJMlGur6vrQYNHgL2Mx8w5qetBbq9Kj0FW8+Nx7WdBU1rp+siqsmvkzoAjsFGyNugD8Z7SsOgUqIR0JNnMWXokKco3m+uq3qaXXmPrAZvnOb7EqENeE8sKc5fHZYpXmi9u6ZbCD4TkGSjuq5AtRWhWFqCdDpdWYAXywG6ZFasEB3XLisOxWOUYLuA3A+ISSqhSMljly+uap24NdjucPMn2F6x+MjzHc23Wo5DDuNocsprgrKDV7CW7PKqKY43XgEiZhWzc5ipszU8xe0IooUS4bTwaYX+F8kWsbM8SbBlRWad1i5GshGM2gJcdNlTHqNoo2i4JMWorRrkOWR3TwwoGs7fUNryBCvB03ZgoseHw1BxpzHF7XFqQrFzg0ZzgTyT58ullOpZ+Hi7/1VfJ00Hf/9p54+No8O2V0/1g2TWdL3dZX/6yZj99eintEOj1OGGt4sZ/HkT+w/nq53/xfcXEZHi8q53ek/X128F8bfrTHx+9hKnTVHU5fKuyuLkf9H56sZpq+huI6tvzQPvlbmKST6fj/2DS49HdmDqb6L1wogrT6RWQ64Rm7T4v/efx86cXZwCBm8xGcOybW+aT1c/3IMDY5Sv0Cr/8+v8BeUy6su0lAAA= -->
