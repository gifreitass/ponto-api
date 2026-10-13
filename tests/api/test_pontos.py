from fastapi.testclient import TestClient

def test_criar_ponto(client: TestClient) -> None:
    response = client.post(
        "/pontos",
        json={
            "funcionario_nome": "Claudia",
            "tipo": "almoço"
        }
    )

    body = response.json()

    assert response.status_code == 200
    assert body["funcionario_nome"] == "Claudia"
    assert body["tipo"] == "almoço"
    assert body["id"] is not None
    assert body["data_hora"] is not None

def test_listar_pontos(client: TestClient) -> None:
    criar = client.post(
        "/pontos/",
        json={
            "funcionario_nome": "Pedro Souza",
            "tipo": "entrada"
        }
    )

    assert criar.status_code == 200

    ponto_criado = criar.json()

    response = client.get("/pontos")

    assert response.status_code == 200

    pontos = response.json()

    assert isinstance(pontos, list)
    assert any(
        ponto["id"] == ponto_criado["id"]
        for ponto in pontos
    )
