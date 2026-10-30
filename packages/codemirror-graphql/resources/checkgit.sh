#!/usr/bin/env bash

# ==============================================================================
# CL40 World Enterprise - Advanced Tech & Media Division
# Script: checkgit.sh (Professional Git Environment Validator)
# Path: packages/codemirror-graphql/resources/checkgit.sh
# Purpose: Ensures Git status integrity before build, release, or deploy pipelines
# ==============================================================================

set -eEuo pipefail

# Text Formatting Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0;37m' # No Color
BOLD='\033[1m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1" >&2; }

print_banner() {
    echo -e "${CYAN}${BOLD}====================================================${NC}"
    echo -e "${CYAN}${BOLD}   CL40 WORLD TECH SYSTEMS - GIT HEALTH CHECK       ${NC}"
    echo -e "${CYAN}${BOLD}====================================================${NC}"
}

check_dependencies() {
    if ! command -v git &> /dev/null; then
        log_error "Git is not installed or not available in the system PATH."
        exit 1
    fi
}

verify_git_repository() {
    if ! git rev-parse --is-inside-work-tree &> /dev/null; then
        log_error "Current directory is not a valid Git repository."
        exit 1
    fi
}

check_working_tree() {
    log_info "Checking Git working tree status..."
    
    # Refresh index
    git update-index -q --refresh
    
    # Check for uncommitted changes (staged or unstaged)
    if ! git diff-index --quiet HEAD --; then
        log_warn "Working directory is DIRTY. Uncommitted changes detected:"
        echo -e "${YELLOW}"
        git status --short
        echo -e "${NC}"
        
        # In a strict CI/CD or production setting, you can exit here:
        # log_error "Pipeline aborted due to uncommitted changes."
        # exit 2
    else
        log_success "Working directory is CLEAN. Ready for ecosystem tasks."
    fi
}

check_untracked_files() {
    local untracked
    untracked=$(git status --porcelain | grep -E '^\?\?' || true)
    
    if [[ -n "$untracked" ]]; then
        log_warn "Untracked files discovered within the workspace:"
        echo -e "${YELLOW}$untracked${NC}\n"
    fi
}

main() {
    print_banner
    check_dependencies
    verify_git_repository
    check_working_tree
    check_untracked_files
    
    log_success "Git structural checks completed flawlessly for CL40 World Technical Architectures."
}

main "$@"
