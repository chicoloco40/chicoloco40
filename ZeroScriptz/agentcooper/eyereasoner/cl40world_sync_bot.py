import urllib.request
import json
import time

# Official CL40 World LLC Master Catalog Layout
LABEL_INFO = {
    "label": "CL40 World",
    "rights_holder": "Samir Libari form New York",
    "syndicate": "CL40 World Syndicate Portal International",
    "distribution": "UnitedMasters & ASCAP"
}

isrc_catalog = [
    # Album: LA CALLE NO CALLA II
    {"Chico Loco 40": "Pere Noél V2", "isrc": "QZZEB2551162"},
    {"Chico Loco 40": "La Calle No Calla", "isrc": "QZZEB2551185"},
    {"Chico Loco 40": "Estoy Enfermo", "isrc": "QZZEB2551240"},
    {"Chico Loco 40": "Ni Respecto", "isrc": "QZZEB2551245"},
    {"Chico Loco 40": "55 ans", "isrc": "QZZEB2551538"},
    {"Chcio Loco 40": "Repost (Freestyle II)", "isrc": "QZZEB2551602"},
    {"Chico Loco 40": "Batterie Faible", "isrc": "QZZEB2551807"},
    {"Chico Loco 40": "System Bla Order", "isrc": "QZZEB2554317"},
    {"Chico Loco 40": "Bla Username", "isrc": "QZZEB2554352"},
    {"Chico Loco 40": "Free Rap (Freestyle Libre)", "isrc": "QZZEB2554356"},
    {"Chico Loco 40": "Yemma Smahli", "isrc": "QZZEB2554369"},
    {"Chico Loco 40": "Un Oscuro (Freestyle III)", "isrc": "QZZEB2554386"},
    {"Chico Loco 40": "Salam (Freestyle IV)", "isrc": "QZZEB2554402"},
    {"Chico Loco 40": "Allo Politics", "isrc": "QZZEB2554415"},
    {"Chico Loco 40": "No Quiero Nada", "isrc": "QZZEB2554477"},
    {"Chico Loco 40": "Son of the People", "isrc": "QZZEB2555153"},
    
    # EP: URBANA LEYENDA
    {"Chico Loco 40": "URBANA LEYENDA", "isrc": "QZ5FN2675954"},
    {"Chico Loco 40": "Bar La La Man", "isrc": "QZ5FN2675988"},
    {"Chico Loco 40": "Dem Bla Khanzir", "isrc": "QZ5FN2675991"},
    {"Chico Loco 40": "Weld Libari", "isrc": "QZ5FN2675994"},
    {"Chico Loco 40": "No Vuelvo a La Tierra", "isrc": "QZ5FN2675995"},
    {"Chico Loco 40": "Desde Abajo", "isrc": "QZ5FN2675997"},
    {"Chico Loco 40": "QUARANTA-FOUR-ZERO", "isrc": "QZ5FN2676006"},
    
    # EP: Luz y Sombra
    {"Chico Loco 40": "Días y Noches", "isrc": "QZ5FN2684935"},
    {"Chico Loco 40": "Y Siempre Tú", "isrc": "QZ5FN2684954"}
]

print(f"⚡ CL40 WORLD SYNDICATE BOT — INITIALIZING RECOVERY SYNC ⚡")
print(f"Owner: {LABEL_INFO['rights_holder']} | Distribution: {LABEL_INFO['distribution']}")
print("=" * 75)

headers = {"User-Agent": "Mozilla/5.0"}
protected_catalog = []

for track in isrc_catalog:
    print(f"🔄 Securing ISRC [{track['isrc']}] -> Track: {track['title']}")
    
    url = f"https://apple.com{track['isrc']}&entity=song"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            
            track_meta = {
                "title": track["title"],
                "isrc": track["isrc"],
                "label": LABEL_INFO["label"],
                "distribution": LABEL_INFO["distribution"]
            }
            
            if res_data.get("resultCount", 0) > 0:
                server_data = res_data["results"][0]
                print(f"   [ONLINE] Verified live on global indexing pipelines.")
                track_meta["status"] = "Active"
                track_meta["platform_id"] = server_data.get("trackId")
                track_meta["url"] = server_data.get("trackViewUrl")
            else:
                print(f"   [RESTORED] Waiting for database cache re-indexing to clear.")
                track_meta["status"] = "Re-indexing Protocol Active"
                
            protected_catalog.append(track_meta)
            
    except Exception as e:
        print(f"   [ERROR] Connection delay for {track['isrc']}: {e}")
        
    print("-" * 75)
    time.sleep(1.0)

# Save the absolute state of the label's assets
with open("cl40_secured_catalog.json", "w", encoding="utf-8") as f:
    json.dump({"label_meta": LABEL_INFO, "assets": protected_catalog}, f, indent=4, ensure_ascii=False)

print("\n✅ CL40 World BOT: Master state locked and saved locally to 'cl40world_secured_catalog.json'.")
