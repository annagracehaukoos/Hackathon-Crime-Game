import random
from flask import Flask
app = Flask(__name__)

LEVELS = [
    { 
        "id": 1,
        "title": "Level 1: Beginners",
        "audio": "https://audio-previews.elements.envatousercontent.com/files/88584159/preview.mp3",
        "choices": ["Car Robbery", "Store Shooting", "Vandalism"],
        "correct": 0, 
    }
]

@app.route('/')
def landing():
    return f"""
    <head>
        <title>Audio Agency</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-white p-8 max-w-md mx-auto min-h-screen flex flex-col justify-center items-center text-center bg-cover bg-center" 
        style="background-image: url('https://as2.ftcdn.net/v2/jpg/02/39/63/87/1000_F_239638729_L2e1s3yVG3JkFpMrFH1wut5Fl4SGY6Rk.jpg'); background-size: cover;">
        <h1 class="text-4xl font-extrabold mb-2 text-white tracking-wider">EchoCrime</h1>
        <p class="mb-8 text-white">Listen Closely. Solve the Case.</p>
        <a href="/game" class="block w-full py-4 px-6 mb-4 bg-red-600 hover:bg-red-700 text-white font-bold rounded shadow-lg tracking-wider text-center transition">
            Click to Start
        </a>
    </body>
    """
@app.route('/game')
def game():
    level = random.choice(LEVELS)
    return f"""
    <head>
        <title>EchoCrime</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-white p-8 max-w-md mx-auto min-h-screen flex flex-col justify-center" 
        style="background-image: url('https://as2.ftcdn.net/v2/jpg/02/39/63/87/1000_F_239638729_L2e1s3yVG3JkFpMrFH1wut5Fl4SGY6Rk.jpg'); background-size: cover;">
        <h1 class="text-2xl font-bold mb-1">EchoCrime</h1>
        <p class="mb-4 text-slate-300">{level['title']}</p>
        <audio controls class="w-full mb-4">
            <source src="{level['audio']}" type="audio/mpeg">
        </audio>
        <button class="block w-full p-3 mb-2 bg-slate-800 rounded hover:bg-slate-950 text-left">
            <span class="text-red-500 font-bold mr-2">1.</span> {level['choices'][0]}
        </button>
        <button class="block w-full p-3 mb-2 bg-slate-800 rounded hover:bg-slate-950 text-left">
            <span class="text-red-500 font-bold mr-2">2.</span> {level['choices'][1]}
        </button>
        <button class="block w-full p-3 mb-2 bg-slate-800 rounded hover:bg-slate-950 text-left">
            <span class="text-red-500 font-bold mr-2">3.</span> {level['choices'][2]}
        </button>
        <a href="/" class="text-xs text-red-600 hover:text-white mt-4 text-center underline">Return to Menu</a>
    </body>
    """
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    