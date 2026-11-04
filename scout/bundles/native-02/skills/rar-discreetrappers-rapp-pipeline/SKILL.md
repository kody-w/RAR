---
name: "rar-discreetrappers-rapp-pipeline"
description: "Unified RAPP Pipeline agent for building AI agents from discovery to deployment.\n\nRECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.\n\nAll actions:\n- AUTO: auto_process (scans inputs, processes, generates reports), generate_report\n- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary\n- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document\n- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code\n- Quality Gates: execute_quality_gate (gate: QG1-QG6)\n- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/rapp_pipeline_agent", "rar_sha256": "a5dc861857f4108578603c1ce6a547ee766c55cd2eb8b0bd5f6cfd1378954089", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Bill Whalen", "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/rapp_pipeline_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_pipeline_agent.py` and in the RCI capsule.

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

RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
      "enum": [
        "transcript_to_agent",
        "auto_process",
        "generate_report",
        "prepare_discovery_call",
        "process_transcript",
        "generate_discovery_summary",
        "generate_mvp_poke",
        "prioritize_features",
        "define_scope",
        "estimate_timeline",
        "generate_full_mvp_document",
        "generate_agent_code",
        "generate_agent_metadata",
        "generate_agent_tests",
        "generate_deployment_config",
        "review_code",
        "execute_quality_gate",
        "get_step_guidance",
        "get_pipeline_status",
        "recommend_next_action",
        "get_step_checklist",
        "validate_step_completion"
      ],
      "type": "string"
    },
    "agent_description": {
      "description": "Description of agent capabilities",
      "type": "string"
    },
    "agent_name": {
      "description": "Name for generated agent (e.g., 'InventoryOptimizer')",
      "type": "string"
    },
    "agent_priority": {
      "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')",
      "type": "string"
    },
    "constraints": {
      "description": "Timeline, budget, or technical constraints",
      "type": "object"
    },
    "customer_name": {
      "description": "Customer/company name",
      "type": "string"
    },
    "data_sources": {
      "description": "Data sources for agent integration",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "deploy_to_storage": {
      "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)",
      "type": "boolean"
    },
    "discovery_data": {
      "description": "Structured discovery data from transcript processing",
      "type": "object"
    },
    "existing_code": {
      "description": "Existing code for review or test generation",
      "type": "string"
    },
    "features": {
      "description": "List of features/capabilities",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "gate": {
      "description": "Quality gate to execute (required for execute_quality_gate action)",
      "enum": [
        "QG1",
        "QG2",
        "QG3",
        "QG4",
        "QG5",
        "QG6"
      ],
      "type": "string"
    },
    "industry": {
      "description": "Customer industry (e.g., retail, healthcare, manufacturing)",
      "type": "string"
    },
    "input_data": {
      "description": "Input data for quality gate validation or other operations",
      "type": "object"
    },
    "problem_statement": {
      "description": "Validated problem statement",
      "type": "string"
    },
    "project_data": {
      "description": "Current project progress data",
      "type": "object"
    },
    "project_id": {
      "description": "Project ID for storing results",
      "type": "string"
    },
    "project_name": {
      "description": "Project name",
      "type": "string"
    },
    "report_type": {
      "description": "Type of report to generate (for generate_report action)",
      "enum": [
        "discovery",
        "qg1",
        "qg2",
        "qg3",
        "qg4",
        "qg5",
        "qg6",
        "mvp",
        "code",
        "deployment",
        "demo",
        "executive_summary",
        "full_pipeline"
      ],
      "type": "string"
    },
    "step": {
      "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
      "maximum": 14,
      "minimum": 1,
      "type": "integer"
    },
    "transcript": {
      "description": "Discovery call transcript to process",
      "type": "string"
    },
    "user_guid": {
      "description": "User GUID for project data access",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_pipeline_agent.py` and embedded as the fenced Python below (sha256 a5dc861857f41085…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_pipeline_agent.py` first:

```bash
python3 rapp_pipeline_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_pipeline_agent.py   # or on stdin
python3 rapp_pipeline_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/rapp_pipeline_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_pipeline_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/rapp_pipeline_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/rapp_pipeline_agent",
    "version": "1.0.2",
    "display_name": "RAPP",
    "description": "Runs the full RAPP pipeline \u2014 discovery, MVP, code gen, quality gates QG1-QG6, PDF reports \u2014 using Azure OpenAI and Azure File Storage.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

try:
    from openai import AzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    AZURE_OPENAI_AVAILABLE = True
    AZURE_OPENAI_IMPORT_ERROR = None
except ImportError as e:
    AzureOpenAI = None
    DefaultAzureCredential = None
    get_bearer_token_provider = None
    AZURE_OPENAI_AVAILABLE = False
    AZURE_OPENAI_IMPORT_ERROR = str(e)

# Import report generator (optional - handles import errors gracefully)
try:
    from utils.rapp_report_generator import RAPPReportGenerator, generate_rapp_report
    REPORT_GENERATOR_AVAILABLE = True
except Exception:
    # Catches ImportError, NameError, and other module-level errors
    REPORT_GENERATOR_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_llm_json_response(response_text: str, fallback_key: str = "raw_response") -> dict:
    """Parse JSON from LLM response, handling markdown code blocks."""
    try:
        text = response_text
        if '```json' in text:
            text = text.split('```json')[-1].split('```')[0]
        elif '```' in text:
            parts = text.split('```')
            if len(parts) >= 2:
                text = parts[1]
        json_start = text.find('{')
        json_end = text.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            return json.loads(text[json_start:json_end])
        return {fallback_key: response_text}
    except json.JSONDecodeError:
        return {fallback_key: response_text}


class RAPPAgent(BasicAgent):
    """
    Unified RAPP Pipeline Agent - handles ALL pipeline operations.

    This is the ONLY agent needed for RAPP Pipeline work. Use this agent for:
    - Discovery call preparation and transcript processing
    - MVP document generation and scope definition
    - Agent code generation and review
    - Quality gate validations (QG1-QG6)
    - Pipeline orchestration and progress tracking

    DO NOT use individual RAPP agents - use this unified agent instead.
    """

    # Pipeline step definitions
    PIPELINE_STEPS = {
        1: {"name": "Discovery Call", "type": "manual"},
        2: {"name": "Transcript Analysis", "type": "audit", "gate": "QG1"},
        3: {"name": "Generate MVP Poke", "type": "manual"},
        4: {"name": "Customer Validation", "type": "audit", "gate": "QG2"},
        5: {"name": "Generate Agent Code", "type": "manual"},
        6: {"name": "Code Quality Review", "type": "audit", "gate": "QG3"},
        7: {"name": "Deploy Prototype", "type": "manual"},
        8: {"name": "Demo Review", "type": "audit", "gate": "QG4"},
        9: {"name": "Generate Video Demo", "type": "manual"},
        10: {"name": "Final Demo Review", "type": "audit", "gate": "QG5"},
        11: {"name": "Iteration Loop", "type": "manual"},
        12: {"name": "Production Deployment", "type": "manual"},
        13: {"name": "Post-Deployment Audit", "type": "audit", "gate": "QG6"},
        14: {"name": "Scale & Maintain", "type": "manual"}
    }

    # Quality gate configurations
    GATE_CONFIGS = {
        "QG1": {"name": "Transcript Validation", "step": 2, "decisions": ["PASS", "CLARIFY", "FAIL"]},
        "QG2": {"name": "Customer Validation", "step": 4, "decisions": ["PROCEED", "REVISE", "HOLD"]},
        "QG3": {"name": "Code Quality Review", "step": 6, "decisions": ["PASS", "FIX_REQUIRED", "FAIL"]},
        "QG4": {"name": "Demo Review", "step": 8, "decisions": ["PASS", "POLISH", "FAIL"]},
        "QG5": {"name": "Final Demo Review", "step": 10, "decisions": ["APPROVE", "MINOR_REVISIONS", "MAJOR_REVISIONS", "REJECT"]},
        "QG6": {"name": "Post-Deployment Audit", "step": 13, "decisions": ["GREEN", "YELLOW", "RED"]}
    }

    # Input file patterns for auto-detection
    INPUT_PATTERNS = {
        "discovery_transcript": ["transcript", "discovery", "call_notes", "meeting_notes"],
        "customer_feedback": ["feedback", "customer_response", "validation", "approval"],
        "code_to_review": [".py"],
        "requirements": ["requirements", "mvp_requirements", "features"],
        "demo_notes": ["demo", "presentation", "video_script"],
        "deployment_metrics": ["metrics", "telemetry", "usage", "health"],
    }

    # Report types for each step
    STEP_REPORTS = {
        1: "discovery",
        2: "qg1",
        3: "mvp",
        4: "qg2",
        5: "code",
        6: "qg3",
        7: "deployment",
        8: "qg4",
        9: "demo",
        10: "qg5",
        11: "iteration",
        12: "production",
        13: "qg6",
        14: "maintenance"
    }

    def __init__(self):
        self.name = 'RAPP'
        self.metadata = {
            "name": self.name,
            "description": """Unified RAPP Pipeline agent for building AI agents from discovery to deployment.

RECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.

All actions:
- AUTO: auto_process (scans inputs, processes, generates reports), generate_report
- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary
- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document
- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code
- Quality Gates: execute_quality_gate (gate: QG1-QG6)
- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
                        "enum": [
                            "transcript_to_agent",
                            "auto_process",
                            "generate_report",
                            "prepare_discovery_call",
                            "process_transcript",
                            "generate_discovery_summary",
                            "generate_mvp_poke",
                            "prioritize_features",
                            "define_scope",
                            "estimate_timeline",
                            "generate_full_mvp_document",
                            "generate_agent_code",
                            "generate_agent_metadata",
                            "generate_agent_tests",
                            "generate_deployment_config",
                            "review_code",
                            "execute_quality_gate",
                            "get_step_guidance",
                            "get_pipeline_status",
                            "recommend_next_action",
                            "get_step_checklist",
                            "validate_step_completion"
                        ]
                    },
                    "report_type": {
                        "type": "string",
                        "description": "Type of report to generate (for generate_report action)",
                        "enum": ["discovery", "qg1", "qg2", "qg3", "qg4", "qg5", "qg6", "mvp", "code", "deployment", "demo", "executive_summary", "full_pipeline"]
                    },
                    "gate": {
                        "type": "string",
                        "description": "Quality gate to execute (required for execute_quality_gate action)",
                        "enum": ["QG1", "QG2", "QG3", "QG4", "QG5", "QG6"]
                    },
                    "step": {
                        "type": "integer",
                        "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
                        "minimum": 1,
                        "maximum": 14
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "Customer/company name"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "Project name"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Customer industry (e.g., retail, healthcare, manufacturing)"
                    },
                    "transcript": {
                        "type": "string",
                        "description": "Discovery call transcript to process"
                    },
                    "problem_statement": {
                        "type": "string",
                        "description": "Validated problem statement"
                    },
                    "discovery_data": {
                        "type": "object",
                        "description": "Structured discovery data from transcript processing"
                    },
                    "input_data": {
                        "type": "object",
                        "description": "Input data for quality gate validation or other operations"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name for generated agent (e.g., 'InventoryOptimizer')"
                    },
                    "agent_description": {
                        "type": "string",
                        "description": "Description of agent capabilities"
                    },
                    "features": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of features/capabilities"
                    },
                    "data_sources": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Data sources for agent integration"
                    },
                    "existing_code": {
                        "type": "string",
                        "description": "Existing code for review or test generation"
                    },
                    "constraints": {
                        "type": "object",
                        "description": "Timeline, budget, or technical constraints"
                    },
                    "project_data": {
                        "type": "object",
                        "description": "Current project progress data"
                    },
                    "project_id": {
                        "type": "string",
                        "description": "Project ID for storing results"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User GUID for project data access"
                    },
                    "deploy_to_storage": {
                        "type": "boolean",
                        "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)"
                    },
                    "agent_priority": {
                        "type": "string",
                        "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')"
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def _get_openai_client(self):
        """Initialize Azure OpenAI client with Entra ID authentication."""
        if not AZURE_OPENAI_AVAILABLE:
            raise RuntimeError(
                "Azure OpenAI support is unavailable. Install openai and "
                f"azure-identity ({AZURE_OPENAI_IMPORT_ERROR})."
            )
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default"
        )
        return AzureOpenAI(
            azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT'),
            azure_ad_token_provider=token_provider,
            api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
        )

    def perform(self, **kwargs):
        """Execute RAPP Pipeline operations."""
        action = kwargs.get('action')
        if not action:
            return json.dumps({"status": "error", "error": "Action is required"})

        try:
            # FAST-PATH: Transcript to agent in one step
            if action == 'transcript_to_agent':
                return self._transcript_to_agent(kwargs)

            # AUTO-PROCESS actions (recommended entry points)
            elif action == 'auto_process':
                return self._auto_process(kwargs)
            elif action == 'generate_report':
                return self._generate_report(kwargs)

            # Discovery actions
            elif action == 'prepare_discovery_call':
                return self._prepare_discovery_call(kwargs)
            elif action == 'process_transcript':
                return self._process_transcript(kwargs)
            elif action == 'generate_discovery_summary':
                return self._generate_discovery_summary(kwargs)

            # MVP actions
            elif action == 'generate_mvp_poke':
                return self._generate_mvp_poke(kwargs)
            elif action == 'prioritize_features':
                return self._prioritize_features(kwargs)
            elif action == 'define_scope':
                return self._define_scope(kwargs)
            elif action == 'estimate_timeline':
                return self._estimate_timeline(kwargs)
            elif action == 'generate_full_mvp_document':
                return self._generate_full_mvp_document(kwargs)

            # Code actions
            elif action == 'generate_agent_code':
                return self._generate_agent_code(kwargs)
            elif action == 'generate_agent_metadata':
                return self._generate_agent_metadata(kwargs)
            elif action == 'generate_agent_tests':
                return self._generate_agent_tests(kwargs)
            elif action == 'generate_deployment_config':
                return self._generate_deployment_config(kwargs)
            elif action == 'review_code':
                return self._review_code(kwargs)

            # Quality gate actions
            elif action == 'execute_quality_gate':
                return self._execute_quality_gate(kwargs)

            # Pipeline orchestration actions
            elif action == 'get_step_guidance':
                return self._get_step_guidance(kwargs)
            elif action == 'get_pipeline_status':
                return self._get_pipeline_status(kwargs)
            elif action == 'recommend_next_action':
                return self._recommend_next_action(kwargs)
            elif action == 'get_step_checklist':
                return self._get_step_checklist(kwargs)
            elif action == 'validate_step_completion':
                return self._validate_step_completion(kwargs)

            else:
                return json.dumps({"status": "error", "error": f"Unknown action: {action}"})

        except Exception as e:
            logger.error(f"Error in RAPP agent: {str(e)}", exc_info=True)
            return json.dumps({"status": "error", "error": str(e), "agent": self.name})

    # =========================================================================
    # DISCOVERY METHODS
    # =========================================================================

    def _prepare_discovery_call(self, kwargs):
        """Generate discovery call preparation guide and questions."""
        customer_name = kwargs.get('customer_name', 'Customer')
        industry = kwargs.get('industry', 'technology')
        existing_context = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""You are a discovery call facilitator for an AI agent development project.

CUSTOMER CONTEXT:
- Company: {customer_name}
- Industry: {industry}
{f"- Existing Notes: {json.dumps(existing_context)}" if existing_context else ""}

Generate a comprehensive discovery call preparation guide including:

1. RESEARCH CHECKLIST (before the call)
- Industry-specific pain points to investigate
- Common AI use cases in this industry
- Competitor analysis points

2. DISCOVERY QUESTIONS (prioritized)
- Opening rapport-building questions
- Problem identification questions
- Data source exploration questions
- Stakeholder mapping questions
- Success criteria questions
- Timeline and budget questions

3. RED FLAGS TO WATCH FOR
- Signs the project may not be a good fit
- Scope creep indicators
- Unrealistic expectations

4. IDEAL OUTCOMES
- What a successful discovery call produces
- Key artifacts to capture

Format as a structured guide that can be used during the call."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "prepare_discovery_call",
            "customer_name": customer_name,
            "industry": industry,
            "discovery_guide": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    def _process_transcript(self, kwargs):
        """Process discovery call transcript and extract structured data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        transcript = kwargs.get('transcript', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        if not transcript:
            return json.dumps({"status": "error", "error": "Transcript is required"})

        client = self._get_openai_client()
        prompt = f"""Analyze this discovery call transcript and extract structured data.

CUSTOMER: {customer_name}

TRANSCRIPT:
{transcript}

Extract the following in JSON format:

{{
  "callMetadata": {{
    "estimatedDuration": "estimated based on content",
    "participants": [{{"name": "", "role": "", "company": ""}}]
  }},
  "businessContext": {{
    "industry": "",
    "companySize": "small/medium/large/enterprise",
    "currentSystems": [],
    "technicalMaturity": "low/medium/high"
  }},
  "problemStatements": [
    {{
      "problem": "clear problem description",
      "verbatimQuote": "exact quote from customer if available",
      "category": "EFFICIENCY|ACCURACY|COST|COMPLIANCE|GROWTH",
      "severity": "LOW|MEDIUM|HIGH|CRITICAL",
      "currentProcess": "how they handle this today",
      "businessImpact": "quantified if possible"
    }}
  ],
  "dataSources": [
    {{
      "systemName": "",
      "dataType": "API|Database|File|Manual|SaaS",
      "accessLevel": "Full|Partial|Unknown|Blocked",
      "dataVolume": "estimated volume",
      "integrationComplexity": "LOW|MEDIUM|HIGH"
    }}
  ],
  "stakeholders": [
    {{
      "name": "",
      "role": "",
      "influenceLevel": "DECISION_MAKER|INFLUENCER|USER|TECHNICAL|BLOCKER",
      "concerns": [],
      "enthusiasm": "LOW|MEDIUM|HIGH"
    }}
  ],
  "successCriteria": [
    {{"metric": "", "currentValue": "", "targetValue": "", "measurementMethod": ""}}
  ],
  "timeline": {{
    "urgency": "LOW|MEDIUM|HIGH|CRITICAL",
    "targetLaunchDate": "",
    "budgetCycle": "",
    "keyMilestones": []
  }},
  "suggestedAgents": ["list of AI agent types that could address the problems"],
  "riskFactors": [{{"risk": "", "likelihood": "LOW|MEDIUM|HIGH", "mitigation": ""}}],
  "nextSteps": []
}}

Also provide:
1. A 3-paragraph executive summary
2. Recommended MVP scope
3. Confidence score (1-10) for data completeness"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        extracted_data = parse_llm_json_response(result, "raw_analysis")

        # Store discovery data if project_id provided
        stored = False
        if project_id:
            stored = self._store_discovery_data(project_id, extracted_data, user_guid)

        return json.dumps({
            "status": "success",
            "action": "process_transcript",
            "customer_name": customer_name,
            "extracted_data": extracted_data,
            "full_analysis": result,
            "stored_for_qg1": stored,
            "project_id": project_id,
            "processed_at": datetime.now().isoformat()
        })

    def _store_discovery_data(self, project_id: str, discovery_data: dict, user_guid: str = "default"):
        """Store discovery data to project storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            self.storage_manager.write_file(
                directory,
                f"discovery_{project_id}.json",
                json.dumps(discovery_data, indent=2)
            )
            return True
        except Exception as e:
            logger.warning(f"Could not store discovery data: {e}")
            return False

    def _generate_discovery_summary(self, kwargs):
        """Generate executive summary from discovery data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""Generate a concise executive summary for this AI agent project.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create:
1. ONE-PARAGRAPH EXECUTIVE SUMMARY (max 100 words)
2. THREE KEY TAKEAWAYS (bullet points)
3. RECOMMENDED NEXT STEP
4. RISK ASSESSMENT (one sentence)

Format for easy reading by executives."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_discovery_summary",
            "customer_name": customer_name,
            "executive_summary": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # MVP GENERATION METHODS
    # =========================================================================

    def _generate_mvp_poke(self, kwargs):
        """Generate a lightweight MVP Poke proposal."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        client = self._get_openai_client()
        prompt = f"""Generate a lightweight MVP "Poke" document for an AI agent project.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a concise MVP Poke with:
1. EXECUTIVE SUMMARY (2-3 sentences)
2. PROBLEM STATEMENT with Current State, Impact, Root Cause
3. PROPOSED SOLUTION with Agent Name and Core Capability
4. MVP FEATURES table (P0, P1, P2 priorities)
5. OUT OF SCOPE items (Phase 2)
6. DATA REQUIREMENTS table
7. SUCCESS METRICS table
8. TECHNICAL APPROACH (brief)
9. RISKS AND MITIGATIONS table
10. TIMELINE ESTIMATE
11. APPROVAL SECTION

Format as clean Markdown suitable for customer presentation.

Return JSON:
{{
  "status": "success",
  "document": "full markdown document",
  "features": {{"p0": [], "p1": [], "p2": []}},
  "outOfScope": [],
  "successMetrics": [{{"metric": "", "current": "", "target": ""}}],
  "estimatedDays": 0
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        parsed = parse_llm_json_response(result, "document")
        parsed["customer_name"] = customer_name
        parsed["project_name"] = project_name
        parsed["generated_at"] = datetime.now().isoformat()
        parsed["status"] = "success"
        parsed["action"] = "generate_mvp_poke"

        if project_id:
            self._update_project_with_mvp(project_id, parsed, user_guid)
            parsed["project_updated"] = True

        return json.dumps(parsed)

    def _update_project_with_mvp(self, project_id: str, mvp_data: dict, user_guid: str = "default"):
        """Update project with MVP document."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["mvp_document"] = mvp_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with MVP: {e}")
            return False

    def _prioritize_features(self, kwargs):
        """Prioritize features using P0/P1/P2 method."""
        discovery_data = kwargs.get('discovery_data', {})
        features = kwargs.get('features', [])
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Prioritize AI agent features for MVP development.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

SUGGESTED FEATURES: {json.dumps(features) if features else 'Derive from discovery'}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Prioritize using P0/P1/P2 framework:
- P0: MUST have for MVP (blocks launch if missing)
- P1: SHOULD have (significant value, low risk)
- P2: COULD have (nice-to-have, defer if needed)
- DEFERRED: Phase 2 or later

Return JSON:
{{
  "features": [
    {{"name": "", "description": "", "priority": "P0|P1|P2|DEFERRED", "effort": "S|M|L", "businessValue": 0, "technicalRisk": "LOW|MEDIUM|HIGH", "rationale": ""}}
  ],
  "mvpCoreFeatures": [],
  "deferredFeatures": [],
  "totalEffort": "S|M|L|XL"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_analysis")
        parsed["status"] = "success"
        parsed["action"] = "prioritize_features"
        parsed["analyzed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _define_scope(self, kwargs):
        """Define clear scope boundaries for MVP."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Define clear scope boundaries for this AI agent MVP.

CUSTOMER: {customer_name}
PROBLEM: {problem_statement}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create explicit scope definition with:
1. IN SCOPE (What we WILL build)
2. OUT OF SCOPE (What we WON'T build in MVP)
3. ASSUMPTIONS
4. DEPENDENCIES
5. CONSTRAINTS
6. SCOPE CREEP INDICATORS

Return JSON:
{{
  "scope": {{
    "inScope": [{{"item": "", "description": "", "priority": "P0|P1|P2"}}],
    "outOfScope": [{{"item": "", "reason": "", "phase": "2|3|future"}}],
    "assumptions": [{{"category": "TECHNICAL|BUSINESS|DATA", "assumption": ""}}],
    "dependencies": [{{"type": "SYSTEM|STAKEHOLDER|DATA", "dependency": "", "risk": "LOW|MEDIUM|HIGH"}}],
    "constraints": [],
    "scopeCreepIndicators": []
  }},
  "scopeStatement": "One paragraph scope statement"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_scope")
        parsed["status"] = "success"
        parsed["action"] = "define_scope"
        parsed["customer_name"] = customer_name
        parsed["defined_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _estimate_timeline(self, kwargs):
        """Estimate MVP development timeline."""
        discovery_data = kwargs.get('discovery_data', {})
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Estimate MVP development timeline for this AI agent project.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Provide realistic timeline with phases, milestones, and risk buffers.

Return JSON:
{{
  "timeline": {{
    "phases": [{{"name": "", "estimatedDays": 0, "dependencies": [], "deliverables": []}}],
    "totalDays": 0,
    "milestones": [{{"name": "", "targetDay": 0, "description": ""}}],
    "criticalPath": [],
    "riskBuffer": {{"days": 0, "reason": ""}}
  }},
  "confidenceLevel": "LOW|MEDIUM|HIGH"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_estimate")
        parsed["status"] = "success"
        parsed["action"] = "estimate_timeline"
        parsed["estimated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _generate_full_mvp_document(self, kwargs):
        """Generate a complete MVP Poke document ready for customer presentation."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent MVP')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Generate a complete, professional MVP Poke document.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a comprehensive document in clean Markdown with:
- Executive Summary
- Problem Statement (Current State, Impact, Root Cause)
- Proposed Solution (Agent Name, Core Capability, How It Works)
- MVP Features (P0/P1/P2 priority table)
- Out of Scope (Phase 2+)
- Data Requirements table
- Integration Points
- Success Metrics table
- Technical Approach
- Assumptions & Dependencies
- Risks & Mitigations table
- Timeline
- Investment & ROI
- Approval section with signature lines

End with scope lock notice."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_full_mvp_document",
            "customer_name": customer_name,
            "project_name": project_name,
            "document": response.choices[0].message.content,
            "format": "markdown",
            "ready_for_customer": True,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # CODE GENERATION METHODS
    # =========================================================================

    def _generate_agent_code(self, kwargs):
        """Generate complete Python agent code."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])
        data_sources = kwargs.get('data_sources', [])
        customer_name = kwargs.get('customer_name', 'Customer')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Create class name
        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATIONS:
- Agent Name: {agent_name}
- Class Name: {class_name}
- Description: {agent_description}
- Features: {json.dumps(features)}
- Data Sources: {json.dumps(data_sources)}
- Customer: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern exactly
2. Include complete JSON Schema metadata for all parameters
3. The perform() method must return JSON string (never dict or exception)
4. Wrap all external calls in try/except
5. Use logging, not print statements
6. No hardcoded credentials - use os.environ
7. Include usage example in __main__
8. Include comprehensive docstrings
9. Handle all edge cases gracefully

Generate the complete Python code."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()

        result = {
            "status": "success",
            "action": "generate_agent_code",
            "agent_name": agent_name,
            "class_name": class_name,
            "file_name": f"{snake_name}.py",
            "code": code,
            "features_implemented": features,
            "generated_at": datetime.now().isoformat()
        }

        if project_id:
            self._update_project_with_code(project_id, result, user_guid)
            result["project_updated"] = True

        return json.dumps(result)

    def _update_project_with_code(self, project_id: str, code_data: dict, user_guid: str = "default"):
        """Update project with generated code."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["generated_code"] = code_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with code: {e}")
            return False

    def _generate_agent_metadata(self, kwargs):
        """Generate metadata schema for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])

        client = self._get_openai_client()
        prompt = f"""Generate a complete JSON Schema metadata definition for an AI agent.

AGENT: {agent_name}
DESCRIPTION: {agent_description}
FEATURES: {json.dumps(features)}

Create a complete metadata object with name, description, and parameters schema.

Return valid JSON:
{{
  "name": "{agent_name}",
  "description": "...",
  "parameters": {{"type": "object", "properties": {{}}, "required": []}}
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_metadata")
        return json.dumps({
            "status": "success",
            "action": "generate_agent_metadata",
            "agent_name": agent_name,
            "metadata": parsed,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_agent_tests(self, kwargs):
        """Generate unit test stubs for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        existing_code = kwargs.get('existing_code', '')
        features = kwargs.get('features', [])

        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate comprehensive pytest unit tests for this agent.

AGENT: {agent_name}
CLASS: {class_name}
FEATURES: {json.dumps(features)}
{f'CODE:{chr(10)}{existing_code}' if existing_code else ''}

Generate pytest-style tests covering initialization, metadata validation, perform() with valid/invalid inputs, error handling, and edge cases. Use mocking appropriately."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        test_code = response.choices[0].message.content
        if '```python' in test_code:
            code_start = test_code.find('```python') + 9
            code_end = test_code.rfind('```')
            if code_end > code_start:
                test_code = test_code[code_start:code_end].strip()

        return json.dumps({
            "status": "success",
            "action": "generate_agent_tests",
            "agent_name": agent_name,
            "test_file_name": f"test_{snake_name}.py",
            "test_code": test_code,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_deployment_config(self, kwargs):
        """Generate deployment configuration."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        customer_name = kwargs.get('customer_name', 'Customer')
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')

        deployment_config = {
            "agent_name": agent_name,
            "file_name": f"{snake_name}_agent.py",
            "deployment_steps": [
                {"step": 1, "action": "Upload agent to Azure File Storage", "command": f"az storage file upload --share-name agents --source {snake_name}_agent.py"},
                {"step": 2, "action": "Verify agent loads", "command": "func start --verbose"},
                {"step": 3, "action": "Test agent endpoint", "command": f'curl -X POST http://localhost:7071/api/businessinsightbot_function -H "Content-Type: application/json" -d \'{{"user_input": "test {agent_name}"}}\''},
                {"step": 4, "action": "Deploy to Azure", "command": "func azure functionapp publish <FUNCTION_APP_NAME> --build remote"}
            ],
            "environment_variables": ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"],
            "azure_file_storage_path": f"agents/{snake_name}_agent.py"
        }

        return json.dumps({
            "status": "success",
            "action": "generate_deployment_config",
            "agent_name": agent_name,
            "customer_name": customer_name,
            "deployment_config": deployment_config,
            "generated_at": datetime.now().isoformat()
        })

    def _review_code(self, kwargs):
        """Review existing code for issues."""
        existing_code = kwargs.get('existing_code', '')
        agent_name = kwargs.get('agent_name', 'Agent')

        if not existing_code:
            return json.dumps({"status": "error", "error": "No code provided for review"})

        client = self._get_openai_client()
        prompt = f"""Review this Python agent code for quality and security.

AGENT: {agent_name}
CODE:
```python
{existing_code}
```

Review for:
1. PATTERN VALIDATION - BasicAgent pattern, metadata schema, perform() returns JSON
2. SECURITY AUDIT - No hardcoded creds, input validation, injection vulnerabilities
3. LOGIC CORRECTNESS - Error handling, edge cases
4. CODE QUALITY - Naming, logging, complexity

Return JSON:
{{
  "overallScore": 0,
  "passesReview": true|false,
  "categories": {{
    "patternValidation": {{"score": 0, "passed": true|false, "issues": []}},
    "securityAudit": {{"score": 0, "passed": true|false, "issues": []}},
    "logicCorrectness": {{"score": 0, "passed": true|false, "issues": []}},
    "codeQuality": {{"score": 0, "passed": true|false, "issues": []}}
  }},
  "criticalIssues": [],
  "fixes": [{{"location": "", "issue": "", "fix": ""}}]
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_review")
        parsed["status"] = "success"
        parsed["action"] = "review_code"
        parsed["agent_name"] = agent_name
        parsed["reviewed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # QUALITY GATE METHODS
    # =========================================================================

    def _execute_quality_gate(self, kwargs):
        """Execute a quality gate validation."""
        gate = kwargs.get('gate')
        if not gate:
            return json.dumps({"status": "error", "error": "Gate identifier (QG1-QG6) is required"})
        if gate not in self.GATE_CONFIGS:
            return json.dumps({"status": "error", "error": f"Invalid gate: {gate}. Use QG1-QG6."})

        input_data = kwargs.get('input_data') or kwargs.get('discovery_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Retrieve discovery data from storage if needed
        if not input_data and project_id:
            input_data = self._get_discovery_data_from_storage(project_id, user_guid)

        client = self._get_openai_client()

        if gate == "QG1":
            result = self._execute_qg1(client, input_data, customer_name)
        elif gate == "QG2":
            result = self._execute_qg2(client, input_data, customer_name, project_name)
        elif gate == "QG3":
            result = self._execute_qg3(client, input_data, customer_name, project_name)
        elif gate == "QG4":
            result = self._execute_qg4(client, input_data, customer_name, project_name)
        elif gate == "QG5":
            result = self._execute_qg5(client, input_data, customer_name, project_name)
        elif gate == "QG6":
            result = self._execute_qg6(client, input_data, customer_name, project_name)

        # Store result in project
        if project_id:
            try:
                parsed_result = json.loads(result)
                self._update_project_with_qg_result(project_id, gate, parsed_result, user_guid)
            except json.JSONDecodeError:
                pass

        return result

    def _get_discovery_data_from_storage(self, project_id: str, user_guid: str) -> dict:
        """Retrieve discovery data from storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            content = self.storage_manager.read_file(directory, f"discovery_{project_id}.json")
            if content:
                return json.loads(content)
            return {}
        except Exception:
            return {}

    def _update_project_with_qg_result(self, project_id: str, gate: str, qg_result: dict, user_guid: str):
        """Update project with quality gate result."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            content = self.storage_manager.read_file(directory, project_file)
            if content:
                project = json.loads(content)
                if "qg_results" not in project:
                    project["qg_results"] = {}
                project["qg_results"][gate] = qg_result
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
        except Exception as e:
            logger.warning(f"Could not update project with QG result: {e}")

    def _execute_qg1(self, client, input_data, customer_name):
        """QG1: Transcript/Discovery Validation."""
        prompt = f"""You are Quality Gate #1 (QG1) - Transcript Validation.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(input_data, indent=2)}

Score each criterion 1-10:
1. PROBLEM CLARITY: Is the problem specific, measurable, with quantified pain points?
2. DATA AVAILABILITY: Are data sources identified with feasible access?
3. STAKEHOLDER ALIGNMENT: Clear decision-maker? Agreement on problem?
4. SUCCESS CRITERIA: Metrics defined with realistic targets?
5. SCOPE BOUNDARIES: MVP scope appropriate? Clear exclusions?

DECISION: Average >= 8: PASS, 6-7: CLARIFY, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, overallScore, scores, validatedProblemStatement, strengths, concerns, clarifyingQuestions, recommendations, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG1")

    def _execute_qg2(self, client, input_data, customer_name, project_name):
        """QG2: Customer Validation (Scope Lock)."""
        prompt = f"""You are Quality Gate #2 (QG2) - Customer Validation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
MVP PROPOSAL & FEEDBACK:
{json.dumps(input_data, indent=2)}

Validate: SCOPE AGREEMENT, DATA ACCESS, STAKEHOLDER BUY-IN, TIMELINE ACCEPTANCE
DECISION: All confirmed: PROCEED (SCOPE LOCKED), Minor issues: REVISE, Major: HOLD

Return ONLY valid JSON with gate, gateName, decision, scopeLocked, scores, lockedFeatures, deferredToPhase2, concerns, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG2")

    def _execute_qg3(self, client, input_data, customer_name, project_name):
        """QG3: Code Quality Review."""
        prompt = f"""You are Quality Gate #3 (QG3) - Code Quality Review.

CUSTOMER: {customer_name}
PROJECT: {project_name}
CODE & SPECIFICATION:
{json.dumps(input_data, indent=2)}

Review: PATTERN VALIDATION, SECURITY AUDIT, LOGIC CORRECTNESS, INTEGRATION COMPATIBILITY, CODE QUALITY
DECISION: All pass: PASS, Fixable: FIX_REQUIRED, Major problems: FAIL

Return ONLY valid JSON with gate, gateName, decision, securityScore, scores, criticalIssues, fixes, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG3")

    def _execute_qg4(self, client, input_data, customer_name, project_name):
        """QG4: Demo Review (Waiter Pattern)."""
        prompt = f"""You are Quality Gate #4 (QG4) - Demo Review using "Waiter Pattern".

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Waiter Pattern: "Would you confidently serve this to the customer?"
Score 1-10: RESPONSE QUALITY, CONVERSATION FLOW, VISUAL PRESENTATION, BUSINESS VALUE, EDGE CASES
DECISION: Average >= 8: PASS, 6-7: POLISH, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, waiterScore, scores, strengths, polishItems, blockers, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG4")

    def _execute_qg5(self, client, input_data, customer_name, project_name):
        """QG5: Final Demo Review (Executive Readiness)."""
        prompt = f"""You are Quality Gate #5 (QG5) - Final Demo Review for Executive Presentation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Score 1-10: OPENING HOOK, PROBLEM ILLUSTRATION, SOLUTION WOW, METRICS CLARITY, INDUSTRY ACCURACY, CLOSING STRENGTH, TECHNICAL POLISH, MVP ALIGNMENT
DECISION: >= 8.5: APPROVE, 7-8.4: MINOR_REVISIONS, 5-6.9: MAJOR_REVISIONS, < 5: REJECT

Return ONLY valid JSON with gate, gateName, decision, executiveReadinessScore, scores, feedback, strengths, approvalReady, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG5")

    def _execute_qg6(self, client, input_data, customer_name, project_name):
        """QG6: Post-Deployment Audit."""
        prompt = f"""You are Quality Gate #6 (QG6) - Post-Deployment Audit.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEPLOYMENT METRICS:
{json.dumps(input_data, indent=2)}

Score: SYSTEM HEALTH (25%), USAGE ADOPTION (25%), BUSINESS VALUE (30%), CUSTOMER SATISFACTION (20%)
STATUS: GREEN (all meeting targets), YELLOW (some below but trending up), RED (critical failing)

Return ONLY valid JSON with gate, gateName, decision, auditDate, scores, roiValidation, recommendations, optimizations, nextAuditDate."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG6")

    def _parse_gate_response(self, response_text, gate):
        """Parse and validate gate response."""
        parsed = parse_llm_json_response(response_text, "raw_response")
        parsed["status"] = "success"
        parsed["gate"] = gate
        parsed["evaluatedAt"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # PIPELINE ORCHESTRATION METHODS
    # =========================================================================

    def _get_step_guidance(self, kwargs):
        """Get detailed guidance for a specific pipeline step."""
        step = kwargs.get('step', 1)
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}. Use 1-14."})

        step_info = self.PIPELINE_STEPS[step]
        client = self._get_openai_client()

        prompt = f"""Provide detailed guidance for RAPP Pipeline Step {step}: {step_info['name']}

CUSTOMER: {customer_name}
PROJECT: {project_name}
STEP TYPE: {step_info['type']}

CURRENT PROJECT DATA:
{json.dumps(project_data, indent=2) if project_data else 'No data yet'}

Provide:
1. STEP OVERVIEW - Purpose and objectives
2. INPUTS REQUIRED - What you need before starting
3. KEY ACTIVITIES - Specific tasks and best practices
4. OUTPUTS EXPECTED - Deliverables and quality criteria
5. COMMON PITFALLS - What to avoid
6. RAPP AGENT ACTIONS - Which action to use (e.g., process_transcript, execute_quality_gate with gate=QG1)
7. SUCCESS CRITERIA - How to know you're done"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "get_step_guidance",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "guidance": response.choices[0].message.content,
            "related_gate": step_info.get('gate'),
            "generated_at": datetime.now().isoformat()
        })

    def _get_pipeline_status(self, kwargs):
        """Get overall pipeline status for a project."""
        project_data = kwargs.get('project_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')

        completed_steps = project_data.get('completed_steps', [])
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        progress_percent = len(completed_steps) / 14 * 100

        # Build step status
        step_status = []
        for step_id, step_info in self.PIPELINE_STEPS.items():
            status = "completed" if step_id in completed_steps else "pending"
            if step_id == current_step:
                status = "in_progress"
            if str(step_id) in step_decisions:
                status = f"{status} ({step_decisions[str(step_id)]})"
            step_status.append({
                "step": step_id,
                "name": step_info['name'],
                "type": step_info['type'],
                "status": status
            })

        return json.dumps({
            "status": "success",
            "action": "get_pipeline_status",
            "customer_name": customer_name,
            "project_name": project_name,
            "progress_percent": round(progress_percent, 1),
            "current_step": current_step,
            "current_step_name": self.PIPELINE_STEPS[current_step]['name'],
            "completed_count": len(completed_steps),
            "total_steps": 14,
            "step_status": step_status,
            "generated_at": datetime.now().isoformat()
        })

    def _recommend_next_action(self, kwargs):
        """Recommend the next action based on current state."""
        project_data = kwargs.get('project_data', {})
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        step_info = self.PIPELINE_STEPS[current_step]
        client = self._get_openai_client()

        prompt = f"""Based on current RAPP Pipeline state, recommend the best next action.

CURRENT STEP: {current_step} - {step_info['name']} ({step_info['type']})
STEP DECISIONS: {json.dumps(step_decisions, indent=2)}

Provide:
1. IMMEDIATE NEXT ACTION - What to do now
2. RAPP AGENT ACTION - The exact action to call (e.g., process_transcript, execute_quality_gate)
3. REQUIRED INPUTS - What parameters are needed
4. BLOCKERS - Any issues to resolve first

Return JSON:
{{
  "recommended_action": "description",
  "rapp_action": "action name from RAPP agent",
  "required_parameters": {{}},
  "blockers": [],
  "priority": "HIGH|MEDIUM|LOW",
  "rationale": "why this is recommended"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_recommendation")
        parsed["status"] = "success"
        parsed["action"] = "recommend_next_action"
        parsed["current_step"] = current_step
        parsed["current_step_name"] = step_info['name']
        parsed["generated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _get_step_checklist(self, kwargs):
        """Get the completion checklist for a step."""
        step = kwargs.get('step', 1)

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]

        checklists = {
            1: ["Scheduled discovery call", "Prepared questions", "Recorded call", "Captured problem statements", "Identified data sources", "Mapped stakeholders", "Documented success criteria"],
            2: ["Reviewed transcript clarity", "Verified data access", "Confirmed stakeholder alignment", "Validated measurable criteria", "Assessed MVP scope", "Made PASS/FAIL/CLARIFY decision"],
            3: ["Created executive summary", "Defined MVP features (P0/P1/P2)", "Listed out-of-scope items", "Documented data requirements", "Set success metrics", "Added approval section"],
            4: ["Presented MVP to customer", "Received feature approval", "Confirmed out-of-scope accepted", "Got decision-maker sign-off", "LOCKED scope"],
            5: ["Generated BasicAgent code", "Defined metadata schema", "Implemented perform() method", "Added input validation", "Integrated Azure OpenAI", "Added error handling", "No hardcoded credentials"],
            6: ["Validated pattern compliance", "Completed security audit", "Verified logic matches MVP", "Checked Azure integration", "Made PASS/FIX/FAIL decision"],
            7: ["Validated Azure infrastructure", "Deployed Function App", "Uploaded agent code", "Configured environment", "Tested endpoint"],
            8: ["Tested all MVP features", "Verified response quality", "Checked conversation flow", "Applied waiter pattern", "Made PASS/POLISH/FAIL decision"],
            9: ["Created narrative arc", "Wrote narration script", "Designed demo steps", "Included metrics", "Generated demo JSON"],
            10: ["Reviewed opening hook", "Validated problem illustration", "Confirmed wow moment", "Checked metrics", "Made APPROVE/REVISE/REJECT decision"],
            11: ["Collected feedback", "Classified items (bug/polish/feature/creep)", "Deferred scope creep", "Created iteration plan"],
            12: ["Completed security hardening", "Deployed production infra", "Configured Key Vault", "Set up monitoring", "Created documentation"],
            13: ["Collected health metrics", "Analyzed usage patterns", "Measured business value", "Gathered customer feedback", "Generated audit report"],
            14: ["Reviewed audit results", "Prioritized optimization backlog", "Identified scaling opportunities", "Documented lessons learned"]
        }

        return json.dumps({
            "status": "success",
            "action": "get_step_checklist",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "checklist": checklists.get(step, []),
            "generated_at": datetime.now().isoformat()
        })

    def _validate_step_completion(self, kwargs):
        """Validate if a step is ready for completion."""
        step = kwargs.get('step', 1)
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]
        step_checklists = project_data.get('step_checklists', {})
        step_decisions = project_data.get('step_decisions', {})

        checklist_data = step_checklists.get(str(step), {})
        checklist_complete = all(checklist_data.values()) if checklist_data else False

        gate_decision = step_decisions.get(str(step))
        gate_passed = gate_decision in ['PASS', 'PROCEED', 'APPROVE', 'GREEN'] if gate_decision else None

        if step_info['type'] == 'audit':
            is_valid = checklist_complete and gate_decision is not None
            can_proceed = gate_passed
        else:
            is_valid = checklist_complete
            can_proceed = is_valid

        return json.dumps({
            "status": "success",
            "action": "validate_step_completion",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "validation": {
                "checklist_complete": checklist_complete,
                "gate_decision": gate_decision,
                "gate_passed": gate_passed,
                "is_valid": is_valid,
                "can_proceed": can_proceed
            },
            "next_step": step + 1 if can_proceed and step < 14 else None,
            "message": f"Step {step} {'ready to proceed' if can_proceed else 'not yet complete'}",
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # AUTO-PROCESS AND REPORT GENERATION METHODS
    # =========================================================================

    def _auto_process(self, kwargs):
        """
        Automatically process a project based on available inputs.

        Scans the project folder for input files, determines the appropriate
        pipeline step, processes the inputs, and generates professional PDF reports.

        Folder structure expected:
            rapp_projects/{project_id}/
                inputs/
                    discovery_transcript.txt
                    customer_feedback.txt
                    code_to_review.py
                    etc.
                outputs/
                    (reports generated here)
                project_state.json
        """
        project_id = kwargs.get('project_id')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        user_guid = kwargs.get('user_guid', 'default')

        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required for auto_process"})

        try:
            # Scan inputs
            inputs = self._scan_project_inputs(project_id, user_guid)
            if not inputs['files']:
                return json.dumps({
                    "status": "error",
                    "error": "No input files found",
                    "expected_location": f"rapp_projects/{project_id}/inputs/",
                    "supported_files": list(self.INPUT_PATTERNS.keys())
                })

            # Load or create project state
            project_state = self._load_project_state(project_id, user_guid)
            project_state['customer_name'] = customer_name
            project_state['project_name'] = project_name

            # Determine what to process based on inputs and current state
            actions_taken = []
            reports_generated = []

            # Process discovery transcript if present
            if inputs.get('discovery_transcript'):
                logger.info(f"Processing discovery transcript for project {project_id}")
                transcript_content = inputs['discovery_transcript']['content']

                # Process transcript
                result = json.loads(self._process_transcript({
                    'customer_name': customer_name,
                    'transcript': transcript_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if result.get('status') == 'success':
                    actions_taken.append("Processed discovery transcript")
                    project_state['discovery_data'] = result.get('extracted_data', {})
                    project_state['current_step'] = 2

                    # Generate discovery report
                    report_path = self._generate_and_save_report(
                        "discovery", result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "discovery", "path": report_path})

                    # Execute QG1
                    qg1_result = json.loads(self._execute_quality_gate({
                        'gate': 'QG1',
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'input_data': result.get('extracted_data', {}),
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if qg1_result.get('status') == 'success':
                        actions_taken.append(f"Executed QG1: {qg1_result.get('decision', 'N/A')}")
                        project_state['qg1_result'] = qg1_result
                        if qg1_result.get('decision') == 'PASS':
                            project_state['completed_steps'] = project_state.get('completed_steps', []) + [1, 2]
                            project_state['current_step'] = 3

                        # Generate QG1 report
                        report_path = self._generate_and_save_report(
                            "qg1", qg1_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "qg1", "path": report_path})

            # Process customer feedback for QG2 if present
            if inputs.get('customer_feedback') and project_state.get('current_step', 1) >= 3:
                logger.info(f"Processing customer feedback for project {project_id}")
                feedback_content = inputs['customer_feedback']['content']

                # First generate MVP if not done
                if not project_state.get('mvp_document'):
                    mvp_result = json.loads(self._generate_full_mvp_document({
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'discovery_data': project_state.get('discovery_data', {}),
                        'problem_statement': project_state.get('discovery_data', {}).get('problemStatements', [{}])[0].get('problem', '')
                    }))

                    if mvp_result.get('status') == 'success':
                        actions_taken.append("Generated MVP document")
                        project_state['mvp_document'] = mvp_result

                        report_path = self._generate_and_save_report(
                            "mvp", mvp_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "mvp", "path": report_path})

                # Execute QG2 with customer feedback
                qg2_input = {
                    'mvp_document': project_state.get('mvp_document', {}),
                    'customer_feedback': feedback_content
                }
                qg2_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG2',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': qg2_input,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg2_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG2: {qg2_result.get('decision', 'N/A')}")
                    project_state['qg2_result'] = qg2_result
                    if qg2_result.get('decision') == 'PROCEED':
                        project_state['scope_locked'] = True
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [3, 4]))
                        project_state['current_step'] = 5

                    report_path = self._generate_and_save_report(
                        "qg2", qg2_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg2", "path": report_path})

            # Process code for review if present
            if inputs.get('code_to_review') and project_state.get('current_step', 1) >= 5:
                logger.info(f"Processing code review for project {project_id}")
                code_content = inputs['code_to_review']['content']

                # First generate agent code if not done
                if not project_state.get('generated_code'):
                    discovery_data = project_state.get('discovery_data', {})
                    suggested_agents = discovery_data.get('suggestedAgents', ['CustomAgent'])
                    agent_name = suggested_agents[0] if suggested_agents else 'CustomAgent'

                    code_result = json.loads(self._generate_agent_code({
                        'agent_name': agent_name,
                        'agent_description': project_state.get('mvp_document', {}).get('document', '')[:500],
                        'features': [p.get('problem', '') for p in discovery_data.get('problemStatements', [])],
                        'customer_name': customer_name,
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if code_result.get('status') == 'success':
                        actions_taken.append("Generated agent code")
                        project_state['generated_code'] = code_result

                        report_path = self._generate_and_save_report(
                            "code", code_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "code", "path": report_path})

                # Execute QG3 code review
                qg3_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG3',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': {
                        'code': code_content,
                        'features': project_state.get('mvp_document', {}).get('features', {})
                    },
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg3_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG3: {qg3_result.get('decision', 'N/A')}")
                    project_state['qg3_result'] = qg3_result
                    if qg3_result.get('decision') == 'PASS':
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [5, 6]))
                        project_state['current_step'] = 7

                    report_path = self._generate_and_save_report(
                        "qg3", qg3_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg3", "path": report_path})

            # Process deployment metrics for QG6 if present
            if inputs.get('deployment_metrics') and project_state.get('current_step', 1) >= 12:
                logger.info(f"Processing deployment metrics for project {project_id}")
                try:
                    metrics_content = json.loads(inputs['deployment_metrics']['content'])
                except json.JSONDecodeError:
                    metrics_content = {"raw_metrics": inputs['deployment_metrics']['content']}

                qg6_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG6',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': metrics_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg6_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG6: {qg6_result.get('decision', 'N/A')}")
                    project_state['qg6_result'] = qg6_result
                    project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [13]))
                    project_state['current_step'] = 14

                    report_path = self._generate_and_save_report(
                        "qg6", qg6_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg6", "path": report_path})

            # Generate executive summary report
            exec_summary = self._generate_executive_summary_data(project_state, customer_name, project_name)
            report_path = self._generate_and_save_report(
                "executive_summary", exec_summary, customer_name, project_name, project_id, user_guid
            )
            if report_path:
                reports_generated.append({"type": "executive_summary", "path": report_path})

            # Save project state
            self._save_project_state(project_id, project_state, user_guid)

            return json.dumps({
                "status": "success",
                "action": "auto_process",
                "project_id": project_id,
                "customer_name": customer_name,
                "project_name": project_name,
                "inputs_detected": list(inputs['files'].keys()),
                "actions_taken": actions_taken,
                "reports_generated": reports_generated,
                "current_step": project_state.get('current_step', 1),
                "completed_steps": project_state.get('completed_steps', []),
                "progress_percent": len(project_state.get('completed_steps', [])) / 14 * 100,
                "processed_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error in auto_process: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "project_id": project_id
            })

    def _scan_project_inputs(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Scan project inputs folder for files."""
        inputs = {'files': {}}
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return inputs

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Determine file type
                file_type = None
                for input_type, patterns in self.INPUT_PATTERNS.items():
                    for pattern in patterns:
                        if pattern in filename_lower:
                            file_type = input_type
                            break
                    if file_type:
                        break

                if file_type:
                    content = self.storage_manager.read_file(input_directory, filename)
                    if content:
                        inputs['files'][filename] = {
                            'type': file_type,
                            'size': len(content)
                        }
                        inputs[file_type] = {
                            'filename': filename,
                            'content': content
                        }

        except Exception as e:
            logger.warning(f"Error scanning inputs for project {project_id}: {e}")

        return inputs

    def _load_project_state(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Load or create project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"

        try:
            content = self.storage_manager.read_file(state_directory, state_file)
            if content:
                return json.loads(content)
        except Exception:
            pass

        return {
            'project_id': project_id,
            'current_step': 1,
            'completed_steps': [],
            'created_at': datetime.now().isoformat()
        }

    def _save_project_state(self, project_id: str, state: Dict[str, Any], user_guid: str):
        """Save project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"
        state['updated_at'] = datetime.now().isoformat()

        try:
            self.storage_manager.write_file(state_directory, state_file, json.dumps(state, indent=2))
        except Exception as e:
            logger.warning(f"Could not save project state: {e}")

    def _generate_and_save_report(
        self,
        report_type: str,
        data: Dict[str, Any],
        customer_name: str,
        project_name: str,
        project_id: str,
        user_guid: str
    ) -> Optional[str]:
        """Generate a PDF report and save it to the outputs folder."""
        if not REPORT_GENERATOR_AVAILABLE:
            logger.warning("Report generator not available. Install reportlab.")
            return None

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{report_type}_report_{timestamp}.pdf"
            output_directory = f"rapp_projects/{project_id}/outputs"

            # Save to storage
            self.storage_manager.write_file(output_directory, filename, pdf_bytes)
            logger.info(f"Generated report: {output_directory}/{filename}")

            return f"{output_directory}/{filename}"

        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return None

    def _generate_executive_summary_data(
        self,
        project_state: Dict[str, Any],
        customer_name: str,
        project_name: str
    ) -> Dict[str, Any]:
        """Generate data for executive summary report."""
        completed_steps = project_state.get('completed_steps', [])
        current_step = project_state.get('current_step', 1)

        qg_decisions = []
        for gate in ['qg1', 'qg2', 'qg3', 'qg4', 'qg5', 'qg6']:
            result = project_state.get(f'{gate}_result', {})
            if result.get('decision'):
                qg_decisions.append(f"{gate.upper()}: {result['decision']}")

        return {
            'summary': f"RAPP Pipeline progress for {project_name} ({customer_name}). "
                      f"Currently at Step {current_step} ({self.PIPELINE_STEPS[current_step]['name']}). "
                      f"Completed {len(completed_steps)} of 14 steps.",
            'metrics': {
                'progress_percent': round(len(completed_steps) / 14 * 100, 1),
                'completed_steps': len(completed_steps),
                'current_step': current_step
            },
            'progress_percent': round(len(completed_steps) / 14 * 100, 1),
            'current_step': current_step,
            'current_step_name': self.PIPELINE_STEPS[current_step]['name'],
            'quality_gate_decisions': qg_decisions,
            'scope_locked': project_state.get('scope_locked', False),
            'discovery_data': project_state.get('discovery_data', {}),
            'generated_at': datetime.now().isoformat()
        }

    def _generate_report(self, kwargs):
        """Generate a professional PDF report for a specific report type."""
        report_type = kwargs.get('report_type')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')
        data = kwargs.get('input_data') or kwargs.get('data', {})

        if not report_type:
            return json.dumps({"status": "error", "error": "report_type is required"})

        if not REPORT_GENERATOR_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": "Report generator not available. Install reportlab: pip install reportlab"
            })

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Save if project_id provided
            output_path = None
            if project_id:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{report_type}_report_{timestamp}.pdf"
                output_directory = f"rapp_projects/{project_id}/outputs"
                self.storage_manager.write_file(output_directory, filename, pdf_bytes)
                output_path = f"{output_directory}/{filename}"

            return json.dumps({
                "status": "success",
                "action": "generate_report",
                "report_type": report_type,
                "customer_name": customer_name,
                "project_name": project_name,
                "output_path": output_path,
                "pdf_size_bytes": len(pdf_bytes),
                "generated_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error generating report: {e}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e)
            })

    # =========================================================================
    # TRANSCRIPT TO AGENT - FAST PATH FOR QUICK ITERATION
    # =========================================================================

    def _transcript_to_agent(self, kwargs):
        """
        FASTEST PATH: Transcript → Deployable Agent + Demo in one step.

        This method:
        1. Reads transcript from Azure storage or inline
        2. Analyzes transcript to extract agent requirements
        3. Generates complete agent Python code (BasicAgent pattern)
        4. Generates demo JSON for ScriptedDemoAgent
        5. Auto-deploys both to agents/ and demos/ folders

        User workflow:
        1. Drop transcript in rapp_projects/{project_id}/inputs/ OR pass inline
        2. Call this action
        3. Agent and demo are ready to use immediately

        Args:
            project_id: Project ID (reads transcript from rapp_projects/{project_id}/inputs/)
            transcript: Inline transcript text (alternative to project_id)
            customer_name: Customer/company name
            agent_priority: Which agent to prioritize (e.g., 'contract', 'chargeback')
            deploy_to_storage: If True, auto-deploy to agents/ and demos/ folders
            user_guid: User GUID for storage access
        """
        project_id = kwargs.get('project_id')
        transcript = kwargs.get('transcript', '')
        customer_name = kwargs.get('customer_name', 'Customer')
        agent_priority = kwargs.get('agent_priority', '')
        deploy_to_storage = kwargs.get('deploy_to_storage', True)
        user_guid = kwargs.get('user_guid', 'default')

        try:
            # Step 1: Get transcript content
            if not transcript and project_id:
                transcript = self._get_transcript_from_storage(project_id, user_guid)

            if not transcript:
                return json.dumps({
                    "status": "error",
                    "error": "No transcript provided. Either pass 'transcript' parameter or ensure transcript file exists in rapp_projects/{project_id}/inputs/",
                    "expected_patterns": self.INPUT_PATTERNS.get('discovery_transcript', [])
                })

            # Step 2: Analyze transcript to extract agent requirements
            logger.info(f"Analyzing transcript for {customer_name}...")
            agent_spec = self._analyze_transcript_for_agent(transcript, customer_name, agent_priority)

            if agent_spec.get('status') == 'error':
                return json.dumps(agent_spec)

            # Step 3: Generate complete agent Python code
            logger.info(f"Generating agent code for {agent_spec.get('agent_name')}...")
            agent_code = self._generate_complete_agent_code(agent_spec, customer_name)

            # Step 4: Generate demo JSON
            logger.info(f"Generating demo JSON...")
            demo_json = self._generate_demo_json(agent_spec, customer_name)

            # Step 5: Generate HTML tester
            logger.info(f"Generating HTML tester...")
            html_tester = self._generate_agent_tester_html(agent_spec, demo_json, customer_name)

            # Step 6: Deploy everything to project folder (and optionally to main folders)
            deployment_results = {}
            if deploy_to_storage:
                deployment_results = self._deploy_project_outputs(
                    project_id=project_id or agent_spec.get('agent_id'),
                    agent_spec=agent_spec,
                    agent_code=agent_code,
                    demo_json=demo_json,
                    html_tester=html_tester,
                    deploy_to_main_folders=kwargs.get('deploy_to_main_folders', True),
                    user_guid=user_guid
                )

            agent_id = agent_spec.get('agent_id')
            project_folder = project_id or agent_id

            # Build response
            result = {
                "status": "success",
                "action": "transcript_to_agent",
                "customer_name": customer_name,
                "project_id": project_folder,
                "agent_spec": {
                    "agent_name": agent_spec.get('agent_name'),
                    "agent_id": agent_id,
                    "class_name": agent_spec.get('class_name'),
                    "description": agent_spec.get('description'),
                    "category": agent_spec.get('category'),
                    "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                    "use_cases": agent_spec.get('use_cases', []),
                    "data_sources": agent_spec.get('data_sources', [])
                },
                "files_generated": {
                    "agent_file": f"{agent_id}_agent.py",
                    "demo_file": f"{agent_id}_demo.json",
                    "tester_file": "agent_tester.html",
                    "agent_code_length": len(agent_code),
                    "demo_json_length": len(json.dumps(demo_json)),
                    "html_tester_length": len(html_tester)
                },
                "project_folder": f"rapp_projects/{project_folder}/outputs/",
                "deployment": deployment_results,
                "agent_code": agent_code,
                "demo_json": demo_json,
                "html_tester": html_tester,
                "next_steps": [
                    f"All files in: rapp_projects/{project_folder}/outputs/",
                    f"Open agent_tester.html to test the agent and demo",
                    f"Agent also deployed to: agents/{agent_id}_agent.py" if deployment_results.get('main_agent_deployed') else f"To deploy: copy {agent_id}_agent.py to agents/",
                    "Restart function app to load the new agent"
                ],
                "generated_at": datetime.now().isoformat()
            }

            return json.dumps(result)

        except Exception as e:
            logger.error(f"Error in transcript_to_agent: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "action": "transcript_to_agent"
            })

    def _get_transcript_from_storage(self, project_id: str, user_guid: str) -> str:
        """Read transcript from project inputs folder."""
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return ""

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Check for transcript patterns
                for pattern in self.INPUT_PATTERNS.get('discovery_transcript', []):
                    if pattern in filename_lower:
                        content = self.storage_manager.read_file(input_directory, filename)
                        if content:
                            logger.info(f"Found transcript: {filename}")
                            return content

            return ""
        except Exception as e:
            logger.warning(f"Error reading transcript from storage: {e}")
            return ""

    def _analyze_transcript_for_agent(self, transcript: str, customer_name: str, agent_priority: str = "") -> Dict[str, Any]:
        """Analyze transcript to extract agent specification."""
        client = self._get_openai_client()

        priority_instruction = ""
        if agent_priority:
            priority_instruction = f"\n\nIMPORTANT: The user wants to prioritize building an agent related to: {agent_priority}. Focus on this area if mentioned in the transcript."

        prompt = f"""Analyze this discovery call transcript and design a production-ready AI agent.

CUSTOMER: {customer_name}
{priority_instruction}

TRANSCRIPT:
{transcript}

Based on the transcript, design ONE specific AI agent that addresses their highest-priority need.

Return ONLY valid JSON (no markdown):
{{
  "agent_name": "Human readable name (e.g., 'Artist Contract Analyzer')",
  "agent_id": "snake_case_agent (e.g., 'artist_contract_analyzer_agent')",
  "class_name": "PascalCaseAgent (e.g., 'ArtistContractAnalyzerAgent')",
  "description": "2-3 sentence description of what the agent does and its value proposition",
  "category": "legal|finance|operations|sales|hr|analytics|communications",
  "problem_statement": "The specific problem this agent solves",
  "target_users": ["list of user roles who will use this"],
  "data_sources": [
    {{"name": "source name", "type": "API|Database|File|Manual", "description": "what data it provides"}}
  ],
  "actions": [
    {{
      "name": "action_name",
      "description": "What this action does",
      "parameters": ["param1", "param2"],
      "example_input": {{"action": "action_name", "param1": "value"}},
      "example_output": "Example response text"
    }}
  ],
  "use_cases": ["list of 4-6 specific use cases"],
  "integrations": ["list of systems this would integrate with"],
  "success_metrics": ["how success is measured"],
  "demo_conversation": [
    {{"role": "user", "content": "Example user message"}},
    {{"role": "agent", "content": "Example agent response with **markdown** formatting"}}
  ],
  "sample_scenarios": [
    {{
      "name": "Scenario Name",
      "description": "What this scenario demonstrates",
      "prompts": ["prompt 1", "prompt 2", "prompt 3"]
    }}
  ]
}}

Design 4-6 actions that cover the main capabilities. Make the demo_conversation show a realistic interaction that demonstrates the agent's value. Include at least 2-3 sample scenarios."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = parse_llm_json_response(response.choices[0].message.content, "raw_spec")

        # Validate required fields
        required = ['agent_name', 'agent_id', 'class_name', 'description', 'actions']
        missing = [f for f in required if not result.get(f)]
        if missing:
            result['status'] = 'error'
            result['error'] = f"Missing required fields: {missing}"
        else:
            result['status'] = 'success'

        return result

    def _generate_complete_agent_code(self, agent_spec: Dict[str, Any], customer_name: str) -> str:
        """Generate complete, production-ready agent Python code."""
        client = self._get_openai_client()

        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATION:
{json.dumps(agent_spec, indent=2)}

CUSTOMER: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern EXACTLY:
   - Import from agents.basic_agent import BasicAgent
   - Class inherits from BasicAgent
   - __init__ sets self.name, self.metadata with full JSON Schema, calls super().__init__()
   - perform(**kwargs) method that routes to action handlers and ALWAYS returns json.dumps()

2. Metadata must include:
   - name: {agent_spec.get('agent_name', 'Agent')}
   - description: Full description with all actions listed
   - parameters: Complete JSON Schema with all action parameters

3. Code quality:
   - Use logging, not print
   - No hardcoded credentials - use os.environ
   - Wrap external calls in try/except
   - Return JSON strings from perform() - NEVER raw dicts or exceptions
   - Include docstrings

4. Action handlers:
   - Create a _handle_{{action_name}} method for each action
   - Each handler returns a dict that gets json.dumps() in perform()
   - Include realistic mock data that demonstrates the agent's capabilities

5. Include:
   - Module docstring with agent purpose and usage
   - Usage example in if __name__ == "__main__" block
   - All necessary imports at the top

Generate the complete Python code - no placeholders, no TODOs. The agent should work immediately when dropped into the agents/ folder."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content

        # Extract code from markdown if present
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()
        elif '```' in code:
            parts = code.split('```')
            if len(parts) >= 2:
                code = parts[1].strip()

        return code

    def _generate_demo_json(self, agent_spec: Dict[str, Any], customer_name: str) -> Dict[str, Any]:
        """Generate demo JSON in the ScriptedDemoAgent format."""

        # Build actions list from spec
        actions = []
        for action in agent_spec.get('actions', []):
            actions.append({
                "name": action.get('name'),
                "description": action.get('description'),
                "parameters": action.get('parameters', []),
                "example": {
                    "input": action.get('example_input', {}),
                    "output": action.get('example_output', '')
                }
            })

        # Build metadata
        parameters_properties = {
            "action": {
                "type": "string",
                "enum": [a.get('name') for a in agent_spec.get('actions', [])],
                "description": "The action to perform"
            }
        }

        # Add common parameters based on actions
        param_set = set()
        for action in agent_spec.get('actions', []):
            for param in action.get('parameters', []):
                param_set.add(param)

        for param in param_set:
            if param != 'action':
                parameters_properties[param] = {
                    "type": "string",
                    "description": f"{param.replace('_', ' ').title()} parameter"
                }

        demo_json = {
            "agent": {
                "id": agent_spec.get('agent_id'),
                "name": agent_spec.get('agent_name'),
                "version": "1.0.0",
                "category": agent_spec.get('category', 'general'),
                "icon": self._get_category_icon(agent_spec.get('category', 'general')),
                "description": agent_spec.get('description'),
                "tokens": 750,
                "author": f"RAPP Pipeline - {customer_name}",
                "created": datetime.now().strftime("%Y-%m-%d"),
                "updated": datetime.now().strftime("%Y-%m-%d")
            },
            "metadata": {
                "name": agent_spec.get('class_name', '').replace('Agent', ''),
                "description": agent_spec.get('description'),
                "parameters": {
                    "type": "object",
                    "properties": parameters_properties,
                    "required": ["action"]
                }
            },
            "actions": actions,
            "useCases": agent_spec.get('use_cases', []),
            "integrations": agent_spec.get('integrations', []),
            "demoConversation": agent_spec.get('demo_conversation', []),
            "sampleScenarios": agent_spec.get('sample_scenarios', [])
        }

        return demo_json

    def _get_category_icon(self, category: str) -> str:
        """Get FontAwesome icon for category."""
        icons = {
            "legal": "fa-gavel",
            "finance": "fa-chart-line",
            "operations": "fa-cogs",
            "sales": "fa-handshake",
            "hr": "fa-users",
            "analytics": "fa-chart-bar",
            "communications": "fa-comments",
            "general": "fa-robot"
        }
        return icons.get(category, "fa-robot")

    def _deploy_project_outputs(self, project_id: str, agent_spec: Dict, agent_code: str,
                                  demo_json: Dict, html_tester: str, deploy_to_main_folders: bool,
                                  user_guid: str) -> Dict:
        """Deploy all generated files to project folder and optionally to main folders."""
        results = {
            "project_deployed": False,
            "main_agent_deployed": False,
            "main_demo_deployed": False,
            "project_path": None,
            "files": [],
            "errors": []
        }

        agent_id = agent_spec.get('agent_id', 'generated_agent')
        output_dir = f"rapp_projects/{project_id}/outputs"

        # Ensure output directory exists
        try:
            self.storage_manager.ensure_directory_exists(output_dir)
        except Exception as e:
            logger.warning(f"Could not ensure directory exists: {e}")

        # Deploy to project folder
        try:
            # Agent code
            agent_filename = f"{agent_id}_agent.py"
            self.storage_manager.write_file(output_dir, agent_filename, agent_code)
            results['files'].append(f"{output_dir}/{agent_filename}")
            logger.info(f"Saved agent to: {output_dir}/{agent_filename}")

            # Demo JSON
            demo_filename = f"{agent_id}_demo.json"
            self.storage_manager.write_file(output_dir, demo_filename, json.dumps(demo_json, indent=2))
            results['files'].append(f"{output_dir}/{demo_filename}")
            logger.info(f"Saved demo to: {output_dir}/{demo_filename}")

            # HTML Tester
            self.storage_manager.write_file(output_dir, "agent_tester.html", html_tester)
            results['files'].append(f"{output_dir}/agent_tester.html")
            logger.info(f"Saved tester to: {output_dir}/agent_tester.html")

            # Result JSON (without the large code/html fields)
            result_summary = {
                "agent_id": agent_id,
                "agent_name": agent_spec.get('agent_name'),
                "customer_name": agent_spec.get('customer_name', 'Unknown'),
                "category": agent_spec.get('category'),
                "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                "generated_at": datetime.now().isoformat(),
                "files": [agent_filename, demo_filename, "agent_tester.html"]
            }
            self.storage_manager.write_file(output_dir, "result.json", json.dumps(result_summary, indent=2))
            results['files'].append(f"{output_dir}/result.json")

            results['project_deployed'] = True
            results['project_path'] = output_dir
            logger.info(f"All project files saved to: {output_dir}")

        except Exception as e:
            results['errors'].append(f"Project deployment failed: {str(e)}")
            logger.error(f"Failed to deploy to project folder: {e}")

        # Optionally deploy to main agents/ and demos/ folders
        if deploy_to_main_folders:
            try:
                agent_path = f"{agent_id}_agent.py"
                self.storage_manager.write_file('agents', agent_path, agent_code)
                results['main_agent_deployed'] = True
                logger.info(f"Deployed agent to: agents/{agent_path}")
            except Exception as e:
                results['errors'].append(f"Main agent deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to agents/: {e}")

            try:
                demo_path = f"{agent_id}_demo.json"
                self.storage_manager.write_file('demos', demo_path, json.dumps(demo_json, indent=2))
                results['main_demo_deployed'] = True
                logger.info(f"Deployed demo to: demos/{demo_path}")
            except Exception as e:
                results['errors'].append(f"Main demo deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to demos/: {e}")

        return results

    def _generate_agent_tester_html(self, agent_spec: Dict, demo_json: Dict, customer_name: str) -> str:
        """Generate a self-contained HTML page to test both the real agent and demo."""
        agent_id = agent_spec.get('agent_id', 'agent')
        agent_name = agent_spec.get('agent_name', 'Agent')
        description = agent_spec.get('description', '')
        actions = agent_spec.get('actions', [])
        demo_conversation = demo_json.get('demoConversation', [])
        sample_scenarios = demo_json.get('sampleScenarios', [])

        # Build action buttons HTML
        action_buttons = ""
        for action in actions:
            action_buttons += f'''
            <button class="action-btn" onclick="testAction('{action.get('name')}')">
                <span class="action-name">{action.get('name')}</span>
                <span class="action-desc">{action.get('description', '')[:50]}...</span>
            </button>'''

        # Build demo conversation HTML
        demo_steps = ""
        for i, msg in enumerate(demo_conversation):
            role = msg.get('role', 'user')
            content = msg.get('content', '').replace('`', '\\`').replace('${', '\\${')
            demo_steps += f'''
            <div class="demo-step" data-step="{i}">
                <div class="step-role {role}">{role.upper()}</div>
                <div class="step-content">{content}</div>
            </div>'''

        # Build sample prompts
        sample_prompts = ""
        for scenario in sample_scenarios:
            for prompt in scenario.get('prompts', []):
                sample_prompts += f'<button class="sample-prompt" onclick="sendMessage(`{prompt}`)">{prompt}</button>'

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{agent_name} - Agent Tester</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

        /* Header */
        .header {{
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid #0f3460;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .header h1 {{ color: #00d4ff; margin-bottom: 8px; }}
        .header p {{ color: #888; font-size: 14px; }}
        .header .customer {{ color: #00ff88; font-size: 12px; margin-top: 8px; }}

        /* Config Panel */
        .config-panel {{
            background: #0a0a1a;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 12px;
            align-items: end;
        }}
        .config-panel label {{ display: block; font-size: 12px; color: #888; margin-bottom: 4px; }}
        .config-panel input {{
            width: 100%;
            padding: 10px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 6px;
            color: #fff;
            font-size: 13px;
        }}
        .config-panel input:focus {{ outline: none; border-color: #00d4ff; }}
        .save-config {{
            padding: 10px 20px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }}

        /* Tabs */
        .tabs {{
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
        }}
        .tab {{
            padding: 12px 24px;
            background: #16213e;
            border: 2px solid #0f3460;
            border-radius: 8px;
            color: #888;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .tab:hover {{ border-color: #00d4ff; }}
        .tab.active {{
            background: #00d4ff;
            color: #1a1a2e;
            border-color: #00d4ff;
            font-weight: bold;
        }}

        /* Main Content Grid */
        .main-grid {{
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 20px;
        }}

        /* Sidebar */
        .sidebar {{
            background: #0f0f1a;
            border-radius: 12px;
            padding: 16px;
        }}
        .sidebar h3 {{
            color: #00d4ff;
            font-size: 14px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #1a4a7a;
        }}
        .action-btn {{
            display: block;
            width: 100%;
            padding: 12px;
            margin-bottom: 8px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .action-btn:hover {{
            background: #1a5a9a;
            border-color: #00d4ff;
            transform: translateX(4px);
        }}
        .action-name {{ display: block; font-weight: bold; margin-bottom: 4px; }}
        .action-desc {{ display: block; font-size: 11px; color: #666; }}

        .sample-prompts {{ margin-top: 16px; }}
        .sample-prompt {{
            display: block;
            width: 100%;
            padding: 8px 12px;
            margin-bottom: 6px;
            background: #0a0a1a;
            border: 1px solid #1a4a7a;
            border-radius: 6px;
            color: #aaa;
            font-size: 12px;
            text-align: left;
            cursor: pointer;
        }}
        .sample-prompt:hover {{ background: #16213e; color: #fff; }}

        /* Chat Area */
        .chat-area {{
            background: #0f0f1a;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            height: 600px;
        }}
        .chat-messages {{
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }}
        .message {{
            margin-bottom: 16px;
            padding: 12px 16px;
            border-radius: 12px;
            max-width: 85%;
        }}
        .message.user {{
            background: #00d4ff;
            color: #1a1a2e;
            margin-left: auto;
        }}
        .message.agent {{
            background: #16213e;
            border: 1px solid #0f3460;
        }}
        .message pre {{
            background: #0a0a1a;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            margin-top: 8px;
            font-size: 12px;
        }}

        .chat-input {{
            padding: 16px;
            border-top: 1px solid #1a4a7a;
            display: flex;
            gap: 12px;
        }}
        .chat-input input {{
            flex: 1;
            padding: 12px 16px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
        }}
        .chat-input input:focus {{ outline: none; border-color: #00d4ff; }}
        .chat-input button {{
            padding: 12px 24px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }}
        .chat-input button:hover {{ background: #00ffff; }}
        .chat-input button:disabled {{ background: #333; color: #666; cursor: not-allowed; }}

        /* Demo Panel */
        .demo-panel {{ display: none; }}
        .demo-panel.active {{ display: block; }}
        .demo-step {{
            background: #16213e;
            border-radius: 8px;
            margin-bottom: 12px;
            overflow: hidden;
        }}
        .step-role {{
            padding: 8px 16px;
            font-size: 11px;
            font-weight: bold;
            background: #0a0a1a;
        }}
        .step-role.user {{ color: #00ff88; }}
        .step-role.agent {{ color: #00d4ff; }}
        .step-content {{
            padding: 16px;
            white-space: pre-wrap;
            line-height: 1.6;
        }}

        .demo-controls {{
            display: flex;
            gap: 12px;
            margin-top: 16px;
        }}
        .demo-btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        .demo-btn.play {{ background: #00ff88; color: #1a1a2e; }}
        .demo-btn.reset {{ background: #ff6b6b; color: #fff; }}

        /* Status */
        .status {{
            padding: 8px 16px;
            background: #0a0a1a;
            border-radius: 6px;
            font-size: 12px;
            color: #666;
            margin-top: 12px;
        }}
        .status.success {{ color: #00ff88; }}
        .status.error {{ color: #ff6b6b; }}
        .status.loading {{ color: #00d4ff; }}

        /* Responsive */
        @media (max-width: 900px) {{
            .main-grid {{ grid-template-columns: 1fr; }}
            .config-panel {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{agent_name}</h1>
            <p>{description}</p>
            <div class="customer">Customer: {customer_name}</div>
        </div>

        <div class="config-panel">
            <div>
                <label>API Endpoint</label>
                <input type="text" id="apiEndpoint" value="http://localhost:7071/api/businessinsightbot_function" placeholder="API URL">
            </div>
            <div>
                <label>Function Key (optional)</label>
                <input type="text" id="apiKey" placeholder="Function key for Azure deployment">
            </div>
            <button class="save-config" onclick="saveConfig()">Save</button>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="switchTab('chat')">Real Agent</button>
            <button class="tab" onclick="switchTab('demo')">Demo Mode</button>
        </div>

        <div class="main-grid">
            <div class="sidebar">
                <h3>Agent Actions</h3>
                {action_buttons}

                <div class="sample-prompts">
                    <h3>Sample Prompts</h3>
                    {sample_prompts}
                </div>
            </div>

            <div id="chatPanel" class="chat-area">
                <div class="chat-messages" id="chatMessages"></div>
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Type a message..." onkeypress="if(event.key==='Enter')sendMessage()">
                    <button onclick="sendMessage()" id="sendBtn">Send</button>
                </div>
                <div class="status" id="status">Ready</div>
            </div>

            <div id="demoPanel" class="demo-panel chat-area">
                <div class="chat-messages">
                    {demo_steps}
                </div>
                <div class="demo-controls" style="padding: 16px;">
                    <button class="demo-btn play" onclick="playDemo()">Play Demo</button>
                    <button class="demo-btn reset" onclick="resetDemo()">Reset</button>
                </div>
                <div class="status" id="demoStatus">Click "Play Demo" to start</div>
            </div>
        </div>
    </div>

    <script>
        // Configuration
        let config = {{
            endpoint: localStorage.getItem('agentTesterEndpoint') || 'http://localhost:7071/api/businessinsightbot_function',
            key: localStorage.getItem('agentTesterKey') || ''
        }};

        // Demo JSON data (embedded)
        const demoJson = {json.dumps(demo_json)};
        const agentId = '{agent_id}';

        // Initialize
        document.getElementById('apiEndpoint').value = config.endpoint;
        document.getElementById('apiKey').value = config.key;

        let conversationHistory = [];
        let currentDemoStep = 0;

        function saveConfig() {{
            config.endpoint = document.getElementById('apiEndpoint').value;
            config.key = document.getElementById('apiKey').value;
            localStorage.setItem('agentTesterEndpoint', config.endpoint);
            localStorage.setItem('agentTesterKey', config.key);
            setStatus('Configuration saved!', 'success');
        }}

        function switchTab(tab) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');

            document.getElementById('chatPanel').style.display = tab === 'chat' ? 'flex' : 'none';
            document.getElementById('demoPanel').style.display = tab === 'demo' ? 'flex' : 'none';
            document.getElementById('demoPanel').classList.toggle('active', tab === 'demo');
        }}

        function setStatus(message, type = '') {{
            const status = document.getElementById('status');
            status.textContent = message;
            status.className = 'status ' + type;
        }}

        function addMessage(content, role) {{
            const messages = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = 'message ' + role;

            // Handle markdown-like formatting
            let formatted = content
                .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\n/g, '<br>')
                .replace(/`([^`]+)`/g, '<code>$1</code>');

            div.innerHTML = formatted;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }}

        async function sendMessage(text) {{
            const input = document.getElementById('messageInput');
            const message = text || input.value.trim();
            if (!message) return;

            input.value = '';
            addMessage(message, 'user');
            setStatus('Sending...', 'loading');
            document.getElementById('sendBtn').disabled = true;

            conversationHistory.push({{ role: 'user', content: message }});

            try {{
                let url = config.endpoint;
                if (config.key) {{
                    url += (url.includes('?') ? '&' : '?') + 'code=' + config.key;
                }}

                const response = await fetch(url, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        user_input: message,
                        conversation_history: conversationHistory
                    }})
                }});

                const data = await response.json();
                const assistantResponse = data.assistant_response || data.error || 'No response';

                addMessage(assistantResponse, 'agent');
                conversationHistory.push({{ role: 'assistant', content: assistantResponse }});
                setStatus('Ready', 'success');

            }} catch (err) {{
                setStatus('Error: ' + err.message, 'error');
                addMessage('Error: ' + err.message, 'agent');
            }}

            document.getElementById('sendBtn').disabled = false;
        }}

        function testAction(actionName) {{
            const prompt = `Test the ${{actionName}} action`;
            sendMessage(prompt);
        }}

        // Demo functions
        function playDemo() {{
            const steps = document.querySelectorAll('.demo-step');
            let i = 0;

            function showNext() {{
                if (i < steps.length) {{
                    steps[i].style.display = 'block';
                    steps[i].scrollIntoView({{ behavior: 'smooth' }});
                    i++;
                    document.getElementById('demoStatus').textContent = `Step ${{i}} of ${{steps.length}}`;
                    setTimeout(showNext, 2000);
                }} else {{
                    document.getElementById('demoStatus').textContent = 'Demo complete!';
                }}
            }}

            // Hide all first
            steps.forEach(s => s.style.display = 'none');
            showNext();
        }}

        function resetDemo() {{
            document.querySelectorAll('.demo-step').forEach(s => s.style.display = 'block');
            document.getElementById('demoStatus').textContent = 'Click "Play Demo" to start';
        }}
    </script>
</body>
</html>'''
        return html


# Usage example
if __name__ == "__main__":
    agent = RAPPAgent()

    # Test discovery preparation
    result = agent.perform(
        action="prepare_discovery_call",
        customer_name="Acme Corp",
        industry="manufacturing"
    )
    print("Prepare Discovery:", json.loads(result)["status"])

    # Test MVP generation
    result = agent.perform(
        action="generate_mvp_poke",
        customer_name="Acme Corp",
        project_name="Inventory Optimizer",
        problem_statement="Manual inventory counts take 4 hours daily"
    )
    print("MVP Poke:", json.loads(result)["status"])

    # Test quality gate
    result = agent.perform(
        action="execute_quality_gate",
        gate="QG1",
        customer_name="Acme Corp",
        input_data={"problemStatements": [{"problem": "Manual data entry"}]}
    )
    print("QG1:", json.loads(result).get("decision", "N/A"))

    # Test pipeline status
    result = agent.perform(
        action="get_pipeline_status",
        customer_name="Acme Corp",
        project_data={"current_step": 3, "completed_steps": [1, 2]}
    )
    print("Status:", json.loads(result)["progress_percent"], "% complete")
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
