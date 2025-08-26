from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI()

# Ruta /predict de prueba
@app.get("/predict")
def predict_root():
    return {"message": "🚀 Bienvenido a DeepVision API con FastAPI"}
