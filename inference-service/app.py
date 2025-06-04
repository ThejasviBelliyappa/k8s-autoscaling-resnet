from flask import Flask, request, jsonify
import torch
from torchvision import models, transforms
from PIL import Image
import io

app = Flask(__name__)
model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

@app.route("/infer", methods=["POST"])
def infer():
    image = Image.open(io.BytesIO(request.data))
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    pred = torch.argmax(output, 1).item()
    return jsonify({'class': int(pred)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
