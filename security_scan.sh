#!/bin/bash

# Security scan script to check for exposed secrets and keys
echo "🔍 Scanning workspace for exposed secrets and keys..."
echo "=================================================="

# Common patterns for secrets and keys
SECRET_PATTERNS=(
    "api[_-]?key"
    "secret[_-]?key"
    "private[_-]?key"
    "access[_-]?token"
    "auth[_-]?token"
    "password"
    "passwd"
    "aws[_-]?access[_-]?key"
    "aws[_-]?secret[_-]?key"
    "ssh[_-]?key"
    "bearer[_-]?token"
    "client[_-]?secret"
    "database[_-]?url"
    "db[_-]?password"
    "jwt[_-]?secret"
    "encryption[_-]?key"
)

# File extensions to scan
FILE_EXTENSIONS=("*.py" "*.js" "*.json" "*.yaml" "*.yml" "*.env" "*.txt" "*.md" "*.cfg" "*.ini" "*.conf")

echo "Scanning Python files for potential secrets..."
echo "---------------------------------------------"

# Scan for common secret patterns in Python files
for pattern in "${SECRET_PATTERNS[@]}"; do
    echo "Checking for pattern: $pattern"
    grep -r -i -n --include="*.py" "$pattern" . 2>/dev/null || echo "  ✅ No matches found"
done

echo ""
echo "Checking for hardcoded credentials..."
echo "------------------------------------"

# Check for hardcoded passwords, tokens, etc.
grep -r -i -n --include="*.py" --include="*.js" --include="*.json" "password\s*=\s*['\"][^'\"]*['\"]" . 2>/dev/null || echo "✅ No hardcoded passwords found"
grep -r -i -n --include="*.py" --include="*.js" --include="*.json" "token\s*=\s*['\"][^'\"]*['\"]" . 2>/dev/null || echo "✅ No hardcoded tokens found"
grep -r -i -n --include="*.py" --include="*.js" --include="*.json" "key\s*=\s*['\"][^'\"]*['\"]" . 2>/dev/null || echo "✅ No hardcoded keys found"

echo ""
echo "Checking for environment files..."
echo "--------------------------------"

# Check for .env files
find . -name ".env*" -type f 2>/dev/null | while read -r file; do
    echo "⚠️  Found environment file: $file"
    echo "   Contents preview:"
    head -5 "$file" 2>/dev/null | sed 's/^/   /'
    echo ""
done

echo ""
echo "Checking for configuration files with potential secrets..."
echo "--------------------------------------------------------"

# Check config files
find . -name "config.*" -o -name "*.conf" -o -name "*.cfg" -o -name "*.ini" | while read -r file; do
    echo "📄 Found config file: $file"
    # Check if it contains password-like patterns
    if grep -i -q "password\|secret\|key\|token" "$file" 2>/dev/null; then
        echo "   ⚠️  Contains potential secrets - please review"
    else
        echo "   ✅ Appears clean"
    fi
done

echo ""
echo "Checking for SSH keys..."
echo "-----------------------"

find . -name "id_rsa" -o -name "id_dsa" -o -name "id_ecdsa" -o -name "id_ed25519" -o -name "*.pem" -o -name "*.key" | while read -r file; do
    echo "🔑 Found potential SSH/private key: $file"
done

echo ""
echo "Checking for database connection strings..."
echo "------------------------------------------"

grep -r -i -n --include="*.py" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml" "mongodb://\|mysql://\|postgresql://\|redis://\|sqlite://" . 2>/dev/null || echo "✅ No database connection strings found"

echo ""
echo "🔍 Scan complete!"
echo "=================="
echo ""
echo "📋 Recommendations:"
echo "- Any secrets found should be moved to environment variables"
echo "- Use .env files for local development (ensure they're in .gitignore)"
echo "- Consider using secret management tools for production"
echo "- Never commit secrets to version control"