from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Uncomment the following route and rename the function if needed
# to avoid conflicts with other routes.
# @app.route('/testimonial')
# def testimonial():
#     return render_template('testimonial.html')

# packages
@app.route('/packages')
def packages():
    return render_template('packages.html')

# gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# about us 
@app.route('/about')
def about():
    return render_template('about.html')

# contact us
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
