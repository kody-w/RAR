---
name: "rar-cowork-cookbook-dashboard-finalize-project-contracts"
description: "Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_finalize_project_contracts", "rar_sha256": "e8998828ada5baad255acc6e7f9a7c6cf3f1221c46d8a059d0bf3ff960667a6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_finalize_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `dashboard_finalize_project_contracts_agent.py` and in the RCI capsule.

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

Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 e8998828ada5baad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_finalize_project_contracts_agent.py` first:

```bash
python3 dashboard_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_finalize_project_contracts_agent.py   # or on stdin
python3 dashboard_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_finalize_project_contracts',
    "version": '2.0.0',
    "display_name": 'Finalize project contracts Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4dbeaffd4a1eff25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardFinalizeProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardFinalizeProjectContracts'
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
    print(DashboardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVpb2X2FyPlR5VJViX6qjIwaBFhAIiUVIuBxldhD7JgR+/d/fi6TMstvtmfbEfBhVZKWAc89+nnPuJX95sbs2KuqXLy+ab+fQ2k7TOPJryM49iCv6ok7AryJxwA/kFnlbx07XFnXz8unF8xu3jss2LnKwfF8XXuf6DWRDjZ8GnydiO859D4rz1q9tt42vPrTRZQny7CZyCrv2oKCooSDO7TQefaisi4vvtg8xgL6BPkNF6ecN4AD0GSCnLvrGrz9BeQHxGElAtgsENlDu+x6Q4wxQG/nQNfZ7v34FCvo3OytTv3n58uNPn15i8P3lyy8vbmo34NYL/6bF6qnA/iGfexMPOKR2HgLScgA+ysF16ddA5Qzc8vwAel59nOz9BP3HfyS9XYfND1++5tDz8/Vl+qd2+V2ztrCbFijq2qXtxGncDq8Qm/b20EC133Z1fncecHEevj5WfudUlNDfp2cfH0JeQ7/9+PUFuKe2pwB8ffkBAr78+lJ30/fXiUv58YfXtAC++PjDdz5N59yd/Pd7lF6/Pa+fbAHhd9I4uEv9O+D6CLXjf335jXHT56H3ZCdY+fJ6KeL844MxiObVz+3c9T/+8Gds3ch3kzRu2n+J748PxpFve8Cmp+I/fLo7+Sdo9jToneefiy1BWP+KJYD8Tdwn6OmoP+N99/8/sE5BGTTvHv+n7P7ZgtnfoR//1Lb/asEnKPj6wvspKLjadlL/C/TLN22/5H784H2/+eGnXwHr/5aNVnS1e+fwLbPzOPCb9tu3Hz8099sffvrxQ1eCXPPt7FtXp/+M5z/z613O7zz4pPr4+7VAvpEnedHn0HumQ78U5b/Vv75CR1C03vf7zRfot/UyfWbQZMSb0IcLflMzDdD1N3784eVXABI5sKZz749Blf/7v0Ny7NZFUwQtpLlF10IgwG2c+ZPyehQDbGrutV37wK9NDBz7pHui2aRxEUA//6d7B1MAiw8wnb+D4Lc3APz2XPLtHQB/foV0wLuo43CigVR2v/+a26Gft5PcsvYBHF7v0Nf6nwEWfZ6+THD587/C/tud02s5/HyH+/iBUionTAjVdKn/OllpRn7+tMkFHcK/+W4HhKSFCzQKYoCvn4D1TZECeG8njzRJnKaQF9dAWFEPd97Aa18mZj///LMDNPuaPyAVgx4tpJkDgnd1oM+fgWlBGodR+zX33aiAPvzy6wfo/0H/1ao780nGHuD7MyZAQ1FTdhCosS4DZFMrARBse/eY/PLr08GATQ56HohgHMT+YzHI0cT33rytbdjPKEFCjg+8DDyclUXdApyG4vYVEgLoXV8gdHo0IXlUNC3k+aCDeX7uTs3JBua8ezIvWqgBidgEwyeoa/y71J+d2r6rmIFit9ufIZnbg75RpOC/Sc07EVhc5DFw/3suPO4DJvWHBlq8sXiFdlNWQqVd22VU208Zgf2IC+gXb8sBcxu00f5rPnVJf3LVvUQe7gFEwDPuM6Sfp5iDJp0BPPCaN9l3Gnvqbvq9y9Vf8+aZ/nY9hcIF7QAIDbvYm5rC354p1URFl3p3/wFN7/37EQXvGZV7Dq7+fEYQ/nG6eO/r0NcOhREc+r82mUwGseu1ulyz+pKHljtdPT8cPfGfAvKYycB8cFfjXlTfZ4Y3xHkD3q95GoOsqYe/PSjv4XnSPMCsq4EOKqtCb5bXd7731J1Ssa6npLe/5m8I/wm46g5nIHqgzkEdTOn3JnB6+qZpBBw2XX/v9vdQAweC5ADpCZWdk4LUCYAjHNtNgFb1VH7P0IA89qdS7KPYjX5nFQS4g3QB/CGgRAxcDrrA3XW7ApgJKi+oi+w7eTzNUOUj0h4EJlj/FTJBBU1Z1ICyBYPQRAO88OHOCsp84GOg4ruHm8guH8pMQ+9TQXuKRZGBxP5tBJ4Pv+f8XZdJfcDV9uwW+LKfcNjzb4/Ivuv5jBVQNpuq9L7o9+F+2gr9thX97Wt+1/Ed+kHxp1MX/41zIJDLWXNH2wm7GoA/mf9MIJAJ94b9+ui5j6b+rsuXP0z6H//aZuDeRY3fR+4LFLVt2XyZzx+d763xvQLkmIMciUu/+d4EP7/V2udnrX1+r7Xf8X646gv01/T7HYtnYn+BkFf4FZ4eSbHrT5n7/AB3cJ8X58/49PRrrvrf4/xMhgl702Eq67dG9EYCulFY++FE/GhMzdTPetBC70gMIvE1f8+FZ6UAoM/DqYs2xW8q+N6RQWQfgXtvGOBR3gLZ3jTHhf60zUkn9Rv/5Uvepemnl9zO/H9xezM1BpCxwCHTxgh4HoxGbezfr97HpOni91u9e10BQPCKL1N5fYKmkfYT9D6dfoLe9gv3XVjegQ3Tj9NkPIkEpODXO+37PtLxX8AmrR3KSfnHJmgayJ6D8h+VmKoKaHyH2al9Pct0kvgHJuBLGPr1H5ko9y92+sSKprWn1h23bxXeAD09MAh9gkD4QOWBYgIY2YEFfxQD5NR+1YEe6U3mfvffd7OKhy2/3t3QPnaSv7y8YcYzBs+pEZCD4vzcTF1yDlIVCATXj6QCz/5H8+STB0A6MMsAJj7NMDSN0kA84di2hxIEaFykTwWMTbmkG2ABgqKIi5MebcME48EOuBUwJEySlE26gN8jPb9N40A86YXatku7FIJ7zEThY7CDuT6CIh6F+YAFFtC0jwMXvS9NAEw+jX0YN3nyfbSdnPK0+ZcXh8QB5QZvBPbx4ebM0aZMylEjh6lJ/2ydGMGJjWpwHOqAJFfyUirraiGyg0+p/nJLiayrpTt9I1i82S7txbU4BK4wGyyc2gzqamtQ2u0gOf0yTcZm8JR5cME2yoYrxJBZHcy9GMxX1dAgHB1XxyyOQe/UbMyiScFklrnP7Z02uwVBo3luje5XFaEz8669UiszheOzmuXrTLWonc2tT5ERWxuOkFHctKr0gs5jJNdFM4ZFnvWl1cW1TdRMVf0YX1Biy8xneH1bLNrqGMbquWTw26xCzrynOUvjeEmsfCQI73TpKR/b36IVSgebPXGmL/5ZjJOYFLPrNj9VpYSMcaTW5DHjNIaQNjsyahnhmO6rLhJpmS7TE1CbYSJlXB+6+UKVbXFLVjbPEl6SguB1l1VkRbOe0But1kqxVKPWH5Zj4YfFiJ2jrYaY/Yk7ncwVWnuXxmZOVXfWRnIDsmx5MK7LZlklWni+3IKSk2eOIrrigHJ8xgUnmE20etlsj4c4k2vLG1CN8W74evBMxeLlQlivqlZDwqZ0t8TQmtL2apRlJyeIHbd7YoceS0PIDvN6k++q0FFiw+zay2Fzu9HOwewv510LI4vSrLG03B03x/a43iVz7AhMiB3MsM1DcuZpRq96teRPS5rQjcAxN4gQna415zlz6zYWymFd1l6HnvyrMqxMEwsW1L6+DcplfUTVFJ/DNDEuXRTJlsKJxbJw2O3PZT16ViUgA93vlapShUU1blA0vzWrY9a7qKn4FWV452Hu7EWbFgSmv5015iJrEbKTUbk5W1UOc6Y+cxnmxFF2RyLClbjul9JydLvLQs3GJD6UFjcyVzm7Zk1WTz9HC1G9tnbUMCct74QLEh4eqTWPCxuUTxQiEbhUwhbkGc8xbMRnN4kX8E71PY/AGNFqGZXqqiTJzJbAiO1t5ddadSvcTHNLeTdEyGUt8+eUx0eb27BWYt+IRhVJrg3gZWkqh55E5sU2iGHpqK+VopJWCJcO1fG6uLD73lGt1R7Woric3VBVcAVPEtcOa0irVKOltbfO9VTZLMfWl5cYW+0vNYlcrRYnckOOKYIXFE2tNrqIHsq+1Fz8IlfWPE9Kj8j708zAZsuljfWFhjTMtZj3KFhcoPIy5/W+3V0pKtvi2PGI7kP1LIeocbSJA+r5l1uKUxdV2e5Ngr1qkUVFOGk35HFvo25P71qyWhmYUopp5EiyWhlqP2uZU7xK8n2LLY66pC4N3IntwpUIxOR8+3qUzIs7P5ntqpo7+iU6r1Tp7JIKssPhhUXhnHXEUTraksvQ2GEabfnt0eRvK6zabOH9PrTxWvfdAdHX47BYU5WFaMVJW4qoO+uGRCvVHWWA9HeODIeHuUOtPC5F14oeLsNcRHvedGPsapdn75gpG/M8Ekti4L2VS6RWhskhLVrRbkvkx8JobgmBHLDKdi9nwWQDntY9U7B1LyNgd2jPjq1R1xuuD8Fe2IeKvh2r09b22bnNRB4xgw+kg9gwlcnhbBuz/GxObbVo7gmN31/GRjgPVrrYdTbaXC5MtLkl2XpUDrcLeShgjL11J76x+l15U8NYwrFKstNFKg5BgzIza3dZEhstNiKZkghyzh3QPV2fXGTfWdur5LHpctNWxmFecJqdyUpeO0kvXKLWMLiNuOWW5aY6IGts56AtTdipLxYLpVW2aFLJO0EtiTNVJLxBNzd2sVWPXLeMxsLYbT2MMZUN77ozdnso67OyxPkeOSt95+Q+aI03kEYEppuzU7AfB8a/1niY2AtHSzrXC4JNKW7lrGb0yCtcjQ81c6MXnUUH80pYnDGXuc1IfrE8CSmaNL5op6f5diM0DdgQG9xNg7dmyyIA/o9irLGGw15EXYF9txylQ1hZliOWcrJwzy1/kmFiqNl9x0a25EWSu6pkR6zsfFGpxAW5iZZ4gOuDGaIBiy/SqJGPw+HaFUZYiIf2tChhtLVCyksphDguNUXH9zzX8NXZq3cUnQvladmoRynh6BUuayHm1KOfalbbVZJB5LxIUoaz7i6w67CsoVZrmHGHcZbC7UxeXtOt02hJ7rCjc1OcQ03gdOs5/a5Gyc1px+c2Zu40T0lIwUBsK0vcGutmi27ocFUwsrqdZxuL6yPLvF2Ey+YoM4IQGbaDqqe9Hc3InEgy1h3KRTq3yPWe0WlkMZfZGj3uLPsYirTpWPO2XR/5huNMob22zoq3ClxIzsvFqmic3YkfCYcVbn53roCnD+WM223DHdf3Pcp5FJ9L/lFO7MHdwwAl4mVlhTg5q8vW2F4cjFo7yin22WLNV90lODkmddpWbqtsBGM9RmLZCLoyI0l9pua63XdEZJCr0xZVRkVte50kiQQDMCohFS638/NAKdmq3CZVdUvUHRBztFbn0UOKnSAdomNah7vDDSDzeN6IelWVGcZwFxkrhmVHa4bnNAsnyqV2Me5Tk4XxrjrEbSyu0o3HNqak2qmQ7VRRXotFFnGXhaEcMjNo24iBGzTdj4e0XOQhfdUD3GSlWeV5+ZjYqM+VqwMrSB1jI8tNbhtolVGSXDl0zs+xnvISx4OR0OXUdhuubuq8vCBwGCt7MLeh2XVxJjBzXyOtUWLNDEyF/HpQ0pPShi4jJ8r+sggXNFZbmOb2bLYu2PWaV1sSxlaFsKX3eEgaVa9LxvXEgh8CcQ2ihcXoVGyWfpqPV71OK1REV8OhS0T7psbEVtki8uLGdNSqUg0Jq5ywOSMjrCr6qW0NGjPgyguXPHvu82DnDAdh7aJLGEYkI952WlAbnDw2R/ZAEJ1faWeUlWc6WyaHAW7gLRyvj0S5wyNigDsDbfdd0lCsNFiwU47kLRo3qua6HSI4cIjoOVIN11igDGTFzVlEzOoluV5oxiiLq1XfRDxoCQaWHHdX7exeKgJVUVk88MycPsfXeN1EegCfz0Ftxk6YbXI11btcGYxiVVDKpdHlY1GtSVnkkFO/KeulR1VbcnLzIau42cqBeSHweCWM6avZBJkstqVtjM6abZ3l6bLaURZKcnbGJvuNjEZ16e28tKDVhpAp0Oso7Kr5+4130lj+WsXWYMWymiGCrEcpGbAHZdno1eYo3Q4bA1aLMjbGsNb5w2r0anYTCojPrK43OArkSvauZzUgCdI/XuLY2K2PCy/tTTqzjXBhbduyz8Ntndx6ltcIYaBXi2QHRgbNcsy6Eox4qQ9Rq5F5uj1q6IiBVhMQjXBDBdhaB2BC50Jrbqvh4bzPbvlgEp20VXViXdoc6S3UHdFkImwlTE4t6t64GJtARNd23Kl5tOs8mq/rQ3jc1fGBi+CtF6+OigUfsPNakEtk5qwX5/ntwo8ZgHaRZCvBx+xDqxPHFWZft5YRZovN7LRXaL5Na3d+1aRcP+rOcIl7hXTP3MrRq5z01qxH+EJ3rNXRGkIOESUW7k9aPdPk8bZqpNVKxOnaA9jPw5v1WY9DD2WbQZYJW1r25PpmgO1ItJ75lblOSMpcos3B7oBW7FGl2wrjdwuaVJwcubLGKHILLw7nPDEW241GysLlnAsbp3HEVjrTJXU+COlcDU/nY3NFy8YLeAodMGXuGhQjHmHGA+nO9Ww3eKerfbzcnKFPFwHrzrabKuo0mDJLkRKdCGx63ADZsLSfMum1RWt0TpK1ZcwwlfZP4gWp51rHhP6pJ45Uiyp85KBgjqj4mBXFKnA7GbT9bXmDfTKWM3xf4oce3/Cpjs47B+1J+0ZZiF27GXW7hupaS+xkre45U4sxxulFfOAZNwuXJ9Xh8R2+Qb121NnDmt4wbFBh7JWOiC1p5mxInudmFMsOpqK3xmkYjYZ3pnmNCn1HbWczMlz3fXASNCo0SQDtzJmHLcWgZjN0NsdDN9nS3pY6UYwxH2G4LUHr37TkgJGih0jOsO0RmqXbpab3MrK64dLsOmqthrKOtJfFqyFr/O5C8C7thOEZd8ztKiLCWeiGupvRh1zQkxETh6b2ZCt3UrzhV+xuyLbdWNj7Rc+TczOsvL7i0RNMDXkuryKjGZSEFy164xo4cuXjLb0OJZSmR4SdFUzYrWlztjTWV8vDuM0wUlvymkhN6VuzVD5qiwtBxurIZIHTLSJt6UkLj3eZNYDBvTnrLge31ubSor5d5+Z+bzjAMVWXN+ywXJ5Qebe/hqUSUf5I52UidGAM9Br1fGNjuTZuWVsT6CnF/XV7UuiB6OnEZnAmtmYz/9Zhw8I5AGjfKJQfLRtUDZotAOiONsWLuC9q29AbdWCseVJjQ8v14pJQS5LmmKRttCI/wrh3xXfwWQLb3YV84gpnZNv63DPkwlWlkWxaG2xqNspBV4TeqDkEV0mMi/WcqTaXG85woXyYdwsyYRvey1uGXmd7iQ9jfuGFScbVNYz17nbBN21ULS7MrM/TiukOCXUhjvTKOtTugShQ0jFF6lq3sYbZjsI3+VXVRhnfp000Myi1O7JzQhcP8TVQqeiUHxqe3iHteqajFILgI3ETXM3C2D7rdi1zEWH5wgPLZFfP6A0n8Zcr1tqOibcrktp0UchvF+ddmpA4A0oOVjqLSfWr7kkeNkPOsLwD0RnF3pOME6lgYaLzGLtQXThyz2C3gXiouGSV42UmdNrNPhzdXBhmCRdvxLpSHJR0V6NN5ZzkLxeFh84Sd8/xVnC9ztWgba6kVOTX08wKSGfBBsw1j+Bqk7EOMpd9xhvFkzmPvMvIwtudTTtd544Scmocz7rAM6eZjRguUbN4eaDS4DDDMucEe4dxfZ4dvPOhilljdly1CJPt2+HWrgsl0eS0oiyOgrVrNbdy3M5Cc6ElUkXO9nm+6A31alXzmR6h5SkznXmqKJRyrnvpTI5MRTu9cFSpIVyQmzYH/cSwNpwrus45GZkxhsWjMsPyciD9tt1jbdkh++BCH+PDKqSLeVe6m7RaBFY/U7Sik85ZsLz4rn9mTZ499u161Tasi+FDMSRB5RiXXSjjbmok631qo1cj22t5cbXHlEzzBtejM02aOKzM+OsJk7mT6GBazQfpqpAbN8tILCK4zV6aDUhB7L2G0Cw56hbn08JfShm2bNL2OK8MrgiK04ie7L3nS6zvwAO+ubA7LDnvcouDKzBLoKulxOspHoTSWCXSVhIUF6FrVBpwq7MThss96XqsDLRLmNWcVW4mz62z7YFlXz69TCfPz/Pjv/QCeTrN+187VHyc/729T7ofHfu29+Uu68tfU+unTy+1GwOlHgeoTdqFz6PGfzg+/fyvvImYOAyPd7PT669b+3bk3trh9EdGL3HudU1bD9+aIu3uh7ifXpyumf7aofn2PKx+uRuXlfeT7zehj5t3K9piogzi6fn9/WTme7Hd+s/L8HmoDBYPIFKx23zDSOKbX5eTsc93G9M57PRy4+XX/w/xLCGR4CUAAA== -->
