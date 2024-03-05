from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# testimonial
testimonials = [
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
    ('Lokendar Jangid','We had the most incredible experience with [Your Tour and Travel Company].','''From the moment we booked our trip to the moment we returned home, everything was seamless and unforgettable. Our tour guide was knowledgeable, friendly, and made every moment of our journey enjoyable. The itinerary was well-planned, allowing us to explore hidden gems and iconic landmarks alike. Thank you for making our vacation truly memorable. We can't wait to book our next adventure with you!'''),
]

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html', testimonials=testimonials)

# packages
@app.route('/packages')
def packages():
    return render_template('packages.html')

# gallery
gallery_images = [
    ('punevisit.jpg'),
    ('punevisit2.jpg'),
    ('punevisit3.jpg'),
    ('punevisit4.jpg'),
    ('punevisit5.avif'),
    ('punevisit6.webp'),
    ('punevisit.jpg'),
    ('punevisit.jpg'),
    ('punevisit.jpg'),
]

@app.route('/gallery')
def gallery():
    return render_template('gallery.html',gallery_images=gallery_images)   

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
