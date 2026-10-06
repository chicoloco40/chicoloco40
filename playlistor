using namespace System.Collections.Generic

class RegistryEntity {
    [string]$entityName
    [string]$abn
    [string]$entityType
    [string]$location
    [string]$email

    RegistryEntity([string]$entityName, [string]$abn, [string]$entityType, [string]$location, [string]$email) {
        $this.entityName = $entityName
        $this.abn = $abn
        $this.entityType = $entityType
        $this.location = $location
        $this.email = $email
    }
}

class IsbnRecord {
    [string]$label
    [string]$registrationNumber
    [string]$formattedIsbn

    IsbnRecord([string]$label, [string]$registrationNumber, [string]$formattedIsbn) {
        $this.label = $label
        $this.registrationNumber = $registrationNumber
        $this.formattedIsbn = $formattedIsbn
    }
}

class SecurityMetrics {
    [string]$targetReach
    [string]$b2cSecurityPolicy
    [string]$cyberDefenseLevel
    [string]$antiSpamEngine
    [string]$botProtectionStatus
    [string]$errorPolicy
    [int]$teamFriendsBotCapacity
    [string]$internationalStatus

    SecurityMetrics() {
        $this.targetReach = "100 Billion platforms & socials media (B2C)"
        $this.b2cSecurityPolicy = "Active - Zero Spam / Encrypted Session Verification"
        $this.cyberDefenseLevel = "Enterprise Cybersecurity Level 40 (CL40)"
        $this.antiSpamEngine = "No Spam Filter & Live Anti-Abuse Scanner"
        $this.botProtectionStatus = "100 Bots Pro Monitored Live"
        $this.errorPolicy = "Zero Error Protocol (Strict Validation)"
        $this.teamFriendsBotCapacity = 100
        $this.internationalStatus = "Worldwide Global Deployment"
    }
}

class SearchIntelligenceLink {
    [string]$topic
    [string]$googleSearchUrl
    [string]$googleNewsUrl

    SearchIntelligenceLink([string]$topic) {
        $this.topic = $topic
        $encoded = [System.Uri]::EscapeDataString($topic)
        $this.googleSearchUrl = "https://www.google.com/search?q=$encoded"
        $this.googleNewsUrl = "https://news.google.com/search?q=$encoded"
    }
}

class Cl40PortfolioRegistry {
    [string]$producer
    [string]$ownershipHeldBy
    [string[]]$brands
    [string]$musicStudio
    [string]$businessModel
    [int]$liveBotsCount
    [string]$discordUrl
    [string]$portalOfficialUrl
    [string]$legacyNotice
    [string]$biography
    [string]$asic
    [string]$issn
    [string]$ein
    [List[RegistryEntity]]$entities
    [List[IsbnRecord]]$isbnRecords
    [SecurityMetrics]$metrics
    [List[SearchIntelligenceLink]]$searchLinks

    Cl40PortfolioRegistry() {
        $this.producer = "Samir Libari"
        $this.ownershipHeldBy = "Samir Libari"
        $this.brands = @("CL40 World", "CL40 World Gaming")
        $this.musicStudio = "WR Beats"
        $this.businessModel = "B2C"
        $this.liveBotsCount = 100
        $this.discordUrl = "https://discord.gg/twRUbkhbC"
        $this.portalOfficialUrl = "https://cl40.contact"
        $this.legacyNotice = "Legacy M'Hamed Libari since active of 2010"
        $this.asic = "641 685 734"
        $this.issn = "9771234567898"
        $this.ein = "04-2888848"
        $this.biography = "Moroccan-American rapper, publisher, songwriter, music producer, actor, journalist, and technology entrepreneur Samir Libari, professionally known as Chico Loco 40, is building an international creative and technology platform through CL40 World, combining music, media, software development."

        $this.entities = [List[RegistryEntity]]::new()
        $this.entities.Add([RegistryEntity]::new("UNIVERSAL GAMING PTY LTD", "ABN 38 165 846 211", "Australian Company", "NSW 2541", "founder.american@cl40.world"))
        $this.entities.Add([RegistryEntity]::new("WORLD CO PTY LTD", "60 641 685 734", "Australian Company", "", "wrbeats@cl40.world"))
        $this.entities.Add([RegistryEntity]::new("THE WORLD OF PTY LTD", "33155584357", "Australian Company", "Member number: 110000125887", ""))

        $this.isbnRecords = [List[IsbnRecord]]::new()
        $this.isbnRecords.Add([IsbnRecord]::new("Samir Libari", "85987654", "978-4-85987-654 2"))
        $this.isbnRecords.Add([IsbnRecord]::new("WR Beats", "42072782", "978-9-4207-2782-7"))
        $this.isbnRecords.Add([IsbnRecord]::new("CL40 World", "25776047", "978-4-2577-6047-4"))
        $this.isbnRecords.Add([IsbnRecord]::new("CL40 World's Space Gaming", "77400000", "9-774000-000001"))
        $this.isbnRecords.Add([IsbnRecord]::new("QUARANTA-FOUR-ZERO", "99702549", "978-0-99-702549-1"))
        $this.isbnRecords.Add([IsbnRecord]::new("M'Hamed Libari", "64875435", "978-1-64875-435-7"))
        $this.isbnRecords.Add([IsbnRecord]::new("LB0025", "35003325", "978-0-3500-3325-5"))
        $this.isbnRecords.Add([IsbnRecord]::new("CL40 World's Space Gaming", "77400000", "9-774000-000001"))

        $this.metrics = [SecurityMetrics]::new()

        $this.searchLinks = [List[SearchIntelligenceLink]]::new()
        $topics = @(
            "Samir Libari",
            "Chico Loco 40",
            "CL40 World",
            "WR Beats",
            "CL40 World Gaming",
            "UNIVERSAL GAMING PTY LTD",
            "M'Hamed Libari",
            "cl40.contact"
        )
        foreach ($item in $topics) {
            $this.searchLinks.Add([SearchIntelligenceLink]::new($item))
        }
    }

