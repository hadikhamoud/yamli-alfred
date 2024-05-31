#!/bin/bash

# Function to transliterate a word using Yamli API
transliterate() {
    local word=$1
    #local url="https://api.yamli.com/transliterate.ashx?word=${word}&tool=api&account_id=000006&prot=https%3A&hostname=www.yamli.com&path=%2Farabic-keyboard%2F&build=5515&sxhr_id=4"
    local url="https://api.yamli.com/transliterate.ashx?word=${word}&tool=api&account_id=000006&prot=https&hostname=AliMZaini&path=yamli-api&build=5515"
    
    # Make the HTTP request and get the response
    local response=$(curl -s "$url")
    
    echo "$response"
    # Parse the JSON response to get the candidates
    local candidates=$(echo "$response" | jq -r '.r' | tr '|' '\n' | sed 's/..$//')

    echo "$candidates"
}

# Check if a word was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <word>"
    exit 1
fi

# Call the transliterate function with the provided word
transliterate "$1"

