from fastapi import FastAPI
import logging
import os
import time
from random import randint

app = FastAPI(title="svc-b")

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("svc-b")

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