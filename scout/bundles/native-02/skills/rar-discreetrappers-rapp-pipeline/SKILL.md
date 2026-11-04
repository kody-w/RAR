---
name: "rar-discreetrappers-rapp-pipeline"
description: "Unified RAPP Pipeline agent for building AI agents from discovery to deployment.\n\nRECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.\n\nAll actions:\n- AUTO: auto_process (scans inputs, processes, generates reports), generate_report\n- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary\n- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document\n- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code\n- Quality Gates: execute_quality_gate (gate: QG1-QG6)\n- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/rapp_pipeline_agent", "rar_sha256": "a5dc861857f4108578603c1ce6a547ee766c55cd2eb8b0bd5f6cfd1378954089", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Bill Whalen", "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"]}
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
