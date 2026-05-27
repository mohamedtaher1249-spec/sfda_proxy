from fastapi import FastAPI
import httpx
import base64

app = FastAPI()

@app.get("/token")
async def get_token():
    client_id = "YOUR_SFDA_CLIENT_ID"
    client_secret = "YOUR_SFDA_CLIENT_SECRET"
    
    credentials = base64.b64encode(
        f"{client_id}:{client_secret}".encode()
    ).decode()
    
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(
            "https://apis.sfda.gov.sa:9002/v2/oauth/accesstoken",
            params={"grant_type": "client_credentials"},
            headers={"Authorization": f"Basic {credentials}"},
            timeout=30
        )
    return response.json()
