from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from pydantic import BaseModel;
from algoritmo import algoritmo_quine_mccluesky;

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
);

class RequisicaoQuine(BaseModel):
    mintermos: list[int];
    bits: int;

@app.post("/minimizar")
def minimizar_funcao(dados: RequisicaoQuine):
    resultado = algoritmo_quine_mccluesky(dados.mintermos, dados.bits);
    return {
        "expressao": resultado
    }