#!/bin/bash

# Convert Windows-style path for Git Bash or WSL
BASE_DIR="."

# Create the base directory
mkdir -p "$BASE_DIR"
cd "$BASE_DIR" || exit 1

# Create shared utils
mkdir -p "$BASE_DIR/shared_utils"

# Topic folder list
TOPICS=(
  "mlops/basics"
  "mlops/cicd"
  "mlops/model-deployment"
  "mlops/experiment-tracking"

  "google-adk/basics"
  "google-adk/advanced"

  "langchain/basics"
  "langchain/tools"
  "langchain/agents"

  "langgraph/getting-started"
  "langgraph/workflows"

  "microsoft-agentic/framework-intro"
  "microsoft-agentic/agent-scenarios"

  "semantic-kernel/plugins"
  "semantic-kernel/planners"

  "a2a-protocol/examples"
  "a2a-protocol/agent-dialogs"

  "mcp-protocol/hello-world"
  "mcp-protocol/agent-interop"

  "projects/smart-agent-suite"
  "projects/mlops-rag-dashboard"
)

# Create the directory structure
for topic in "${TOPICS[@]}"; do
  mkdir -p "$BASE_DIR/$topic"
done

echo "✅ Folder structure created at $BASE_DIR"
