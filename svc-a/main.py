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
	logger.info("svc-a ping recibido")
	return {"svc": "a", "status": "ok"}

@app.get("/work")
def work():
	duration = randint(50, 250) / 1000
	logger.info(f"svc-a inicia trabajo; duracion_esperada_ms={int(duration*1000)}")
	time.sleep(duration)
	if randint(0,9) == 0:
		logger.error("svc-a error simulado en /work")
		return {"svc":"a","ok":False}
	logger.info("svc-a trabajo completado")
	return {"svc":"a","ok":True}