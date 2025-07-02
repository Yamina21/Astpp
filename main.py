from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

ASTPP_API_URL = "https://transactions.unifiedcom.cloud"
API_AUTH_KEY = "HA39iPY7X2OFUQoQKw1MaiwZwVioQdw7"  # From astpp-config.conf




@app.post("/create-customer")
async def create_customer():
    endpoint = "/admin/customer/"

    headers = {
        "x-auth-token": "HA39iPY7X2OFUQoQKw1MaiwZwVioQdw7",
        "Content-Type": "application/json"
    }
    customer_data = {
        
        "token": "Qiszd3AwQUN4bkVzTTZSTWpjUTBWUT09",
        "action": "customer_create",
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "yaminaguenez@gmail.com",
        "company_name": "DemoNet Ltd.",
        "address_1": "123 Demo Street",
        "city": "Algiers",
        "province": "Algiers-Centre",
        "postal_code": "16000",
        "reseller_id": "2",
        "telephone_1": "+213770112233",
        "sweep_id": "2",
        "posttoexternal": "1",
        "invoice_day": "28",
        "tax_number": "DZ123456789"
        }



    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(
                f"{ASTPP_API_URL}{endpoint}",
                json=customer_data,
                headers=headers
            )
        if response.status_code == 200:


            return {"message": "Customer created successfully", "data": response.json()}
        
        else:
            print("Status Code:", response.status_code)
            print("Headers:", response.headers)
            print("Body:", response.text)
            raise HTTPException(status_code=response.status_code, detail=response.text)
       

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