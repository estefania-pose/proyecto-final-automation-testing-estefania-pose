import pytest
import requests
from faker import Faker
from utils.logger import logger

fake = Faker()

@pytest.mark.api
@pytest.mark.smoke
def test_get_lista_posts(base_url_posts):
    """Valida obtención de recursos con GET (status, headers, estructura y tiempo)."""
    logger.info("API GET: Consultando lista de posts")
    resp = requests.get(base_url_posts)
    
    assert resp.status_code == 200
    assert "application/json" in resp.headers["Content-Type"]
    assert resp.elapsed.total_seconds() < 2.0
    
    data = resp.json()
    assert len(data) > 0
    assert {"userId", "id", "title", "body"} <= set(data[0].keys())

@pytest.mark.api
def test_get_post_inexistente(base_url_posts):
    """Escenario negativo: valida código 404 ante un ID que no existe."""
    logger.info("API GET negativo: Consultando post inexistente")
    resp = requests.get(f"{base_url_posts}/999999")
    assert resp.status_code == 404

@pytest.mark.api
@pytest.mark.e2e
def test_ciclo_vida_crud_post(base_url_posts):
    """Flujo CRUD completo encadenado: POST -> PUT -> PATCH -> DELETE."""
    # 1. POST (Crear con datos aleatorios de Faker)
    payload_crear = {
        "title": fake.sentence(nb_words=4),
        "body": fake.text(max_nb_chars=60),
        "userId": 1
    }
    logger.info(f"API POST: Creando post '{payload_crear['title']}'")
    resp_post = requests.post(base_url_posts, json=payload_crear)
    assert resp_post.status_code == 201
    nuevo_post = resp_post.json()
    assert "id" in nuevo_post
    post_id = 1  # JSONPlaceholder simula IDs nuevos en 101, usamos 1 para PUT/PATCH/DELETE reales

    # 2. PUT (Reemplazo total)
    payload_put = {"id": post_id, "title": "Título Reemplazado", "body": "Cuerpo nuevo", "userId": 1}
    logger.info("API PUT: Reemplazando recurso completo")
    resp_put = requests.put(f"{base_url_posts}/{post_id}", json=payload_put)
    assert resp_put.status_code == 200
    assert resp_put.json()["title"] == "Título Reemplazado"

    # 3. PATCH (Actualización parcial)
    logger.info("API PATCH: Actualizando solo el título")
    resp_patch = requests.patch(f"{base_url_posts}/{post_id}", json={"title": "Título Parcial"})
    assert resp_patch.status_code == 200
    assert resp_patch.json()["title"] == "Título Parcial"

    # 4. DELETE (Eliminación)
    logger.info("API DELETE: Eliminando post")
    resp_del = requests.delete(f"{base_url_posts}/{post_id}")
    assert resp_del.status_code == 200