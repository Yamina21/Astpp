from fastapi import FastAPI, HTTPException
import httpx
from typing import Optional, Dict, Any
import logging



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
ASTPP_API_URL = "https://transactions.unifiedcom.cloud"
API_AUTH_KEY = "HA39iPY7X2OFUQoQKw1MaiwZwVioQdw7"  # From astpp-config.conf

from fastapi import FastAPI, HTTPException
import httpx
import json
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("astpp")

ASTPP_API_URL = "https://transactions.unifiedcom.cloud"

@app.post("/create-customer")
async def create_customer():
    endpoint = "/admin/customer/"

    headers = {
        "x-auth-token": "HA39iPY7X2OFUQoQKw1MaiwZwVioQdw7", #api_auth_key in astpp-config.conf
        "Content-Type": "application/json"
    }

    customer_data = {
        "id":"5", #Admin ID
        "token": "Qiszd3AwQUN4bkVzTTZSTWpjUTBWUT09", #Get token after login successfuly  
        "action": "customer_create",               
        "first_name": "yamina",
        "last_name": "test",
        "email": "yaminaguenez@gmail.com",
        "company_name": "DemoNet Ltd.",
        "address_1": "123 Demo Street",
        "city": "Algiers",
        "province": "",
        "postal_code": "16000",
        "reseller_id": "",
        "telephone_1": "+213658453511",
        "sweep_id": "",
        "posttoexternal": "1",
        "invoice_day": "28",
        "tax_number": "123456789"
    }

    logger.info("Sending customer creation request to: %s", f"{ASTPP_API_URL}{endpoint}")
    logger.info("Headers: %s", json.dumps(headers, indent=2))
    logger.info("Payload: %s", json.dumps(customer_data, indent=2))

    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(
            f"{ASTPP_API_URL}{endpoint}",
            json=customer_data,
            headers=headers
        )

        logger.info("Response Status Code: %s", response.status_code)
        logger.info("Response Headers: %s", response.headers)
        logger.info("Response Body: %s", response.text)

        if response.status_code == 200:
            return {"message": "Customer created successfully", "data": response.json()}
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )


@app.post("/login")
async def login():
    login_data = {
        "username": "faridjema",
        "password": "dbgbZ3X@",
        "device_id": "75037171-014d-4e41-aa7a-c886001146a3",
        "callkit_token": "BE6CAF775FFC2C1AAD28D9992E467156F044D68D21C59E4973C3A692DACAB03C",
        "apns_token": "63c7620a2c5ce0a1717850ecb559fb994c57bc6180f49c2e815efab09421f924",
        "mobile_type": "PC"
    }

    endpoint = "/api/login/"

    headers = {
        "x-auth-token": "HA39iPY7X2OFUQoQKw1MaiwZwVioQdw7",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient(verify=False, timeout=10.0) as client:
            response = await client.post(
                f"{ASTPP_API_URL}{endpoint}",
                json=login_data,
                headers=headers
            )
            print(f"Login attempt at {endpoint}: {response.status_code}")
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"Login failed with status code {response.status_code}",
                    "details": response.text
                }
    except httpx.RequestError as exc:
        return {
            "error": "Connection failed",
            "details": str(exc)
        }