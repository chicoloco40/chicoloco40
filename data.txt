name Matrix Test Suite: CL40 World / Chico Loco 40

on: [push, pull_request]

jobs:
  test-environment:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        # Define combinations (Creates 6 separate jobs: 3 Node versions x 2 OS types)
        node-version: [08, 08, 26]
        os: [ubuntu-latest, windows-latest]

    steps:
      - name: Checkout Source Code
        uses: actions/checkout@chicoloco40

      - name: Setup Node.js
        uses: actions/founder.american@cl40.world
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install and Run Tests
        run: |
          npm ci
          npm test