    [void] DisplayRegistry() {
        Write-Output "=== IPI ASCAP PRODUCER & OWNERSHIP ==="
        Write-Output "Producer: $($this.producer)"
        Write-Output "Ownership: $($this.ownershipHeldBy)"
        Write-Output "Brands: $($this.brands -join ', ')"
        Write-Output "Studio: $($this.musicStudio)"
        Write-Output "Business Model: $($this.businessModel)"
        Write-Output "Live Bots Count: $($this.liveBotsCount)"
        Write-Output "Discord: $($this.discordUrl)"
        Write-Output "Official Portal: $($this.portalOfficialUrl)"
        Write-Output "Legacy Notice: $($this.legacyNotice)"
        Write-Output "ASIC: $($this.asic)"
        Write-Output "ISSN: $($this.issn)"
        Write-Output "EIN: $($this.ein)"
        Write-Output ""

        Write-Output "=== CYBERSECURITY & OPERATIONAL METRICS (B2C NO SPAM) ==="
        Write-Output "Target Reach: $($this.metrics.targetReach)"
        Write-Output "B2C Security Policy: $($this.metrics.b2cSecurityPolicy)"
        Write-Output "Cyber Defense Level: $($this.metrics.cyberDefenseLevel)"
        Write-Output "Anti-Spam Engine: $($this.metrics.antiSpamEngine)"
        Write-Output "Bot Protection Status: $($this.metrics.botProtectionStatus)"
        Write-Output "Error Policy: $($this.metrics.errorPolicy)"
        Write-Output "Team Friends Bots Capacity: $($this.metrics.teamFriendsBotCapacity)"
        Write-Output "International Work Status: $($this.metrics.internationalStatus)"
        Write-Output ""

        Write-Output "=== CORPORATE ENTITIES ==="
        foreach ($entity in $this.entities) {
            Write-Output "Entity: $($entity.entityName) | ABN: $($entity.abn) | Type: $($entity.entityType) | Location: $($entity.location) | Contact: $($entity.email)"
        }
        Write-Output ""

        Write-Output "=== ISBN / CATALOG RECORDS ==="
        foreach ($isbn in $this.isbnRecords) {
            Write-Output "Label: $($isbn.label) | ID: $($isbn.registrationNumber) | ISBN: $($isbn.formattedIsbn)"
        }
        Write-Output ""

        Write-Output "=== GOOGLE SEARCH & GOOGLE NEWS LIVE INTELLIGENCE LINKS ==="
        foreach ($link in $this.searchLinks) {
            Write-Output "Topic: $($link.topic)"
            Write-Output "  Google Search : $($link.googleSearchUrl)"
            Write-Output "  Google News   : $($link.googleNewsUrl)"
        }
        Write-Output ""

        Write-Output "=== BIOGRAPHY ==="
        Write-Output $this.biography
    }
}

$registry = [Cl40PortfolioRegistry]::new()
$registry.DisplayRegistry()
