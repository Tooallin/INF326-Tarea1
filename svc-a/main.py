from fastapi import FastAPI, HTTPException
import logging
import os
import time
from random import randint
import httpx

app = FastAPI(title="svc-a")

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("svc-a")

SVC_B_URL = os.getenv("SVC_B_URL", "http://svc-a:8000").rstrip("/")

@app.get("/ping")
def ping():
	logger.info("[SVC-A] Ping recibido")
	return {"svc": "a", "status": "ok"}

@app.get("/work")
def work():
	duration = randint(50, 250) / 1000
	logger.info("[SVC-A] Inicia trabajo")
	time.sleep(duration)
	logger.info(f"[SVC-A] Trabajo completado tras: {int(duration*1000)} ms")
	return {"svc":"a", "work": "done"}

@app.get("/makework")
async def makework():
	logger.info("[SVC-A] Haciendo trabajar a svc-b")
	try:
		async with httpx.AsyncClient(timeout=2.0) as client:
			resp = await client.get(f"{SVC_B_URL}/work")
			resp.raise_for_status()
			data = resp.json()
			logger.info("[SVC-A] Trabajo completado por svc-b")
			return {"svc": "a", "svc-b-response": data}
	except Exception as e:
		logger.exception(f"[SVC-A] Error al contactar con svc-b por la URL {SVC_B_URL}")
		raise HTTPException(status_code=502, detail=f"svc-b-error: {e}")