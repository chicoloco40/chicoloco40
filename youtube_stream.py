import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# List dyal YouTube Playlists w Links dyalk
youtube_links = [
    "https://www.youtube.com/watch?v=BsLFnZcO0jU&list=OLAK5uy_l0DNrUIxmX8KmlOj2aMKi7YiJDyUrUfE0",
    "https://www.youtube.com/watch?v=Miz9B5h1Rsk&list=OLAK5uy_msBiW_RpElEZ1Um_Ch3Bv7vVKs8551I3I",
    "https://www.youtube.com/watch?v=hpPcJAt44jM&list=OLAK5uy_kTTYk4AAHIMbKcVE9acb3nXEBSDSqfVzQ",
    "https://www.youtube.com/watch?v=4CSGRsHGh7Q&list=OLAK5uy_kGlBntSLZX9l9vo3XuObquhGFGCE4ivpY",
    "https://www.youtube.com/watch?v=NvLGEhgpoe0&list=PLAKJfHyNgaLE&index=1"
]

def stream_playlist(url):
    options = Options()
    options.add_argument("--headless")  # B했지만 background bla GUI
    options.add_argument("--mute-audio") # Optional: bash t-kon l-khdma stable f VPS
    options.add_argument("--autoplay-policy=no-user-gesture-required")
    
    driver = webdriver.Chrome(options=options)
    try:
        print(f"[STREAM ACTIVE] Opening: {url}")
        driver.get(url)
        time.sleep(600)  # 10 minutes stream duration kol link (t-9dr t-zidha)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True: # Loop infinite bach yb9aw shammalin
        for link in youtube_links:
            stream_playlist(link)
