from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    # run the C++ binary
    result = subprocess.run(["./my_cpp_app"], capture_output=True, text=True)
    print(result.stdout)

    # read output written by C++
    with open("cpp_module_output.txt") as f:
        cpp_output = f.read().strip()

    return jsonify({
        "message": "Hello from Python Flask!",
        "cpp_output": cpp_output
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
