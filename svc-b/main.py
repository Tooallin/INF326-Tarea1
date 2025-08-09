from fastapi import FastAPI
import logging
import os
import time
from random import random

app = FastAPI(title="svc-b")

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("svc-b")

@app.get("/ping")
def ping():
	logger.info("svc-b ping ok")
	return {"svc": "b", "status": "ok"}

@app.get("/compute")
def compute():
	logger.info("svc-b compute start")
	time.sleep(0.2 + random())
	logger.warning("svc-b aviso: operación costosa")
	return {"svc":"b","result":42}