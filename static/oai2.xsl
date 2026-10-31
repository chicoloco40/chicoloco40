<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
                xmlns:xsl="http://w3.org"
                xmlns:oai="http://openarchives.org"
                xmlns:dc="http://purl.org">
    <xsl:output method="html" indent="yes" encoding="UTF-8"/>

    <!-- Master Template Gate -->
    <xsl:template match="/">
        <html>
            <head>
                <title>Chico Loco 40 - Media Matrix Sync Interface</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #0f172a;
                        color: #f8fafc;
                        margin: 0;
                        padding: 40px;
                    }
                    .container {
                        max-width: 1000px;
                        margin: 0 auto;
                    }
                    .header-panel {
                        border-bottom: 2px solid #334155;
                        padding-bottom: 20px;
                        margin-bottom: 30px;
                    }
                    h1 {
                        color: #ffffff;
                        margin: 0 0 10px 0;
                        font-size: 2.25rem;
                    }
                    .status-badge {
                        display: inline-block;
                        background-color: rgba(34, 197, 94, 0.1);
                        color: #22c55e;
                        padding: 6px 16px;
                        border-radius: 50px;
                        font-weight: 600;
                        font-size: 0.875rem;
                        border: 1px solid rgba(34, 197, 94, 0.2);
                    }
                    .record-card {
                        background-color: #1e293b;
                        border: 1px solid #334155;
                        border-radius: 8px;
                        padding: 24px;
                        margin-bottom: 16px;
                    }
                    .meta-title {
                        color: #38bdf8;
                        font-size: 1.25rem;
                        font-weight: 600;
                        margin: 0 0 8px 0;
                    }
                    .meta-desc {
                        color: #94a3b8;
                        margin: 0 0 12px 0;
                        font-size: 0.95rem;
                        line-height: 1.5;
                    }
                    .meta-spec {
                        font-size: 0.85rem;
                        color: #10b981;
                        font-family: monospace;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header-panel">
                        <h1>Symphony Core Repository Ledger</h1>
                        <div class="status-badge">⚡ Status Code: 111 Core Operational</div>
                    </div>
                    
                    <!-- Loop and render incoming repository nodes safely -->
                    <xsl:apply-templates select="//oai:record"/>
                </div>
            </body>
        </html>
    </xsl:template>

    <!-- Template rule to parse and layout metadata entries -->
    <xsl:template match="oai:record">
        <div class="record-card">
            <div class="meta-title">
                <xsl:value-of select="oai:metadata/dc:title"/>
            </div>
            <div class="meta-desc">
                <xsl:value-of select="oai:metadata/dc:description"/>
            </div>
            <div class="meta-spec">
                Identifier: <xsl:value-of select="oai:header/oai:identifier"/> 
                | Datestamp: <xsl:value-of select="oai:header/oai:datestamp"/>
            </div>
        </div>
    </xsl:template>
</xsl:stylesheet>
