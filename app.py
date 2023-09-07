import os
import platform
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_file", methods=["POST"])
def run_file():
    try:
        # Get the selected file name from the POST request
        file_name = request.json["file"]
        
        # Define the path to the directory where your .arexport files are stored
        file_directory = "uploads"  # Adjust this path accordingly

        # Construct the full path to the selected .arexport file
        file_path = os.path.join(file_directory, file_name)

        # Determine the appropriate command to open the file based on the operating system
        if platform.system() == "Windows":
            os.system(f"start {file_path}")  # On Windows, use "start" command
        elif platform.system() == "Linux":
            os.system(f"xdg-open {file_path}")  # On Linux, use "xdg-open"
        elif platform.system() == "Darwin":
            os.system(f"open {file_path}")  # On macOS, use "open"
        else:
            return jsonify({"status": "error", "message": "Unsupported operating system"})

        return jsonify({"status": "success", "message": "File opened successfully"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
