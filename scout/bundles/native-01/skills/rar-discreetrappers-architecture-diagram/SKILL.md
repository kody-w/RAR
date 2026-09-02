---
name: "rar-discreetrappers-architecture-diagram"
description: "Generate professional architecture diagrams.\n\nSupported diagram types:\n- azure: Azure cloud architecture\n- agent_system: AI agent/orchestrator architecture\n- multi_tier: N-tier application architecture\n- microservices: Microservices architecture\n- data_flow: Data pipeline/flow diagram\n- custom: Custom node/connection diagram\n\nOutput formats: png, svg, pdf, mermaid, drawio\n\nActions:\n- create_diagram: Create a diagram from specification\n- diagram_from_agents: Generate diagram from RAPP agent configurations\n- list_node_types: List available node types\n- generate_mermaid: Generate Mermaid.js code\n\nExample:\n{\n  \"action\": \"create_diagram\",\n  \"diagram_type\": \"azure\",\n  \"title\": \"RAPP Architecture\",\n  \"output_format\": \"png\",\n  \"nodes\": [\n    {\"id\": \"user\", \"type\": \"user\", \"label\": \"User\"},\n    {\"id\": \"func\", \"type\": \"function_app\", \"label\": \"Azure Functions\"},\n    {\"id\": \"openai\", \"type\": \"openai\", \"label\": \"Azure OpenAI\"}\n  ],\n  \"connections\": [\n    {\"from\": \"user\", \"to\": \"func\", \"label\": \"HTTP\"},\n    {\"from\": \"func\", \"to\": \"openai\", \"label\": \"API\"}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/architecture_diagram_agent", "rar_sha256": "97485b27444625b332f52f9df07e46ed70d6a24dd250eba01bb78660056c36ba", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "architecture_diagram_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/architecture-diagram:abfc6de19cc04b7f37992824d310a670480aa0327900a2a92014baa0b2a801b5", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/architecture_diagram_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `architecture_diagram_agent.py` is
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

Architecture Diagram Agent
Purpose: Generate professional architecture diagrams for system documentation

Supported diagram types:
- Cloud architecture (Azure, AWS, GCP, On-premise)
- Multi-tier/N-tier architecture
- Microservices architecture
- Data flow diagrams
- Agent/AI system architecture
- Network topology

Output formats:
- PNG (default)
- SVG (for web/scalable)
- PDF (for documents)
- Mermaid (text-based, for markdown)
- Draw.io XML (for Visio compatibility)

Dependencies:
- diagrams: Python library for cloud architecture diagrams
- graphviz: Graph visualization (required by diagrams)

