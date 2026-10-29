package com.cl40world.newyorkapp

import java.net.URL
import java.net.HttpURLConnection
import java.io.OutputStreamWriter
import org.json.JSONObject

class GeminiMobileClient {
    private val targetIP = "45.219.113.102"
    private val activeModel = "gemini-2.5-flash"

    fun sendPromptToNewYorkNode(apiKey: String, promptText: String): String {
        return try {
            val urlString = "http://$targetIP/v1beta/models/$activeModel:generateContent?key=$apiKey"
            val url = URL(urlString)
            val connection = url.openConnection() as HttpURLConnection
            connection.requestMethod = "POST"
            connection.setRequestProperty("Content-Type", "application/json")
            connection.doOutput = true

            // Escaped standard JSON Payload mapping variables
            val payload = JSONObject().apply {
                put("contents", org.json.JSONArray().put(JSONObject().apply {
                    put("parts", org.json.JSONArray().put(JSONObject().apply {
                        put("text", promptText)
                    }))
                }))
            }

            val writer = OutputStreamWriter(connection.outputStream)
            writer.write(payload.toString())
            writer.flush()

            val responseCode = connection.responseCode
            if (responseCode == HttpURLConnection.HTTP_OK) {
                connection.inputStream.bufferedReader().use { it.readText() }
            } else {
                "ERROR: Target node returned system status $responseCode"
            }
        } catch (e: Exception) {
            "CRITICAL: Connection failed - ${e.message}"
        }
    }
}
