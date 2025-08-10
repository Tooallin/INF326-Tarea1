from fastapi import FastAPI
import logging
import os
import time
from random import randint

app = FastAPI(title="svc-a")

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("svc-a")

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