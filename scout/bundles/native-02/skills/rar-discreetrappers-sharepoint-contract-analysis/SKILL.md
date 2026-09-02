---
name: "rar-discreetrappers-sharepoint-contract-analysis"
description: "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sharepoint_contract_analysis_agent", "rar_sha256": "befdce082ff846fa57e936fc130bd1e423451de8da911a50674b9a4c9c261d32", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sharepoint_contract_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/sharepoint-contract-analysis:e190260c1300b93326fdb899e202a8b3fc7816c63950d663e041c97e158f38f7", "kind": "skill"}, "version": "1.0.2", "author": "Bill Whalen", "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/sharepoint_contract_analysis_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sharepoint_contract_analysis_agent.py` is
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

Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
      "enum": [
        "list_contracts",
        "full_workup",
        "analyze_contract",
        "extract_clauses",
        "summarize_contract",
        "identify_risks",
        "compare_contracts"
      ],
      "type": "string"
    },
    "audience": {
      "description": "Target audience for summary: legal, business, executive",
      "enum": [
        "legal",
        "business",
        "executive"
      ],
      "type": "string"
    },
    "clause_types": {
      "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "contract_name": {
      "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')",
      "type": "string"
    },
    "contract_name_b": {
      "description": "Second contract name for comparison (used with compare_contracts action)",
      "type": "string"
    },
    "summary_type": {
      "description": "Type of summary: executive (brief), detailed, or legal",
      "enum": [
        "executive",
        "detailed",
        "legal"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_contract_analysis_agent.py` and embedded as the fenced Python below (sha256 befdce082ff846fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_contract_analysis_agent.py` first:

```bash
python3 sharepoint_contract_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_contract_analysis_agent.py   # or on stdin
python3 sharepoint_contract_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/sharepoint_contract_analysis_agent",
    "version": "1.0.2",
    "display_name": "ContractAnalysis",
    "description": "Analyzes contract documents in Azure File Storage with Azure OpenAI \u2014 clause extraction, risk flagging, and comparison.",
    "author": "Bill Whalen",
    "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": ["AZURE_FILES_SHARE_NAME", "AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT", "AZURE_STORAGE_ACCOUNT_NAME"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import io
import re
from datetime import datetime
from typing import Optional, Dict, List, Any
from agents.basic_agent import BasicAgent

# Document processing imports
# Note: Auto-installation of missing packages is handled globally by function_app.py
# These imports will trigger auto-install if the packages are missing

# PDF support - try pypdf (modern) first, then PyPDF2 (legacy)
PDF_SUPPORT = False
pypdf_module = None

try:
    import pypdf
    pypdf_module = pypdf
    PDF_SUPPORT = True
except ImportError:
    try:
        import PyPDF2
        pypdf_module = PyPDF2
        PDF_SUPPORT = True
    except ImportError:
        logging.warning("PDF support disabled - pypdf/PyPDF2 not available")

# PDF generation support (reportlab)
PDF_GENERATION = False
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    PDF_GENERATION = True
except ImportError:
    logging.warning("PDF generation disabled - reportlab not available")

# DOCX support
DOCX_SUPPORT = False
DocxDocument = None

try:
    from docx import Document as DocxDocument
    DOCX_SUPPORT = True
except ImportError:
    logging.warning("DOCX support disabled - python-docx not available")

# Azure imports
try:
    from azure.identity import DefaultAzureCredential
    from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient, ShareServiceClient
    from openai import AzureOpenAI
    from azure.identity import get_bearer_token_provider
    AZURE_SUPPORT = True
except ImportError as e:
    AZURE_SUPPORT = False
    logging.warning(f"Azure SDK not fully installed: {e}")


class ContractAnalysisAgent(BasicAgent):
    """
    Production contract analysis agent that reads documents from Azure File Storage
    and uses Azure OpenAI to extract clauses, generate summaries, and identify risks.

    Storage Structure:
        contracts/           - Root folder for all contracts
        contracts/templates/ - Standard contract templates for comparison
        contracts/analysis/  - Stored analysis results (optional)

    Supported Actions:
        - list_contracts: List available contracts in storage
        - analyze_contract: Full analysis with all extractions
        - extract_clauses: Extract specific clause categories
        - summarize_contract: Generate executive summary
        - identify_risks: Compare against standard terms
        - compare_contracts: Compare two contracts side-by-side
    """

    def __init__(self):
        self.name = 'ContractAnalysis'
        self.metadata = {
            "name": self.name,
            "description": "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
                        "enum": [
                            "list_contracts",
                            "full_workup",
                            "analyze_contract",
                            "extract_clauses",
                            "summarize_contract",
                            "identify_risks",
                            "compare_contracts"
                        ]
                    },
                    "contract_name": {
                        "type": "string",
                        "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')"
                    },
                    "contract_name_b": {
                        "type": "string",
                        "description": "Second contract name for comparison (used with compare_contracts action)"
                    },
                    "clause_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration"
                    },
                    "summary_type": {
                        "type": "string",
                        "description": "Type of summary: executive (brief), detailed, or legal",
                        "enum": ["executive", "detailed", "legal"]
                    },
                    "audience": {
                        "type": "string",
                        "description": "Target audience for summary: legal, business, executive",
                        "enum": ["legal", "business", "executive"]
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

        # Initialize Azure clients
        self.storage_account = os.environ.get('AZURE_STORAGE_ACCOUNT_NAME', 'stov4bzgynnlvii')
        self.share_name = os.environ.get('AZURE_FILES_SHARE_NAME', 'azfrapp-ov4bzgynnlviiov4bzgynnlvii')
        self.contracts_folder = 'contracts'

        # Initialize OpenAI client
        self.openai_client = None
        self.deployment_name = os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-5.1-chat')
        self._init_openai_client()

    def _init_openai_client(self):
        """Initialize Azure OpenAI client with managed identity."""
        try:
            endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
            if not endpoint:
                logging.warning("AZURE_OPENAI_ENDPOINT not set")
                return

            credential = DefaultAzureCredential()
            token_provider = get_bearer_token_provider(
                credential,
                "https://cognitiveservices.azure.com/.default"
            )

            self.openai_client = AzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token_provider=token_provider,
                api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
            )
            logging.info("ContractAnalysisAgent: OpenAI client initialized")
        except Exception as e:
            logging.error(f"Failed to initialize OpenAI client: {e}")

    def _get_share_service_client(self) -> Optional[ShareServiceClient]:
        """Get Azure File Share service client."""
        try:
            credential = DefaultAzureCredential()
            account_url = f"https://{self.storage_account}.file.core.windows.net"
            return ShareServiceClient(
                account_url=account_url,
                credential=credential,
                token_intent="backup"  # Required for token-based auth
            )
        except Exception as e:
            logging.error(f"Failed to create share service client: {e}")
            return None

    def _list_files_in_folder(self, folder_path: str = None) -> List[Dict]:
        """List all files in the contracts folder."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return []

            share_client = service_client.get_share_client(self.share_name)
            target_folder = folder_path or self.contracts_folder

            try:
                directory_client = share_client.get_directory_client(target_folder)
                files = []

                for item in directory_client.list_directories_and_files():
                    if not item.get('is_directory', False):
                        file_name = item['name']
                        # Get file properties
                        file_client = directory_client.get_file_client(file_name)
                        props = file_client.get_file_properties()

                        files.append({
                            "name": file_name,
                            "size_kb": round(props.size / 1024, 2),
                            "last_modified": props.last_modified.isoformat() if props.last_modified else None,
                            "path": f"{target_folder}/{file_name}"
                        })

                return files
            except Exception as e:
                if "ResourceNotFound" in str(e):
                    logging.info(f"Folder {target_folder} does not exist, will be created on first upload")
                    return []
                raise

        except Exception as e:
            logging.error(f"Error listing files: {e}")
            return []

    def _read_file_content(self, file_path: str) -> Optional[bytes]:
        """Read file content from Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return None

            share_client = service_client.get_share_client(self.share_name)
            file_client = share_client.get_file_client(file_path)

            download = file_client.download_file()
            return download.readall()

        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return None

    def _write_file_content(self, file_path: str, content: str) -> bool:
        """Write content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            content_bytes = content.encode('utf-8')
            file_client.upload_file(content_bytes)

            logging.info(f"Successfully wrote file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing file {file_path}: {e}")
            return False

    def _generate_download_url(self, file_path: str) -> str:
        """Generate a download URL for the file.

        Note: This storage account uses Entra ID authentication only (shared key access disabled).
        The returned URL requires authentication to access. Users can:
        1. Open in Azure Portal to download
        2. Use Azure Storage Explorer with their credentials
        3. Access via authenticated API calls
        """
        account_url = f"https://{self.storage_account}.file.core.windows.net"
        file_url = f"{account_url}/{self.share_name}/{file_path}"
        return file_url

    def _save_analysis_report(self, contract_name: str, analysis_data: Dict) -> Dict:
        """Save analysis report as professional PDF and return download info."""
        try:
            # Generate report filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = contract_name.rsplit('.', 1)[0]  # Remove extension
            report_name = f"{base_name}_analysis_{timestamp}.pdf"
            report_path = f"contracts/analysis/{report_name}"

            # Generate PDF report
            if PDF_GENERATION:
                pdf_bytes = self._generate_pdf_report(contract_name, analysis_data)
                if pdf_bytes:
                    # Write PDF to storage
                    if self._write_file_bytes(report_path, pdf_bytes):
                        download_url = self._generate_download_url(report_path)
                        return {
                            "saved": True,
                            "format": "PDF",
                            "report_name": report_name,
                            "report_path": report_path,
                            "download_url": download_url,
                            "size_kb": round(len(pdf_bytes) / 1024, 2)
                        }

            # Fallback to JSON if PDF generation fails
            report_name = f"{base_name}_analysis_{timestamp}.json"
            report_path = f"contracts/analysis/{report_name}"
            report_content = json.dumps(analysis_data, indent=2, default=str)

            if self._write_file_content(report_path, report_content):
                download_url = self._generate_download_url(report_path)
                return {
                    "saved": True,
                    "format": "JSON",
                    "report_name": report_name,
                    "report_path": report_path,
                    "download_url": download_url,
                    "size_kb": round(len(report_content) / 1024, 2)
                }
            else:
                return {"saved": False, "error": "Failed to write file"}

        except Exception as e:
            logging.error(f"Error saving analysis report: {e}")
            return {"saved": False, "error": str(e)}

    def _write_file_bytes(self, file_path: str, content: bytes) -> bool:
        """Write binary content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            file_client.upload_file(content)

            logging.info(f"Successfully wrote binary file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing binary file {file_path}: {e}")
            return False

    def _generate_pdf_report(self, contract_name: str, analysis_data: Dict) -> Optional[bytes]:
        """Generate a professional PDF analysis report."""
        if not PDF_GENERATION:
            return None

        try:
            # === DEBUG LOGGING: Dump structure of all data sections ===
            logging.info("=" * 60)
            logging.info("PDF GENERATION - DATA STRUCTURE ANALYSIS")
            logging.info("=" * 60)

            # Check executive_summary
            exec_summary = analysis_data.get('executive_summary', {})
            if isinstance(exec_summary, dict):
                logging.info(f"executive_summary keys: {list(exec_summary.keys())}")
                if exec_summary.get('parse_error'):
                    logging.error(f"executive_summary has PARSE ERROR")
                logging.info(f"  - summary length: {len(exec_summary.get('summary', ''))}")
                logging.info(f"  - risk_level: {exec_summary.get('risk_level', 'MISSING')}")
                logging.info(f"  - key_points count: {len(exec_summary.get('key_points', []))}")
            else:
                logging.error(f"executive_summary is NOT a dict: {type(exec_summary)}")

            # Check risk_assessment
            risk_assessment = analysis_data.get('risk_assessment', {})
            if isinstance(risk_assessment, dict):
                logging.info(f"risk_assessment keys: {list(risk_assessment.keys())}")
                if risk_assessment.get('parse_error'):
                    logging.error(f"risk_assessment has PARSE ERROR - raw: {risk_assessment.get('raw_analysis', '')[:500]}")
                logging.info(f"  - overall_risk_level: {risk_assessment.get('overall_risk_level', 'MISSING')}")
                logging.info(f"  - risk_score: {risk_assessment.get('risk_score', 'MISSING')}")
                logging.info(f"  - risks count: {len(risk_assessment.get('risks', []))}")
                logging.info(f"  - summary length: {len(risk_assessment.get('summary', ''))}")
            else:
                logging.error(f"risk_assessment is NOT a dict: {type(risk_assessment)}")

            # Check full_analysis
            full_analysis = analysis_data.get('full_analysis', {})
            if isinstance(full_analysis, dict):
                logging.info(f"full_analysis keys: {list(full_analysis.keys())}")
                if full_analysis.get('parse_error'):
                    logging.error(f"full_analysis has PARSE ERROR - raw: {full_analysis.get('raw_analysis', '')[:500]}")
                logging.info(f"  - contract_type: {full_analysis.get('contract_type', 'MISSING')}")
                logging.info(f"  - parties count: {len(full_analysis.get('parties', []))}")
                logging.info(f"  - financial_terms keys: {list(full_analysis.get('financial_terms', {}).keys()) if isinstance(full_analysis.get('financial_terms'), dict) else 'NOT DICT'}")
            else:
                logging.error(f"full_analysis is NOT a dict: {type(full_analysis)}")

            # Check extracted_clauses
            extracted_clauses = analysis_data.get('extracted_clauses', {})
            if isinstance(extracted_clauses, dict):
                logging.info(f"extracted_clauses keys: {list(extracted_clauses.keys())}")
                if extracted_clauses.get('parse_error'):
                    logging.error(f"extracted_clauses has PARSE ERROR")

            logging.info("=" * 60)

            # Create PDF in memory
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                leftMargin=0.75*inch,
                rightMargin=0.75*inch,
                topMargin=0.75*inch,
                bottomMargin=0.75*inch
            )

            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor('#1a365d')
            )
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceBefore=20,
                spaceAfter=10,
                textColor=colors.HexColor('#2c5282')
            )
            subheading_style = ParagraphStyle(
                'CustomSubHeading',
                parent=styles['Heading3'],
                fontSize=12,
                spaceBefore=12,
                spaceAfter=6,
                textColor=colors.HexColor('#4a5568')
            )
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=8,
                leading=14,
                alignment=TA_JUSTIFY
            )
            bullet_style = ParagraphStyle(
                'CustomBullet',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=4,
                leftIndent=20,
                bulletIndent=10
            )
            risk_high = ParagraphStyle(
                'RiskHigh',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#c53030'),
                spaceAfter=8
            )
            risk_medium = ParagraphStyle(
                'RiskMedium',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#dd6b20'),
                spaceAfter=8
            )
            risk_low = ParagraphStyle(
                'RiskLow',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#38a169'),
                spaceAfter=8
            )

            story = []

            # Title
            story.append(Paragraph("CONTRACT ANALYSIS REPORT", title_style))
            story.append(Spacer(1, 0.1*inch))

            # Contract info header
            story.append(Paragraph(f"<b>Contract:</b> {contract_name}", body_style))
            story.append(Paragraph(f"<b>Analysis Date:</b> {analysis_data.get('analyzed_at', datetime.now().isoformat())}", body_style))
            story.append(Spacer(1, 0.2*inch))

            # Horizontal line
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.2*inch))

            # Executive Summary Section
            exec_summary = analysis_data.get('executive_summary', {})
            if exec_summary:
                story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

                if isinstance(exec_summary, dict):
                    summary_text = exec_summary.get('summary', '')
                    if summary_text:
                        # Use larger max_length for executive summary - don't truncate
                        story.append(Paragraph(self._clean_text(summary_text, max_length=2000), body_style))

                    # Risk Level Box
                    risk_level = exec_summary.get('risk_level', 'unknown').upper()
                    risk_style = risk_high if risk_level == 'HIGH' else (risk_medium if risk_level == 'MEDIUM' else risk_low)
                    story.append(Spacer(1, 0.1*inch))
                    story.append(Paragraph(f"<b>Overall Risk Level: {risk_level}</b>", risk_style))

                    # Key Points
                    key_points = exec_summary.get('key_points', [])
                    if key_points:
                        story.append(Paragraph("<b>Key Points:</b>", subheading_style))
                        for point in key_points[:10]:  # Limit to 10 points
                            if isinstance(point, dict):
                                # Format dict with point and clickable ref
                                point_text = point.get('point', '')
                                point_ref = point.get('ref', '')
                                clickable_ref = self._format_clickable_ref(point_ref, analysis_data.get('_contract_text', '')) if point_ref else ""
                                formatted = f"{self._clean_text(point_text, max_length=300)} {clickable_ref}"
                            else:
                                formatted = self._clean_text(str(point), max_length=300)
                            story.append(Paragraph(f"* {formatted}", bullet_style))

                    # Recommendation
                    recommendation = exec_summary.get('recommendation', '')
                    if recommendation:
                        story.append(Spacer(1, 0.1*inch))
                        story.append(Paragraph(f"<b>Recommendation:</b> {self._clean_text(recommendation, max_length=1000)}", body_style))

            story.append(PageBreak())

            # Risk Assessment Section
            risk_assessment = analysis_data.get('risk_assessment', {})
            story.append(Paragraph("RISK ASSESSMENT", heading_style))

            if isinstance(risk_assessment, dict):
                # Check for parse error
                if risk_assessment.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Risk assessment data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = risk_assessment.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 2000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:2000], max_length=2000), body_style))
                else:
                    # Overall risk
                    overall_risk = risk_assessment.get('overall_risk_level', 'Unknown').upper()
                    risk_score = risk_assessment.get('risk_score', 'N/A')
                    risk_style = risk_high if overall_risk == 'HIGH' else (risk_medium if overall_risk == 'MEDIUM' else risk_low)
                    story.append(Paragraph(f"<b>Risk Level: {overall_risk} | Score: {risk_score}/100</b>", risk_style))

                    # Summary
                    risk_summary = risk_assessment.get('summary', '')
                    if risk_summary:
                        story.append(Paragraph(self._clean_text(risk_summary, max_length=1000), body_style))
                    else:
                        story.append(Paragraph("<i>No risk summary available.</i>", body_style))

                    # Individual risks
                    risks = risk_assessment.get('risks', [])
                    if risks:
                        story.append(Paragraph("<b>Identified Risks:</b>", subheading_style))

                        # Create table cell style for wrapping text
                        cell_style = ParagraphStyle(
                            'CellStyle',
                            parent=styles['Normal'],
                            fontSize=8,
                            leading=10,
                            spaceAfter=0
                        )
                        header_cell_style = ParagraphStyle(
                            'HeaderCellStyle',
                            parent=styles['Normal'],
                            fontSize=9,
                            leading=11,
                            textColor=colors.white,
                            fontName='Helvetica-Bold'
                        )

                        # Build header row with Paragraphs
                        risk_data = [[
                            Paragraph('Category', header_cell_style),
                            Paragraph('Severity', header_cell_style),
                            Paragraph('Description', header_cell_style)
                        ]]

                        for risk in risks[:10]:  # Limit to 10 risks
                            if isinstance(risk, dict):
                                desc_text = self._clean_text(risk.get('description', 'N/A'), max_length=300)
                                risk_data.append([
                                    Paragraph(risk.get('category', 'N/A'), cell_style),
                                    Paragraph(risk.get('severity', 'N/A').upper(), cell_style),
                                    Paragraph(desc_text, cell_style)
                                ])

                        if len(risk_data) > 1:
                            # Adjusted widths: Category 1", Severity 0.7", Description 5"
                            risk_table = Table(risk_data, colWidths=[1*inch, 0.7*inch, 5*inch])
                            risk_table.setStyle(TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
                                ('FONTSIZE', (0, 0), (-1, -1), 8),
                                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
                                ('TOPPADDING', (0, 0), (-1, -1), 4),
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                                ('LEFTPADDING', (0, 0), (-1, -1), 4),
                                ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                            ]))
                            story.append(risk_table)
                    else:
                        story.append(Paragraph("<i>No individual risks identified.</i>", body_style))

                    # Artist-favorable terms from risk assessment
                    artist_favorable = risk_assessment.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:6]:
                            if isinstance(term, dict):
                                term_text = term.get('term', 'N/A')
                                label_impact = term.get('label_impact', '')
                                ref = term.get('ref', '')
                                impact_text = f" - {label_impact}" if label_impact else ""
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(term_text))}{impact_text}{ref_text}", bullet_style))

                    # Negotiation points
                    negotiation = risk_assessment.get('negotiation_points', risk_assessment.get('negotiation_priorities', []))
                    if negotiation:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Recommended Negotiation Points:</b>", subheading_style))
                        for point in negotiation[:8]:
                            if isinstance(point, dict):
                                priority_text = point.get('priority', point.get('point', str(point)))
                                ref = point.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(priority_text))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(point))}", bullet_style))

                    # Deal breakers
                    deal_breakers = risk_assessment.get('deal_breakers', [])
                    if deal_breakers:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Potential Deal Breakers:</b>", subheading_style))
                        for item in deal_breakers[:5]:
                            if isinstance(item, dict):
                                issue = item.get('issue', 'N/A')
                                ref = item.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(issue))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(item))}", bullet_style))
            else:
                story.append(Paragraph("<i>Risk assessment data not available.</i>", body_style))

            story.append(PageBreak())

            # Full Analysis Section
            full_analysis = analysis_data.get('full_analysis', {})
            logging.info(f"PDF Generation - full_analysis keys: {list(full_analysis.keys()) if isinstance(full_analysis, dict) else 'NOT DICT'}")

            story.append(Paragraph("DETAILED CONTRACT ANALYSIS", heading_style))

            if isinstance(full_analysis, dict):
                # Check for parse error
                if full_analysis.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Detailed analysis data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = full_analysis.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 3000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:3000], max_length=3000), body_style))
                else:
                    # Contract Type
                    contract_type = full_analysis.get('contract_type', 'Not identified')
                    logging.info(f"PDF Generation - contract_type: {contract_type}")
                    story.append(Paragraph(f"<b>Contract Type:</b> {contract_type}", body_style))

                    # Get contract text for snippets
                    contract_text = analysis_data.get('_contract_text', '')
                    logging.info(f"PDF Generation - contract_text length: {len(contract_text) if contract_text else 0}")

                    # Parties
                    parties = full_analysis.get('parties', [])
                    logging.info(f"PDF Generation - parties count: {len(parties) if parties else 0}")
                    if parties:
                        story.append(Paragraph("<b>Parties:</b>", subheading_style))
                        for party in parties:
                            if isinstance(party, dict):
                                try:
                                    party_ref = party.get('ref', '')
                                    clickable_ref = self._format_clickable_ref(party_ref, contract_text) if party_ref else ""
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')} {clickable_ref}", bullet_style))
                                except Exception as e:
                                    logging.error(f"Error rendering party: {e}")
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')}", bullet_style))

                    # Term - handle both string and dict formats
                    term = full_analysis.get('term_duration', '')
                    if term:
                        if isinstance(term, dict):
                            term_val = term.get('value', 'N/A')
                            term_ref = term.get('ref', '')
                            clickable_ref = self._format_clickable_ref(term_ref, contract_text) if term_ref else ""
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term_val))} {clickable_ref}", body_style))
                        else:
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term))}", body_style))

                    # Effective Date
                    effective_date = full_analysis.get('effective_date', {})
                    if effective_date and isinstance(effective_date, dict):
                        date_val = effective_date.get('value', '')
                        if date_val:
                            date_ref = effective_date.get('ref', '')
                            clickable_ref = self._format_clickable_ref(date_ref, contract_text) if date_ref else ""
                            story.append(Paragraph(f"<b>Effective Date:</b> {self._clean_text(str(date_val))} {clickable_ref}", body_style))

                    # Financial Terms
                    financial = full_analysis.get('financial_terms', {})
                    if financial and isinstance(financial, dict):
                        story.append(Paragraph("<b>Financial Terms:</b>", subheading_style))
                        # Use the formatter for complex nested values
                        if financial.get('advances'):
                            formatted_advances = self._format_value_for_pdf(financial.get('advances'))
                            story.append(Paragraph(f"* Advances: {formatted_advances}", bullet_style))
                        if financial.get('royalty_rates'):
                            formatted_royalties = self._format_value_for_pdf(financial.get('royalty_rates'))
                            story.append(Paragraph(f"* Royalty Rates: {formatted_royalties}", bullet_style))
                        if financial.get('payment_schedule'):
                            formatted_schedule = self._format_value_for_pdf(financial.get('payment_schedule'))
                            story.append(Paragraph(f"* Payment Schedule: {formatted_schedule}", bullet_style))
                        if financial.get('label_investment'):
                            formatted_investment = self._format_value_for_pdf(financial.get('label_investment'))
                            story.append(Paragraph(f"* Label Investment: {formatted_investment}", bullet_style))
                        if financial.get('recoupment_terms'):
                            formatted_recoup = self._format_value_for_pdf(financial.get('recoupment_terms'))
                            story.append(Paragraph(f"* Recoupment: {formatted_recoup}", bullet_style))

                    # Rights Secured (AI returns 'rights_secured' not 'rights_granted')
                    rights = full_analysis.get('rights_secured', []) or full_analysis.get('rights_granted', [])
                    if rights:
                        story.append(Paragraph("<b>Rights Secured:</b>", subheading_style))
                        for right in rights[:8]:
                            if isinstance(right, dict):
                                exclusivity = "Exclusive" if right.get('exclusivity') else "Non-exclusive"
                                right_desc = right.get('right', '') or right.get('description', 'N/A')
                                scope = right.get('scope', '')
                                duration = right.get('duration', '')
                                ref = right.get('ref', '')

                                details = [f"{exclusivity}"]
                                if scope:
                                    details.append(f"Territory: {scope}")
                                if duration:
                                    details.append(f"Duration: {duration}")

                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(right_desc))} ({', '.join(details)}) {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist Obligations
                    artist_obligations = full_analysis.get('artist_obligations', [])
                    if artist_obligations:
                        story.append(Paragraph("<b>Artist Obligations:</b>", subheading_style))
                        for obligation in artist_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                deadline = obligation.get('deadline', '')
                                ref = obligation.get('ref', '')

                                deadline_text = f" (Deadline: {deadline})" if deadline else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{deadline_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Obligations
                    label_obligations = full_analysis.get('label_obligations', [])
                    if label_obligations:
                        story.append(Paragraph("<b>Label Obligations:</b>", subheading_style))
                        for obligation in label_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                impact = obligation.get('financial_impact', '')
                                ref = obligation.get('ref', '')

                                impact_text = f" (Cost: {impact})" if impact else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{impact_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Protections
                    protections = full_analysis.get('label_protections', [])
                    if protections:
                        story.append(Paragraph("<b>Label Protections:</b>", subheading_style))
                        for protection in protections[:6]:
                            if isinstance(protection, dict):
                                clause = protection.get('clause', 'N/A')
                                ref = protection.get('ref', '')
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(clause))} {clickable_ref}", bullet_style))

                    # Termination Clauses
                    termination = full_analysis.get('termination_clauses', [])
                    if termination:
                        story.append(Paragraph("<b>Termination Provisions:</b>", subheading_style))
                        for term_clause in termination[:6]:
                            if isinstance(term_clause, dict):
                                trigger = term_clause.get('trigger', 'N/A')
                                who = term_clause.get('who_can_trigger', '')
                                impact = term_clause.get('label_impact', '')
                                ref = term_clause.get('ref', '')

                                who_text = f" (By: {who})" if who else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(trigger))}{who_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist-Favorable Terms (risks to label)
                    artist_favorable = full_analysis.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:5]:
                            if isinstance(term, dict):
                                term_desc = term.get('term', 'N/A')
                                concern = term.get('concern', '')
                                ref = term.get('ref', '')

                                concern_text = f" - {concern}" if concern else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(term_desc))}{concern_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Overall Assessment
                    assessment = full_analysis.get('overall_assessment', '')
                    if assessment:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Overall Assessment:</b>", subheading_style))
                        story.append(Paragraph(self._clean_text(str(assessment)), body_style))
            else:
                story.append(Paragraph("<i>Detailed analysis data not available or could not be parsed.</i>", body_style))

            # SOURCE CONTRACT SECTION - Appended with page anchors for clickable references
            contract_text = analysis_data.get('_contract_text', '')
            if contract_text:
                story.append(PageBreak())
                story.append(Paragraph("SOURCE CONTRACT", heading_style))
                story.append(Paragraph(
                    "<i>The original contract text is included below. Click any page reference in the analysis above to jump directly to that location.</i>",
                    body_style
                ))
                story.append(Spacer(1, 0.2*inch))

                # Style for contract text (smaller, monospace-like)
                contract_style = ParagraphStyle(
                    'ContractText',
                    parent=styles['Normal'],
                    fontSize=9,
                    spaceAfter=6,
                    leading=12,
                    leftIndent=10,
                    rightIndent=10
                )

                # Split contract by page markers and create anchors
                # Look for [PAGE N] markers in the text
                page_pattern = re.compile(r'\[PAGE\s*(\d+)\]', re.IGNORECASE)

                # Split text by page markers, keeping the markers
                parts = page_pattern.split(contract_text)

                if len(parts) > 1:
                    # We have page markers
                    current_page = None
                    for i, part in enumerate(parts):
                        if i % 2 == 1:  # This is a page number
                            current_page = part
                            # Create anchor for this page
                            anchor_name = f"contract_page_{current_page}"
                            story.append(Spacer(1, 0.15*inch))
                            # Page header with anchor
                            story.append(Paragraph(
                                f'<a name="{anchor_name}"/><b>--- PAGE {current_page} ---</b>',
                                subheading_style
                            ))
                        else:
                            # This is content
                            if part.strip():
                                # Clean and split into paragraphs
                                paragraphs = part.strip().split('\n\n')
                                for para in paragraphs:
                                    if para.strip():
                                        clean_para = self._clean_text(para.strip(), max_length=2000)
                                        if clean_para:
                                            story.append(Paragraph(clean_para, contract_style))
                else:
                    # No page markers - create anchors for every ~2000 chars as "pages"
                    chunk_size = 2000
                    chunks = [contract_text[i:i+chunk_size] for i in range(0, len(contract_text), chunk_size)]
                    for page_num, chunk in enumerate(chunks, 1):
                        anchor_name = f"contract_page_{page_num}"
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph(
                            f'<a name="{anchor_name}"/><b>--- PAGE {page_num} ---</b>',
                            subheading_style
                        ))
                        clean_chunk = self._clean_text(chunk.strip(), max_length=2500)
                        if clean_chunk:
                            story.append(Paragraph(clean_chunk, contract_style))

            # Footer
            story.append(Spacer(1, 0.5*inch))
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.1*inch))

            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.grey,
                alignment=TA_CENTER
            )
            story.append(Paragraph(
                f"Generated by ContractAnalysis Agent | {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
                footer_style
            ))
            story.append(Paragraph(
                "This analysis is for informational purposes only and does not constitute legal advice.",
                footer_style
            ))

            # Build PDF
            doc.build(story)
            pdf_bytes = buffer.getvalue()
            buffer.close()

            logging.info(f"Generated PDF report: {len(pdf_bytes)} bytes")
            return pdf_bytes

        except Exception as e:
            logging.error(f"Error generating PDF report: {e}")
            return None

    def _clean_text(self, text: str, max_length: int = 500) -> str:
        """Clean text for PDF rendering - escape special characters and normalize Unicode."""
        if not text:
            return ""
        text = str(text)

        # Normalize Unicode characters that don't render in standard PDF fonts
        unicode_replacements = {
            '\u2011': '-',   # Non-breaking hyphen → regular hyphen
            '\u2010': '-',   # Hyphen → regular hyphen
            '\u2012': '-',   # Figure dash → regular hyphen
            '\u2013': '-',   # En-dash → regular hyphen
            '\u2014': '-',   # Em-dash → regular hyphen
            '\u2015': '-',   # Horizontal bar → regular hyphen
            '\u2018': "'",   # Left single quote → apostrophe
            '\u2019': "'",   # Right single quote → apostrophe
            '\u201a': "'",   # Single low quote → apostrophe
            '\u201b': "'",   # Single high-reversed quote → apostrophe
            '\u201c': '"',   # Left double quote → regular quote
            '\u201d': '"',   # Right double quote → regular quote
            '\u201e': '"',   # Double low quote → regular quote
            '\u201f': '"',   # Double high-reversed quote → regular quote
            '\u2022': '*',   # Bullet → asterisk
            '\u2023': '>',   # Triangular bullet → greater than
            '\u2024': '.',   # One dot leader → period
            '\u2025': '..',  # Two dot leader → two periods
            '\u2026': '...', # Ellipsis → three periods
            '\u2027': '-',   # Hyphenation point → hyphen
            '\u2032': "'",   # Prime → apostrophe
            '\u2033': '"',   # Double prime → quote
            '\u2039': '<',   # Single left angle quote
            '\u203a': '>',   # Single right angle quote
            '\u00ab': '<<',  # Left double angle quote
            '\u00bb': '>>',  # Right double angle quote
            '\u00a0': ' ',   # Non-breaking space → regular space
            '\u200b': '',    # Zero-width space → remove
            '\u200c': '',    # Zero-width non-joiner → remove
            '\u200d': '',    # Zero-width joiner → remove
            '\ufeff': '',    # BOM → remove
            '\u00b7': '*',   # Middle dot → asterisk
            '\u2212': '-',   # Minus sign → hyphen
            '\u00d7': 'x',   # Multiplication sign → x
            '\u00f7': '/',   # Division sign → slash
            '\u2248': '~',   # Almost equal → tilde
            '\u2260': '!=',  # Not equal → !=
            '\u2264': '<=',  # Less than or equal
            '\u2265': '>=',  # Greater than or equal
            '\u00b0': ' deg', # Degree symbol
            '\u00a9': '(c)', # Copyright
            '\u00ae': '(R)', # Registered
            '\u2122': '(TM)', # Trademark
        }

        for unicode_char, replacement in unicode_replacements.items():
            text = text.replace(unicode_char, replacement)

        # Replace any remaining non-ASCII characters that might cause issues
        # Keep basic extended ASCII (accented letters) but remove other oddities
        cleaned_chars = []
        for char in text:
            if ord(char) < 128:  # Standard ASCII
                cleaned_chars.append(char)
            elif ord(char) < 256:  # Extended ASCII (accented chars) - keep these
                cleaned_chars.append(char)
            else:  # Other Unicode - replace with space or skip
                cleaned_chars.append(' ')
        text = ''.join(cleaned_chars)

        # Clean up multiple spaces
        while '  ' in text:
            text = text.replace('  ', ' ')

        # Replace problematic characters for reportlab XML
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('\n', ' ')
        text = text.replace('\r', '')

        # Limit length to prevent overflow
        if max_length and len(text) > max_length:
            text = text[:max_length - 3] + "..."
        return text.strip()

    def _format_clickable_ref(self, ref_text: str, contract_text: str = '') -> str:
        """Format a reference string as a clickable internal PDF link with snippet.

        Converts refs like "Page 3, Section 4.1" to clickable links that jump
        to the corresponding page in the appended contract text.
        Includes a short snippet from the referenced page for context.
        """
        if not ref_text or ref_text == 'N/A':
            return ""

        # Extract page number from reference (e.g., "Page 3" or "Pages 3-4")
        page_match = re.search(r'[Pp]age[s]?\s*(\d+)', str(ref_text))
        if page_match:
            page_num = page_match.group(1)
            anchor_name = f"contract_page_{page_num}"
            clean_ref = self._clean_text(str(ref_text), max_length=100)

            # Extract a snippet from the referenced page if contract text is available
            snippet = ""
            if contract_text:
                # Find the page marker and extract text after it
                page_pattern = re.compile(rf'\[PAGE\s*{page_num}\](.*?)(?:\[PAGE\s*\d+\]|$)', re.IGNORECASE | re.DOTALL)
                match = page_pattern.search(contract_text)
                if match:
                    page_content = match.group(1).strip()
                    # Get first 80 chars as snippet, clean it up
                    if page_content:
                        snippet_text = page_content[:120].replace('\n', ' ').strip()
                        # Truncate at word boundary
                        if len(snippet_text) >= 80:
                            last_space = snippet_text[:80].rfind(' ')
                            if last_space > 40:
                                snippet_text = snippet_text[:last_space]
                        snippet = self._clean_text(snippet_text, max_length=80)

            # Build the clickable reference with optional snippet
            if snippet:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a> <font size="8" color="gray">["{snippet}..."]</font>'
            else:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a>'
        else:
            # No page number found, just return plain ref
            clean_ref = self._clean_text(str(ref_text), max_length=100)
            return f"<i>(Ref: {clean_ref})</i>"

    def _format_value_for_pdf(self, value: Any, indent: int = 0) -> str:
        """Format a value (potentially nested dict/list) into readable text for PDF."""
        if value is None:
            return "N/A"

        if isinstance(value, str):
            return self._clean_text(value, max_length=None)

        if isinstance(value, (int, float, bool)):
            return str(value)

        if isinstance(value, list):
            if not value:
                return "None"
            # For simple lists, join with commas
            if all(isinstance(item, str) for item in value):
                return ", ".join(str(item) for item in value[:5])  # Limit to 5 items
            # For complex lists, format each item
            parts = []
            for item in value[:5]:
                parts.append(self._format_value_for_pdf(item, indent + 1))
            return "; ".join(parts)

        if isinstance(value, dict):
            # Format dict as readable key-value pairs
            parts = []
            for k, v in value.items():
                # Clean up key name (replace underscores, capitalize)
                key_name = k.replace('_', ' ').title()
                formatted_value = self._format_value_for_pdf(v, indent + 1)
                if formatted_value and formatted_value != "N/A":
                    parts.append(f"{key_name}: {formatted_value}")
            return "; ".join(parts) if parts else "N/A"

        return str(value)

    def _extract_text_from_pdf(self, content: bytes) -> str:
        """Extract text from PDF content using pypdf or PyPDF2.

        Includes clear page markers for document reference tracking.
        """
        if not PDF_SUPPORT or pypdf_module is None:
            return "[ERROR: PDF library not available. Install with: pip install pypdf]"

        try:
            pdf_file = io.BytesIO(content)
            pdf_reader = pypdf_module.PdfReader(pdf_file)

            text_parts = []
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    # Clear page markers for AI to reference
                    text_parts.append(f"[PAGE {page_num + 1}]\n{page_text}\n[END PAGE {page_num + 1}]")

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"PDF extraction error: {e}")
            return f"[ERROR: Failed to extract PDF text: {e}]"

    def _extract_text_from_docx(self, content: bytes) -> str:
        """Extract text from DOCX content."""
        if not DOCX_SUPPORT or DocxDocument is None:
            return "[ERROR: python-docx not available. Install with: pip install python-docx]"

        try:
            doc_file = io.BytesIO(content)
            doc = DocxDocument(doc_file)

            text_parts = []
            for para in doc.paragraphs:
                if para.text.strip():
                    text_parts.append(para.text)

            # Also extract tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells)
                    if row_text.strip():
                        text_parts.append(row_text)

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"DOCX extraction error: {e}")
            return f"[ERROR: Failed to extract DOCX text: {e}]"

    def _extract_text(self, file_path: str, content: bytes) -> str:
        """Extract text based on file extension."""
        ext = file_path.lower().split('.')[-1]

        if ext == 'pdf':
            return self._extract_text_from_pdf(content)
        elif ext in ['docx', 'doc']:
            return self._extract_text_from_docx(content)
        elif ext == 'txt':
            return content.decode('utf-8', errors='ignore')
        else:
            return f"[ERROR: Unsupported file format: {ext}. Supported: pdf, docx, txt]"

    def _extract_json_from_response(self, response: str) -> Dict:
        """Extract JSON from AI response, handling various formats."""
        if not response:
            logging.error("_extract_json_from_response: Empty response received")
            return {"parse_error": True, "raw_analysis": response, "error_type": "empty_response"}

        # Clean up common issues in AI responses
        cleaned_response = response.strip()

        # Remove control characters that can break JSON parsing
        cleaned_response = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', cleaned_response)

        # Check for truncated JSON (common when hitting token limits)
        # If it starts with { but doesn't end with }, try to repair it
        if cleaned_response.startswith('{') and not cleaned_response.rstrip().endswith('}'):
            logging.warning("_extract_json_from_response: Detected possibly truncated JSON, attempting repair...")
            # Try to find the last complete key-value pair and close the JSON
            repaired = self._repair_truncated_json(cleaned_response)
            if repaired:
                try:
                    result = json.loads(repaired)
                    logging.info(f"_extract_json_from_response: Parsed from repaired truncated JSON, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Repaired JSON still invalid: {e}")

        # Try 1: Look for ```json code block
        json_match = re.search(r'```json\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if json_match:
            try:
                result = json.loads(json_match.group(1))
                logging.info(f"_extract_json_from_response: Parsed from ```json block, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                logging.warning(f"_extract_json_from_response: Failed to parse ```json block: {e}")

        # Try 2: Look for ``` code block without json tag
        code_match = re.search(r'```\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if code_match:
            code_content = code_match.group(1).strip()
            if code_content.startswith('{'):
                try:
                    result = json.loads(code_content)
                    logging.info(f"_extract_json_from_response: Parsed from ``` block, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Failed to parse ``` block: {e}")

        # Try 3: Look for first { to last } (the JSON object)
        first_brace = cleaned_response.find('{')
        last_brace = cleaned_response.rfind('}')
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_str = cleaned_response[first_brace:last_brace + 1]
            try:
                result = json.loads(json_str)
                logging.info(f"_extract_json_from_response: Parsed from braces, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                # Try to fix common JSON issues
                logging.warning(f"_extract_json_from_response: Initial brace parse failed: {e}")

                # Apply multiple fixes in sequence
                fixed_json = json_str

                # Fix 1: Remove trailing commas before ] or }
                fixed_json = re.sub(r',\s*([}\]])', r'\1', fixed_json)

                # Fix 2: Fix missing commas between } and { or ] and [
                fixed_json = re.sub(r'}\s*{', '},{', fixed_json)
                fixed_json = re.sub(r']\s*\[', '],[', fixed_json)

                # Fix 3: Fix missing commas between } and "
                fixed_json = re.sub(r'}\s*"', '},"', fixed_json)
                fixed_json = re.sub(r']\s*"', '],"', fixed_json)

                # Fix 4: Fix newlines inside strings (convert to spaces)
                # This is tricky - need to only fix inside strings
                # For now, just remove literal newlines that aren't escaped
                fixed_json = re.sub(r'(?<!\\)\n', ' ', fixed_json)

                try:
                    result = json.loads(fixed_json)
                    logging.info(f"_extract_json_from_response: Parsed after JSON fixes, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e2:
                    logging.warning(f"_extract_json_from_response: JSON fixes didn't help: {e2}")

                # Try to find and fix the specific position of the error
                try:
                    # Sometimes the AI includes extra text after the JSON
                    # Try parsing incrementally to find where valid JSON ends
                    for end_pos in range(last_brace, first_brace, -1):
                        if cleaned_response[end_pos] == '}':
                            try:
                                result = json.loads(cleaned_response[first_brace:end_pos + 1])
                                logging.info(f"_extract_json_from_response: Parsed with truncated end, keys: {list(result.keys())}")
                                return result
                            except json.JSONDecodeError:
                                continue
                except Exception:
                    pass

        # Try 4: Direct parse (if entire response is JSON)
        try:
            result = json.loads(cleaned_response)
            logging.info(f"_extract_json_from_response: Parsed directly, keys: {list(result.keys())}")
            return result
        except json.JSONDecodeError as e:
            logging.warning(f"_extract_json_from_response: Direct parse failed: {e}")

        # Failed to parse - log detailed error info
        logging.error(f"_extract_json_from_response: ALL PARSE ATTEMPTS FAILED")
        logging.error(f"Response length: {len(response)}")
        logging.error(f"Response starts with: {response[:200]}")
        logging.error(f"Response ends with: {response[-200:] if len(response) > 200 else response}")

        return {"parse_error": True, "raw_analysis": response, "error_type": "json_parse_failed"}

    def _repair_truncated_json(self, json_str: str) -> Optional[str]:
        """Attempt to repair truncated JSON by closing unclosed brackets/braces."""
        try:
            # Track the nesting level
            stack = []
            in_string = False
            escape_next = False
            last_complete_pos = 0

            for i, char in enumerate(json_str):
                if escape_next:
                    escape_next = False
                    continue

                if char == '\\' and in_string:
                    escape_next = True
                    continue

                if char == '"' and not escape_next:
                    in_string = not in_string
                    continue

                if in_string:
                    continue

                if char == '{':
                    stack.append('}')
                elif char == '[':
                    stack.append(']')
                elif char in '}]':
                    if stack and stack[-1] == char:
                        stack.pop()
                        last_complete_pos = i + 1

                # Track positions after complete key-value pairs
                if char == ',' and not in_string:
                    last_complete_pos = i + 1

            # If we're still in a string, try to close it
            if in_string:
                json_str = json_str + '"'

            # Find the last complete structure and close everything
            # Try to truncate at the last comma and close
            if stack:
                # Find last comma outside of string
                truncate_pos = json_str.rfind(',')
                if truncate_pos > 0:
                    # Truncate at last comma and close all open brackets
                    repaired = json_str[:truncate_pos]
                    repaired += ''.join(reversed(stack))
                    return repaired
                else:
                    # Just close all open brackets
                    return json_str + ''.join(reversed(stack))

            return json_str

        except Exception as e:
            logging.warning(f"_repair_truncated_json failed: {e}")
            return None

    def _call_openai(self, system_prompt: str, user_prompt: str, max_tokens: int = 4000) -> str:
        """Call Azure OpenAI with the given prompts. Handles model-specific parameter differences."""
        if not self.openai_client:
            return "[ERROR: OpenAI client not initialized]"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Try different parameter combinations for model compatibility
        # gpt-5.x models may not support temperature or max_tokens
        param_combinations = [
            # Try minimal params first (most compatible with newer models)
            {"model": self.deployment_name, "messages": messages, "max_completion_tokens": max_tokens},
            # Try with max_tokens instead
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens},
            # Try with temperature for older models
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens, "temperature": 0.3},
        ]

        last_error = None
        for params in param_combinations:
            try:
                response = self.openai_client.chat.completions.create(**params)
                return response.choices[0].message.content
            except Exception as e:
                error_msg = str(e).lower()
                # If it's a parameter compatibility error, try next combination
                if "unsupported" in error_msg or "not supported" in error_msg:
                    logging.info(f"Parameter compatibility issue, trying next combination: {e}")
                    last_error = e
                    continue
                # For other errors, fail immediately
                logging.error(f"OpenAI call failed: {e}")
                return f"[ERROR: OpenAI analysis failed: {e}]"

        # All combinations failed
        logging.error(f"All parameter combinations failed. Last error: {last_error}")
        return f"[ERROR: OpenAI analysis failed after trying multiple parameter combinations: {last_error}]"

    def _chunk_text(self, text: str, max_chars: int = 30000) -> List[str]:
        """Split text into chunks for processing large documents."""
        if len(text) <= max_chars:
            return [text]

        chunks = []
        current_chunk = ""

        # Split by paragraphs to maintain context
        paragraphs = text.split('\n\n')

        for para in paragraphs:
            if len(current_chunk) + len(para) < max_chars:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _analyze_full_contract(self, text: str, file_name: str) -> Dict:
        """Perform comprehensive contract analysis from LABEL perspective."""
        system_prompt = """You are an expert contract analyst working for a MAJOR RECORD LABEL (Label perspective).
Your job is to analyze contracts and assess them from the LABEL'S business interests.

This is a BUSINESS ANALYSIS tool for internal use. You are analyzing an ACTUAL contract document.
The document text includes [PAGE N] markers showing where each page begins - use these for references.

Analyze the provided contract and extract structured information.
IMPORTANT: All assessments should be from the LABEL's perspective - what benefits the label, what risks the label faces.

REFERENCE FORMAT: Use the [PAGE N] markers in the text to identify page numbers.
- If you see content after "[PAGE 3]", reference it as "Page 3"
- If the document has visible section/article numbers, include them: "Page 3, Section 4.1"
- If no section numbers are visible, just use the page: "Page 3"
- References help readers locate content but don't need to be formal citations

Return your analysis as a valid JSON object with the following structure:
{
    "contract_type": "type of contract (e.g., Recording Agreement, Licensing Deal, Service Agreement)",
    "parties": [{"name": "party name", "role": "role in contract (Label/Artist/Licensor/etc)", "ref": "Page X"}],
    "effective_date": {"value": "date or null if not found", "ref": "Page X"},
    "term_duration": {"value": "duration description", "ref": "Page X, Section Y"},
    "financial_terms": {
        "advances": {"value": "amount or null", "ref": "Page X, Section Y"},
        "royalty_rates": {"value": "rates description", "ref": "Page X, Section Y"},
        "payment_schedule": {"value": "description or null", "ref": "Page X"},
        "label_investment": {"value": "total label financial commitment", "ref": "Page X"},
        "recoupment_terms": {"value": "how label recoups investment", "ref": "Page X, Section Y"},
        "other_payments": [{"description": "...", "ref": "Page X"}]
    },
    "rights_secured": [{"right": "description", "scope": "scope/territory", "exclusivity": true/false, "duration": "how long label holds rights", "ref": "Page X, Section Y"}],
    "label_protections": [{"clause": "protection description", "ref": "Page X, Section Y"}],
    "artist_obligations": [{"obligation": "what artist must do", "deadline": "when", "consequence_if_breached": "label remedy", "ref": "Page X, Section Y"}],
    "label_obligations": [{"obligation": "what label must do", "financial_impact": "cost to label", "ref": "Page X, Section Y"}],
    "termination_clauses": [{"trigger": "what triggers termination", "who_can_trigger": "label/artist/either", "label_impact": "effect on label", "ref": "Page X, Section Y"}],
    "key_dates": [{"event": "description", "date": "date or relative timing", "ref": "Page X"}],
    "artist_favorable_terms": [{"term": "term that favors artist MORE than industry standard", "concern": "why this is a concern for label", "ref": "Page X, Section Y"}],
    "missing_label_protections": ["standard label protections that appear to be missing"],
    "overall_assessment": "2-3 sentence assessment from LABEL's perspective - is this deal favorable to the label?"
}

Be thorough but concise. Extract actual values from the contract text.
Remember: You work for the LABEL. Artist-favorable terms are potential concerns.
ALWAYS include page/section references for every finding.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just analyze and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with analysis
4. Do NOT mention length limits or offer to split output - just output the JSON
5. Start your response with { and end with } - nothing else
6. If information is missing, use null or "Not specified" - do not ask about it

Your response must be valid JSON starting with { and ending with }."""

        # Handle large documents by chunking
        chunks = self._chunk_text(text)

        if len(chunks) == 1:
            user_prompt = f"Analyze this contract:\n\n{text}"
            # Use larger max_tokens for full contract analysis to accommodate detailed JSON
            response = self._call_openai(system_prompt, user_prompt, max_tokens=16000)
        else:
            # For large documents, analyze chunks and synthesize
            chunk_analyses = []
            for i, chunk in enumerate(chunks):
                user_prompt = f"Analyze this section (Part {i+1} of {len(chunks)}) of a contract:\n\n{chunk}"
                chunk_response = self._call_openai(system_prompt, user_prompt, max_tokens=2000)
                chunk_analyses.append(chunk_response)

            # Synthesize the chunks
            synthesis_prompt = """You are synthesizing multiple partial analyses of a single contract.
Combine these analyses into one comprehensive JSON structure, removing duplicates and resolving any conflicts.

CRITICAL: Output ONLY valid JSON. Start with { and end with }. No other text.
Do NOT ask questions. Do NOT offer options. Just output the combined JSON immediately."""

            user_prompt = f"Combine these partial contract analyses:\n\n" + "\n\n---\n\n".join(chunk_analyses)
            response = self._call_openai(synthesis_prompt, user_prompt)

        # Parse the JSON response with retry logic for empty results
        essential_keys = ['contract_type', 'parties', 'rights_secured', 'financial_terms']
        max_retries = 3

        for attempt in range(max_retries):
            analysis = self._extract_json_from_response(response)

            # Check if analysis has essential keys (not just empty or error)
            has_essential_data = any(
                key in analysis and analysis[key]
                for key in essential_keys
            )

            if has_essential_data or analysis.get('parse_error'):
                # Either we got good data or a clear error - don't retry
                break

            if attempt < max_retries - 1:
                logging.warning(f"Full analysis returned empty (attempt {attempt + 1}/{max_retries}). Retrying...")
                # Retry with more forceful prompt
                retry_prompt = f"""IMPORTANT: Your previous response was empty or incomplete.
You MUST output a complete JSON object with contract analysis.

Analyze this contract NOW and output ONLY the JSON (start with {{ end with }}):

{text[:40000]}"""
                response = self._call_openai(system_prompt, retry_prompt, max_tokens=16000)

        # DEBUG: Enhanced logging for analysis result
        logging.info("=" * 40)
        logging.info("_analyze_full_contract - RESULT ANALYSIS")
        logging.info(f"Full analysis completed with keys: {list(analysis.keys())}")
        logging.info(f"Raw response length: {len(response) if response else 0}")
        logging.info(f"Raw response preview: {response[:500] if response else 'None'}")

        if analysis.get('parse_error'):
            logging.error(f"_analyze_full_contract - JSON PARSE FAILED!")
            logging.error(f"Raw analysis: {analysis.get('raw_analysis', '')[:1000]}")

        # Log specific key values
        logging.info(f"  - contract_type: {analysis.get('contract_type', 'MISSING')}")
        logging.info(f"  - parties: {len(analysis.get('parties', []))} found")
        logging.info(f"  - financial_terms: {type(analysis.get('financial_terms')).__name__}")
        logging.info(f"  - rights_secured: {len(analysis.get('rights_secured', []))} found")

        if not any(key in analysis for key in essential_keys):
            logging.warning(f"Analysis may be incomplete - no essential keys found!")
        logging.info("=" * 40)

        analysis["_metadata"] = {
            "file_name": file_name,
            "analyzed_at": datetime.now().isoformat(),
            "text_length": len(text),
            "chunks_processed": len(chunks),
            "retry_attempts": attempt + 1
        }
        return analysis

    def _extract_specific_clauses(self, text: str, clause_types: List[str]) -> Dict:
        """Extract specific types of clauses from the contract."""
        clause_descriptions = {
            "financial": "All financial terms including advances, royalties, payments, fees, revenue sharing, expenses",
            "rights": "All rights granted or reserved including intellectual property, licensing, usage rights, exclusivity",
            "obligations": "All obligations and duties of each party, deliverables, performance requirements",
            "termination": "Termination conditions, notice periods, breach definitions, consequences of termination",
            "exclusivity": "Exclusivity clauses, non-compete provisions, first refusal rights",
            "territory": "Geographic scope, territory definitions, regional limitations",
            "duration": "Term length, renewal options, extension conditions, effective dates"
        }

        types_to_extract = [ct for ct in clause_types if ct in clause_descriptions]
        if not types_to_extract:
            types_to_extract = list(clause_descriptions.keys())

        extraction_details = "\n".join([f"- {ct}: {clause_descriptions[ct]}" for ct in types_to_extract])

        system_prompt = f"""You are a contract clause extraction specialist.
Extract the following types of clauses from the contract:

{extraction_details}

CRITICAL: For EVERY clause extracted, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Return a JSON object where each key is a clause type and the value is an array of extracted clauses.
Each clause should have: "text" (the clause text or summary - keep under 200 words), "ref" (Page X, Section Y), "key_points" (2-3 bullet points).

Example format:
{{
    "financial": [
        {{"text": "...", "ref": "Page 3, Section 4.1", "key_points": ["Advance of $X", "Royalty rate of Y%"]}}
    ]
}}

ALWAYS include page and section references for every extracted clause.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just extract and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with extraction
4. Do NOT mention length limits or offer to split output - output the JSON directly
5. Start your response with {{ and end with }} - nothing else
6. If a clause type has no matches, use an empty array: "type": []
7. Keep each clause summary under 200 words - summarize if needed
8. Extract UP TO 3-5 most important clauses per category (prioritize key terms)

Your response must be valid JSON starting with {{ and ending with }}."""

        # For large documents, process only the most relevant text
        text_to_process = text[:35000]  # Reduced limit for better processing

        user_prompt = f"Extract clauses from this contract. Output ONLY valid JSON:\n\n{text_to_process}"
        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)

        # Add logging for debugging
        logging.info(f"_extract_specific_clauses - Response length: {len(response) if response else 0}")

        result = self._extract_json_from_response(response)

        # If parse failed, try with retry
        if result.get('parse_error'):
            logging.warning("_extract_specific_clauses - Initial parse failed, retrying...")
            retry_prompt = f"""IMPORTANT: Output ONLY valid JSON. No other text. Start with {{ end with }}.

Extract clauses from this contract into JSON format:
{text_to_process[:25000]}"""
            response = self._call_openai(system_prompt, retry_prompt, max_tokens=6000)
            result = self._extract_json_from_response(response)

        return result

    def _generate_summary(self, text: str, summary_type: str, audience: str) -> Dict:
        """Generate a summary tailored to the audience - FROM LABEL PERSPECTIVE."""
        audience_instructions = {
            "legal": "Use precise legal terminology. Include specific clause references. Highlight legal risks to the LABEL and compliance considerations.",
            "business": "Focus on commercial terms and business implications FOR THE LABEL. Emphasize label ROI, recoupment timeline, and operational impacts to the label.",
            "executive": "Provide a high-level overview for LABEL C-suite. Focus on label investment, rights secured, strategic value, and key risks to the label. Keep it concise."
        }

        length_instructions = {
            "executive": "Provide a brief 150-200 word summary with key bullet points.",
            "detailed": "Provide a comprehensive 400-500 word summary covering all major aspects.",
            "legal": "Provide a thorough legal summary of 300-400 words with specific clause references."
        }

        system_prompt = f"""You are a contract summarization expert working for a MAJOR RECORD LABEL.
Your summaries are FOR LABEL EXECUTIVES and should reflect the LABEL's interests and perspective.

{audience_instructions.get(audience, audience_instructions['business'])}
{length_instructions.get(summary_type, length_instructions['detailed'])}

IMPORTANT: Frame everything from the label's business perspective:
- "Label investment" instead of "artist advance"
- "Rights secured by label" instead of "rights granted"
- "Artist-favorable terms" = potential concerns for the label
- Risk assessment = risks TO THE LABEL

CRITICAL: Include document references (Page X, Section Y) for key claims.
The document text includes [PAGE N] markers - use these for exact page numbers.

CRITICAL: The recommendation MUST align with the risk level:
- LOW risk: "Proceed" or "Proceed as drafted"
- MEDIUM risk: "Proceed with caution; consider negotiating [specific terms]"
- HIGH risk: "Do not proceed without changes to [specific critical terms]" or "Renegotiate [specific issues] before proceeding"

Return a JSON object with:
{{
    "summary": "the main summary text FROM LABEL PERSPECTIVE",
    "key_points": [{{"point": "bullet point text", "ref": "Page X, Section Y"}}],
    "label_investment_total": {{"value": "total financial commitment from label", "ref": "Page X"}},
    "rights_secured": {{"value": "summary of rights label obtains", "ref": "Page X, Section Y"}},
    "critical_dates": [{{"event": "...", "date": "...", "ref": "Page X"}}],
    "action_items": ["any actions needed by label team"],
    "risk_level": "low/medium/high (risk TO THE LABEL)",
    "artist_leverage_concerns": [{{"concern": "term giving artist unusual leverage", "ref": "Page X, Section Y"}}],
    "recommendation": "recommendation aligned with risk level - if HIGH risk, must specify required changes before proceeding"
}}

ALWAYS include page/section references for key findings.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the summary and return the JSON."""

        user_prompt = f"Summarize this contract for a {audience} audience:\n\n{text[:40000]}"
        response = self._call_openai(system_prompt, user_prompt)
        return self._extract_json_from_response(response)

    def _identify_risks(self, text: str) -> Dict:
        """Identify risks TO THE LABEL and deviations from standard terms."""
        system_prompt = """You are a contract risk analyst working for a MAJOR RECORD LABEL.
Your job is to identify risks TO THE LABEL, not to the artist.

IMPORTANT PERSPECTIVE:
- Artist-favorable terms = RISKS to the label (higher costs, less control, early reversion)
- High advances/royalties = FINANCIAL RISK to label
- Strong artist termination rights = OPERATIONAL RISK to label
- Early master reversion = ASSET RISK to label
- Creative control for artist = COMMERCIAL RISK to label
- Non-recoupable payments = DIRECT COST to label

CRITICAL: For EVERY risk identified, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Analyze the contract for RISKS TO THE LABEL:
1. Financial exposure (high advances, guaranteed payments, non-recoupable costs)
2. Asset risks (early master reversion, limited rights duration, territory restrictions)
3. Operational risks (artist approval requirements, key man clauses, delivery delays)
4. Revenue risks (high royalty rates, favorable streaming splits, limited 360 participation)
5. Legal/compliance risks (regulatory, indemnification gaps)
6. Competitive risks (artist leverage, termination options)

Return a JSON object:
{
    "overall_risk_level": "low/medium/high (RISK TO LABEL)",
    "risk_score": 1-100 (higher = worse for label),
    "label_financial_exposure": "total potential label investment/loss",
    "risks": [
        {
            "category": "financial/asset/operational/revenue/legal/competitive",
            "severity": "low/medium/high/critical",
            "description": "what the risk TO THE LABEL is",
            "ref": "Page X, Section Y",
            "label_impact": "specific impact on label operations/finances",
            "recommendation": "how label should address this in negotiation"
        }
    ],
    "artist_favorable_terms": [
        {"term": "what favors the artist", "industry_standard": "what's typical", "label_impact": "why this hurts the label", "ref": "Page X, Section Y"}
    ],
    "missing_label_protections": ["standard label protections not found in this contract"],
    "negotiation_priorities": [{"priority": "item label should push back on", "ref": "Page X, Section Y"}],
    "deal_breakers": [{"issue": "term that may be unacceptable", "ref": "Page X, Section Y"}],
    "summary": "2-3 sentence risk summary FROM LABEL'S PERSPECTIVE"
}

ALWAYS cite the specific page and section for every risk and concern.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the analysis and return the JSON."""

        user_prompt = f"Analyze risks in this contract:\n\n{text[:50000]}"
        response = self._call_openai(system_prompt, user_prompt)

        # DEBUG: Log the raw response before parsing
        logging.info(f"_identify_risks - Raw response length: {len(response) if response else 0}")
        logging.info(f"_identify_risks - Raw response preview: {response[:1000] if response else 'EMPTY'}")

        result = self._extract_json_from_response(response)

        # DEBUG: Log the parsed result
        logging.info(f"_identify_risks - Parsed result keys: {list(result.keys()) if isinstance(result, dict) else 'NOT DICT'}")
        if isinstance(result, dict) and result.get('parse_error'):
            logging.error(f"_identify_risks - JSON PARSE FAILED!")

        return result

    def _compare_contracts(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare two contracts using sectioned analysis for better coverage."""

        # For any substantial contracts, use sectioned comparison to avoid truncation
        # Sectioned mode analyzes each area (financial, rights, etc.) separately
        # This provides better coverage and avoids the model refusing due to incomplete text
        total_length = len(text_a) + len(text_b)
        max_single_contract = max(len(text_a), len(text_b))

        # Use sectioned mode if total > 30k OR if either contract alone is > 20k
        # This ensures we don't truncate important contract content
        use_sectioned = total_length > 30000 or max_single_contract > 20000

        if use_sectioned:
            return self._compare_contracts_sectioned(text_a, text_b, name_a, name_b)

        system_prompt = """You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
This is a BUSINESS ANALYSIS exercise for training purposes, NOT legal advice.

Your task: Compare these two contracts and identify factual differences in their terms.
Analyze which contract has more favorable terms from a BUSINESS perspective (lower financial commitments, stronger protections, better rights retention).

When comparing terms, note which contract (A or B) has:
- Lower advance/payment obligations
- Longer rights retention periods
- Broader territorial coverage
- More comprehensive protections
- Clearer deliverable requirements

CRITICAL: Include document references for BOTH contracts in the format:
- "ref_a": "Page X, Section Y" (for Contract A)
- "ref_b": "Page X, Section Y" (for Contract B)
The document text includes [PAGE N] markers - use these for exact page numbers.

Compare these two contracts and identify:
1. Key differences in financial terms, rights, obligations
2. Which contract has more protective clauses (from a business standpoint)
3. Which contract has higher financial exposure
4. Notable terms that differ significantly between the two

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which contract has more protective business terms)",
    "key_differences": [
        {
            "aspect": "what's being compared",
            "contract_a": "terms in first contract",
            "contract_b": "terms in second contract",
            "ref_a": "Page X, Section Y",
            "ref_b": "Page X, Section Y",
            "label_preference": "a/b (which has stronger business protections)",
            "label_impact": "business significance of this difference"
        }
    ],
    "unique_to_a": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "unique_to_b": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "financial_comparison": {
        "contract_a": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "contract_b": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high (financial/operational risk level)",
        "contract_b_risk_level": "low/medium/high (financial/operational risk level)",
        "lower_label_risk": "a/b"
    },
    "overall_assessment": "factual summary of which contract has more favorable business terms and key differences",
    "recommended_standard_terms": ["notable terms from either contract worth considering"]
}

ALWAYS include page/section references from both contracts for every comparison point.

IMPORTANT: This is an educational analysis. Provide factual comparisons. Do NOT ask clarifying questions. Just execute the comparison and return the JSON."""

        user_prompt = f"""Compare these two contracts:

=== CONTRACT A: {name_a} ===
{text_a[:30000]}

=== CONTRACT B: {name_b} ===
{text_b[:30000]}"""

        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)
        result = self._extract_json_from_response(response)
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "standard"
        }
        return result

    def _compare_contracts_sectioned(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare large contracts by analyzing sections separately then synthesizing."""
        logging.info(f"Using sectioned comparison for large contracts: {name_a} vs {name_b}")

        # Define comparison sections
        sections = {
            "financial": {
                "focus": "advances, royalties, recoupment, payment schedules, 360 terms, merchandise, touring splits",
                "analysis_criteria": "Compare total financial commitments, royalty rates, recoupment structures"
            },
            "rights": {
                "focus": "master ownership, duration of rights, territory, exclusivity, reversion triggers, publishing",
                "analysis_criteria": "Compare scope and duration of rights granted, territorial coverage, reversion terms"
            },
            "obligations": {
                "focus": "delivery requirements, album commitments, promotional obligations, key man clauses",
                "analysis_criteria": "Compare deliverable requirements, commitment levels, operational obligations"
            },
            "termination_risk": {
                "focus": "termination triggers, exit clauses, breach remedies, force majeure, key man provisions",
                "analysis_criteria": "Compare termination conditions, exit mechanisms, breach remedies"
            }
        }

        section_results = {}

        for section_name, section_info in sections.items():
            section_prompt = f"""You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
Focus ONLY on {section_name.upper()} terms in these two contracts.

FOCUS AREAS: {section_info['focus']}
ANALYSIS CRITERIA: {section_info['analysis_criteria']}

Extract and compare {section_name} terms from both contracts factually.

Return a JSON object with this EXACT structure:
{{
    "section": "{section_name}",
    "contract_a_terms": {{
        "summary": "brief summary of {section_name} terms in Contract A",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "contract_b_terms": {{
        "summary": "brief summary of {section_name} terms in Contract B",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "differences": [
        {{
            "aspect": "specific term being compared",
            "contract_a": "value/term in A",
            "contract_b": "value/term in B",
            "label_preference": "a/b/neutral (which has more favorable business terms)",
            "reason": "factual explanation of the difference"
        }}
    ],
    "section_winner": "a/b/neutral (which contract has more favorable terms in this section)",
    "section_assessment": "1-2 sentence factual assessment of key differences"
}}

IMPORTANT: This is educational analysis. Do NOT ask questions. Just analyze and return the JSON."""

            user_prompt = f"""Compare {section_name.upper()} terms:

=== CONTRACT A: {name_a} ===
{text_a[:50000]}

=== CONTRACT B: {name_b} ===
{text_b[:50000]}"""

            response = self._call_openai(section_prompt, user_prompt, max_tokens=3000)
            section_results[section_name] = self._extract_json_from_response(response)

        # Synthesize all section results into final comparison
        synthesis_prompt = """You are an educational contract analysis assistant synthesizing sectioned comparison results.

Based on the section-by-section analysis provided, create a comprehensive factual comparison summary.

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which has more favorable business terms overall)",
    "section_winners": {
        "financial": "a/b/neutral",
        "rights": "a/b/neutral",
        "obligations": "a/b/neutral",
        "termination_risk": "a/b/neutral"
    },
    "key_differences": [
        {
            "aspect": "term being compared",
            "contract_a": "value in A",
            "contract_b": "value in B",
            "label_preference": "a/b (which has more favorable terms)",
            "label_impact": "business significance of this difference"
        }
    ],
    "financial_comparison": {
        "contract_a": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "contract_b": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high",
        "contract_b_risk_level": "low/medium/high",
        "lower_label_risk": "a/b"
    },
    "deal_breakers": [{"contract": "a/b", "issue": "notable concern"}],
    "overall_assessment": "2-3 sentence factual summary of key differences between the contracts",
    "recommended_standard_terms": ["notable terms from either contract"]
}

IMPORTANT: This is educational analysis. Provide factual comparisons only."""

        synthesis_user = f"""Synthesize these section comparisons:

{json.dumps(section_results, indent=2, default=str)}

Contract A: {name_a}
Contract B: {name_b}"""

        synthesis_response = self._call_openai(synthesis_prompt, synthesis_user, max_tokens=4000)
        result = self._extract_json_from_response(synthesis_response)

        # Add section details and metadata
        result["_section_details"] = section_results
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "sectioned",
            "sections_analyzed": list(sections.keys())
        }

        return result

    def perform(self, **kwargs) -> str:
        """Execute contract analysis action."""
        try:
            action = kwargs.get('action', 'list_contracts')
            contract_name = kwargs.get('contract_name')
            contract_name_b = kwargs.get('contract_name_b')
            clause_types = kwargs.get('clause_types', [])
            summary_type = kwargs.get('summary_type', 'detailed')
            audience = kwargs.get('audience', 'business')

            # List contracts
            if action == 'list_contracts':
                files = self._list_files_in_folder()
                return json.dumps({
                    "status": "success",
                    "action": "list_contracts",
                    "contracts_folder": self.contracts_folder,
                    "files": files,
                    "count": len(files),
                    "supported_formats": ["pdf", "docx", "txt"],
                    "usage": "Use contract_name parameter with the file name to analyze"
                }, indent=2)

            # All other actions require a contract name
            if not contract_name:
                return json.dumps({
                    "status": "error",
                    "message": "contract_name is required for this action",
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Read the contract
            file_path = f"{self.contracts_folder}/{contract_name}"
            content = self._read_file_content(file_path)

            if not content:
                return json.dumps({
                    "status": "error",
                    "message": f"Could not read contract: {contract_name}",
                    "path_tried": file_path,
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Extract text
            text = self._extract_text(file_path, content)
            if text.startswith("[ERROR"):
                return json.dumps({
                    "status": "error",
                    "message": text
                }, indent=2)

            # Execute the requested action
            if action == 'full_workup':
                # Comprehensive analysis: runs everything in one go
                logging.info(f"Running full workup on {contract_name}")

                # 1. Full contract analysis
                analysis = self._analyze_full_contract(text, contract_name)

                # 2. Risk identification (run first - this is the authoritative risk source)
                risks = self._identify_risks(text)

                # 3. Executive summary for business audience
                summary = self._generate_summary(text, 'executive', 'business')

                # 4. Extract key clauses (all types)
                all_clause_types = ['financial', 'rights', 'obligations', 'termination', 'exclusivity', 'territory', 'duration']
                clauses = self._extract_specific_clauses(text, all_clause_types)

                # Synchronize risk levels - use risk assessment as authoritative source
                # This ensures consistency throughout the PDF report
                authoritative_risk_level = risks.get('overall_risk_level', 'unknown')
                authoritative_risk_score = risks.get('risk_score', 'N/A')
                if isinstance(summary, dict):
                    summary['risk_level'] = authoritative_risk_level
                    summary['risk_score'] = authoritative_risk_score

                # Compile full report (include contract text for PDF with clickable references)
                full_report = {
                    "contract": contract_name,
                    "analyzed_at": datetime.now().isoformat(),
                    "executive_summary": summary,
                    "full_analysis": analysis,
                    "risk_assessment": risks,
                    "extracted_clauses": clauses,
                    "text_length": len(text),
                    "_contract_text": text  # Include for PDF generation with clickable refs
                }

                # Save the analysis report to Azure storage
                save_result = self._save_analysis_report(contract_name, full_report)

                # Build concise chat response (fits on one screen)
                risk_level = risks.get('overall_risk_level', 'Unknown').upper()
                risk_score = risks.get('risk_score', 'N/A')
                risk_summary = risks.get('summary', '')

                # Get top 3 risks with references
                top_risks = []
                for r in risks.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:80]
                        severity = r.get('severity', '').upper()
                        top_risks.append(f"- [{severity}] {desc} (Ref: {ref})")

                # Get key financial terms with references
                fin_terms = analysis.get('financial_terms', {})
                advances = fin_terms.get('advances', {})
                adv_val = advances.get('value', 'N/A') if isinstance(advances, dict) else advances
                adv_ref = advances.get('ref', '') if isinstance(advances, dict) else ''

                royalties = fin_terms.get('royalty_rates', {})
                roy_val = royalties.get('value', 'N/A') if isinstance(royalties, dict) else royalties
                roy_ref = royalties.get('ref', '') if isinstance(royalties, dict) else ''

                # Build the chat summary (short, fits one screen)
                chat_summary = {
                    "headline": f"Analysis Complete: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "key_findings": [
                        f"Advance: {adv_val}" + (f" (Ref: {adv_ref})" if adv_ref else ""),
                        f"Royalty: {roy_val}" + (f" (Ref: {roy_ref})" if roy_ref else ""),
                    ],
                    "top_risks": top_risks,
                    "recommendation": summary.get('recommendation', '') if isinstance(summary, dict) else '',
                    "full_report": {
                        "message": "Full analysis with all details saved to PDF report:",
                        "download_url": save_result.get('download_url', 'Report generation failed'),
                        "report_name": save_result.get('report_name', ''),
                        "size_kb": save_result.get('size_kb', 0)
                    }
                }

                return json.dumps({
                    "status": "success",
                    "action": "full_workup",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {
                        "executive_summary": summary,
                        "full_analysis": analysis,
                        "risk_assessment": risks,
                        "extracted_clauses": clauses,
                        "report_saved": save_result
                    },
                    "_metadata": {
                        "analyzed_at": datetime.now().isoformat(),
                        "file_name": contract_name,
                        "text_length": len(text)
                    }
                }, indent=2)

            elif action == 'analyze_contract':
                result = self._analyze_full_contract(text, contract_name)
                return json.dumps({
                    "status": "success",
                    "action": "analyze_contract",
                    "contract": contract_name,
                    "analysis": result
                }, indent=2)

            elif action == 'extract_clauses':
                result = self._extract_specific_clauses(text, clause_types)

                # Build concise chat summary
                clause_summary = []
                for clause_type, clauses in result.items():
                    if isinstance(clauses, list) and len(clauses) > 0:
                        # Get first clause of each type with its reference
                        first_clause = clauses[0]
                        if isinstance(first_clause, dict):
                            clause_summary.append({
                                "type": clause_type,
                                "count": len(clauses),
                                "sample": first_clause.get('text', '')[:100] + "..." if len(first_clause.get('text', '')) > 100 else first_clause.get('text', ''),
                                "ref": first_clause.get('ref', 'N/A')
                            })

                chat_summary = {
                    "headline": f"Clauses Extracted: {contract_name}",
                    "clause_types_found": list(result.keys()) if isinstance(result, dict) else [],
                    "summary": clause_summary
                }

                return json.dumps({
                    "status": "success",
                    "action": "extract_clauses",
                    "contract": contract_name,
                    "clause_types_requested": clause_types or "all",
                    "chat_response": chat_summary,
                    "_full_data": {"extractions": result}
                }, indent=2)

            elif action == 'summarize_contract':
                result = self._generate_summary(text, summary_type, audience)

                # Build concise chat response
                summary_text = result.get('summary', '') if isinstance(result, dict) else str(result)

                # Extract key points with refs
                key_points = []
                for pt in (result.get('key_points', []) if isinstance(result, dict) else [])[:4]:
                    if isinstance(pt, dict):
                        key_points.append({
                            "point": pt.get('point', ''),
                            "ref": pt.get('ref', 'N/A')
                        })
                    else:
                        key_points.append({"point": str(pt), "ref": "N/A"})

                chat_summary = {
                    "headline": f"Summary: {contract_name}",
                    "risk_level": result.get('risk_level', 'N/A') if isinstance(result, dict) else 'N/A',
                    "summary": summary_text[:300] + "..." if len(summary_text) > 300 else summary_text,
                    "key_points": key_points,
                    "recommendation": result.get('recommendation', '') if isinstance(result, dict) else ''
                }

                return json.dumps({
                    "status": "success",
                    "action": "summarize_contract",
                    "contract": contract_name,
                    "summary_type": summary_type,
                    "audience": audience,
                    "chat_response": chat_summary,
                    "_full_data": {"result": result}
                }, indent=2)

            elif action == 'identify_risks':
                result = self._identify_risks(text)

                # Build concise chat response
                risk_level = result.get('overall_risk_level', 'Unknown').upper()
                risk_score = result.get('risk_score', 'N/A')

                # Get top 3 risks with references
                top_risks = []
                for r in result.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:100]
                        severity = r.get('severity', '').upper()
                        top_risks.append({
                            "severity": severity,
                            "description": desc,
                            "ref": ref
                        })

                # Get deal breakers with references
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:2]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "issue": db.get('issue', ''),
                            "ref": db.get('ref', 'N/A')
                        })

                chat_summary = {
                    "headline": f"Risk Analysis: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "financial_exposure": result.get('label_financial_exposure', 'N/A'),
                    "top_risks": top_risks,
                    "deal_breakers": deal_breakers,
                    "summary": result.get('summary', '')
                }

                return json.dumps({
                    "status": "success",
                    "action": "identify_risks",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {"risk_analysis": result}
                }, indent=2)

            elif action == 'compare_contracts':
                if not contract_name_b:
                    return json.dumps({
                        "status": "error",
                        "message": "contract_name_b is required for comparison",
                        "available_contracts": self._list_files_in_folder()
                    }, indent=2)

                # Read second contract
                file_path_b = f"{self.contracts_folder}/{contract_name_b}"
                content_b = self._read_file_content(file_path_b)

                if not content_b:
                    return json.dumps({
                        "status": "error",
                        "message": f"Could not read second contract: {contract_name_b}"
                    }, indent=2)

                text_b = self._extract_text(file_path_b, content_b)
                result = self._compare_contracts(text, text_b, contract_name, contract_name_b)

                # Build concise chat response
                more_favorable = result.get('more_label_favorable', 'neutral')
                winner = contract_name if more_favorable == 'a' else (contract_name_b if more_favorable == 'b' else 'Neither')

                # Get comparison mode from metadata
                metadata = result.get('_metadata', {})
                comparison_mode = metadata.get('comparison_mode', 'standard')

                # Get top key differences with refs
                key_diffs = []
                for diff in result.get('key_differences', [])[:5]:
                    if isinstance(diff, dict):
                        key_diffs.append({
                            "aspect": diff.get('aspect', ''),
                            "contract_a": diff.get('contract_a', '')[:60],
                            "contract_b": diff.get('contract_b', '')[:60],
                            "preference": diff.get('label_preference', '').upper(),
                            "impact": diff.get('label_impact', '')[:100] if diff.get('label_impact') else ''
                        })

                # Financial comparison
                fin_comp = result.get('financial_comparison', {})
                financial_summary = {
                    "contract_a_investment": fin_comp.get('contract_a', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_investment": fin_comp.get('contract_b', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_b'), dict) else 'N/A',
                    "lower_cost": fin_comp.get('lower_label_cost', 'N/A'),
                    "better_margin": fin_comp.get('better_label_margin', 'N/A')
                }

                # Rights comparison
                rights_comp = result.get('rights_comparison', {})
                rights_summary = {
                    "contract_a_duration": rights_comp.get('contract_a', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_duration": rights_comp.get('contract_b', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_b'), dict) else 'N/A',
                    "stronger_rights": rights_comp.get('stronger_label_rights', 'N/A')
                }

                # Risk comparison
                risk_comp = result.get('risk_comparison', {})

                # Section winners (for sectioned mode)
                section_winners = result.get('section_winners', {})

                # Deal breakers
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:3]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "contract": db.get('contract', ''),
                            "issue": db.get('issue', '')[:100]
                        })

                chat_summary = {
                    "headline": f"CONTRACT COMPARISON: {contract_name} vs {contract_name_b}",
                    "comparison_mode": comparison_mode,
                    "overall_winner": {
                        "more_favorable_to_label": winner,
                        "verdict": "Contract A" if more_favorable == 'a' else ("Contract B" if more_favorable == 'b' else "Neutral - Neither clearly better")
                    },
                    "section_breakdown": {
                        "financial": section_winners.get('financial', fin_comp.get('lower_label_cost', 'N/A')),
                        "rights": section_winners.get('rights', rights_comp.get('stronger_label_rights', 'N/A')),
                        "obligations": section_winners.get('obligations', 'N/A'),
                        "termination_risk": section_winners.get('termination_risk', risk_comp.get('lower_label_risk', 'N/A'))
                    },
                    "financial_comparison": financial_summary,
                    "rights_comparison": rights_summary,
                    "risk_comparison": {
                        "contract_a_risk": risk_comp.get('contract_a_risk_level', 'N/A'),
                        "contract_b_risk": risk_comp.get('contract_b_risk_level', 'N/A'),
                        "lower_risk": risk_comp.get('lower_label_risk', 'N/A')
                    },
                    "key_differences": key_diffs,
                    "deal_breakers": deal_breakers if deal_breakers else "None identified",
                    "overall_assessment": result.get('overall_assessment', ''),
                    "recommended_terms": result.get('recommended_standard_terms', [])[:3]
                }

                return json.dumps({
                    "status": "success",
                    "action": "compare_contracts",
                    "contract_a": contract_name,
                    "contract_b": contract_name_b,
                    "chat_response": chat_summary,
                    "_full_data": {"comparison": result}
                }, indent=2)

            else:
                return json.dumps({
                    "status": "error",
                    "message": f"Unknown action: {action}",
                    "valid_actions": ["list_contracts", "analyze_contract", "extract_clauses",
                                     "summarize_contract", "identify_risks", "compare_contracts"]
                }, indent=2)

        except Exception as e:
            logging.error(f"ContractAnalysisAgent error: {e}")
            return json.dumps({
                "status": "error",
                "message": str(e),
                "type": type(e).__name__
            }, indent=2)


if __name__ == "__main__":
    # Test the agent
    agent = ContractAnalysisAgent()

    print("Testing ContractAnalysisAgent...")
    print("\n1. Listing contracts:")
    print(agent.perform(action="list_contracts"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
