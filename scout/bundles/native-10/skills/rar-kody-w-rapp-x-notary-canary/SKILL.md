---
name: "rar-kody-w-rapp-x-notary-canary"
description: "Validates the Issues-backed RAR notarization lifecycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_x_notary_canary_agent", "rar_sha256": "5d34d87380925aa0f60c14e0066c8aa5e59ecd884bf19034619ebea58ad27149", "source_kind": "rar-agent", "source_commit": "6b476f64439c79606c401a412ac5f468d15459e9", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_x_notary_canary_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-x-notary-canary:33eee7877885635c66aa7660de86e5c23e515d6195eed0d5c504c45db331c01b", "kind": "skill"}, "version": "1.2.0", "author": "Kody W", "tags": ["canary", "notary", "rapp_x"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp_x_notary_canary_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_x_notary_canary_agent.py` is
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

RAPP + X notarization canary for end-to-end registry validation.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_x_notary_canary_agent.py` and embedded as the fenced Python below (sha256 5d34d87380925aa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_x_notary_canary_agent.py` first:

```bash
python3 rapp_x_notary_canary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_x_notary_canary_agent.py   # or on stdin
python3 rapp_x_notary_canary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP + X notarization canary for end-to-end registry validation."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_x_notary_canary_agent",
    "version": "1.2.0",
    "display_name": "RAPP X Notary Canary",
    "description": "Validates the Issues-backed RAR notarization lifecycle.",
    "author": "Kody W",
    "tags": ["canary", "notary", "rapp_x"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class RappXNotaryCanaryAgent(BasicAgent):
    def __init__(self):
        self.name = "RappXNotaryCanaryAgent"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {"type": "object", "properties": {}},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        return f"RAPP + X canary v1.2 restored: {kwargs.get('message', 'ok')}"


if __name__ == "__main__":
    print(RappXNotaryCanaryAgent().perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61Wa5OqSBL9KxXOh54Z2xbkIboxG+v1bft+29sbdgkFlECBFPjq7f++WWL3vROxe+fL+sFQqMw8efLkgfccThM3jHPV3HNoXdAq95izCDdjGiU0ZHB5iX1q4YRwlLgEdTlPCS/ssOkRC01rU8TCBMf0isVx5FObmBfTJ0+Qh5xxEPmE56r//NdjjsLvXPU9Z/qYw6XcFEfReiiCL3XM4LvmEJZAmI+ZA/ejC+Bi8D8isR3GAVyyiI3u/37lxLcf0e+/eyccO/w3VPg74klcfWXo/olJksYM2a+5aW08Rnm0RuatDjrKTyW4zZMwJlYVvWcpnhyS/PoQEM6xQx4e0UPoPfz28ZrLfQB2BrlTU7QooP/yCxpQMw55aCdoZoZpguKUJTQgr+yVzV3K0TzEPAGG3mbP3X7/KbDeEM0YhCZw6ieoHWPqoygO9+SWGIU2evuHB0MonIoxkLM9b2/cXrYZ7i0WBL09obkLdcKYOpRhH926u90SFUyXmB5Pg8JRFAEAlN2qTutdaD/iqU/+ht7+d/qn6CKQvjKgD1MGCRISRGEMI/YvCHOE0e6SkALM1oSuQ98XUkDiK42eRPsrl7A7KZAYkTMx04QgPzQBrE1BD4+C/NA/EkAGkLlHfR9ZNAYeQhgPZpagsyqSvb297TB3X1mmBgVlyuRFOPAFGBUKUUxsnzpu8sqI6Ybo4f3jAf0b/SzqllzUGIMebxzFBBD2ZqMhAj2kARzjSEyeYOs2nPePjHyBjpEYHUlMbZotBmT7PmnRQTaRz3FAzwIiie+V/swbOrnAC6IJsEV5wh9fmUgRwtH4RDn5JDELzqj/nG9WR8yE3zmEOdlxGNzO3kQmhmmGsfWEujb6YgrahbkmYqJuyBPQZUSYRZh5gUicfB8hqARxWG9uXx5RyqFVkfltB6kFOcHWhONvaFAfoyQMffgSBN3KQ3TIqBj8XaDZZUgSP4DGvn2meEJDAmyiCIMy3Rhzcjtn40wRYfwVD8kxYuSEhJ0QMaOb8dyU97Xnf7Kk+9KDaSDor5CEBSIERhxgWphBZm8ih/AeahLGSa7KUt9/zDEckJ9ZlcAbkATGKpwNdhncKaHC8d7BNZJLJKLDndhwYSORj5PMyt5zEIahLha/MxVkyoSAn24nVP1idSuSYRFy26Gbdd/MZYsBhmDvh1uOkMI2U0KuCnZGHnMQDBoGBq43l85lCMCsv9vSDU9c4EINRflJgkwCn4DtUWb9UEBcptYdP7WqP3pZ4VzI2ilk7VQVhRBSNsplw9B0RTN1HeOyrksWMXSimSWFaLJm6XJFI8SSLM3UJNVUNWunKLIpyTuox2G5AnyvV5QFwYD0i8W/ttJcFsBdXNJ0iNAsRbWMsmJIlZKGsWTrkimrRJJ03TQw1ohWIaZlGOrOliuSogI6siNYM7BVKstqReS7L3ZWYPtpop988zCNTbI1wyCgAqO+U8u6rauqUjHLFV3STVWSsSqXsKnZqm5YsqZCUZH5HnrnXIwk6+FD6Ar8lMRHUef9PkOhKl2Fkx2Vd2vZp15Ulov5qrgb1C6VvGxOUjpPm8y2Bot6x+KDdmMwandDkkxazS7lJ28VXHs+mUnrqFEc88NFvUwte9f5tjesjhEFA26zRJmWDEc5Ts5OGhedw3Ff20RJvzbsd6WWPGaL4BJUTqPe82hRLMUzd6F4L8G+3/TU3WmxosqUmGW3zTY9aTAy1+1BVKpdNq3lQm7NjovisXsghhFIuNKiZqvMry1toJTyjVbHcHdWs+2qkdHA8bVCqbWcSL2W7HdO2Fv3g0OzphybVhqU0xajp5m90qeNfiOKlmRRZq38ubWeO/Jpb7Pn43Q+teq7fb2TJ4ph1U+tyszZrVaNVaiCWFRpOBnmo7q9F1PejHbd/GDoLSPlZTdMm/GQhySV3Z62JO11f1zbpenweXkZG/JkPq5UTnG5nnQ9+UWOQm5vGq1Ijl6sb1d56E6NcX/6IpnRZKauppdmKSSxN5lzPz18m+nzcx9r+nm4WkbzSZqcS8vm5tDvXmQ+Ypt+OPSdqd1rbYgdUaMf1dvF4XoxOlZovGtOZ9NdPcWjJq7J4713dNatZoN1DavFec/tycOwOTnimkQ7q36jKT1fms32oX4orq97fVo7xuNe06PO1ZftbxWIXE+4643P/egQy47F525wGqvjS+9ZaY/kUX6M62Pp22ieyOx5X84fphoALLJgRvDY44YRKWxpdmfsmRRp0itdG9YyX0w352l+MaZU5oeXuq6P2tbxWPH6hh0c1Oildw7ck9emidXwVFJZ9/KDniSNuG4Z6X7q91Tap0bpyuvp+nSc7KW+92IFnaks7xrm3sXKi4Kl/cKJi+P2xtOaXalemuwN4hPHrK89yXnpvOyH3QrDSdNdSx0zbZnSstw49+YBG8AL73LheVd74ZU2FWU+HRadzu4ar+XJZAFr9McfsI63B26uKiuq9pgTbzX3R8VfebdzpdH2HqwrZdjr/5v7ZE4QHgEKM4mwc3ihsaq34tWf4wLHj00KIDKDBwk6d5PJTLTw3zxcHLxkLwAhS8g5+XxqJti5PU2+jmVh90fE9izKwdOeZ08XeBmHoh//AaN27tGJDAAA -->
