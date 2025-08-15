from fastapi import FastAPI, HTTPException
import logging
import os
import time
from random import randint
import httpx

app = FastAPI(title="svc-b")

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("svc-b")

SVC_A_URL = os.getenv("SVC_A_URL", "http://svc-a:8000").rstrip("/")

@app.get("/ping")
def ping():
	logger.info("[SVC-B] Ping recibido")
	return {"svc": "b", "status": "ok"}

@app.get("/work")
def work():
	duration = randint(50, 250) / 1000
	logger.info("[SVC-B] Inicia trabajo")
	time.sleep(duration)
	logger.info(f"[SVC-B] Trabajo completado tras: {int(duration*1000)} ms")
	return {"svc":"b", "work": "done"}

@app.get("/makework")
async def makework():
	logger.info("[SVC-B] Haciendo trabajar a svc-a")
	try:
		async with httpx.AsyncClient(timeout=2.0) as client:
			resp = await client.get(f"{SVC_A_URL}/work")
			resp.raise_for_status()
			data = resp.json()
			logger.info("[SVC-B] Trabajo completado por svc-a")
			return {"svc": "b", "svc-a-response": data}
	except Exception as e:
		logger.exception(f"[SVC-B] Error al contactar con svc-a por la URL {SVC_A_URL}")
		raise HTTPException(status_code=502, detail=f"svc-a-error: {e}")