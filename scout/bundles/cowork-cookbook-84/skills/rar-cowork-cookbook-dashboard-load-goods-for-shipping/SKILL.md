---
name: "rar-cowork-cookbook-dashboard-load-goods-for-shipping"
description: "Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_load_goods_for_shipping", "rar_sha256": "4eede99ca6ba017d782c5b7ed68f42a5c39db6d4766f8916efa4eef9b8125e53", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_load_goods_for_shipping`. The original RAPP
agent is preserved byte-for-byte in `dashboard_load_goods_for_shipping_agent.py` and in the RCI capsule.

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

Load goods for shipping Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 4eede99ca6ba017d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_load_goods_for_shipping_agent.py` first:

```bash
python3 dashboard_load_goods_for_shipping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_load_goods_for_shipping_agent.py   # or on stdin
python3 dashboard_load_goods_for_shipping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Load goods for shipping Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_load_goods_for_shipping',
    "version": '2.0.0',
    "display_name": 'Load goods for shipping Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-load-goods-for-shipping',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a99dc89a7942ed30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/load-goods-for-shipping'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-load-goods-for-shipping', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardLoadGoodsForShipping(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardLoadGoodsForShipping'
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
    print(DashboardLoadGoodsForShipping().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abPixrblX1Gf96HKj6qD5qFuOKJBCCE0ABoQyOUoa5bQiGbk9n/vFHBO2dfX715H9IfG4TpIytx759rD2pni1xe7baKievnyovl2DvF2msaRX0F27kFs0RdVAv4UiQP+h9wib6rYaZuiql8+vXh+7VZx2cRFDqbvq8JrXb+GbKj20+DzNNiOc9+D4rzxK9tt4s6HNrosQZ5dR05hVx4UFBWUFrYHhUXh1ffLOorLMs5D6DNUlH5eg+nAmBvkVEVf+9UnKC+gFUYSkO0CbTWU+74HlDg3qIl8qIv93q9egXX+YGdl6tcvX376+dNLDL6/fPn1xU3tGtx6Wb2ZIAHt/KR8XVTaUzWYndrgz5eX8gbAycF16VfAuAzc8vwAel59nBb6Cfrv/056uwrrH758zaHn5+vL9J/a5nermsKuG2Cka5e2E6dxc3uFFmlv32qo8pu2yu+oAWzz8PUx87ukooR+nJ59fCh5Df3m49cXAE1lT8h/ffkBAqh9fana6fvrJKX8+MNrWgAcPv7wXU7dOhffbSZhwOrXb8/rp1gw8PvQOLhr/RFIffjY8b++/G5x0+dh97ROMPPl9VLE+ceH4LIqOj+3c9f/+MNfiXUj303SuG7+I7k/PQRHvu2BNT0N/+HTHeSfodlzQe8y/1ptCdz6d1YChr+p+wQ9gfor2Xf8/0l0CuK/fkf8X4r7VxNmP0I//eXa/qcJn6Dg68vKT0GmVbaT+l+gX79pe4796YP3/eaHn38Dov+tGK1oK/cu4Vtm53Hg1823bz99qO+3P/z804e2BLHm29m3tkr/lcx/hetdzx8QfI76+Me5QL+RJ3nR59B7pEO/FuX/qn57hY52Gnvf79dfoN/ny/SZQdMi3pQ+IPhdztTA1t/h+MPLb6BA5GA1rXt/DLL8v/4LkmO3KuoiaCDNLdoGAg5u4syfjNejGNSl+p7blQ9wrWMA7HMciP/Jw5PFRQD98r/dexUF9fBRRefv1e/bVPm+3SvfN1BOvr1Vvl9eIR0ILqo4jHM7hdTFfv81t0M/byalZeWDOtjda17jfwYzP09fpjr5y7+V/e0u5rW8/XKv8PGjPqmsMNWmuk3912l9ZuTnz9W4gBT8wXdboCEtXGBOEIOq+gmsuy5SUNGbCYs6idMU8uIKLLyobnfZAK8vk7BffvnFAWZ9zR/FFIMerFHPwYB3c6DPn8G6gjQOo+Zr7rtRAX349bcP0P+B/qdZd+GTjj2o6k9vAAu32k6BQHa1GRg2EQgovoBjJm/8+tsTXSAmBzQHfBcHsf+YDKIz8b03qLXN4jNKkJDjAwABvFlZVM1ETHHzCgkB9G4vUDo9mmp4VNQN5PmAtzw/dydKssFy3pHMiwaqQQjWwe0T1Nb+XesvTmXfTcxAmtvNL5DM7gFjFCn4ZzLzPghMLvIYwP8eCI/7QEj1oYaWbyJeIWWKR6i0K7uMKvupI7AffgFM8TYdCLcBefZf84kb/Qmqe3I84AGDADLu06WfJ58D+s9AJfDqN933MfbEa/qd36qvef0MfLuaXOECIgBKwzb2Jjr4xzOk6qhoU++OH7D0ztoPL3hPr9xjUPqLtkD4527incqhry0KIzj0/1UnMi1lwfMqxy90bgVxiq6eHxBPZk2ueDRgoCe4K72n0/c+4a3KvBXbr3kag3ipbv94jLw75jnmUcDaCtigLlTobdnVXe49aKcgrKop3O2v+VtV/wRwupcw4DeQ4SADpsB7Uzg9fbM0AmhN198Z/u5kgB4ICxCYUNk6KQiaAADh2G4CrKqmxHv6BUSwPyVhH8Vu9IdVQUA6CBQgHwJGxCCVQOW/Q6cUYJnABUFVZN+Hx1PfVD7c7EGgXfVfIRPkzhQ/NUhY0PxMYwAKH+6ioMwHGAMT3xGuI7t8GDN1uE8D7ckXRQZC+vceeD78Hu13WybzgVTbsxuAZT+VX88fHp59t/PpK2BsNuXnfdIf3f1cK/R7+vnH1/xu43vFB2mfTsz9O3AgEMhZfa+zU9WqQeXJ/GcAgUi4k/Trg2cfRP5uy5c/tfUf/17nf2dO44+e+wJFTVPWX+bzB9u9kd0rqBlzECNx6dffie/zlGif74l2p6+3RPuD4AdOX6C/Z9wfRDyj+guEvMKv8PRIil1/CtvnB2DBfl6eP+PT06+56n938jMSppKb3qacfuOftyGAhMLKD6fBDz6qJxrrAXPeCzBww9f8PRCeaQLqex5O5FkXv0vfOxEDtz689s4T4FHeAN3e1LiF/rSnSSfza//lS96m6aeX3M78/2AvM3EBCFUAxrQDAmkD+qAm9u9X7z3RdPHHDd09oUAl8IovU159gqb+9RP03op+gt42B/ftVt6C3dFPUxs8qQRDwZ/3se+7Rcd/Abux5lZOhj92PFP39eyK/2zElE7A4nt9nRjrmZ+Txj8JAV/C0K/+LGR3/2KnzyJRN/bE1nHzlto1sNMDvc8nCLgOpBzIIlAcWzDhz2qAnsq/toAWvWm53/H7vqzisZbf7jA0j23jry9vxeLpg2eLCIaDrPxcT8Q4B2EKFILrR0CBZ3+/eXwKAPUN9C5AAj6REsO4NunYMEJ5FI26hEP5HkkHOGoTLsZ4DunhFEkGNIOQfmCDKQHj0AhK+AQG5D3i8ttE//FkFGrbLu1SCO4xlE26PgY7mOsjKOJRmA8TDBbQtI8DfN6nJqA4Plf6WNkE43sfOyHyXPCvLw6Jg5EbvBYWjw87Z442iUmOEjmzigwW9YVJmkE6lg0ipTKyO7neViZ2SaZpVH4mq7PBaUm61JeL3cGrDv44P0SzQmWSDt5Jsbq+GZSWW5hllQO3LdhViO2JMfcW6pGD/auFj6klEudzk5pWJtmNCDZOaCPe1kSaNFJ/opgaG61ZryqzxnAtdMQwikgdzBAz+nZWo1yNdMm2HTGrG43g+t165jSH5hq2vDkXj7ujuEBNGSFa066Oqbom+6Rab3KMSEd6zDMO6+EicrOb5qQZs24HLY7bCGc2BSFn+hH19npDuntzm0sMSc/ideaMS1krsptV3UoEriQ/a7FKCbRaGE77rbHeu0q3FdtSF+E1hvdiZl7bpp+7g2jU6jZmWQMxlaEQu1VJDK5oNapRkUTIVNr6bMMpypsILloBiyz3Z3K9LQTE3MKoezLXaOVdant1urZnLSc7T7oapUaPC10X0l2/YecjZ+GYrXFjUxwUoyS8A+sJ7h4vjlp2NiuxatzR3M28KBFv2HbbLBfH/NKRtbbN28hd4efgmh/LspUTtFR3fpA5LArHSo7ZCD5i7oK4ahdj7WJL2vVMTqkFdHUOmvMZAc8J3dJmtVgOdTW36XUFVwZ+EfvNBT+B6smyjXCm8m5nX0QkZkbZoAg6Nfcz2hWlbElaiOM1WKXjl+OYwn2LJX1dVcP6mFt+RRf+otp4kRXFylURDOVymUtsLZ1sdkl3tDRcPdYKFdfyUXzWCLmCXttB1QmT1Pb8aePAZser+1owubk9criq3trtuRxFSZFNfeYy3sml7JakK9mi9rJUj3R7ifRsSOJD6rCjcoWzdCvqJiLq9qZTRNU4kfgIWwOT8yXD6iRLzG7SbL/HXbynEyIL2f1xfhYCndTduS7NWXwXH8n1WOXafEukjXjaKqXpHbP19ZwE0kk7J6bOzeqIQzxnuRL5WsusgNFIjPRWDWjytDLczhVJMi7FzvdkgoXxVkOMMST529CcCY7LOlw+CPXKE5OSDTRX8Ou2VjeacEPV63LtIla5SY+6DZMy0eNZdRmSjObU2gt2tCeHqEs6Nz25uCop4ByWtKxSW0FIGRFLlVzazxU3u1YhetNres/jGFdoY72dpXO6Khc42eZhwuh4K9R7MrvS8rGc7UOVU87ZzuHXBuzt9CESMH1o2cUQHxZyI67zdnMpr1VpMLh14TkmWdpaA2dNkvbGmt23O59f3tgTK3e32aHSyU0gNHP2MCaz1SL2Vkd/xx1v43K+PK3hRiHtY8djKy3ANbQoqT2vwlabDVu5P5xb7OLp7FYU6XIpt+Z1zpKr5LaqzXWeeIGB6zsjIxKiETI6leeFL9UkHMhBJ623gE7lqzNj7YxFFP4Y5TYVuXSO9DvHT8JEQvuV6cZwbopFOx/5VSOXdWxTIR+27M0dHVNTOarKzJiqUNY/jUZdUISkLA3RmWGXmXrxYrhAidk5l3N7jXIZSe9vTDLGy9mqHmqP43SqX1nz6zbM6YMxniuzUz1iRRKzOXkOLiDticBfEOfar5VouzR5xPXOW3GDhDmvC6U+JvEwILyLpwSOrRyRrXhun4hkg91Q4bAh/Zza1gG/sgfWQkuMcxSa9Lpz0rqHjkeXJ/J6ywRKpW7LU5xw+3zJOcQimfcWvlxZ4RCs7P6w2Gk+L/ALZGkrRYxFFqrCNVv1y7ltHD3t3MMCf72ikeju7HqM+tmhiHjaOuICh+ziiNqz/mznM8j5AF910+7Pi6aTcEXvPNovaul4IAtqv8svMLM/dcOsGLgwpUvhhmXAk+VW3GcUopVKXmur5HDcnAqTqN0536/Oujsb2vlywblSh9GzsWOwPKCwOaKjajAk7KDNRLPWEJGZH5VYW+jV4lLqPOy7vST0YUKchLImz4tWxgA0p1CU4AhfbgvFdLsDLwx1ll7drGSzLuCORjjXPMVmtjAb2D7XhVTA+oVeHdVmuOKwz8cBkhV2scHUDC7XhGJb8shUcRpt15rEEv6mbkrVNWVGE1kzWhZjHqLSZZg1jRXsMhFOGy716dOluWy8VbHAFssi7GvrRiSGt7Kq2rVy0UDPSLNFlxde81H1NBIkxffqZQMS0rdNadU2NkGGxk4rDpXRHEn9hukknjkLSuUuGplhwz5KJG2ZUYUc1bjRy+crN3iVk93GiqNiH5UOy8s14xcXPTdo7+A6CyZJLqiJNrq+Wmzy2R5z1DYEFKQOabrK4NBqeIyLD6FwIa5UCNodERblQ5fGscllYhCGN2F1qOt6F2ZtX4pYpFtZ3a1mfGsI8tU8s6vuSjontkBZZsiGlMhjsSnwrkYwhPGr43FpYotE1J0+yYZhC1cuY7UlvjLUtlQrhnUSZ8NkQlZYzCrQz8tCS0mEWZpUYzm57sKpjjjbTFVatkqItXA5YAXDCYfWQyvjqOk0Q5XCfqvbR3h0yEi9BbDF6r5li1f0tAcFSQxv2CCjp12mBMVeBAxQpHXv0Fyxhltzu9zCIpftYnFkD9rlmgw2faFaghH8bFgdVsstNUMHpjYCJkKQbKfGBG6HBhfWLVXm+sEer3p2ta9sWxU3Yx8EWHcbUlo2N6PA3+CQSpYbat1slrK3U8exVBysXCftvEtXhJcXSI0Qcs5RNorZnYg6RRxxF2ENd21Uc2ocymttWcNS5WybWsBN9RxQS9c6hnwtRJub354sMjBm+I1YFoAalxrpueVRm/WutsUjyeQVM1Xh0zaRdgrlVTGb+s3GSVdqO1sLBiI6J6k51vIJltmQXwmn8TRfi2zMrOWdgqCgZYqzq7qvZDbN8CIc5gOrOMnRFQQXXauCWpXSQa8SOMc1imB1qfLLVvO96Ngs5inI3ouS86vWO0pjPHRbj95lbNYcjpwl2fz5ehJ2uYxjTH1WBT0lpLOCJAIjXK8ZrKS7aLCos86lpUVFAn4yh4112JK8TEv9dTgh2uVSI9tKywnlyCbDRUO9XEwMyjOTlHeSq+9zdZ82TGkpTErjHGMZQnfwiRVTEPTumJJMyFrV3rvs4LMx466LxqNx9LqxPTFQj45Oa6O9a1PYH47xsKMSHT7pXaU029ucLtXNwmQCbkz75JzuxP6Q6EcFFexLxpxvhX8VKFPj0itLBjyIW3yntviBXMbjvPX4XSpZuXapZqtTe/VzDgf930bdH3SbhisxW3OsGV9sd0uvrtViuQj7UXPLxcGSvEPqomYaz+KjHMt0YRt+WerHY0tijR10MModRs6uCeUmjauDfA6EAz/bjNpIVT5yTNkhwsLMWnUIXKOJWCQqSs0C+nBZsJ41kx3Nsclh1boxlRQL2ttJpskuF2KglaZoGRaMszvZim6OzVj08rK/8fLMV8llVbCENPdvylW/YjsYKVSBk2kxsBHKkE9NUyGjHTkkGZ882DHY08phe23m0vvh0s+ba2+wLRkPCrz1yyLkkQV59G7qdSGAkC8IMTXXpCBz/MGLQplfkja7X98W676VxvS8jqPs5tobMbU3OpW5uj1bXcPQOjAe37ANw+C7oUA2rtlvNdlleYRdM/XmdMEVrjpk5wvLUUwkFLBHwUmTCmp+FJZeY/ad70c2uUjUjvbEbm7DFBlXJSBWNeWMSIrtvZlVud1doiUZ0SpudErkXwa4HihA27cZg48twuNMe6Uvp93cIDERRZLYp3oc5GhHgS1h3uK8iLutxzoS2yuj5VrE+iAsc2UskfUOxtcJiYvp6dgpShYsDPdyBPRvnfbeIZDOjDE2SKsiLBEL8XpUxLOQqzw1OH1ncIMVoqHdittOGfo1dd3N2vm6E6jDcqYTMLU4MYGRuism1hmsLPuzuHMWo4Ouwe63U9VK0gfYyuaprvqHlX0ONq5LgbSJndE7X2Dfj+dzlLzN8QXIsVqR8NOcPuwp1GBSClvtu5jNUY20DZTzXOm8ROzC3gsjbOZhbc/rGJFAoapmfcIchrNi7pMUbA/YpX5pbotsLwewIBTzbXdcw5utPL+S+0tuHm/k0dkxSC8XPAKThrUJcZcyJcPcC94KczKauGCptCe1c0Zy6TrlA9hVu8qSZ5t+gQit0++xMYD1VWB5qsmrqo/xq14KJKcrxJnWaujtpggH2J9FLDPTNlXbw+5qmxayOrNj8swEcmRvZohz6eyTpe1nzZwYBjwiVD0wVGohq1uOofaaQ26iYjf6c+vmsFWKdht9YcqHdSUSrVXZMyYdAkrNT2MYtnS33nQ7nsqoPHelkokyPGTnitbkiSsxUUKdYFs++QqHJDkcNKJkCkNrBviNEcKDy7O7VAN9YG4pjlxJqbrfk7eFx/Mza9hy+6XbIAsTq2OGXLqqROV1Y+GVc6EW+zw8i8hlDdrwORtvOuoc7CmiOzXDRqr3x4Wn2UbadvMZQpzX6yWuWWzYa8oOM5dCvdnFN74wJYS6ecaVJ1b7Vspz2M15D56hmyCv8ryZ+aQreRHY0aMuc5Tk8dybMUYcmphRQTe1H6Ol344j2zHNmRKCygZbF2TsqiHHYtB4jt4qO+PiHJFPZ1pWnEOoMiBAz1LKrEsGoXwsdWQTZxClVw5SVNS7WWXjubWskL1/dJJRP3lVgzZrFt4xu1shqTOXCj18twkv44JbqeL8el1U6JVKSJkVl/Rlw5j1ZbhGah9cGFIX923mJ1UnrW6AHBpXGPAD2iCSuBxoh8lbfk4QLTnO/fay83xO2UcdF2HtrMO0wjcO3antpTXWHpugPvKbZjwkWBW1FEYpteHhHdJLZ6zFyP28rrszra58b750TucmCHiWVlVCJWLWlpe6ZajYambPo5zrr91ZLchjRcViF7ZMxRSgQGnseS1qMymnSPJILNUtbTqXfncyTX+99mibAvypNHNvhmyoI3wo7JLZNKsLLOD7Qt4UIrd2r2wXjyt4R7mRcZX85UmwSJRmfLQlIlL2NFlb1KEHANoXoJXcUrvNQBvrweEYPKfG5bhgxzPbbspD2oSrjOGPO2PFOHZiJct8VRfJYqCvKM0ny9vJu6XFLm+N3aXayZvcwDIV6xmSxhYaKe1uJk7BuhIxF9BLmDQq+MTgwWaz31JNJ+iXwgkBEYDdLtEM0rY6Bsg2REAJG9wbRZDO7LAcZ+1p4eLL1q30gloYqVqK7eFwOZNWw9JL1zNKa4uXSNbB5eDtXWU8cS5c5R5xXUvVbq8GPeugG5qJ4mSxWPz448unl+k4+nmo/J+/SZ6O+f6fnTY+DgbfXi/dD5R92/ty1/Xlb9j086eXyo2BRY8z1Tptw+cB5D+dqH7+t28lpum3x+vZ6T3Y0Lwdvzd2OP266CXOvbZuqtu3ukjb+6HupxenraefOtTfnofXL/dlZeX9JPxN48v0s4PpxLkAk5vi2/NHGvfb0/sd34vtxn9ehs9zZjD/BnwUu/U3jCS++VU5Lfb5qmM6nZ3edbz89n8BPPCvJdklAAA= -->
