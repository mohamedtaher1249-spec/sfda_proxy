from fastapi import FastAPI
import httpx
import base64
import logging

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running"}

@app.get("/token")
async def get_token():
    try:
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
            logging.debug(f"Status: {response.status_code}")
            logging.debug(f"Response: {response.text}")
            return response.json()

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}
