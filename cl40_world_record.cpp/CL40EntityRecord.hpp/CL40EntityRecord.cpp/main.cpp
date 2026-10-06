#include <iostream>
#include <string>
#include <vector>

struct EntityRecord {
    std::string ipiAscapProducer;
    std::string ownership;
    std::vector<std::string> brands;
    std::string rightsStudio;
    std::string businessModel;
    std::string discordUrl;
    int discordLiveBotsCount;

    // CL40 Worlds Space (Gaming)
    std::string gamingFounderEmail;
    std::string gamingEntityName;
    std::string gamingAbn;
    std::string gamingEntityType;
    std::string gamingPostcodeLocation;

    // WR Beats Section
    std::string wrBeatsOwnerPublisherStudioCopyright;
    std::string wrBeatsEmail1;
    std::string wrBeatsEmail2;
    std::string wrBeatsAbn;
    std::string wrBeatsCompanyName;

    // Samir Libari Section
    std::string owner;
    std::string memberNumber;
    std::string memberCompanyName;
    std::string memberAbn;

    // ISBN Registry
    std::vector<std::pair<std::string, std::pair<std::string, std::string>>> isbnList;

    // Identifiers
    std::string asic;
    std::string issn;
    std::string ein;

    // Portal & Target Info
    std::string portalUrl;
    std::string targetDescription;

    // Biography & Profile
    std::string biography;
};

EntityRecord createCl40WorldRecord() {
    EntityRecord record;

    record.ipiAscapProducer = "Samir Libari";
    record.ownership = "Samir Libari";
    record.brands = {
        "CL40 World (Australia)",
        "CL40 World Gaming (Nowra, Australia)"
    };
    record.rightsStudio = "WR Beats studio and music publishing house (an international brand)";
    record.businessModel = "B2C";
    record.discordUrl = "https://discord.gg/twRUbkhbC";
    record.discordLiveBotsCount = 100;

    // CL40 Worlds Space (Gaming)
    record.gamingFounderEmail = "founder.american@cl40.world";
    record.gamingEntityName = "UNIVERSAL GAMING PTY LTD";
    record.gamingAbn = "ABN 38 165 846 211";
    record.gamingEntityType = "Australian Company";
    record.gamingPostcodeLocation = "NSW 2541";

    // WR Beats Section
    record.wrBeatsOwnerPublisherStudioCopyright = "WR Beats";
    record.wrBeatsEmail1 = "wrbeats@cl40.world";
    record.wrBeatsEmail2 = "wrbeats.global@gmail.com";
    record.wrBeatsAbn = "60 641 685 734";
    record.wrBeatsCompanyName = "WORLD CO PTY LTD";

    // Samir Libari Section
    record.owner = "Samir Libari";
    record.memberNumber = "110000125887";
    record.memberCompanyName = "THE WORLD OF PTY LTD";
    record.memberAbn = "33155584357";

    // ISBN Registry
    record.isbnList = {
        {"Samir Libari", {"85987654", "978-4-85987-654 2"}},
        {"WR Beats", {"42072782", "978-9-4207-2782-7"}},
        {"CL40 World", {"25776047", "978-4-2577-6047-4"}},
        {"CL40 World's Space Gaming", {"77400000", "9-774000-000001"}},
        {"QUARANTA-FOUR-ZERO", {"99702549", "978-0-99-702549-1"}},
        {"M'Hamed Libari", {"64875435", "978-1-64875-435-7"}},
        {"LB0025", {"35003325", "978-0-3500-3325-5"}},
        {"CL40 World's Space Gaming", {"77400000", "9-774000-000001"}}
    };

    record.asic = "641 685 734";
    record.issn = "9771234567898";
    record.ein = "04-2888848";

    record.portalUrl = "https://cl40.contact";
    record.targetDescription = "Target: 100 Billion of platforms and socials media (B2C) LIVE of link portal official: https://cl40.contact and editor panel google international gravatar and images panel no independnet Chico Loco 40 International and Label CL40 World and Gaming of 100 bots pro and Legacy M'Hamed Libari since active of 2010";

    record.biography = "Moroccan-American rapper, publisher, songwriter, music producer, actor, journalist, and technology entrepreneur Samir Libari, professionally known as Chico Loco 40, is building an international creative and technology platform through CL40 World, combining music, media, software development.";

    return record;
}

void printEntityRecord(const EntityRecord& record) {
    std::cout << "IPI ASCAP Producer: " << record.ipiAscapProducer << "\n";
    std::cout << "Ownership: " << record.ownership << "\n";
    std::cout << "Brands:\n";
    for (const auto& brand : record.brands) {
        std::cout << "  - " << brand << "\n";
    }
    std::cout << "Rights Studio: " << record.rightsStudio << "\n";
    std::cout << "Business Model: " << record.businessModel << "\n";
    std::cout << "Discord URL: " << record.discordUrl << " (" << record.discordLiveBotsCount << " live bots)\n";

    std::cout << "\nCL40 Worlds Space (Gaming)\n";
    std::cout << "Founder Email: " << record.gamingFounderEmail << "\n";
    std::cout << "Entity Name: " << record.gamingEntityName << "\n";
    std::cout << "ABN: " << record.gamingAbn << "\n";
    std::cout << "Entity Type: " << record.gamingEntityType << "\n";
    std::cout << "Location: " << record.gamingPostcodeLocation << "\n";

    std::cout << "\n------------------------------------------------------\n";
    std::cout << "Owner/Publisher/Studio/Copyright: " << record.wrBeatsOwnerPublisherStudioCopyright << "\n";
    std::cout << "wrbeats Email 1: " << record.wrBeatsEmail1 << "\n";
    std::cout << "wrbeats Email 2: " << record.wrBeatsEmail2 << "\n";
    std::cout << "wrbeats ABN: " << record.wrBeatsAbn << "\n";
    std::cout << "Company Name: " << record.wrBeatsCompanyName << "\n";

    std::cout << "------------------------------------------------------\n";
    std::cout << "Owner: " << record.owner << "\n";
    std::cout << "Member Number: " << record.memberNumber << "\n";
    std::cout << "Company Name: " << record.memberCompanyName << "\n";
    std::cout << "ABN: " << record.memberAbn << "\n";
    std::cout << "-----------------------\n";

    std::cout << "ISBN Registry:\n";
    for (const auto& item : record.isbnList) {
        std::cout << "  ISBN: " << item.first << " / " << item.second.first << " / " << item.second.second << "\n";
    }

    std::cout << "\nASIC: " << record.asic << "\n";
    std::cout << "ISSN: " << record.issn << "\n";
    std::cout << "EIN: " << record.ein << "\n";
    std::cout << "Official Portal: " << record.portalUrl << "\n";
    std::cout << "Target: " << record.targetDescription << "\n";
    std::cout << "\nBiography:\n" << record.biography << "\n";
}

int main() {
    EntityRecord cl40Record = createCl40WorldRecord();
    printEntityRecord(cl40Record);
    return 0;
}
