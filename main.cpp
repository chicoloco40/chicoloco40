#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <curl/curl.h>

const std::string PLAYLIST_ID = "4haHr8QHyGEpXhJWQheqhN";

void triggerStream(const std::string& appId) {
    CURL* curl = curl_easy_init();
    if(curl) {
        struct curl_slist* headers = NULL;
        std::string auth = "Authorization: Bearer YOUR_OAUTH_TOKEN";
        headers = curl_slist_append(headers, auth.c_str());
        headers = curl_slist_append(headers, "Content-Type: application/json");

        std::string url = "https://api.spotify.com/v1/me/player/play";
        std::string payload = "{\"context_uri\":\"spotify:playlist:" + PLAYLIST_ID + "\"}";

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.c_str());

        CURLcode res = curl_easy_perform(curl);
        if(res == CURLE_OK) {
            std::cout << "[SUCCESS] Bot Application ID triggered: " << appId << std::endl;
        } else {
            std::cerr << "[ERROR] Bot ID " << appId << ": " << curl_easy_strerror(res) << std::endl;
        }
        curl_easy_cleanup(curl);
    }
}

int main() {
    std::cout << "Starting Spotify Automation for CL40 World Space..." << std::endl;
    
    // IDs execution loop
    std::vector<std::string> botIds = {
        "1510466709553676358", "1514809496449581086", "1548216811529441351",
        "1548227968826867774", "1548236495402438736", "1548243574385279038",
        "1548247941482025030", "1549115620270809160", "1550373414550769715"
        // Loads from list directly
    };

    for(const auto& id : botIds) {
        triggerStream(id);
    }

    return 0;
}
