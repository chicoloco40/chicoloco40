#ifndef GEMINI_CLIENT_PC_H
#define GEMINI_CLIENT_PC_H

#include <string>

class GeminiClientPC {
public:
    GeminiClientPC();
    ~GeminiClientPC();

    bool InitializeClient();
    std::string SendPrompt(const std::string& prompt);

private:
    std::string apiKey;
    std::string targetIP;
    std::string activeModel;
    bool isReady;
};

#endif // GEMINI_CLIENT_PC_H
