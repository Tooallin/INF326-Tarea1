# INF326-Tarea1

## Levantamiento
- Ejecutar el comando ``docker compose up -d --build``
- Para remover todo ``docker compose down --rmi all --volumes --remove-orphans``

## Estructura Loki
Se utilizó **Grafana Loki 2.9.8** para almacenar y consultar logs. Se monta el archivo de configuración ``loki-config.yml`` en el contenedor. Utiliza el puerto **3100** para que el resto de servicios le envien y consulten logs. Los datos persistentes son almacenados en el volumen ``loki-data``. Posee un ``healthcheck`` que va revisando cada 10 segundos si es que el servicio esta listo.

## Estructura Promtail
Se utilizó **Grafana Promtail 2.9.8** para recolectar logs de los contenedores y enviarlos a Loki. Se monta el archivo de configuración ``promtail-config.yml``. Arranca solo cuando Loki este disponible.

## Estructura Grafana
Se utilizó **Grafana 11.0.0** para visualizar los datos. Las credenciales definidas por defecto corresponden a ``admin/admin`` (user/password). Posee volumenes para la persistencia de configuraciones y dashboards. Arranca solo cuando Loki este disponible. Esta se encuentra disponible en:
-http://localhost:3000/

## Service A (svc-a)
Servicio creado mediante **FastAPI**. Posee dos endpoints, ``/ping`` (para verificar el estado del servicio), ``/work`` (inicia un trabajo de duración aleatoria) y ``/makework`` (contacta con svc-b y lo hace trabajar). Los endpoints corresponden a:
-http://localhost:8001/ping
-http://localhost:8001/work
-http://localhost:8001/makework

## Service B (svc-b)
Servicio creado mediante **FastAPI**. Posee dos endpoints, ``/ping`` (para verificar el estado del servicio), ``/work`` (inicia un trabajo de duración aleatoria) y ``/makework`` (contacta con svc-a y lo hace trabajar). Los endpoints corresponde a:
-http://localhost:8002/ping
-http://localhost:8002/work
-http://localhost:8002/makework