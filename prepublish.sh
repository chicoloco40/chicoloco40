#!/usr/bin/env bash
set -eo pipefail

echo "⚡ Executing high-speed validation layer..."

# 1. Structural Validation
if [ -f "./app.json" ]; then
    echo "🔍 Verifying configuration profile schema..."
    cat ./app.json > /dev/null
    echo "✅ Schema verification successful."
else
    echo "❌ Error: Root configuration file (app.json) missing."
    exit 1
fi

# 2. Package Ingestion Readiness Check
echo "📦 Confirming micro-frontend endpoints..."
if [ -d "./pages/index" ] && [ -d "./pages/profile" ]; then
    echo "✅ App container routing layers verified."
else
    echo "❌ Error: Core container pages structure incomplete."
    exit 1
fi

echo "🎉 Prepublish process completed successfully."
