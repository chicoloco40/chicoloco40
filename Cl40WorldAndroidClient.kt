package com.cl40world.newyorkapp

import java.net.URL
import java.net.HttpURLConnection
import java.io.OutputStreamWriter
import org.json.JSONObject
import org.json.JSONArray

class Cl40WorldAndroidClient {
    // Hardware Context: Samsung Galaxy Android Engine
    private val gatewayIP = "45.219.113.102"
    private val targetModel = "gemini-2.5-flash"

    fun executeGalaxyStream(systemKey: String, userPrompt: String): String {
        return try {
            val endpoint = "http://$gatewayIP/v1beta/models/$targetModel:generateContent?key=$systemKey"
            val url = URL(endpoint)
            val connection = url.openConnection() as HttpURLConnection
            connection.requestMethod = "POST"
            connection.setRequestProperty("Content-Type", "application/json")
            connection.doOutput = true

            val payload = JSONObject().apply {
                put("contents", JSONArray().put(JSONObject().apply {
                    put("parts", JSONArray().put(JSONObject().apply {
                        put("text", userPrompt)
                    }))
                }))
            }

            val writer = OutputStreamWriter(connection.outputStream)
            writer.write(payload.toString())
            writer.flush()

            if (connection.responseCode == HttpURLConnection.HTTP_OK) {
                connection.inputStream.bufferedReader().use { it.readText() }
            } else {
                "SAMSUNG-GALAXY-ERROR: Node returned status ${connection.responseCode}"
            }
        } catch (e: Exception) {
            "SAMSUNG-GALAXY-CRITICAL: Pipeline down - ${e.message}"
        }
    }
}
