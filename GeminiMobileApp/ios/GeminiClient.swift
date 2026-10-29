import Foundation

class GeminiMobileClient {
    private let targetIP = "45.219.113.102"
    private let activeModel = "gemini-2.5-flash"
    
    func sendPromptToNewYorkNode(apiKey: String, promptText: String, completion: @escaping (String) -> Void) {
        let urlString = "http://\(targetIP)/v1beta/models/\(activeModel):generateContent?key=\(apiKey)"
        guard let url = URL(string: urlString) else {
            completion("ERROR: Invalid URL configuration.")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // Structured JSON body initialization
        let payload: [String: Any] = [
            "contents": [
                ["parts": [["text": promptText]]]
            ]
        ]
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: payload, options: [])
        } catch {
            completion("ERROR: Serialization failed.")
            return
        }
        
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                completion("CRITICAL: Connection failed - \(error.localizedDescription)")
                return
            }
            guard let data = data, let responseString = String(data: data, encoding: .utf8) else {
                completion("ERROR: Empty response payload received.")
                return
            }
            completion(responseString)
        }
        task.resume()
    }
}
