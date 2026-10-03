from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Prometheus monitoring
metrics = PrometheusMetrics(app)

# In-memory product inventory
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 800,
        "quantity": 25
    }
]


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(products)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Product Inventory",
        "status": "Running",
        "endpoints": {
            "GET /items": "View products",
            "POST /items": "Add product",
            "GET /health": "Health check"
        }
    })


@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    if "name" not in data or "price" not in data or "quantity" not in data:
        return jsonify({
            "error": "name, price and quantity are required"
        }), 400

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"]
    }

    products.append(new_product)

    return jsonify({
        "message": "Product added successfully",
        "product": new_product
    }), 201


@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
        "project": "Product Inventory",
        "status": "Running",
        "endpoints": {
            "GET /items": "View products",
            "POST /items": "Add product",
            "GET /health": "Health check"
        }
    })