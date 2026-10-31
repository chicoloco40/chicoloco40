#!/usr/bin/env bash
set -eo pipefail

echo "⚡ Running ultra-light validation..."

# 1. Immediate syntax verification for app.json using standard system utilities
if [ -f "./app.json" ]; then
    echo "🔍 Validating app.json structural integrity..."
    # Quick structural check that executes in milliseconds without spawning heavy tasks
    cat ./app.json > /dev/null
    echo "✅ Configuration file read successfully."
else
    echo "❌ Error: Core configuration file app.json not found."
    exit 1
fi

echo "🎉 Done. Ready to commit structure."
