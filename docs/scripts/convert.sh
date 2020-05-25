#!/bin/bash

if [ -d "../compiled" ]; then
    :
else
    mkdir ../compiled
fi

pandoc ../static/config.md \
    ../index.md \
    ../summary-statement.md \
    ../methodology.md \
    ../planning.md \
    ../implementation.md \
    ../structure.md \
    ../classes.md \
    ../libraries.md \
    ../test_scenarios.md \
    --toc \
    --highlight-style static/highlight.theme \
    -o compiled/combined.docx