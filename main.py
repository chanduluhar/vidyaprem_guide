from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

# --- Page Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# --- Video Serving Route (Fix for local video playback) ---
@app.route('/videos/<path:filename>')
def serve_videos(filename):
    # Serves videos from static/videos directory with correct MIME type
    return send_from_directory('static/images', filename, mimetype='video/mp4')





