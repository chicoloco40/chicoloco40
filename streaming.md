      - name: Build with Next.js
        run: npm run build && npm run export    # ensure export exists if you rely on ./out
        env:
          # Site (public)
          NEXT_PUBLIC_SITE_URL: https://cl40.contact

          # Spotify (client id is public; client secret should NOT be here)
          NEXT_PUBLIC_SPOTIFY_CLIENT_ID: ${{ secrets.SPOTIFY_CLIENT_ID }}

          # Discord (public values okay; secrets must not be exposed)
          NEXT_PUBLIC_DISCORD_APPLICATION_ID: ${{ secrets.DISCORD_APPLICATION_ID }}
          NEXT_PUBLIC_DISCORD_PUBLIC_KEY: ${{ secrets.DISCORD_PUBLIC_KEY }}
          NEXT_PUBLIC_DISCORD_INVITE: https://discord.gg/SzqSrCHJH
          NEXT_PUBLIC_DISCORD_CLIENT_ID: ${{ secrets.DISCORD_CLIENT_ID }}

          # Webhook B2C — DO NOT expose this to the client
          B2C_WEBHOOK: ${{ secrets.B2C_WEBHOOK }}
