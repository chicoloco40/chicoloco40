#!/usr/bin/env bash

set -eo pipefail

echo "🚀 Starting Prepublish Validation..."

# 1. Run the Git check script first
if [ -f "./packages/codemirror-graphql/resources/checkgit.sh" ]; then
  bash "./packages/codemirror-graphql/resources/checkgit.sh"
else
  echo "⚠️ Warning: checkgit.sh not found, skipping Git check."
fi

# 2. Install dependencies safely if needed (optional but recommended for CI/CD)
echo "📦 Verifying dependencies..."
npm ci --quiet || npm install --quiet

# 3. Run Code Quality Checks (Linting & Formatting)
echo "🧹 Running Linters and Formatters..."
npm run lint || { echo "❌ Linting failed."; exit 1; }

# 4. Run Automated Tests
echo "🧪 Running Test Suite..."
npm test || { echo "❌ Tests failed. Fix them before publishing."; exit 1; }

# 5. Build the Project
echo "🏗️ Building the production bundle..."
npm run build || { echo "❌ Build failed."; exit 1; }

echo "🎉 Prepublish checks passed successfully! Ready to publish."