Usage:
1. Simple: action="create_diagram", diagram_type="azure", title="My Architecture"
2. Custom: action="create_diagram", nodes=[...], connections=[...], clusters=[...]
3. From agent config: action="diagram_from_agents", agents=[...]

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "create_diagram",
        "diagram_from_agents",
        "list_node_types",
        "generate_mermaid"
      ],
      "type": "string"
    },
    "agents": {
      "description": "Agent configurations for diagram_from_agents",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "clusters": {
      "items": {
        "properties": {
          "id": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "nodes": {
            "items": {
              "type": "string"
            },
            "type": "array"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "connections": {
      "items": {
        "properties": {
          "from": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "style": {
            "type": "string"
          },
          "to": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "customer": {
      "description": "Customer name - creates a subfolder in arch_diagrams for this customer",
      "type": "string"
    },
    "diagram_type": {
      "enum": [
        "azure",
        "agent_system",
        "multi_tier",
        "microservices",
        "data_flow",
        "custom"
      ],
      "type": "string"
    },
    "nodes": {
      "items": {
        "properties": {
          "cluster": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "output_dir": {
      "type": "string"
    },
    "output_filename": {
      "type": "string"
    },
    "output_format": {
      "enum": [
        "png",
        "svg",
        "pdf",
        "mermaid",
        "drawio"
      ],
      "type": "string"
    },
    "style": {
      "enum": [
        "default",
        "dark",
        "minimal"
      ],
      "type": "string"
    },
    "title": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `architecture_diagram_agent.py` and embedded as the fenced Python below (sha256 97485b27444625b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `architecture_diagram_agent.py` first:

```bash
python3 architecture_diagram_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 architecture_diagram_agent.py   # or on stdin
python3 architecture_diagram_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Architecture Diagram Agent
Purpose: Generate professional architecture diagrams for system documentation

Supported diagram types:
- Cloud architecture (Azure, AWS, GCP, On-premise)
- Multi-tier/N-tier architecture
- Microservices architecture
- Data flow diagrams
- Agent/AI system architecture
- Network topology

Output formats:
- PNG (default)
- SVG (for web/scalable)
- PDF (for documents)
- Mermaid (text-based, for markdown)
- Draw.io XML (for Visio compatibility)

Dependencies:
- diagrams: Python library for cloud architecture diagrams
- graphviz: Graph visualization (required by diagrams)

Usage:
1. Simple: action="create_diagram", diagram_type="azure", title="My Architecture"
2. Custom: action="create_diagram", nodes=[...], connections=[...], clusters=[...]
3. From agent config: action="diagram_from_agents", agents=[...]
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/architecture_diagram_agent",
    "version": "1.0.1",
    "display_name": "ArchitectureDiagramAgent",
    "description": "Generates architecture diagrams as PNG, SVG, PDF, Mermaid, or Draw.io XML from node/connection configs via the diagrams+graphviz library.",
    "author": "Bill Whalen",
    "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import tempfile
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent

# Check for diagrams library and set up Graphviz path
DIAGRAMS_AVAILABLE = False
DIAGRAMS_IMPORT_ERROR = ""

# Ensure Graphviz is on PATH for Windows
import platform
if platform.system() == "Windows":
    graphviz_paths = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
    ]
    for gv_path in graphviz_paths:
        if os.path.exists(gv_path) and gv_path not in os.environ.get("PATH", ""):
            os.environ["PATH"] = gv_path + os.pathsep + os.environ.get("PATH", "")
            break

try:
    from diagrams import Diagram, Cluster, Edge
    from diagrams.azure.compute import FunctionApps, VM, ContainerInstances, KubernetesServices
    from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis, DatabaseForPostgresqlServers
    from diagrams.azure.integration import LogicApps, ServiceBus, APIManagement
    from diagrams.azure.ml import CognitiveServices, MachineLearningServiceWorkspaces, BotServices
    from diagrams.azure.network import LoadBalancers, VirtualNetworks, ApplicationGateway, CDNProfiles, Firewall
    from diagrams.azure.security import KeyVaults, ApplicationSecurityGroups
    from diagrams.azure.storage import StorageAccounts, BlobStorage, DataLakeStorage
    from diagrams.azure.web import AppServices, AppServicePlans
    from diagrams.azure.analytics import AnalysisServices, DataFactories, Databricks
    from diagrams.onprem.client import Users, Client
    from diagrams.onprem.compute import Server
    from diagrams.onprem.network import Internet
    from diagrams.programming.language import Python
    from diagrams.generic.compute import Rack
    from diagrams.generic.database import SQL
    from diagrams.generic.storage import Storage
    from diagrams.saas.chat import Slack, Teams
    DIAGRAMS_AVAILABLE = True
except ImportError as e:
    DIAGRAMS_IMPORT_ERROR = str(e)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ArchitectureDiagramAgent(BasicAgent):
    """
    Agent for generating professional architecture diagrams.
    Supports Azure, AWS, GCP, and custom architectures.
    """

    # Node type mappings for Azure
    AZURE_NODES = {
        "function": "FunctionApps",
        "function_app": "FunctionApps",
        "functions": "FunctionApps",
        "vm": "VM",
        "container": "ContainerInstances",
        "aks": "KubernetesServices",
        "kubernetes": "KubernetesServices",
        "app_service": "AppServices",
        "web_app": "AppServices",
        "cosmos": "CosmosDb",
        "cosmosdb": "CosmosDb",
        "sql": "SQLDatabases",
        "postgres": "DatabaseForPostgresqlServers",
        "redis": "CacheForRedis",
        "blob": "BlobStorage",
        "storage": "StorageAccounts",
        "datalake": "DataLakeStorage",
        "logic_app": "LogicApps",
        "service_bus": "ServiceBus",
        "apim": "APIManagement",
        "api_management": "APIManagement",
        "cognitive": "CognitiveServices",
        "openai": "CognitiveServices",
        "ai": "CognitiveServices",
        "bot": "BotServices",
        "ml": "MachineLearningServiceWorkspaces",
        "databricks": "Databricks",
        "data_factory": "DataFactories",
        "load_balancer": "LoadBalancers",
        "vnet": "VirtualNetworks",
        "app_gateway": "ApplicationGateway",
        "cdn": "CDNProfiles",
        "firewall": "Firewall",
        "key_vault": "KeyVaults",
        "security": "ApplicationSecurityGroups",
    }

    # Generic node types
    GENERIC_NODES = {
        "user": "Users",
        "users": "Users",
        "client": "Client",
        "internet": "Internet",
        "teams": "Teams",
        "slack": "Slack",
        "server": "Server",
        "database": "SQL",
        "storage": "Storage",
        "compute": "Rack",
        "python": "Python",
        "agent": "Rack",
    }

    # Diagram styles - Professional Visio-quality settings
    STYLES = {
        "default": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "white",
                "pad": "1.0",
                "splines": "spline",
                "nodesep": "1.2",
                "ranksep": "1.5",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "color": "#666666",
                "penwidth": "1.5",
            }
        },
        "professional": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.5",
                "ranksep": "2.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+25,25",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
            }
        },
        "microsoft": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "#FAFAFA",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.8",
                "ranksep": "2.5",
                "dpi": "300",
                "overlap": "false",
                "sep": "+30,30",
                "esep": "+15,15",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
                "arrowsize": "1.0",
            }
        },
        "enterprise": {
            "graph_attr": {
                "fontsize": "20",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "2.0",
                "splines": "spline",
                "nodesep": "2.0",
                "ranksep": "3.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+40,40",
                "esep": "+20,20",
                "concentrate": "false",
            },
            "node_attr": {
                "fontsize": "15",
                "fontname": "Segoe UI",
                "margin": "0.3,0.2",
            },
            "edge_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.5",
                "arrowsize": "1.2",
                "labeldistance": "3.0",
                "labelangle": "25",
            }
        },
        "dark": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "#1a1a2e",
                "fontcolor": "white",
                "pad": "1.0",
                "dpi": "300",
                "overlap": "false",
                "nodesep": "1.5",
                "ranksep": "2.0",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "fontcolor": "white",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "fontcolor": "white",
                "color": "#00BCF2",
                "penwidth": "1.5",
            }
        },
        "minimal": {
            "graph_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI Light",
                "bgcolor": "white",
                "pad": "0.8",
                "splines": "polyline",
                "nodesep": "1.0",
                "ranksep": "1.2",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI Light",
            },
            "edge_attr": {
                "fontsize": "10",
                "fontname": "Segoe UI Light",
                "color": "#999999",
                "penwidth": "1.0",
            }
        }
    }

    def __init__(self):
        self.name = 'ArchitectureDiagramAgent'
        self.metadata = {
            "name": self.name,
            "description": """Generate professional architecture diagrams.

Supported diagram types:
- azure: Azure cloud architecture
- agent_system: AI agent/orchestrator architecture
- multi_tier: N-tier application architecture
- microservices: Microservices architecture
- data_flow: Data pipeline/flow diagram
- custom: Custom node/connection diagram

Output formats: png, svg, pdf, mermaid, drawio

Actions:
- create_diagram: Create a diagram from specification
- diagram_from_agents: Generate diagram from RAPP agent configurations
- list_node_types: List available node types
- generate_mermaid: Generate Mermaid.js code

Example:
{
  "action": "create_diagram",
  "diagram_type": "azure",
  "title": "RAPP Architecture",
  "output_format": "png",
  "nodes": [
    {"id": "user", "type": "user", "label": "User"},
    {"id": "func", "type": "function_app", "label": "Azure Functions"},
    {"id": "openai", "type": "openai", "label": "Azure OpenAI"}
  ],
  "connections": [
    {"from": "user", "to": "func", "label": "HTTP"},
    {"from": "func", "to": "openai", "label": "API"}
  ]
}""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                    },
                    "diagram_type": {
                        "type": "string",
                        "enum": ["azure", "agent_system", "multi_tier", "microservices", "data_flow", "custom"]
                    },
                    "title": {"type": "string"},
                    "output_format": {
                        "type": "string",
                        "enum": ["png", "svg", "pdf", "mermaid", "drawio"]
                    },
                    "style": {
                        "type": "string",
                        "enum": ["default", "dark", "minimal"]
                    },
                    "nodes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "label": {"type": "string"},
                                "cluster": {"type": "string"}
                            }
                        }
                    },
                    "connections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "from": {"type": "string"},
                                "to": {"type": "string"},
                                "label": {"type": "string"},
                                "style": {"type": "string"}
                            }
                        }
                    },
                    "clusters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "label": {"type": "string"},
                                "nodes": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    },
                    "agents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Agent configurations for diagram_from_agents"
                    },
                    "customer": {
                        "type": "string",
                        "description": "Customer name - creates a subfolder in arch_diagrams for this customer"
                    },
                    "output_filename": {"type": "string"},
                    "output_dir": {"type": "string"}
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)
        self.base_path = self._find_base_path()

    def _find_base_path(self) -> str:
        """Find the base path for the RAPP project."""
        possible_paths = [
            os.getcwd(),
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ]
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "agents")):
                return path
        return os.getcwd()

    def perform(self, **kwargs) -> str:
        """Execute the requested action."""
        action = kwargs.get('action', 'create_diagram')

        try:
            if action == 'list_node_types':
                return self._list_node_types()
            elif action == 'generate_mermaid':
                return self._generate_mermaid(**kwargs)
            elif action == 'diagram_from_agents':
                return self._diagram_from_agents(**kwargs)
            elif action == 'create_diagram':
                output_format = kwargs.get('output_format', 'png')
                if output_format == 'mermaid':
                    return self._generate_mermaid(**kwargs)
                elif output_format == 'drawio':
                    return self._generate_drawio(**kwargs)
                else:
                    return self._create_diagram(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}",
                    "available_actions": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                })
        except Exception as e:
            logger.error(f"Diagram generation error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })

    def _list_node_types(self) -> str:
        """List available node types."""
        return json.dumps({
            "status": "success",
            "azure_nodes": list(self.AZURE_NODES.keys()),
            "generic_nodes": list(self.GENERIC_NODES.keys()),
            "note": "Use these type values in the 'type' field of node definitions"
        }, indent=2)

    def _create_diagram(self, **kwargs) -> str:
        """Create a diagram using the diagrams library."""
        if not DIAGRAMS_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": f"diagrams library not available: {DIAGRAMS_IMPORT_ERROR}",
                "suggestion": "Install with: pip install diagrams",
                "fallback": "Use output_format='mermaid' for text-based diagrams"
            })

        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        output_format = kwargs.get('output_format', 'png')
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')
        style = kwargs.get('style', 'professional')  # Default to professional style
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            # Sanitize customer name for folder (lowercase, replace spaces with underscores)
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Clean filename (remove extension if present)
        if output_filename.endswith(('.png', '.svg', '.pdf')):
            output_filename = output_filename.rsplit('.', 1)[0]

        # Use temp directory for rendering to avoid path issues with spaces/OneDrive
        import shutil
        temp_dir = tempfile.mkdtemp()
        temp_output_path = os.path.join(temp_dir, output_filename)
        final_output_dir = output_dir
        final_output_path = os.path.join(final_output_dir, f"{output_filename}.{output_format}")

        # Get style configuration
        style_config = self.STYLES.get(style, self.STYLES["professional"])

        try:
            with Diagram(
                title,
                filename=temp_output_path,
                outformat=output_format,
                show=False,
                graph_attr=style_config["graph_attr"],
                node_attr=style_config.get("node_attr", {}),
                edge_attr=style_config.get("edge_attr", {})
            ):
                # Create node objects
                node_objects = {}

                # Handle clusters
                cluster_objects = {}
                for cluster in clusters:
                    cluster_id = cluster.get('id', cluster.get('label', 'Cluster'))
                    cluster_label = cluster.get('label', cluster_id)
                    cluster_objects[cluster_id] = {"label": cluster_label, "nodes": cluster.get('nodes', [])}

                # Create nodes within clusters first
                for cluster_id, cluster_info in cluster_objects.items():
                    with Cluster(cluster_info["label"]):
                        for node in nodes:
                            if node.get('cluster') == cluster_id:
                                node_obj = self._create_node(node)
                                if node_obj:
                                    node_objects[node['id']] = node_obj

                # Create standalone nodes
                for node in nodes:
                    if node['id'] not in node_objects:
                        node_obj = self._create_node(node)
                        if node_obj:
                            node_objects[node['id']] = node_obj

                # Create connections
                for conn in connections:
                    from_id = conn.get('from')
                    to_id = conn.get('to')
                    label = conn.get('label', '')
                    
                    if from_id in node_objects and to_id in node_objects:
                        if label:
                            node_objects[from_id] >> Edge(label=label) >> node_objects[to_id]
                        else:
                            node_objects[from_id] >> node_objects[to_id]

            # Move file from temp to final location
            temp_file = f"{temp_output_path}.{output_format}"
            if os.path.exists(temp_file):
                shutil.copy2(temp_file, final_output_path)
                # Clean up temp directory
                shutil.rmtree(temp_dir, ignore_errors=True)
            
            return json.dumps({
                "status": "success",
                "filename": f"{output_filename}.{output_format}",
                "path": final_output_path,
                "diagram_type": diagram_type,
                "style": style,
                "node_count": len(nodes),
                "connection_count": len(connections),
                "note": "Professional Visio-quality diagram with Azure icons"
            }, indent=2)

        except Exception as e:
            logger.error(f"Diagram creation failed: {e}")
            # Clean up temp directory
            if 'temp_dir' in locals():
                shutil.rmtree(temp_dir, ignore_errors=True)
            # Fallback to mermaid
            return self._generate_mermaid(**kwargs)

    def _create_node(self, node: Dict) -> Any:
        """Create a diagram node based on type."""
        node_type = node.get('type', 'server').lower()
        label = node.get('label', node.get('id', 'Node'))

        # Try Azure nodes first
        if node_type in self.AZURE_NODES:
            node_class_name = self.AZURE_NODES[node_type]
            # Get the class from the appropriate module
            if node_class_name == "FunctionApps":
                return FunctionApps(label)
            elif node_class_name == "VM":
                return VM(label)
            elif node_class_name == "ContainerInstances":
                return ContainerInstances(label)
            elif node_class_name == "KubernetesServices":
                return KubernetesServices(label)
            elif node_class_name == "AppServices":
                return AppServices(label)
            elif node_class_name == "CosmosDb":
                return CosmosDb(label)
            elif node_class_name == "SQLDatabases":
                return SQLDatabases(label)
            elif node_class_name == "DatabaseForPostgresqlServers":
                return DatabaseForPostgresqlServers(label)
            elif node_class_name == "CacheForRedis":
                return CacheForRedis(label)
            elif node_class_name == "BlobStorage":
                return BlobStorage(label)
            elif node_class_name == "StorageAccounts":
                return StorageAccounts(label)
            elif node_class_name == "DataLakeStorage":
                return DataLakeStorage(label)
            elif node_class_name == "LogicApps":
                return LogicApps(label)
            elif node_class_name == "ServiceBus":
                return ServiceBus(label)
            elif node_class_name == "APIManagement":
                return APIManagement(label)
            elif node_class_name == "CognitiveServices":
                return CognitiveServices(label)
            elif node_class_name == "BotServices":
                return BotServices(label)
            elif node_class_name == "MachineLearningServiceWorkspaces":
                return MachineLearningServiceWorkspaces(label)
            elif node_class_name == "Databricks":
                return Databricks(label)
            elif node_class_name == "DataFactories":
                return DataFactories(label)
            elif node_class_name == "LoadBalancers":
                return LoadBalancers(label)
            elif node_class_name == "VirtualNetworks":
                return VirtualNetworks(label)
            elif node_class_name == "ApplicationGateway":
                return ApplicationGateway(label)
            elif node_class_name == "CDNProfiles":
                return CDNProfiles(label)
            elif node_class_name == "Firewall":
                return Firewall(label)
            elif node_class_name == "KeyVaults":
                return KeyVaults(label)
            elif node_class_name == "ApplicationSecurityGroups":
                return ApplicationSecurityGroups(label)

        # Try generic nodes
        if node_type in self.GENERIC_NODES:
            node_class_name = self.GENERIC_NODES[node_type]
            if node_class_name == "Users":
                return Users(label)
            elif node_class_name == "Client":
                return Client(label)
            elif node_class_name == "Internet":
                return Internet(label)
            elif node_class_name == "Teams":
                return Teams(label)
            elif node_class_name == "Slack":
                return Slack(label)
            elif node_class_name == "Server":
                return Server(label)
            elif node_class_name == "SQL":
                return SQL(label)
            elif node_class_name == "Storage":
                return Storage(label)
            elif node_class_name == "Rack":
                return Rack(label)
            elif node_class_name == "Python":
                return Python(label)

        # Default to Server
        return Server(label)

    def _generate_mermaid(self, **kwargs) -> str:
        """Generate Mermaid.js diagram code."""
        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Build mermaid code
        lines = ["```mermaid", "flowchart TB"]
        
        # Add title as comment
        lines.append(f"    %% {title}")
        lines.append("")

        # Group nodes by cluster
        cluster_nodes = {}
        standalone_nodes = []
        
        for node in nodes:
            cluster_id = node.get('cluster')
            if cluster_id:
                if cluster_id not in cluster_nodes:
                    cluster_nodes[cluster_id] = []
                cluster_nodes[cluster_id].append(node)
            else:
                standalone_nodes.append(node)

        # Add clusters
        for cluster in clusters:
            cluster_id = cluster.get('id', '')
            cluster_label = cluster.get('label', cluster_id)
            lines.append(f"    subgraph {cluster_id}[{cluster_label}]")
            
            # Add nodes in this cluster
            for node in cluster_nodes.get(cluster_id, []):
                node_id = node.get('id', '')
                label = node.get('label', node_id)
                shape = self._get_mermaid_shape(node.get('type', 'server'))
                lines.append(f"        {node_id}{shape[0]}{label}{shape[1]}")
            
            lines.append("    end")
            lines.append("")

        # Add standalone nodes
        for node in standalone_nodes:
            node_id = node.get('id', '')
            label = node.get('label', node_id)
            shape = self._get_mermaid_shape(node.get('type', 'server'))
            lines.append(f"    {node_id}{shape[0]}{label}{shape[1]}")

        lines.append("")

        # Add connections
        for conn in connections:
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            style = conn.get('style', 'arrow')
            
            arrow = self._get_mermaid_arrow(style)
            if label:
                lines.append(f"    {from_id} {arrow}|{label}| {to_id}")
            else:
                lines.append(f"    {from_id} {arrow} {to_id}")

        lines.append("```")

        mermaid_code = "\n".join(lines)

        # Save to file if requested
        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            md_path = os.path.join(output_dir, f"{output_filename}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(mermaid_code)

            return json.dumps({
                "status": "success",
                "format": "mermaid",
                "filename": f"{output_filename}.md",
                "path": md_path,
                "mermaid_code": mermaid_code
            }, indent=2)

        return json.dumps({
            "status": "success",
            "format": "mermaid",
            "mermaid_code": mermaid_code
        }, indent=2)

    def _get_mermaid_shape(self, node_type: str) -> Tuple[str, str]:
        """Get Mermaid shape markers for a node type."""
        shapes = {
            "user": ["((", "))"],       # Circle
            "users": ["((", "))"],
            "database": ["[(", ")]"],   # Cylinder
            "sql": ["[(", ")]"],
            "cosmos": ["[(", ")]"],
            "cosmosdb": ["[(", ")]"],
            "storage": ["[(", ")]"],
            "blob": ["[(", ")]"],
            "function": ["[/", "\\]"],  # Trapezoid
            "function_app": ["[/", "\\]"],
            "openai": ["{{", "}}"],     # Hexagon
            "cognitive": ["{{", "}}"],
            "ml": ["{{", "}}"],
            "agent": [">", "]"],        # Flag
            "server": ["[", "]"],       # Rectangle
            "default": ["[", "]"],
        }
        return shapes.get(node_type.lower(), shapes["default"])

    def _get_mermaid_arrow(self, style: str) -> str:
        """Get Mermaid arrow style."""
        arrows = {
            "arrow": "-->",
            "dotted": "-.->",
            "thick": "==>",
            "bidirectional": "<-->",
        }
        return arrows.get(style, "-->")

    def _generate_drawio(self, **kwargs) -> str:
        """Generate Draw.io XML (compatible with Visio import)."""
        title = kwargs.get('title', 'Architecture Diagram')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Draw.io XML structure
        xml_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<mxfile host="app.diagrams.net">',
            '  <diagram name="Page-1">',
            '    <mxGraphModel dx="1000" dy="600" grid="1" gridSize="10">',
            '      <root>',
            '        <mxCell id="0"/>',
            '        <mxCell id="1" parent="0"/>',
        ]

        # Add nodes
        x, y = 100, 100
        node_positions = {}
        
        for i, node in enumerate(nodes):
            node_id = node.get('id', f'node_{i}')
            label = node.get('label', node_id)
            node_type = node.get('type', 'server')
            
            # Calculate position (simple grid layout)
            pos_x = 100 + (i % 4) * 200
            pos_y = 100 + (i // 4) * 150
            node_positions[node_id] = (pos_x, pos_y)
            
            # Get shape style based on type
            style = self._get_drawio_style(node_type)
            
            xml_parts.append(f'        <mxCell id="{node_id}" value="{label}" style="{style}" vertex="1" parent="1">')
            xml_parts.append(f'          <mxGeometry x="{pos_x}" y="{pos_y}" width="120" height="60" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        # Add connections
        for i, conn in enumerate(connections):
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            edge_id = f'edge_{i}'
            
            xml_parts.append(f'        <mxCell id="{edge_id}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" source="{from_id}" target="{to_id}" parent="1">')
            xml_parts.append('          <mxGeometry relative="1" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        xml_parts.extend([
            '      </root>',
            '    </mxGraphModel>',
            '  </diagram>',
            '</mxfile>',
        ])

        xml_content = '\n'.join(xml_parts)

        # Save to file
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        xml_path = os.path.join(output_dir, f"{output_filename}.drawio")
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

        return json.dumps({
            "status": "success",
            "format": "drawio",
            "filename": f"{output_filename}.drawio",
            "path": xml_path,
            "note": "Open with draw.io or import into Visio"
        }, indent=2)

    def _get_drawio_style(self, node_type: str) -> str:
        """Get Draw.io style for a node type."""
        styles = {
            "user": "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
            "database": "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;fillColor=#f5f5f5;strokeColor=#666666;",
            "function": "shape=step;perimeter=stepPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#fff2cc;strokeColor=#d6b656;",
            "openai": "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;",
            "agent": "shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
            "server": "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
        }
        return styles.get(node_type.lower(), styles["server"])

    def _diagram_from_agents(self, **kwargs) -> str:
        """Generate diagram from RAPP agent configurations."""
        agents = kwargs.get('agents', [])
        title = kwargs.get('title', 'RAPP Agent Architecture')
        output_format = kwargs.get('output_format', 'png')

        if not agents:
            # Try to load agents from the agents directory
            agents = self._discover_agents()

        # Build nodes and connections from agent configs
        nodes = []
        connections = []

        # Add user node
        nodes.append({"id": "user", "type": "user", "label": "User"})

        # Add RAPP core
        nodes.append({"id": "rapp_core", "type": "function_app", "label": "RAPP Core\n(Azure Functions)", "cluster": "azure"})
        connections.append({"from": "user", "to": "rapp_core", "label": "HTTP"})

        # Add OpenAI
        nodes.append({"id": "openai", "type": "openai", "label": "Azure OpenAI", "cluster": "azure"})
        connections.append({"from": "rapp_core", "to": "openai", "label": "API"})

        # Add agents
        for i, agent in enumerate(agents):
            agent_id = f"agent_{i}"
            agent_name = agent.get('name', agent.get('id', f'Agent {i+1}'))
            nodes.append({
                "id": agent_id,
                "type": "agent",
                "label": agent_name,
                "cluster": "agents"
            })
            connections.append({"from": "rapp_core", "to": agent_id, "label": ""})

        # Define clusters
        clusters = [
            {"id": "azure", "label": "Azure Cloud"},
            {"id": "agents", "label": "RAPP Agents"}
        ]

        # Create the diagram
        return self._create_diagram(
            title=title,
            nodes=nodes,
            connections=connections,
            clusters=clusters,
            output_format=output_format,
            **kwargs
        )

    def _discover_agents(self) -> List[Dict]:
        """Discover agents from the agents directory."""
        agents = []
        agents_dir = os.path.join(self.base_path, 'agents')
        
        if os.path.exists(agents_dir):
            for filename in os.listdir(agents_dir):
                if filename.endswith('_agent.py') and not filename.startswith('__'):
                    agent_name = filename.replace('_agent.py', '').replace('_', ' ').title()
                    agents.append({"name": agent_name, "file": filename})

        return agents[:10]  # Limit to 10 agents for readability
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
