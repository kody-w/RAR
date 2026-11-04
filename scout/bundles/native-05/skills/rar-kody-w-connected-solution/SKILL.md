---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "2653cc11fe301bc460b4fd94cffb59bfc854f1d88fb5f35a363e3b4aba52e6ce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/connected_solution_agent`. The original RAPP
agent is preserved byte-for-byte in `connected_solution_agent.py` and in the RCI capsule.

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

Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "capir_mode": {
      "description": "How to build the deterministic per-capability topic inside each sub-agent (the topic that runs the agent.py's perform() logic on STATIC synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else real seeded data, else SYNTHESIZES static stand-in records from the agent's inferred data shape \u2014 so EVERY agent.py maps to a self-documented topic; 'static' uses only real seeded data (no synthetic stand-in); 'embedded' uses only an embedded CapIR; 'off' emits instructions-only sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
      "type": "string"
    },
    "credentials_path": {
      "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE (under a top-level 'Values' object or at the root). Used only for deploy; the secret is never echoed back. If omitted, env vars / ~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
      "type": "string"
    },
    "deploy": {
      "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot Studio (Dataverse) environment and publish every bot (sub-agents first, orchestrator last) \u2014 no pac CLI needed, stdlib only. App-registration credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file \u2014 NEVER from chat. Default false (package only).",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Optional override for the target Dataverse environment URL (e.g. https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
      "type": "string"
    },
    "orchestrator_channels": {
      "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false (headlessly publishable). True requires a maker-portal publish.",
      "type": "boolean"
    },
    "orchestrator_name": {
      "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
      "type": "string"
    },
    "output_path": {
      "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
      "type": "string"
    },
    "publish": {
      "description": "When deploy=true, also publish the bots after import (default true). false imports without publishing.",
      "type": "boolean"
    },
    "publisher_display": {
      "description": "Solution publisher friendly name (default 'Default Publisher').",
      "type": "string"
    },
    "publisher_name": {
      "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a distinct solution instead of updating ones that already exist.",
      "type": "string"
    },
    "solution_display_name": {
      "description": "Solution friendly name.",
      "type": "string"
    },
    "solution_name": {
      "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
      "type": "string"
    },
    "stack_dir": {
      "description": "Path to an agent stack folder. Each BasicAgent *.py under it (or its agents/ subfolder) becomes one connected sub-agent; metadata.json (name/description/features/starters) shapes the orchestrator.",
      "type": "string"
    },
    "subagents": {
      "description": "Alternative to stack_dir: explicit sub-agents, each an object with agent_name, display_name, description, instructions.",
      "type": "array"
    },
    "version": {
      "description": "Solution version, e.g. 1.0.0.0.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `connected_solution_agent.py` and embedded as the fenced Python below (sha256 2653cc11fe301bc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `connected_solution_agent.py` first:

```bash
python3 connected_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 connected_solution_agent.py   # or on stdin
python3 connected_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/connected_solution_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/connected_solution_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/connected_solution_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/connected_solution_agent",
    "version": "1.0.3",
    "display_name": "ConnectedSolution",
    "description": "Packages a BasicAgent stack into an import-ready Copilot Studio connected-agents solution zip, optionally publishing via the Dataverse Web API.",
    "author": "Kody Wildfeuer",
    "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import io
import os
import re
import sys
import json
import ast
import base64
import uuid
import zipfile
import logging
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

# PUBLISHER PREFIX. Kody, 2026-08-27: "make it aibast for now."
#
# Env-overridable rather than hardcoded, because this repo is public: a bare "aibast"
# default would stamp every stranger's generated solution with a publisher that is not
# theirs, and a solution carrying the wrong publisher is a real problem for them to unpick
# in a tenant. Setting RAPP_PUBLISHER_PREFIX overrides it; unset, it is aibast.
_DEFAULT_PUBLISHER_PREFIX = os.getenv("RAPP_PUBLISHER_PREFIX", "aibast")

logger = logging.getLogger("connected_solution_agent")

# BasicAgent base — use the RAPP runtime's when present, else a minimal shim so
# this file also runs standalone (python connected_solution_agent.py <stack_dir>).
try:  # the RAPP runtime's base when hosted; a minimal shim when standalone
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", self.__class__.__name__)
                self.metadata = metadata or getattr(self, "metadata", {})

# ============================================================================
# Embedded Copilot Studio solution templates (verbatim from the proven packager)
# ============================================================================

DEFAULT_ICON_BASE64 = (
    "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"
)

SOLUTION_XML_NATIVE = """\
<ImportExportXml version="9.2.26023.151" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <SolutionManifest>
    <UniqueName>{solution_unique_name}</UniqueName>
    <LocalizedNames>
      <LocalizedName description="{solution_display_name}" languagecode="1033" />
    </LocalizedNames>
    <Descriptions />
    <Version>{solution_version}</Version>
    <Managed>{managed_flag}</Managed>
    <Publisher>
      <UniqueName>{publisher_unique_name}</UniqueName>
      <LocalizedNames>
        <LocalizedName description="{publisher_display_name}" languagecode="1033" />
      </LocalizedNames>
      <Descriptions>
        <Description description="Auto-generated publisher" languagecode="1033" />
      </Descriptions>
      <EMailAddress xsi:nil="true"></EMailAddress>
      <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
      <CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
      <Addresses>
        <Address>
          <AddressNumber>1</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
        <Address>
          <AddressNumber>2</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
      </Addresses>
    </Publisher>
    <RootComponents />
    <MissingDependencies />
  </SolutionManifest>
</ImportExportXml>"""

CUSTOMIZATIONS_XML_NATIVE = """\
<ImportExportXml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <Entities></Entities>
  <Roles></Roles>
  <Workflows></Workflows>
  <FieldSecurityProfiles></FieldSecurityProfiles>
  <Templates />
  <EntityMaps />
  <EntityRelationships />
  <OrganizationSettings />
  <optionsets />
  <CustomControls />
  <EntityDataProviders />
  <connectionreferences>
{connection_references}
  </connectionreferences>
  <Languages>
    <Language>1033</Language>
  </Languages>
</ImportExportXml>"""

CONTENT_TYPES_XML_NATIVE = '<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/octet-stream" /><Default Extension="json" ContentType="application/octet-stream" />{overrides}</Types>'

CONTENT_TYPE_OVERRIDE = '<Override PartName="/{part_name}" ContentType="application/octet-stream" />'

BOT_XML = """\
<bot schemaname="{bot_schema}">
  <authenticationmode>2</authenticationmode>
  <authenticationtrigger>1</authenticationtrigger>
  <iconbase64>{icon_base64}</iconbase64>
  <iscustomizable>0</iscustomizable>
  <language>1033</language>
  <name>{bot_display_name}</name>
  <runtimeprovider>0</runtimeprovider>
  <template>default-2.1.0</template>
</bot>"""

BOT_CONFIGURATION_JSON_NATIVE = """{{
  "$kind": "BotConfiguration",
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": false
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

ORCHESTRATOR_CHANNELS_BLOCK = """
  "channels": [
    {
      "$kind": "ChannelDefinition",
      "channelId": "MsTeams"
    },
    {
      "$kind": "ChannelDefinition",
      "channelId": "Microsoft365Copilot"
    }
  ],"""

ORCHESTRATOR_CONFIGURATION_JSON = """{{
  "$kind": "BotConfiguration",{channels_block}
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,{publish_on_import_line}
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "isLightweightBot": false,
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": true
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

GPT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>15</componenttype>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

GPT_DATA_YAML = """\
kind: GptComponentMetadata
displayName: {display_name}
instructions: |-
{instructions_indented}
gptCapabilities:
  webBrowsing: true
  codeInterpreter: true

aISettings:
  model:
    modelNameHint: GPT5Chat

  extensionData:
    lastUsedCustomModel: {{}}

declarativeSkillsMetadata:"""

BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>{component_type}</componenttype>{description_element}
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

CONN_REF_SET_XML = """\
<botcomponent_connectionreferenceset>
{entries}
</botcomponent_connectionreferenceset>"""

INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>9</componenttype>
  <description>{description}</description>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{orchestrator_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

INVOKE_CONNECTED_AGENT_DATA = """\
kind: TaskDialog
modelDisplayName: {display_name}
modelDescription: |-
{description_indented}{inputs_block}
action:
  kind: InvokeConnectedAgentTaskAction{input_type_block}
  botSchemaName: {child_schema}
  historyType:
    kind: ConversationHistory"""


def _connected_inputs_yaml(params):
    """The orchestrator-side typed inputs for a connected agent, from the source
    agent.py's perform() params. Per the Copilot Studio connected-agent schema:
    `inputs` (AutomaticTaskInput list) sits at the TaskDialog root and `inputType`
    sits INSIDE the action block. These populate the connected agent's Inputs
    panel and let the orchestrator pass the params when it delegates. Returns
    (inputs_block, input_type_block) — both '' when there are no params."""
    params = params or []
    if not params:
        return "", ""
    inlines, props = [], []
    for entry in params:
        pn = entry[0] if isinstance(entry, (list, tuple)) else entry
        required = bool(entry[2]) if isinstance(entry, (list, tuple)) and len(entry) > 2 else False
        name = re.sub(r"[^A-Za-z0-9_]", "", str(pn)) or "input"
        inlines.append("  - kind: AutomaticTaskInput\n    propertyName: " + name)
        props.append("      " + name + ":\n"
                     "        displayName: " + name + "\n"
                     "        isRequired: " + ("true" if required else "false") + "\n"
                     "        type: String")
    return ("\ninputs:\n" + "\n".join(inlines),
            "\n  inputType:\n    properties:\n" + "\n".join(props))

INVOKE_CONNECTED_AGENT_DEPENDENCIES = '[{{"type":"bot","schemaName":"{child_schema}"}}]'

SYSTEM_TOPICS = {
    "ConversationStart": {
        "display_name": "Conversation Start",
        "description": "This system topic triggers when the agent receives an Activity indicating the beginning of a new conversation. If you do not want the agent to initiate the conversation, disable this topic.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnConversationStart
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_M0LuhV
      activity:
        text:
          - Hello, I'm {{System.Bot.Name}}. How can I help?
        speak:
          - Hello and thank you for calling {{System.Bot.Name}}. Please note that some responses are generated by AI and may require verification for accuracy. How may I help you today?"""
    },
    "EndofConversation": {
        "display_name": "End of Conversation",
        "description": "This system topic is only triggered by a redirect action,\nand guides the user through rating their conversation with the agent.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: Question
      id: 41d42054-d4cb-4e90-b922-2b16b37fe379
      conversationOutcome: ResolvedImplied
      alwaysPrompt: true
      variable: init:Topic.SurveyResponse
      prompt: Did that answer your question?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition-0
      conditions:
        - id: condition-0-item-0
          condition: =Topic.SurveyResponse = true
          actions:
            - kind: CSATQuestion
              id: csat_1
              conversationOutcome: ResolvedConfirmed

            - kind: SendActivity
              id: sendMessage_8r29O0
              activity: Thanks for your feedback.

            - kind: Question
              id: question_1
              alwaysPrompt: true
              variable: init:Topic.Continue
              prompt: Can I help with anything else?
              entity: BooleanPrebuiltEntity

            - kind: ConditionGroup
              id: condition-1
              conditions:
                - id: condition-1-item-0
                  condition: =Topic.Continue = true
                  actions:
                    - kind: SendActivity
                      id: sendMessage_4eOE6h
                      activity: Go ahead. I'm listening.

              elseActions:
                - kind: SendActivity
                  id: yHBz55
                  activity: Ok, goodbye.

                - kind: EndConversation
                  id: jh1GMT

      elseActions:
        - kind: Question
          id: PM68ot
          alwaysPrompt: true
          variable: init:Topic.TryAgain
          prompt: Sorry I wasn't able to help better. Would you like to try again?
          entity: BooleanPrebuiltEntity

        - kind: ConditionGroup
          id: KNxYBf
          conditions:
            - id: DPveFP
              condition: =Topic.TryAgain = false
              actions:
                - kind: BeginDialog
                  id: cngqi4
                  dialog: {bot_schema}.topic.Escalate

          elseActions:
            - kind: SendActivity
              id: GrVHEW
              activity: Go ahead. I'm listening."""
    },
    "Escalate": {
        "display_name": "Escalate",
        "description": "This system topic is triggered when the user indicates they would like to speak to a representative.\nYou can configure how the agent will handle human hand-off scenarios in the agent settings..\nIf your agent does not handle escalations, this topic should be disabled.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnEscalate
  id: main
  intent:
    displayName: Escalate
    includeInOnSelectIntent: false
    triggerQueries:
      - Talk to agent
      - Talk to a person
      - Talk to someone
      - Call back
      - Call customer service
      - Call me please
      - Call support
      - Call technical support
      - Can an agent call me
      - Can I call
      - Can I get in touch with someone else
      - Can I get real agent support
      - Can I get transferred to a person to call
      - Can I have a call in number Or can I be called
      - Can I have a representative call me
      - Can I schedule a call
      - Can I speak to a representative
      - Can I talk to a human
      - Can I talk to a human assistant
      - Can someone call me
      - Chat with a human
      - Chat with a representative
      - Chat with agent
      - Chat with someone please
      - Connect me to a live agent
      - Connect me to a person
      - Could some one contact me by phone
      - Customer agent
      - Customer representative
      - Customer service
      - I need a manager to contact me
      - I need customer service
      - I need help from a person
      - I need to speak with a live argent
      - I need to talk to a specialist please
      - I want to talk to customer service
      - I want to proceed with live support
      - I want to speak with a consultant
      - I want to speak with a live tech
      - I would like to speak with an associate
      - I would like to talk to a technician
      - Talk with tech support member

  actions:
    - kind: SendActivity
      id: sendMessage_s39DCt
      conversationOutcome: Escalated
      activity: |-
        Escalating to a representative is not currently configured for this agent, however this is where the agent could provide information about how to get in touch with someone another way.

        Is there anything else I can help you with?"""
    },
    "Fallback": {
        "display_name": "Fallback",
        "description": "This system topic triggers when the user's utterance does not match any existing topics.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_LktzXw
      conditions:
        - id: conditionItem_tlGIVo
          condition: =System.FallbackCount < 3
          actions:
            - kind: SendActivity
              id: sendMessage_QZreqo
              activity: I'm sorry, I'm not sure how to help with that. Can you try rephrasing?

      elseActions:
        - kind: BeginDialog
          id: 5aXj5M
          dialog: {bot_schema}.topic.Escalate"""
    },
    "Goodbye": {
        "display_name": "Goodbye",
        "description": "This topic triggers when the user says goodbye. By default, it does not end the conversation. If you would like to end the conversation when the user says goodbye, you can add an \"End of Conversation\" action to this topic, or redirect to the \"End of Conversation\" system topic.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Goodbye
    includeInOnSelectIntent: false
    triggerQueries:
      - Bye
      - Bye for now
      - Bye now
      - Good bye
      - No thank you. Goodbye.
      - See you later

  actions:
    - kind: Question
      id: question_zf2HhP
      variable: Topic.EndConversation
      prompt: Would you like to end our conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition_DGc1Wy
      conditions:
        - id: condition_DGc1Wy-item-0
          condition: =Topic.EndConversation = true
          actions:
            - kind: BeginDialog
              id: dn94DC
              dialog: {bot_schema}.topic.EndofConversation

        - id: condition_DGc1Wy-item-1
          condition: =Topic.EndConversation = false
          actions:
            - kind: SendActivity
              id: sendMessage_LdLhmf
              activity: Go ahead. I'm listening."""
    },
    "Greeting": {
        "display_name": "Greeting",
        "description": "This topic is triggered when the user greets the agent.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Greeting
    includeInOnSelectIntent: false
    triggerQueries:
      - Good afternoon
      - Good morning
      - Hello
      - Hey
      - Hi

  actions:
    - kind: SendActivity
      id: sendMessage_abmysR
      activity:
        text:
          - Hello, how can I help you today?
        speak:
          - Hello, <break strength="medium" /> how can I help?

    - kind: CancelAllDialogs
      id: cancelAllDialogs_01At22"""
    },
    "MultipleTopicsMatched": {
        "display_name": "Multiple Topics Matched",
        "description": "This system topic triggers when the agent matches multiple Topics with the incoming message and needs to clarify which one should be triggered.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSelectIntent
  id: main
  triggerBehavior: Always
  actions:
    - kind: SetVariable
      id: setVariable_M6434i
      variable: init:Topic.IntentOptions
      value: =System.Recognizer.IntentOptions

    - kind: SetTextVariable
      id: setTextVariable_0
      variable: Topic.NoneOfTheseDisplayName
      value: None of these

    - kind: EditTable
      id: sendMessage_g5Ls09
      changeType: Add
      itemsVariable: Topic.IntentOptions
      value: "={{ DisplayName: Topic.NoneOfTheseDisplayName, TopicId: \\"NoTopic\\", TriggerId: \\"NoTrigger\\", Score: 1.0 }}"

    - kind: Question
      id: question_zf2HhP
      interruptionPolicy:
        allowInterruption: false

      alwaysPrompt: true
      variable: System.Recognizer.SelectedIntent
      prompt: "To clarify, did you mean:"
      entity:
        kind: DynamicClosedListEntity
        items: =Topic.IntentOptions

    - kind: ConditionGroup
      id: conditionGroup_60PuXb
      conditions:
        - id: conditionItem_rs7GgM
          condition: =System.Recognizer.SelectedIntent.TopicId = "NoTopic"
          actions:
            - kind: ReplaceDialog
              id: YZXRDb
              dialog: {bot_schema}.topic.Fallback"""
    },
    "OnError": {
        "display_name": "On Error",
        "description": "This system topic triggers when the agent encounters an error. When using the test chat pane, the full error description is displayed.",
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnError
  id: main
  actions:
    - kind: SetVariable
      id: setVariable_timestamp
      variable: init:Topic.CurrentTime
      value: =Text(Now(), DateTimeFormat.UTC)

    - kind: ConditionGroup
      id: condition_1
      conditions:
        - id: bL4wmY
          condition: =System.Conversation.InTestMode = true
          actions:
            - kind: SendActivity
              id: sendMessage_XJBYMo
              activity: |-
                Error Message: {{System.Error.Message}}
                Error Code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}

      elseActions:
        - kind: SendActivity
          id: sendMessage_dZ0gaF
          activity:
            text:
              - |-
                An error has occurred.
                Error code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}.
            speak:
              - An error has occurred, please try again.

    - kind: LogCustomTelemetryEvent
      id: 9KwEAn
      eventName: OnErrorLog
      properties: "={{ErrorMessage: System.Error.Message, ErrorCode: System.Error.Code, TimeUTC: Topic.CurrentTime, ConversationId: System.Conversation.Id}}"

    - kind: CancelAllDialogs
      id: NW7NyY"""
    },
    "ResetConversation": {
        "display_name": "Reset Conversation",
        "description": None,
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_OPsT1O
      activity: What can I help you with?

    - kind: ClearAllVariables
      id: clearAllVariables_73bTFR
      variables: ConversationScopedVariables

    - kind: CancelAllDialogs
      id: cancelAllDialogs_12Gt21"""
    },
    "Search": {
        "display_name": "Conversational boosting",
        "description": "Create generative answers from knowledge sources.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  priority: -1
  actions:
    - kind: SearchAndSummarizeContent
      id: search-content
      variable: Topic.Answer
      userInput: =System.Activity.Text

    - kind: ConditionGroup
      id: has-answer-conditions
      conditions:
        - id: has-answer
          condition: =!IsBlank(Topic.Answer)
          actions:
            - kind: EndDialog
              id: end-topic
              clearTopicQueue: true"""
    },
    "Signin": {
        "display_name": "Sign in ",
        "description": "This system topic triggers when the agent needs to sign in the user or require the user to sign in",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSignIn
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_ypjGKL
      conditions:
        - id: conditionItem_7XYIIR
          condition: =System.SignInReason = SignInReason.SignInRequired
          actions:
            - kind: SendActivity
              id: sendMessage_1jHUNO
              activity: Hello! To be able to help you, I'll need you to sign in.

    - kind: OAuthInput
      id: gOjhZA
      title: Login
      text: To continue, please login"""
    },
    "StartOver": {
        "display_name": "Start Over",
        "description": None,
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Start Over
    includeInOnSelectIntent: false
    triggerQueries:
      - let's begin again
      - start over
      - start again
      - restart

  actions:
    - kind: Question
      id: question_zguoVV
      alwaysPrompt: false
      variable: init:Topic.Confirm
      prompt: Are you sure you want to restart the conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: conditionGroup_lvx2zV
      conditions:
        - id: conditionItem_sVQtHa
          condition: =Topic.Confirm = true
          actions:
            - kind: BeginDialog
              id: 0YKYsy
              dialog: {bot_schema}.topic.ResetConversation

      elseActions:
        - kind: SendActivity
          id: sendMessage_lk2CyQ
          activity: Ok. Let's carry on."""
    },
    "ThankYou": {
        "display_name": "Thank you",
        "description": "This topic triggers when the user says thank you.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Thank you
    includeInOnSelectIntent: false
    triggerQueries:
      - thanks
      - thank you
      - thanks so much
      - ty

  actions:
    - kind: SendActivity
      id: sendMessage_9iz6v7
      activity: You're welcome."""
    },
}


# ============================================================================
# Packager: orchestrator + connected sub-agents, with the 42-char name cap,
# 100-char schema cap, and optional channels (default off = headless-publishable)
# ============================================================================

MAX_SCHEMA = 100


_CONNECTED_INFIX = ".InvokeConnectedAgentTaskAction."   # 32 chars (incl. both dots)


_MIN_ACTION_BUDGET = 26   # always leave at least this many chars for the action suffix


MAX_BOT_NAME = 42


def _cap_bot_name(name: str, preserve_suffix: Optional[str] = None) -> str:
    """Truncate a bot display name to the 42-char limit, keeping a trailing word
    like 'Orchestrator' intact when present."""
    name = (name or "").strip()
    if len(name) <= MAX_BOT_NAME:
        return name
    if preserve_suffix and name.endswith(preserve_suffix):
        budget = MAX_BOT_NAME - len(preserve_suffix) - 1
        head = name[: -len(preserve_suffix)].rstrip()[:budget].rstrip()
        return f"{head} {preserve_suffix}"
    return name[:MAX_BOT_NAME].rstrip()


def _sanitize_schema(name: str) -> str:
    """Lowercase alphanumeric fragment for a bot schema name."""
    return re.sub(r"[^a-zA-Z0-9]", "", name or "").lower()


def _pascal(name: str) -> str:
    """PascalCase alphanumeric fragment for a connected-action schema name."""
    parts = re.split(r"[^a-zA-Z0-9]+", name or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _xml_escape(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(f"{pad}{line}" for line in (text or "").split("\n"))


def _yaml_display_safe(text: str) -> str:
    """Make a one-line value safe as a bare YAML scalar (no colons/quotes/newlines)."""
    clean = re.sub(r"\s+", " ", (text or "").replace(":", " -")).strip()
    return clean.replace('"', "").replace("'", "")


# ============================================================================
# CapIR -> deterministic capability topic (the 1:1 conversion)
#
# A converted agent.py compiles its perform() to a CapIR (t2p-capir/1.0). When a
# sub-agent carries that CapIR, the packager emits a REAL Copilot Studio topic
# that runs the SAME steps perform() runs: OnRecognizedIntent (the agent's real
# triggers) -> Question (the user's real input) -> SetVariable Table() of the
# SEEDED records -> Filter by the real query -> branch -> SendActivity, plus a
# document render for artifact-producing capabilities. The control flow is real;
# only the DATA is mocked. Flipping the in-topic Table() to a Dataverse /
# SharePoint connector (binding.connector) is the one-line move to live data, and
# the same filter/respond/document logic runs unchanged. This is the opposite of
# an actions:[]+modelDescription "gamed" topic.
# ============================================================================

def _yaml_dq(text) -> str:
    """A YAML double-quoted scalar: robust for Power Fx expressions and message
    text (escapes backslash/quote, encodes newlines)."""
    s = (str(text).replace("\\", "\\\\").replace('"', '\\"')
         .replace("\n", "\\n").replace("\t", "\\t").replace("\r", ""))
    return '"' + s + '"'


def _pfx_str(value) -> str:
    """A Power Fx double-quoted string literal (internal quotes doubled)."""
    return '"' + str(value).replace('"', '""') + '"'


def _pfx_safe_text(text) -> str:
    """Strip literal braces from message text so Copilot Studio does not parse
    them as variable bindings (unparseable {...} fails publish). Template tokens
    like {Topic.X} are added AFTER this, so they survive."""
    return str(text).replace("{", "(").replace("}", ")")


def _capir_topic_fields(records):
    """Stable union of record field names (the Table()/filter columns) when the
    binding omits an explicit field list (recovered / recompiled CapIRs)."""
    fields = []
    for r in records or []:
        if isinstance(r, dict):
            for k in r.keys():
                if k not in fields:
                    fields.append(k)
    return fields


def _numeric_metric_field(records, fields, hint=None):
    """Pick the field numeric-threshold queries compare against (e.g. "assets
    above a 30% failure probability" -> a real `Value(field) >= 0.30`). A field
    qualifies only if it parses as a number in EVERY record (so Power Fx Value()
    never errors). Prefers probability/score-like names and 0..1-ranged fields;
    honors an explicit binding `metric_field` hint."""
    if hint and hint in (fields or []):
        return hint
    if not records:
        return None
    numeric, ratio = [], []
    for f in fields:
        vals, ok = [], True
        for r in records:
            if not isinstance(r, dict) or f not in r or str(r.get(f)).strip() == "":
                ok = False; break
            try:
                vals.append(float(str(r.get(f)).strip()))
            except (TypeError, ValueError):
                ok = False; break
        if ok and vals:
            numeric.append(f)
            if all(0.0 <= v <= 1.0 for v in vals):
                ratio.append(f)
    pool = ratio or numeric
    if not pool:
        return None
    for pat in (r"p_?fail|prob|likeli|risk", r"score|rate|ratio|pct|percent|conf"):
        for f in pool:
            if re.search(pat, f, re.I):
                return f
    return pool[0]


# The load-bearing perform() constants (t2p-capir/1.0 CAPIR_CONSTS). The topic
# reads these off the CapIR when present so it mirrors the agent.py's numbers.
_CAPIR_TOPIC_CONSTS = {
    "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


def capir_topic_action_name(capir: dict) -> str:
    """The custom-topic schema suffix for a capability: Handle<Pascal(key)>."""
    key = (capir or {}).get("key") or "capability"
    return "Handle" + (_pascal(key) or "Capability")


def capir_topic_data_yaml(display_name: str, capir: dict) -> str:
    """Render a capability's CapIR into a REAL deterministic Copilot Studio topic
    'data' YAML that goes INSIDE the sub-agent: OnRecognizedIntent triggers ->
    Question (slot) -> SetVariable Table() of the SEEDED records -> Filter by the
    real query -> ConditionGroup on the match count -> SendActivity, plus (for an
    artifact capability) a SetVariable that renders the document from the matched
    (or fallback) records exactly like perform()'s artifact step. The synthetic
    records live IN the topic and the control flow runs deterministically; only
    the DATA is mocked. Structural 1:1 with the generated agent.py's perform()."""
    capir = capir or {}
    consts = dict(_CAPIR_TOPIC_CONSTS)
    consts.update(capir.get("consts") or {})
    binding = capir.get("binding") or {}
    fields = binding.get("fields") or _capir_topic_fields(binding.get("records"))
    table = binding.get("table") or "records"
    records = binding.get("records") or []
    customer = str(capir.get("customer") or "the customer")
    response = _pfx_safe_text(capir.get("response") or f"Here is how I handle {display_name}.")
    # triggers + grounding facts + the artifact doc come straight from the steps
    triggers, facts, doc = [], [], None
    for step in capir.get("steps") or []:
        op = step.get("op")
        if op == "trigger_match":
            triggers = step.get("queries") or []
        elif op == "knowledge_lookup":
            facts = step.get("facts") or []
        elif op == "artifact":
            doc = step.get("doc")
    prompt = None
    for slot in capir.get("slots") or []:
        prompt = slot.get("prompt"); break
    prompt = prompt or f"What would you like help with for {display_name}?"

    # Power Fx: a real Table() of the seeded records, a real query Filter, a real
    # count, then a real branch -- the exact perform() path.
    recs = []
    for r in records:
        if isinstance(r, dict):
            cells = ", ".join("%s: %s" % (f, _pfx_str(r.get(f, ""))) for f in fields)
            recs.append("{" + cells + "}")
    table_pfx = "=Table(" + ", ".join(recs) + ")" if recs else "=Blank()"
    conds = " || ".join("(Lower(ThisRecord.%s) in Lower(Topic.Query))" % f for f in fields)
    text_clause = "(%s)" % (conds or "false")

    # numeric-threshold support: a query like "assets above a 30% failure
    # probability" sets Topic.Threshold (number, %-aware) + Topic.Direction
    # (ge/le) and the Filter does a REAL Value()-comparison on the metric field,
    # not just text containment. Falls back to text match when no number is asked.
    metric_field = _numeric_metric_field(records, fields, (binding.get("metric_field")))
    threshold_actions, filter_inner = "", text_clause
    if metric_field:
        num_re = r"\d+\.?\d*"
        thr_pfx = ('=If(IsMatch(Topic.Query, "\\d"), '
                   'Value(First(MatchAll(Topic.Query, "' + num_re + '")).FullMatch) '
                   '/ If(IsMatch(Topic.Query, "%"), 100, 1), Blank())')
        dir_pfx = ('=If(IsMatch(Lower(Topic.Query), "above|over|greater|more than|exceed|at least|higher|>"), "ge", '
                   'If(IsMatch(Lower(Topic.Query), "below|under|less|fewer|within|at most|lower|<"), "le", "ge"))')
        threshold_actions = (
            "    - kind: SetVariable\n"
            "      id: setThreshold\n"
            "      variable: Topic.Threshold\n"
            "      value: " + _yaml_dq(thr_pfx) + "\n"
            "    - kind: SetVariable\n"
            "      id: setDirection\n"
            "      variable: Topic.Direction\n"
            "      value: " + _yaml_dq(dir_pfx) + "\n")
        num_clause = ('(!IsBlank(Topic.Threshold) && If(Topic.Direction = "le", '
                      'Value(ThisRecord.' + metric_field + ') <= Topic.Threshold, '
                      'Value(ThisRecord.' + metric_field + ') >= Topic.Threshold))')
        filter_inner = "(" + text_clause + " || " + num_clause + ")"
    filter_pfx = "=Filter(Topic.Records, !IsBlank(Topic.Query) && " + filter_inner + ")"

    grounding = "\n".join("- " + _pfx_safe_text(f) for f in facts)
    ground_block = ("\n\nGrounded in what you told us:\n" + grounding) if grounding else ""

    # artifact (op==artifact): render the document from the matched-or-fallback
    # records, exactly like perform()'s artifact step (hits[:pdf_records] with a
    # data[:fallback_take] fallback). Materializing the real downloadable file is
    # the live-data flip -- a Create-file / Convert-to-PDF flow over these records.
    doc_actions, doc_block = "", ""
    if doc and fields:
        cells_pfx = ' & " | " & '.join('"%s: " & Text(ThisRecord.%s)' % (f, f) for f in fields)
        source = ("If(Topic.MatchCount > 0, Topic.Matches, FirstN(Topic.Records, %d))"
                  % consts["fallback_take"])
        document_pfx = ("=Concat(FirstN(%s, %d), %s & Char(10))"
                        % (source, consts["pdf_records"], cells_pfx))
        doc_actions = (
            "    - kind: SetVariable\n"
            "      id: setDocument\n"
            "      variable: Topic.Document\n"
            "      value: " + _yaml_dq(document_pfx) + "\n")
        prepared = _pfx_safe_text(consts["pdf_prepared"].replace("{customer}", customer))
        footer = _pfx_safe_text(consts["pdf_footer"])
        safe_doc = _pfx_safe_text(str(doc))
        doc_block = ("\n\n[" + safe_doc + "] " + prepared + ":\n"
                     + "{Topic.Document}\n" + footer
                     + "\n(In production, a Create-file / Convert-to-PDF flow over these "
                       "records delivers the real " + safe_doc + ".)")

    hit_msg = (response + ground_block
               + "\n\nI found {Topic.MatchCount} matching record(s) in the "
               + table + " data (synthetic demo data - no customer data needed)."
               + doc_block)
    miss_msg = (response + ground_block
                + "\n\nNo matching record in the " + table
                + " data; here are reference examples to ground the answer."
                + doc_block)
    trig = "\n".join("      - " + _yaml_dq(t) for t in triggers) or ("      - " + _yaml_dq(display_name))

    # intake: ask for the value to filter on. We intentionally do NOT read an
    # orchestrator-passed `Global.<param>` here. A connected agent can only
    # reference a global it has DECLARED as external-settable, and the solution
    # package format gives no reliable way to emit that declaration — referencing
    # an undeclared Global makes Copilot Studio's topic checker throw a
    # PowerFxError ("Identifier not recognized"), which blocks publish. The
    # orchestrator still DECLARES + PASSES the typed inputs (see the connected
    # action's inputType); the agent's generative layer receives them, and this
    # deterministic topic captures the value it filters on via the Question.
    intake_actions = (
        "    - kind: Question\n"
        "      id: question_query\n"
        "      variable: Topic.Query\n"
        "      prompt: " + _yaml_dq(prompt) + "\n"
        "      entity: StringPrebuiltEntity\n")

    return (
        "kind: AdaptiveDialog\n"
        "beginDialog:\n"
        "  kind: OnRecognizedIntent\n"
        "  id: main\n"
        "  intent:\n"
        "    displayName: " + _yaml_dq(display_name) + "\n"
        "    includeInOnSelectIntent: false\n"
        "    triggerQueries:\n" + trig + "\n"
        "  actions:\n"
        + intake_actions +
        "    - kind: SetVariable\n"
        "      id: setRecords\n"
        "      variable: Topic.Records\n"
        "      value: " + _yaml_dq(table_pfx) + "\n"
        + threshold_actions +
        "    - kind: SetVariable\n"
        "      id: setMatches\n"
        "      variable: Topic.Matches\n"
        "      value: " + _yaml_dq(filter_pfx) + "\n"
        "    - kind: SetVariable\n"
        "      id: setCount\n"
        "      variable: Topic.MatchCount\n"
        "      value: " + _yaml_dq("=CountRows(Topic.Matches)") + "\n"
        + doc_actions +
        "    - kind: ConditionGroup\n"
        "      id: hasMatches\n"
        "      conditions:\n"
        "        - id: hasMatches_hit\n"
        "          condition: " + _yaml_dq("=Topic.MatchCount > 0") + "\n"
        "          actions:\n"
        "            - kind: SendActivity\n"
        "              id: replyHit\n"
        "              activity: " + _yaml_dq(hit_msg) + "\n"
        "      elseActions:\n"
        "        - kind: SendActivity\n"
        "          id: replyMiss\n"
        "          activity: " + _yaml_dq(miss_msg) + "\n"
    )


@dataclass
class SubAgentSpec:
    """One connected sub-agent (one agent.py promoted to its own bot)."""
    agent_name: str           # e.g. "loanoriginationassistant"
    display_name: str         # e.g. "Loan Origination Assistant"
    description: str          # routing description the orchestrator selects on
    instructions: str         # the sub-agent's gpt.default instruction blob
    # The capability's compiled CapIR (t2p-capir/1.0), records already injected.
    # When present, the packager emits a REAL deterministic topic INSIDE this
    # sub-agent that runs the same steps as the converted agent.py's perform(),
    # instead of leaving the behavior to the gpt.default instruction blob. The
    # instructions remain as the persona/router fallback.
    capir: Optional[dict] = None
    # The source agent.py's perform() params [(name, description, required), ...],
    # declared as typed INPUTS on the orchestrator's connected-agent action so the
    # Copilot Studio orchestrator passes them when it delegates (the agent's
    # "Inputs" panel) — the contract, structurally, not just in the description.
    params: Optional[list] = None


@dataclass
class ConnectedSolutionSpec:
    """A single solution bundling an orchestrator + N connected sub-agents."""
    solution_unique_name: str
    solution_display_name: str
    orchestrator_display_name: str
    subagents: List[SubAgentSpec]
    orchestrator_instructions: str = ""   # synthesized if empty
    publisher_prefix: str = _DEFAULT_PUBLISHER_PREFIX
    publisher_unique_name: str = "DefaultPublisher"
    publisher_display_name: str = "Default Publisher"
    solution_version: str = "1.0.0.0"
    managed: bool = False
    orchestrator_schema_suffix: str = "orchestrator"
    # When True the orchestrator auto-publishes on import. Leave False so the
    # import itself never depends on the (slower, fail-prone) publish step.
    orchestrator_publish_on_import: bool = False
    # When True the orchestrator declares MsTeams + M365 Copilot channels. This
    # requires a maker-portal publish (headless `pac copilot publish` 409s on the
    # channel registration). Default False = fully headlessly publishable.
    orchestrator_channels: bool = False


class ConnectedSolutionPackager:
    """Assembles a multi-bot connected-agent solution zip from a spec."""

    def __init__(self, spec: ConnectedSolutionSpec):
        self.spec = spec
        # publisher_prefix is the one untamed length input feeding the schema caps
        # below; bound it to Dataverse's 8-char prefix limit so no schema exceeds
        # MAX_SCHEMA for ANY direct caller (perform() already caps it). Mutate the
        # spec too so the CustomizationPrefix stays consistent with the schemas.
        spec.publisher_prefix = spec.publisher_prefix[:8]
        prefix = spec.publisher_prefix

        # Connected-agent components are named
        #   {orch_schema}.InvokeConnectedAgentTaskAction.{Action}
        # and the full schema name must stay within Dataverse's 100-char limit.
        # Cap the orchestrator schema (reserving room for the action suffix) so a
        # long stack name can never push a component name over the limit.
        suffix = spec.orchestrator_schema_suffix
        base = re.sub(r"stack$", "", _sanitize_schema(spec.solution_unique_name)) or "agents"
        orch = f"{prefix}_{base}{suffix}"
        max_orch = MAX_SCHEMA - len(_CONNECTED_INFIX) - _MIN_ACTION_BUDGET   # 42
        if len(orch) > max_orch:
            keep = max(4, max_orch - len(prefix) - 1 - len(suffix))
            orch = f"{prefix}_{base[:keep]}{suffix}"
        self.orch_schema = orch
        # Whatever room is left after the (capped) orchestrator schema + infix.
        self._action_budget = MAX_SCHEMA - len(_CONNECTED_INFIX) - len(self.orch_schema)

        # Assign a unique schema name + connected-action name to each sub-agent.
        self._children = []  # list of (SubAgentSpec, child_schema, action_name)
        seen_schemas = {self.orch_schema}
        seen_actions = set()
        # Children need room for a ".topic.<Name>" suffix within MAX_SCHEMA. The
        # orchestrator schema is capped above; children were NOT, so a long
        # solution + capability name overflowed the Dataverse 100-char limit.
        child_base_max = max(4, MAX_SCHEMA - 35 - len(prefix) - 1)
        for sub in spec.subagents:
            base = (_sanitize_schema(sub.agent_name) or "agent")[:child_base_max]
            child_schema = f"{prefix}_{base}"
            n = 2
            while child_schema in seen_schemas:
                child_schema = f"{prefix}_{base}{n}"
                n += 1
            seen_schemas.add(child_schema)

            pascal = _pascal(sub.display_name or sub.agent_name) or "Agent"
            action = pascal[: self._action_budget]
            n = 2
            while action in seen_actions:
                tag = str(n)
                action = pascal[: max(1, self._action_budget - len(tag))] + tag
                n += 1
            seen_actions.add(action)

            self._children.append((sub, child_schema, action))

    # -- public ----------------------------------------------------------

    def package(self, output_path: Optional[Path] = None) -> bytes:
        buf = io.BytesIO()
        overrides: List[str] = []  # /data parts for [Content_Types].xml

        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. solution + customizations (connector-less, empty RootComponents)
            zf.writestr("solution.xml", self._solution_xml())
            zf.writestr(
                "customizations.xml",
                CUSTOMIZATIONS_XML_NATIVE.format(connection_references=""),
            )

            # 2. Orchestrator bot (router) — instructions list the sub-agents
            self._write_bot(
                zf,
                bot_schema=self.orch_schema,
                display_name=self.spec.orchestrator_display_name,
                instructions=self._orchestrator_instructions(),
                overrides=overrides,
                is_orchestrator=True,
            )

            # 3. Connected-agent delegation components (under the orchestrator)
            for sub, child_schema, action in self._children:
                self._write_connected_action(
                    zf, sub, child_schema, action, overrides
                )

            # 4. Each sub-agent as its own connectable bot — now carrying the REAL
            #    deterministic capability topic (1:1 with its agent.py) when a
            #    CapIR is present.
            for sub, child_schema, _action in self._children:
                self._write_bot(
                    zf,
                    bot_schema=child_schema,
                    display_name=sub.display_name,
                    instructions=sub.instructions,
                    overrides=overrides,
                    capir=sub.capir,
                )

            # 5. Empty connection reference set (no connectors in this topology)
            zf.writestr(
                "Assets/botcomponent_connectionreferenceset.xml",
                CONN_REF_SET_XML.format(entries=""),
            )

            # 6. [Content_Types].xml — every extensionless /data part listed
            zf.writestr(
                "[Content_Types].xml",
                CONTENT_TYPES_XML_NATIVE.format(overrides="".join(overrides)),
            )

        data = buf.getvalue()
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(data)
        return data

    @property
    def bot_schemas(self) -> List[str]:
        return [self.orch_schema] + [c[1] for c in self._children]

    # -- bot writers -----------------------------------------------------

    def _write_bot(
        self,
        zf: zipfile.ZipFile,
        bot_schema: str,
        display_name: str,
        instructions: str,
        overrides: List[str],
        is_orchestrator: bool = False,
        capir: Optional[dict] = None,
    ) -> None:
        """Write a complete bot: bot.xml, configuration.json, gpt.default, system
        topics, and (for a sub-agent carrying a CapIR) the REAL deterministic
        capability topic that runs the same steps as the converted agent.py."""
        # Copilot Studio caps the bot name at 42 chars; keep "Orchestrator" intact.
        display_name = _cap_bot_name(
            display_name, preserve_suffix="Orchestrator" if is_orchestrator else None
        )
        # bot.xml + configuration.json
        zf.writestr(
            f"bots/{bot_schema}/bot.xml",
            BOT_XML.format(
                bot_schema=bot_schema,
                bot_display_name=display_name,
                icon_base64=DEFAULT_ICON_BASE64,
            ),
        )
        gpt_schema = f"{bot_schema}.gpt.default"
        if is_orchestrator:
            # The connected-agent root needs the channels + isLightweightBot config
            # or its post-publish provisioning fails with a 409 ExternalServiceException.
            poi = '\n  "publishOnImport": true,' if self.spec.orchestrator_publish_on_import else ""
            channels = ORCHESTRATOR_CHANNELS_BLOCK if self.spec.orchestrator_channels else ""
            config_json = ORCHESTRATOR_CONFIGURATION_JSON.format(
                gpt_schema=gpt_schema, publish_on_import_line=poi, channels_block=channels
            )
        else:
            config_json = BOT_CONFIGURATION_JSON_NATIVE.format(gpt_schema=gpt_schema)
        zf.writestr(f"bots/{bot_schema}/configuration.json", config_json)

        # gpt.default component (instructions)
        gpt_folder = f"botcomponents/{gpt_schema}"
        zf.writestr(
            f"{gpt_folder}/botcomponent.xml",
            GPT_BOTCOMPONENT_XML.format(
                schema_name=gpt_schema,
                display_name=display_name,
                bot_schema=bot_schema,
            ),
        )
        instr = instructions or f"You are {display_name}. Help the user with their request."
        zf.writestr(
            f"{gpt_folder}/data",
            GPT_DATA_YAML.format(
                display_name=display_name,
                instructions_indented=_indent(instr, 2),
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{gpt_folder}/data"))

        # system topics (one set per bot)
        for topic_key, topic_data in SYSTEM_TOPICS.items():
            schema_name = f"{bot_schema}.topic.{topic_key}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(bot_schema, topic_key, topic_data),
            )
            zf.writestr(
                f"{folder}/data",
                topic_data["data"].format(bot_schema=bot_schema),
            )
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

        # custom per-capability topic: the REAL deterministic behavior, INSIDE
        # this sub-agent (1:1 with the converted agent.py's CapIR steps). The
        # orchestrator stays a pure router and never carries one.
        if capir and not is_orchestrator:
            action = capir_topic_action_name(capir)
            # keep "{bot_schema}.topic.{action}" within the 100-char schema limit
            action = action[: max(4, MAX_SCHEMA - len(bot_schema) - len(".topic."))]
            schema_name = f"{bot_schema}.topic.{action}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(
                    bot_schema, action,
                    {"display_name": _xml_escape(display_name),
                     "description": f"Deterministic handler for {display_name} "
                                    "(seeded records + the real user query, 1:1 with the agent.py)."}),
            )
            zf.writestr(f"{folder}/data", capir_topic_data_yaml(display_name, capir))
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    def _write_connected_action(
        self,
        zf: zipfile.ZipFile,
        sub: SubAgentSpec,
        child_schema: str,
        action: str,
        overrides: List[str],
    ) -> None:
        """Write the orchestrator's delegation component for one sub-agent."""
        schema_name = f"{self.orch_schema}.InvokeConnectedAgentTaskAction.{action}"
        folder = f"botcomponents/{schema_name}"
        description = sub.description or f"Delegate to {sub.display_name}."

        zf.writestr(
            f"{folder}/botcomponent.xml",
            INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML.format(
                schema_name=schema_name,
                description=_xml_escape(description),
                display_name=_xml_escape(sub.display_name),
                orchestrator_schema=self.orch_schema,
            ),
        )
        zf.writestr(
            f"{folder}/dependencies.json",
            INVOKE_CONNECTED_AGENT_DEPENDENCIES.format(child_schema=child_schema),
        )
        inputs_block, input_type_block = _connected_inputs_yaml(getattr(sub, "params", None))
        zf.writestr(
            f"{folder}/data",
            INVOKE_CONNECTED_AGENT_DATA.format(
                display_name=_yaml_display_safe(sub.display_name),
                description_indented=_indent(description, 2),
                child_schema=child_schema,
                inputs_block=inputs_block,
                input_type_block=input_type_block,
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    # -- xml helpers -----------------------------------------------------

    def _topic_botcomponent_xml(self, bot_schema, topic_key, topic_data) -> str:
        schema_name = f"{bot_schema}.topic.{topic_key}"
        desc = topic_data.get("description")
        desc_element = ""
        if desc:
            desc_element = f"\n  <description>{_xml_escape(desc)}</description>"
        return BOTCOMPONENT_XML.format(
            schema_name=schema_name,
            component_type=9,
            display_name=topic_data["display_name"],
            bot_schema=bot_schema,
            description_element=desc_element,
        )

    def _solution_xml(self) -> str:
        return SOLUTION_XML_NATIVE.format(
            solution_unique_name=self.spec.solution_unique_name,
            solution_display_name=self.spec.solution_display_name,
            publisher_unique_name=self.spec.publisher_unique_name,
            publisher_display_name=self.spec.publisher_display_name,
            publisher_prefix=self.spec.publisher_prefix,
            solution_version=self.spec.solution_version,
            managed_flag="1" if self.spec.managed else "0",
        )

    # -- orchestrator instructions --------------------------------------

    def _orchestrator_instructions(self) -> str:
        if self.spec.orchestrator_instructions:
            return self.spec.orchestrator_instructions
        lines = [
            f"You are {self.spec.orchestrator_display_name}, the orchestrator for the "
            f"{self.spec.solution_display_name} workflow. You route each user request to the "
            "right connected sub-agent and never answer specialized questions yourself.",
            "",
            "Connected sub-agents you can delegate to:",
        ]
        for sub, _schema, _action in self._children:
            one_line = re.sub(r"\s+", " ", (sub.description or sub.display_name)).strip()
            lines.append(f"- {sub.display_name}: {one_line}")
        lines += [
            "",
            "Routing rules:",
            "- Read the user's request, pick the single best-matching sub-agent from the list, and delegate to it.",
            "- Pass each sub-agent only the inputs it needs; do not paraphrase or pre-answer its work.",
            "- If the request spans several sub-agents, handle one sub-agent per turn and confirm before moving on.",
            "- If no sub-agent fits, say so and ask a clarifying question rather than inventing an answer.",
        ]
        return "\n".join(lines)


def generate_connected_solution(
    spec: ConnectedSolutionSpec,
    output_path: Optional[Path] = None,
) -> bytes:
    """Build a connected (multi-bot) solution zip from a ConnectedSolutionSpec."""
    return ConnectedSolutionPackager(spec).package(output_path=output_path)


# ============================================================================
# Build sub-agents from an agent stack (agents/*.py + metadata.json) and validate
# ============================================================================

def _humanize(name: str) -> str:
    name = re.sub(r"_stacks$", "", name or "")
    name = name.replace("_", " ").replace("-", " ").strip()
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _humanize_class(name: str) -> str:
    name = re.sub(r"Agent$", "", name or "")
    name = re.sub(r"_agent$", "", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").strip()
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _safe_literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


# Class-body literals a converted agent.py embeds. CAPIR is the compiled CapIR
# (perform()'s spec); SYNTHETIC_DATA holds the seeded records (the build keeps
# them OUT of the CapIR binding, so we re-inject them); the rest let us recompile
# a CapIR when one was not embedded.
_RECOVERED_ATTRS = {"CAPIR", "SYNTHETIC_DATA", "KNOWLEDGE", "RESPONSE",
                    "DOC_NAME", "CUSTOMER", "TRIGGERS"}


def _parse_basic_agent(py_path: Path):
    """AST-extract (display_name, agent_name, description, module_doc, params,
    recovered) from a BasicAgent .py — `recovered` carries any embedded CapIR /
    seeded records used to build the deterministic capability topic."""
    src = py_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    module_doc = (ast.get_docstring(tree) or "").strip()

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "BasicAgent" for b in node.bases
        ):
            cls = node
            break
    if cls is None:
        return None

    self_name = None
    description = ""
    params = []  # (name, description, required)
    recovered = {}  # class-level CAPIR / SYNTHETIC_DATA / ... for deterministic topics
    for sub in ast.walk(cls):
        if not isinstance(sub, ast.Assign):
            continue
        for tgt in sub.targets:
            # class-body literals the build stage embeds (CAPIR = {...},
            # SYNTHETIC_DATA = [...], KNOWLEDGE / RESPONSE / DOC_NAME / CUSTOMER / TRIGGERS)
            if isinstance(tgt, ast.Name) and tgt.id in _RECOVERED_ATTRS:
                val = _safe_literal(sub.value)
                if val is not None:
                    recovered[tgt.id] = val
                continue
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name" and isinstance(sub.value, ast.Constant) and isinstance(sub.value.value, str):
                self_name = sub.value.value
            elif tgt.attr == "metadata" and isinstance(sub.value, ast.Dict):
                # Walk the dict node key-by-key: the metadata literal contains a
                # non-literal value ("name": self.name), so literal_eval on the
                # whole dict fails — pull the literal keys we care about directly.
                for k, v in zip(sub.value.keys, sub.value.values):
                    key = k.value if isinstance(k, ast.Constant) else None
                    if key == "description":
                        dv = _safe_literal(v)
                        if isinstance(dv, str):
                            description = dv.strip()
                    elif key == "parameters":
                        pv = _safe_literal(v)
                        if isinstance(pv, dict):
                            props = pv.get("properties") or {}
                            req = set(pv.get("required") or [])
                            for pn, pinfo in props.items():
                                pdesc = (pinfo.get("description") if isinstance(pinfo, dict) else "") or pn
                                params.append((pn, pdesc, pn in req))

    stem_name = re.sub(r"_agent$", "", py_path.stem)
    agent_name = stem_name
    display = _humanize_class(self_name or stem_name)
    if not description:
        # First paragraph of the module docstring.
        description = re.sub(r"\s+", " ", module_doc.split("\n\n")[0]).strip()
    # Statically infer the SHAPE of the data this agent works with (the dict keys
    # its perform()/helpers read & write) so we can synthesize matching static
    # stand-in records — no execution, no domain rules.
    recovered["INFERRED_FIELDS"] = _infer_record_fields(tree, exclude=[p[0] for p in params])
    return display, agent_name, description, module_doc, params, recovered


def _stack_subagent_instructions(display, description, module_doc, params) -> str:
    """The sub-agent's brain: self-documents the agent.py end-to-end — its purpose
    and its FULL input contract (what the orchestrator passes to delegate). Generic
    for ANY agent.py; no domain assumptions."""
    lines = [f"You are the {display} agent.", "", "# Purpose"]
    lines.append(module_doc.strip() if module_doc else (description or f"Handle {display} requests."))
    lines += ["", "# Inputs the orchestrator passes you"]
    if params:
        for pn, pdesc, required in params:
            tag = "required" if required else "optional"
            clean = re.sub(r"\s+", " ", pdesc).strip()
            lines.append(f"- {pn} ({tag}): {clean}")
    else:
        lines.append("- No structured inputs are required; use the user's request directly.")
    lines += ["", "# How you answer",
              "- Run your deterministic capability topic and ground every answer in its seeded records.",
              "- That seeded data is SYNTHETIC stand-in data for your real source system, so you load "
              "and run end-to-end with no live connection. Swapping the topic's Table() for the live "
              "connector takes you to production with no change to the logic.",
              "- Stay in your lane: if the request belongs to another connected agent, say so and let "
              "the orchestrator route it."]
    return "\n".join(lines)


def _contract_description(description, params, limit=850):
    """The orchestrator-facing routing description: the agent's purpose PLUS its
    input contract, so the Copilot Studio agent knows what to pass when it
    delegates. Self-documenting, generic, length-capped for the component."""
    base = re.sub(r"\s+", " ", description or "").strip()
    if params:
        ins = "; ".join("%s (%s)" % (pn, "required" if req else "optional")
                        for pn, _pd, req in params)
        base = (base + " Inputs to pass: " + ins + ".").strip()
    return base[:limit]


# t2p-capir/1.0 — the load-bearing perform() constants, mirrored so a recompiled
# CapIR carries the same numbers the agent.py uses.
_CAPIR_SCHEMA = "t2p-capir/1.0"
_RECOMPILE_CONSTS = {
    "word_min_len": 3, "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


# Envelope / structural dict keys that are NOT data columns, so schema inference
# never mistakes the result wrapper for record fields.
_ENVELOPE_KEYS = {"status", "agent", "data", "parameters", "properties",
                  "required", "type", "name", "description", "items", "enum",
                  "error", "result", "results", "success", "ok", "count", "as_of_utc"}
# Objects whose `.get("x")` calls are NOT record reads (input kwargs, env, etc.).
_SKIP_GET_OBJS = {"kwargs", "self", "metadata", "os", "sys", "environ", "params", "config"}


def _flatten_record(r):
    """Flatten one record to top-level scalar fields (the Table()/filter columns):
    a nested dict is merged up one level; lists/dicts are json-encoded to strings."""
    if not isinstance(r, dict):
        return {}
    out = {}
    for k, v in r.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[str(kk)] = vv if not isinstance(vv, (list, dict)) else json.dumps(vv, ensure_ascii=False)
        elif isinstance(v, list):
            out[str(k)] = json.dumps(v, ensure_ascii=False)
        else:
            out[str(k)] = v
    return out


def _infer_record_fields(tree, exclude=None, max_fields=14):
    """Infer the SHAPE of the data an agent.py works with by statically scanning
    its code for the dict keys it reads/writes: `rec.get("field")`, `rec["field"]`
    and `{"field": ...}` literals. Excludes input-param names + envelope keys so
    only genuine data columns remain. 100% static — no execution, no domain rules."""
    exclude = set(exclude or []) | _ENVELOPE_KEYS
    keys = []

    def add(k):
        if (isinstance(k, str) and k and k.isidentifier()
                and k not in exclude and k not in keys):
            keys.append(k)

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            obj = node.func.value
            if isinstance(obj, ast.Name) and obj.id in _SKIP_GET_OBJS:
                continue
            a = node.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                add(a.value)
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                add(sl.value)
        elif isinstance(node, ast.Dict):
            klits = [k.value for k in node.keys
                     if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "status" in klits and "data" in klits:
                continue  # a result-envelope literal, not a data record
            for k in klits:
                add(k)
    return keys[:max_fields]


def _synthesize_value(field, i):
    """A clearly-synthetic, generic value for `field` on row i — typed by the field
    NAME's TOKENS only (token-matched, so "age" never fires inside "message"). No
    domain knowledge. Deterministic (index-based, no RNG)."""
    f = field.lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"prob", "probability", "score", "rate", "ratio", "pct", "percent",
               "confidence", "likelihood", "fail", "risk"}:
        return round(0.15 + 0.7 * (((i - 1) % 5) / 4.0), 2)   # 0.15 .. 0.85
    if f.startswith(("is_", "has_")) or toks & {"enabled", "active", "flag", "bool"}:
        return (i % 2 == 0)
    if toks & {"date", "time", "utc", "timestamp", "datetime", "created", "updated"}:
        return "2026-01-%02dT00:00:00Z" % min(i, 28)
    if toks & {"id", "guid", "uuid", "code", "ref"}:
        return "%s-%04d" % ((re.sub(r"[^A-Za-z]", "", field).upper()[:4] or "REC"), i)
    if toks & {"count", "qty", "quantity", "amount", "price", "cost", "value", "age",
               "days", "years", "hours", "num", "number", "level", "index", "size",
               "total", "kv", "voltage", "pct"}:
        return i * 10
    return "synthetic %s %d" % (f.replace("_", " "), i)


def _synthesize_records(fields, n=5):
    """Generate n self-documenting STATIC stand-in records over `fields` — the
    synthetic data that lets the topic load and run end-to-end with no live
    connection. Generic for any field set; swap the Table() for the live connector."""
    fields = [f for f in (fields or []) if f] or ["id", "label", "detail"]
    return [{f: _synthesize_value(f, i) for f in fields} for i in range(1, n + 1)]


def _resolve_capir(recovered, display, agent_name, description, params, capir_mode):
    """Decide the CapIR a sub-agent's deterministic topic is built from — the
    topic that IS this agent.py's perform() running on STATIC stand-in data, so
    the Copilot Studio orchestrator gets the same result it would by chatting the
    brainstem and invoking the agent.py.

    Policy (capir_mode):
      off       -> never emit a topic (instructions-blob only)
      embedded  -> only when the agent.py embeds a CAPIR literal
      static    -> embedded, else recompile ONLY from real seeded data
                   (SYNTHETIC_DATA); do not synthesize a stand-in
      auto      -> (default) embedded, else recompile from SYNTHETIC_DATA, else
                   SYNTHESIZE static stand-in data from the agent's inferred data
                   shape. Maps EVERY agent.py to a self-documented topic."""
    mode = (capir_mode or "auto").lower()
    if mode in ("capture", "always", "run"):
        mode = "auto"
    if mode == "off":
        return None
    synth = recovered.get("SYNTHETIC_DATA") or []
    embedded = recovered.get("CAPIR")
    if isinstance(embedded, dict) and embedded.get("steps"):
        binding = dict(embedded.get("binding") or {})
        if not binding.get("records"):
            binding["records"] = synth
        if not binding.get("fields"):
            binding["fields"] = _capir_topic_fields(binding.get("records"))
        out = {**embedded, "binding": binding}
        out.setdefault("customer", recovered.get("CUSTOMER") or "the customer")
        return out
    if mode == "embedded":
        return None
    if mode == "static":
        return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                          params, records=synth) if synth else None
    # auto: always map — real seeded data if present, else a STATIC stand-in
    # synthesized from the agent's inferred data shape (its perform() field reads).
    records = synth
    if not records:
        fields = recovered.get("INFERRED_FIELDS") or [p[0] for p in (params or [])]
        records = _synthesize_records(fields)
    return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                      params, records=records)


def _recompile_capir_from_meta(recovered, display, agent_name, description, params, records=None):
    """Build a CapIR for an agent.py with no embedded CAPIR — mirrors T2P's
    _compile_capir shape from its records (real or synthesized), KNOWLEDGE,
    RESPONSE, DOC_NAME, TRIGGERS plus the parsed metadata. Same structure and
    perform()-parity constants as the generated path; only the source differs."""
    records = [_flatten_record(r) for r in (records if records is not None
               else (recovered.get("SYNTHETIC_DATA") or []))][:10]
    knowledge = list(recovered.get("KNOWLEDGE") or [])
    triggers = list(recovered.get("TRIGGERS") or [])
    if not triggers:
        triggers = [display] + ([re.sub(r"\s+", " ", description).strip()[:60]]
                                if description else [])
    response = recovered.get("RESPONSE") or description or f"Here is how I handle {display}."
    doc = recovered.get("DOC_NAME") or None
    key = re.sub(r"[^a-z0-9_]", "", (agent_name or display).lower().replace(" ", "_")) or "capability"
    fields = _capir_topic_fields(records)
    prompt = f"What would you like to ask the {display} agent? (a keyword, id, or value to filter on)"
    binding = {
        "connector": "table",
        "table": "rec_" + key,
        "library": display + " Library",
        "fields": fields,
        "key_field": fields[0] if fields else "id",
        "row_count": len(records),
        "records": records,
    }
    steps = [
        {"id": "trigger", "op": "trigger_match", "queries": triggers},
        {"id": "slot_query", "op": "slot_fill", "slot": "query"},
        {"id": "ground", "op": "knowledge_lookup", "facts": knowledge, "into": "Grounding"},
        {"id": "lookup", "op": "record_lookup", "source": "binding", "from": "query",
         "into": "Matches", "take": _RECOMPILE_CONSTS["example_take"],
         "fallback_take": _RECOMPILE_CONSTS["fallback_take"]},
        {"id": "respond", "op": "respond", "template_kind": "standard"},
    ]
    if doc:
        steps.append({"id": "artifact", "op": "artifact", "doc": doc,
                      "from": ["Grounding", "Matches"]})
    return {
        "schema": _CAPIR_SCHEMA,
        "key": key,
        "response": response,
        "customer": recovered.get("CUSTOMER") or "the customer",
        "binding": binding,
        "slots": [{"name": "query", "entity": "StringPrebuiltEntity",
                   "prompt": prompt, "required": True}],
        "consts": dict(_RECOMPILE_CONSTS),
        "steps": steps,
        "expect": list(triggers),
        "triggers_owned": True,
    }


def _subagents_from_stack(stack_dir: Path, capir_mode: str = "auto") -> List[SubAgentSpec]:
    agents_dir = stack_dir / "agents"
    if not agents_dir.is_dir():
        agents_dir = stack_dir
    subs: List[SubAgentSpec] = []
    for py in sorted(agents_dir.glob("*.py")):
        if py.name.startswith("_") or py.name == "basic_agent.py":
            continue
        parsed = _parse_basic_agent(py)
        if not parsed:
            logger.warning("  - %s: no BasicAgent subclass, skipping", py.name)
            continue
        display, agent_name, description, module_doc, params, recovered = parsed
        capir = _resolve_capir(recovered, display, agent_name, description, params, capir_mode)
        subs.append(SubAgentSpec(
            agent_name=agent_name,
            display_name=display,
            # description carries the input contract so the orchestrator knows what
            # to pass when it delegates (self-documented, like the agent.py).
            description=_contract_description(description, params) or f"Handle {display} requests.",
            instructions=_stack_subagent_instructions(display, description, module_doc, params),
            capir=capir,
            params=params,
        ))
        logger.info("  + %s%s", display, "  [deterministic topic]" if capir else "")
    return subs


def _load_stack_metadata(stack_dir: Path) -> dict:
    mpath = stack_dir / "metadata.json"
    if mpath.is_file():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _orchestrator_instructions_from_metadata(meta: dict, subs: List[SubAgentSpec]) -> str:
    name = meta.get("name", "the agent stack")
    desc = meta.get("description", "")
    lines = [f"You are the orchestrator for {name}.", ""]
    if desc:
        lines += [desc, ""]
    lines.append("You route each user request to the right connected sub-agent and never do their specialized work yourself.")
    features = meta.get("features") or []
    if features:
        lines += ["", "End-to-end flow this stack supports, in order:"]
        lines += [f"- {f}" for f in features]
    lines += ["", "Connected sub-agents you can delegate to:"]
    for sub in subs:
        lines.append(f"- {sub.display_name}: {sub.description}")
    starters = meta.get("starters") or []
    if starters:
        lines += ["", "Example requests you should expect:"]
        lines += [f"- {s}" for s in starters]
    lines += [
        "",
        "Routing rules:",
        "- Pick the single best-matching connected agent for the request and delegate to it; pass it the inputs named in its description.",
        "- Calling a connected agent gives you the SAME result you would get by chatting the source brainstem and letting it invoke that agent.py — each connected agent's topic runs the agent's deterministic logic on its seeded sample data.",
        "- If a request spans several connected agents, handle one per turn, show its result, then continue to the next.",
        "- If a required input is missing, ask for it. The seeded data is synthetic stand-in data; do not invent records beyond it.",
        "- If no connected agent fits, say so and ask a clarifying question.",
    ]
    return "\n".join(lines)


def validate_connected_solution(zip_path: Path) -> bool:
    """Structural checks that the connected solution is import-shaped."""
    ok = True
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())

        for required in ("[Content_Types].xml", "solution.xml", "customizations.xml"):
            if required not in names:
                logger.error("  X missing %s", required)
                ok = False

        bots = sorted({n.split("/")[1] for n in names if n.startswith("bots/")})
        logger.info("  bots: %d (%s)", len(bots), ", ".join(bots))

        # Every connected-action must reference an existing child bot.
        actions = [n for n in names if ".InvokeConnectedAgentTaskAction." in n and n.endswith("/dependencies.json")]
        logger.info("  connected-agent actions: %d", len(actions))
        for dep in actions:
            child = json.loads(zf.read(dep).decode("utf-8"))[0]["schemaName"]
            if f"bots/{child}/bot.xml" not in names:
                logger.error("  X action %s -> missing child bot %s", dep, child)
                ok = False
            data_path = dep.rsplit("/", 1)[0] + "/data"
            if data_path in names:
                data_text = zf.read(data_path).decode("utf-8")
                if f"botSchemaName: {child}" not in data_text:
                    logger.error("  X %s data does not invoke %s", data_path, child)
                    ok = False

        # Every extensionless /data part must be declared in [Content_Types].xml.
        ct = zf.read("[Content_Types].xml").decode("utf-8")
        data_parts = [n for n in names if n.endswith("/data")]
        missing = [p for p in data_parts if f'PartName="/{p}"' not in ct]
        if missing:
            logger.error("  X %d /data parts missing from [Content_Types].xml (e.g. %s)",
                         len(missing), missing[0])
            ok = False
        else:
            logger.info("  content-types: all %d /data parts declared", len(data_parts))

        # Each bot needs gpt.default + the system-topic set.
        for bot in bots:
            if f"botcomponents/{bot}.gpt.default/data" not in names:
                logger.error("  X bot %s missing gpt.default", bot)
                ok = False

        # No botcomponent schema name may exceed the Dataverse 100-char limit.
        schemas = {n.split("/")[1] for n in names if n.startswith("botcomponents/")}
        longest = max(schemas, key=len) if schemas else ""
        if len(longest) > 100:
            logger.error("  X schema name too long (%d > 100): %s", len(longest), longest)
            ok = False
        else:
            logger.info("  schema lengths: max %d/100 (%s)", len(longest), longest)

        # Copilot Studio rejects bot display names longer than 42 chars.
        worst_name, worst_len = "", 0
        for bot in bots:
            bx = zf.read(f"bots/{bot}/bot.xml").decode("utf-8")
            m = re.search(r"<name>(.*?)</name>", bx, re.DOTALL)
            nm = (m.group(1).strip() if m else "")
            if len(nm) > worst_len:
                worst_name, worst_len = nm, len(nm)
        if worst_len > 42:
            logger.error("  X bot name too long (%d > 42): %s", worst_len, worst_name)
            ok = False
        else:
            logger.info("  bot names: max %d/42 (%s)", worst_len, worst_name)
    return ok


# ===========================================================================
# Autonomous deploy to Microsoft Copilot Studio (Dataverse Web API, stdlib only)
#
# Self-contained so this one file, dropped into any brainstem, can BOTH package a
# connected-agents solution AND import + publish it into a real Copilot Studio
# environment — no pac CLI, no third-party packages. App-registration credentials
# come ONLY from env vars or a settings file, never from chat, and the secret is
# never echoed back. Same proven path as the T2P deploy agent: service-principal
# token -> ImportSolution -> PvaPublish (children first, orchestrator last).
# ===========================================================================

_DEPLOY_AUTH = "https://login.microsoftonline.com"


def _http(url, data=None, headers=None, method=None, timeout=300):
    """Minimal stdlib HTTP: dict data -> form-encoded (OAuth), else JSON bytes."""
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body
    except Exception as e:  # network / DNS / timeout
        return 0, str(e)


def _extract_dyn_creds(creds):
    """From a settings dict ({IsEncrypted,Values} or bare), a Values dict, or a
    JSON string -> {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try:
            creds = json.loads(creds)
        except Exception:
            return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": str(res).rstrip("/")}


def _deploy_creds(kwargs):
    """Resolve app-registration creds for deploy — env / settings file ONLY, never
    from chat. Returns (creds_dict, source_label) or (None, None)."""
    candidates = [
        os.path.expanduser(kwargs["credentials_path"]) if kwargs.get("credentials_path") else None,
        os.environ.get("RAPP_DEPLOY_SETTINGS"),
        os.path.expanduser("~/.rapp_deploy_settings.json"),
        "local.settings.json",
    ]
    for cand in candidates:
        if cand and os.path.isfile(cand):
            try:
                c = _extract_dyn_creds(json.load(open(cand)))
                if c:
                    return c, cand
            except Exception:
                pass
    c = _extract_dyn_creds({"Values": dict(os.environ)})
    if c:
        return c, "process env"
    return None, None


def _sp_token(client_id, secret, tenant, resource):
    """Service-principal (client-credentials) token for the Dataverse env."""
    code, t = _http(f"{_DEPLOY_AUTH}/{tenant}/oauth2/v2.0/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                    headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError("service-principal auth failed: " + str(t)[:200])
    return t["access_token"]


def _dataverse_action(resource, token, action, body=None, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    return _http(resource.rstrip("/") + "/api/data/v9.2/" + action, data=data, method=method,
                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                          "Accept": "application/json", "OData-MaxVersion": "4.0",
                          "OData-Version": "4.0"})


def _import_solution(resource, token, zip_bytes):
    """ImportSolution (unmanaged, overwrite) then PublishAllXml."""
    code, r = _dataverse_action(resource, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()),
        "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError("ImportSolution failed (%s): %s" % (code, str(r)[:400]))
    _dataverse_action(resource, token, "PublishAllXml")


def _find_botid(resource, token, schema):
    qs = urllib.parse.urlencode({"$select": "botid,schemaname",
                                 "$filter": "schemaname eq '%s'" % schema,
                                 "$orderby": "createdon desc", "$top": "1"})
    code, r = _http(resource.rstrip("/") + "/api/data/v9.2/bots?" + qs,
                    headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    rows = (r.get("value") if isinstance(r, dict) else None) or []
    return rows[0]["botid"] if rows else None


def _publish_botid(botid, resource, token):
    """Publish ONE bot via the Dataverse PvaPublish Web API action. PURE HTTPS —
    no pac/CLI/subprocess — so this agent.py runs identically in a local brainstem
    AND inside an Azure-Function-hosted brainstem (no binary to ship)."""
    code, r = _dataverse_action(resource, token,
                                "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % botid, {})
    if code in (200, 204):
        return {"bot_id": botid, "status": "publish_requested", "via": "PvaPublish"}
    return {"bot_id": botid, "status": "publish_failed", "via": "PvaPublish", "error": str(r)[:160]}


def _publish_connected(bot_schemas, resource, token):
    """Publish every bot — CHILDREN first, ORCHESTRATOR last (a connected-agent
    root cannot publish until its invoked sub-agents are published)."""
    if not bot_schemas:
        return []
    orch = bot_schemas[0]
    order = list(bot_schemas[1:]) + [orch]
    out = []
    for schema in order:
        botid = _find_botid(resource, token, schema)
        if not botid:
            out.append({"schema": schema, "status": "not_found"})
            continue
        out.append({"schema": schema, **_publish_botid(botid, resource, token)})
    return out


def _run_deploy(zip_bytes, bot_schemas, orch_display, kwargs):
    """Import + (optionally) publish the connected solution into Copilot Studio.
    Returns a result dict with a human `summary`; never includes the secret."""
    creds, src = _deploy_creds(kwargs)
    if creds and kwargs.get("environment_url"):
        creds = {**creds, "resource": str(kwargs["environment_url"]).rstrip("/")}
    if not creds:
        return {"status": "creds_missing",
                "summary": "NOT deployed — no app-registration credentials found.",
                "how_to": ("Set env DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / "
                           "DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE, or pass "
                           "credentials_path=<local.settings.json>, or place "
                           "~/.rapp_deploy_settings.json. Secrets never travel through chat.")}
    publish = bool(kwargs.get("publish", True))
    try:
        token = _sp_token(creds["client_id"], creds["client_secret"],
                          creds["tenant_id"], creds["resource"])
    except Exception as e:
        return {"status": "auth_failed", "summary": "NOT deployed — service-principal auth failed.",
                "error": str(e)[:300], "creds_source": src, "environment": creds["resource"]}
    try:
        _import_solution(creds["resource"], token, zip_bytes)
    except Exception as e:
        return {"status": "import_failed", "summary": "Import FAILED.", "error": str(e)[:400],
                "environment": creds["resource"], "creds_source": src}
    published = _publish_connected(bot_schemas, creds["resource"], token) if publish else []
    npub = sum(1 for p in published if p.get("status") in ("published", "publish_requested"))
    summary = ("Imported into " + creds["resource"] + " and "
               + (("published %d/%d bots. " % (npub, len(published))) if publish else "skipped publish. ")
               + "Open Copilot Studio, select that environment, open '"
               + orch_display[:42] + "' and use the Test pane.")
    return {"status": "deployed", "summary": summary, "environment": creds["resource"],
            "orchestrator": orch_display[:42], "publish_enabled": publish,
            "published": published, "creds_source": src,
            "test_in_studio": "https://copilotstudio.microsoft.com"}


# ---------------------------------------------------------------------------
# RAPP agent wrapper
# ---------------------------------------------------------------------------

class ConnectedSolutionAgent(BasicAgent):
    """Generate a connected-agent (orchestrator + sub-agents) Copilot Studio solution."""

    def __init__(self):
        self.name = "ConnectedSolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn an agent stack (a folder of BasicAgent *.py files + optional "
                "metadata.json) or an explicit list of sub-agents into ONE import-ready "
                "Microsoft Copilot Studio connected-agent solution: an orchestrator plus "
                "one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. "
                "When an agent.py carries its compiled CapIR (t2p-capir/1.0) — or one can be "
                "recompiled from its seeded data — each sub-agent ALSO gets a REAL "
                "deterministic capability topic that runs the same steps as the agent.py's "
                "perform() (trigger -> the user's real query -> filter the seeded records -> "
                "branch -> respond, plus the document for artifact capabilities); only the "
                "data is mocked, so flipping the in-topic Table() to a live Dataverse / "
                "SharePoint connector is the one-line move to production. No code deploy. Bot "
                "names are auto-capped to 42 chars and orchestrator channels default off so it "
                "imports and publishes fully headlessly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "stack_dir": {
                        "type": "string",
                        "description": "Path to an agent stack folder. Each BasicAgent *.py under it "
                                       "(or its agents/ subfolder) becomes one connected sub-agent; "
                                       "metadata.json (name/description/features/starters) shapes the orchestrator.",
                    },
                    "subagents": {
                        "type": "array",
                        "description": "Alternative to stack_dir: explicit sub-agents, each an object with "
                                       "agent_name, display_name, description, instructions.",
                    },
                    "solution_name": {
                        "type": "string",
                        "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
                    },
                    "solution_display_name": {"type": "string", "description": "Solution friendly name."},
                    "orchestrator_name": {
                        "type": "string",
                        "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
                    },
                    "orchestrator_channels": {
                        "type": "boolean",
                        "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false "
                                       "(headlessly publishable). True requires a maker-portal publish.",
                    },
                    "capir_mode": {
                        "type": "string",
                        "description": "How to build the deterministic per-capability topic inside each "
                                       "sub-agent (the topic that runs the agent.py's perform() logic on STATIC "
                                       "synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else "
                                       "real seeded data, else SYNTHESIZES static stand-in records from the "
                                       "agent's inferred data shape — so EVERY agent.py maps to a self-documented "
                                       "topic; 'static' uses only real seeded data (no synthetic stand-in); "
                                       "'embedded' uses only an embedded CapIR; 'off' emits instructions-only "
                                       "sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
                    },
                    "version": {"type": "string", "description": "Solution version, e.g. 1.0.0.0."},
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
                    },
                    "deploy": {
                        "type": "boolean",
                        "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot "
                                       "Studio (Dataverse) environment and publish every bot (sub-agents first, "
                                       "orchestrator last) — no pac CLI needed, stdlib only. App-registration "
                                       "credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) "
                                       "or a settings file — NEVER from chat. Default false (package only).",
                    },
                    "publish": {
                        "type": "boolean",
                        "description": "When deploy=true, also publish the bots after import (default true). "
                                       "false imports without publishing.",
                    },
                    "credentials_path": {
                        "type": "string",
                        "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE "
                                       "(under a top-level 'Values' object or at the root). Used only for deploy; "
                                       "the secret is never echoed back. If omitted, env vars / "
                                       "~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Optional override for the target Dataverse environment URL (e.g. "
                                       "https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, "
                                       "default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a "
                                       "distinct solution instead of updating ones that already exist.",
                    },
                    "publisher_name": {
                        "type": "string",
                        "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh "
                                       "publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
                    },
                    "publisher_display": {
                        "type": "string",
                        "description": "Solution publisher friendly name (default 'Default Publisher').",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        stack_dir = kwargs.get("stack_dir")
        subagents_in = kwargs.get("subagents")
        if not stack_dir and not subagents_in:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide 'stack_dir' (a folder of BasicAgent *.py + optional metadata.json) "
                           "or 'subagents' (a list of {agent_name, display_name, description, instructions}).",
            }

        meta: Dict[str, Any] = {}
        if stack_dir:
            sd = Path(stack_dir)
            if not sd.exists():
                return {"status": "error", "agent": self.name, "message": f"stack_dir not found: {sd}"}
            subs = _subagents_from_stack(sd, capir_mode=str(kwargs.get("capir_mode") or "auto"))
            meta = _load_stack_metadata(sd)
            fallback = _humanize(sd.name)
        else:
            subs = []
            for s in subagents_in:
                dn = s.get("display_name") or s.get("agent_name") or "Agent"
                subs.append(SubAgentSpec(
                    agent_name=s.get("agent_name") or dn,
                    display_name=dn,
                    description=(s.get("description") or "").strip() or f"Handle {dn} requests.",
                    instructions=s.get("instructions") or "",
                    capir=s.get("capir") if isinstance(s.get("capir"), dict) else None,
                ))
            fallback = kwargs.get("solution_name") or "Connected Agents"

        if not subs:
            return {"status": "error", "agent": self.name, "message": "No sub-agents found to bundle."}

        short = re.sub(r"\b(Agent\s+Stack|Agent|Stack)\b", "", meta.get("name", "")).strip()
        unique = re.sub(r"[^A-Za-z0-9]", "",
                        kwargs.get("solution_name") or meta.get("id", "") or fallback.replace(" ", ""))
        display = kwargs.get("solution_display_name") or meta.get("name") or f"{fallback} Agents"
        orch_name = kwargs.get("orchestrator_name") or f"{short or fallback} Orchestrator"
        orch_instructions = _orchestrator_instructions_from_metadata(meta, subs) if meta else ""

        spec = ConnectedSolutionSpec(
            solution_unique_name=unique or "ConnectedAgents",
            solution_display_name=display,
            orchestrator_display_name=orch_name,
            subagents=subs,
            orchestrator_instructions=orch_instructions,
            orchestrator_channels=bool(kwargs.get("orchestrator_channels", False)),
            solution_version=kwargs.get("version", "1.0.0.0"),
            # publisher controls — a fresh publisher_prefix mints brand-new bot
            # schema names (an isolated, clearly-distinct solution), instead of
            # updating bots that already exist under the default 'rapp' prefix.
            publisher_prefix=re.sub(r"[^a-z0-9]", "", str(kwargs.get("publisher_prefix") or _DEFAULT_PUBLISHER_PREFIX).lower())[:8] or _DEFAULT_PUBLISHER_PREFIX,
            publisher_unique_name=kwargs.get("publisher_name") or "DefaultPublisher",
            publisher_display_name=kwargs.get("publisher_display") or "Default Publisher",
        )
        packager = ConnectedSolutionPackager(spec)
        out = Path(kwargs.get("output_path") or f"{spec.solution_unique_name}_connected_solution.zip")
        data = packager.package(output_path=out)
        ok = validate_connected_solution(out)

        # autonomous deploy: import into Copilot Studio + publish the bots
        # (children first, orchestrator last). Creds come ONLY from env / a
        # settings file — never from chat.
        deploy_result = _run_deploy(data, list(packager.bot_schemas), display, kwargs) \
            if kwargs.get("deploy") else None

        capir_topics = sum(1 for s in subs if getattr(s, "capir", None))
        msg = (f"Generated '{out.name}' — {len(packager.bot_schemas)} bots "
               f"(1 orchestrator + {len(subs)} connected sub-agents, "
               f"{capir_topics} with a deterministic capability topic), "
               f"{round(len(data)/1024,1)} KB. Validation: {'pass' if ok else 'fail'}.")
        if deploy_result:
            msg += " " + deploy_result.get("summary", "")

        data_block = {
            "solution_path": str(out),
            "size_kb": round(len(data) / 1024, 1),
            "orchestrator_schema": packager.orch_schema,
            "sub_agents": [s.display_name for s in subs],
            "capir_topics": capir_topics,
            "deterministic_topics": [s.display_name for s in subs if getattr(s, "capir", None)],
            "validation": "pass" if ok else "fail",
        }
        status = "success" if ok else "error"
        if deploy_result:
            data_block["deploy"] = deploy_result
            if deploy_result.get("status") not in ("deployed",):
                status = "partial"
        else:
            data_block["deploy_hint"] = ("Pass deploy=true to import + publish into your Copilot Studio "
                                         "environment automatically (creds from env DYNAMICS_365_CLIENT_ID/"
                                         "SECRET/TENANT_ID/RESOURCE or a settings file via credentials_path).")
            data_block["m365_exposure"] = ("Set orchestrator_channels=true and publish the orchestrator "
                                           "in the maker portal for M365/Teams exposure.")
        return {"status": status, "agent": self.name, "message": msg, "data": data_block}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("usage: python connected_solution_agent.py <stack_dir> [output.zip]")
        sys.exit(1)
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    result = ConnectedSolutionAgent().perform(stack_dir=target, output_path=out_path)
    print(json.dumps(result, indent=2))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
