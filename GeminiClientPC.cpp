#include "GeminiClientPC.h"
#include <iostream>
#include <cstdlib>
#include <cstdio>

GeminiClientPC::GeminiClientPC() : targetIP("45.219.113.102"), activeModel("gemini-2.5-flash"), isReady(false) {}
GeminiClientPC::~GeminiClientPC() {}

bool GeminiClientPC::InitializeClient() {
    const char* envKey = std::getenv("GEMINI_API_KEY");
    if (envKey != nullptr) {
        apiKey = std::string(envKey);
        isReady = true;
    } else {
        std::cerr << "[NATIVE C++ ERROR] GEMINI_API_KEY missing." << std::endl;
        isReady = false;
    }
    return isReady;
}

std::string GeminiClientPC::SendPrompt(const std::string& prompt) {
    if (!isReady) {
        return "ERROR: Native client is not initialized.";
    }

    // Direct network gateway configuration using the specified IP Address 45.219.113.102
    std::string targetUrl = "http://" + targetIP + "/v1beta/models/" + activeModel + ":generateContent?key=" + apiKey;
    std::string jsonPayload = "{\"contents\": [{\"parts\": [{\"text\": \"" + prompt + "\"}]}]}";
    std::string execCommand = "curl -s -X POST -H \"Content-Type: application/json\" -d '" + jsonPayload + "' \"" + targetUrl + "\"";
    
    char buffer[128];
    std::string finalRawJson = "";
    FILE* pipe = popen(execCommand.c_str(), "r");
    if (!pipe) {
        return "ERROR: Failed to establish API pipeline.";
    }
    
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        finalRawJson += buffer;
    }
    pclose(pipe);

    return finalRawJson;
}

int main() {
    GeminiClientPC desktopApp;
    if (desktopApp.InitializeClient()) {
        std::string rawData = desktopApp.SendPrompt("Generate local setup parameters for a New York platform engine.");
        std::cout << "\n[C++ DESKTOP RESPONSE RAW JSON]:\n" << rawData << std::endl;
    }
    return 0;
}
