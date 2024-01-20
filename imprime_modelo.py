import transformers

# Obtiene información sobre el modelo
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
info = transformers.models.info("a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5")

# Imprime la información del modelo
print(info)