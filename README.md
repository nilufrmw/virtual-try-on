# Virtual Try-On Web App

A minimal, full-stack Virtual Try-On web application. It takes an upper-body photo of a person and an image of a garment, then uses the open-source IDM-VTON model hosted on Hugging Face to generate an image of the person wearing that garment.

---

## How It Works

1. Frontend: A clean, responsive interface to select a person photo and a clothing item with instant file previews.
2. Backend (Flask): Temporarily saves both files to an uploads/ directory.
3. Inference (Hugging Face ZeroGPU): Uses gradio_client to offload heavy diffusion model execution to remote GPU servers—no local GPU needed.
4. Result: Once inference completes, the rendered image streams back to the browser alongside a live timer.

---

## Project Structure

virtual-tryon/
├── app.py              # Flask server and Gradio API client
├── templates/
│   └── index.html      # Frontend UI (HTML, CSS, Vanilla JS)
├── uploads/            # Temporary storage for uploaded images
└── README.md

---

## Prerequisites

- Python 3.10+
- A free Hugging Face account for an API access token.

---

## Setup & Installation

1. Enter the project directory:
   cd ~/virtual-tryon

2. Install dependencies:
   pip3 install flask gradio_client werkzeug --break-system-packages

3. Generate a free Hugging Face access token:
   - Navigate to huggingface.co/settings/tokens
   - Create a token with "Read" permissions and copy it.

4. Set the token in app.py:
   client = Client("yisol/IDM-VTON", token="hf_your_token_here")

---

## Running the Application

1. Start the Flask server:
   python3 app.py

2. Open in a web browser:
   http://127.0.0.1:5000

3. Select an upper-body image in box 1 (Person).
4. Select a garment image in box 2 (Garment).
5. Click "Generate Try-On". Box 3 (Result) displays the final image once processing finishes (~20–40 seconds).

---

## Free Quota & Limits

- Hugging Face ZeroGPU allocates roughly 60 seconds of free A100 GPU compute per day per account.
- This allows approximately 5–8 generations per day (or 2–3 requests in a single burst).
- The quota regenerates continuously over a rolling 24-hour window at zero cost.
