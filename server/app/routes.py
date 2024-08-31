from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from .models import Item, db
import os

main = Blueprint('main', __name__)

# Konfigurasi untuk penyimpanan gambar
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
# Pastikan folder uploads ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Fungsi untuk memeriksa apakah file memiliki ekstensi yang diizinkan
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/items', methods=['GET'])
def get_items():
    category = request.args.get('category')
    
    if category:
        items = Item.query.filter_by(category=category).all()  # Filter by category
    else:
        items = Item.query.all()

    return jsonify([
        {'id': item.id, 'name': item.name, 'quantity': item.quantity, 'category': item.category, 'image': item.image}
        for item in items
    ])

    category = request.args.get('category')

    if category:
        item = Item.query.filter_by(category=category).all()
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'image': item.image} for item in items])

@main.route('/items/search', methods=['GET'])
def search_items():
    query = request.args.get('q', '')
    items = Item.query.filter(Item.name.ilike(f'%{query}%')).all()
    return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'image': item.image} for item in items])

@main.route('/items', methods=['POST'])
def add_item():
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    category = request.form.get('category')
    
    # Mengunggah file gambar
    image = None
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            image = filename

    new_item = Item(name=name, quantity=quantity, image=image, category=category)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Item added successfully'}), 201

@main.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    category = request.form.get('category')  # Get the category from form data

    item.name = name
    item.quantity = quantity
    item.category = category

    # Mengunggah file gambar baru jika ada
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            item.image = filename

    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

    item = Item.query.get_or_404(id)
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    category = request.form.get('category')
    image = request.form.get('image')

    item.name = name
    item.quantity = quantity
    item.category = category
    item.image = image

    # Mengunggah file gambar baru jika ada
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            item.image = filename

    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@main.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    
    # Hapus gambar terkait jika ada
    if item.image:
        image_path = os.path.join(UPLOAD_FOLDER, item.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

@main.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    print(f"Serving file from: {full_path}")  # Debugging path
    if os.path.isfile(full_path):
        return send_from_directory(UPLOAD_FOLDER, filename)
    else:
        return jsonify({"error": "File not found"}), 404

