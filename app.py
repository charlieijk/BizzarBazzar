from flask import Flask, render_template, request, session, redirect, url_for, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from database import get_db, close_db
from forms import (HomeForm, RegisterForm, LoginForm, ReviewForm, BizzarForm, 
                  EditForm, RecommendForm, AdminRegisterForm, AdminLoginForm, 
                  ResetPasswordForm, ResetAdminPasswordForm, InvestorForm, DeleteUserForm)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# Database setup
app.teardown_appcontext(close_db)

def init_db():
    """Initialize the database with schema.sql"""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    form = HomeForm()
    return render_template('home.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        
        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('register.html', form=form)
        
        db = get_db()
        
        # Check if username already exists
        existing_user = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
        if existing_user:
            flash('Username already exists')
            return render_template('register.html', form=form)
        
        # Insert new user
        hashed_password = generate_password_hash(password)
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                  (username, hashed_password))
        db.commit()
        
        flash('Registration successful')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('marketplace'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html', form=form)

@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    form = AdminRegisterForm()
    if form.validate_on_submit():
        admin_username = form.admin_username.data
        admin_password = form.admin_password.data
        confirm_password = form.confirm_password.data
        
        if admin_password != confirm_password:
            flash('Passwords do not match')
            return render_template('admin_register.html', form=form)
        
        db = get_db()
        
        # Check if admin username already exists
        existing_admin = db.execute('SELECT id FROM administrator WHERE admin_username = ?', 
                                   (admin_username,)).fetchone()
        if existing_admin:
            flash('Admin username already exists')
            return render_template('admin_register.html', form=form)
        
        # Insert new admin
        hashed_password = generate_password_hash(admin_password)
        db.execute('INSERT INTO administrator (admin_username, admin_password) VALUES (?, ?)', 
                  (admin_username, hashed_password))
        db.commit()
        
        flash('Admin registration successful')
        return redirect(url_for('admin_login'))
    
    return render_template('admin_register.html', form=form)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin_username = form.admin_username.data
        admin_password = form.admin_password.data
        
        db = get_db()
        admin = db.execute('SELECT * FROM administrator WHERE admin_username = ?', 
                          (admin_username,)).fetchone()
        
        if admin and check_password_hash(admin['admin_password'], admin_password):
            session['admin_id'] = admin['id']
            session['admin_username'] = admin['admin_username']
            return redirect(url_for('admin_page'))
        else:
            flash('Invalid admin credentials')
    
    return render_template('admin_login.html', form=form)

@app.route('/admin_page')
def admin_page():
    if 'admin_id' not in session:
        flash('Please log in as admin')
        return redirect(url_for('admin_login'))
    
    db = get_db()
    bizzars = db.execute('SELECT * FROM bizzar').fetchall()
    users = db.execute('SELECT * FROM users').fetchall()
    
    return render_template('admin_page.html', bizzars=bizzars, users=users)

@app.route('/marketplace')
def marketplace():
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    db = get_db()
    bizzars = db.execute('SELECT * FROM bizzar').fetchall()
    
    return render_template('marketplace.html', bizzars=bizzars)

@app.route('/marketplace_info/<int:bizzar_id>')
def marketplace_info(bizzar_id):
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    db = get_db()
    bizzar = db.execute('SELECT * FROM bizzar WHERE bizzar_id = ?', (bizzar_id,)).fetchone()
    
    if not bizzar:
        flash('Bizzar not found')
        return redirect(url_for('marketplace'))
    
    return render_template('marketplace_info.html', bizzar=bizzar)

@app.route('/create_bizzar', methods=['GET', 'POST'])
def create_bizzar():
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    form = BizzarForm()
    if form.validate_on_submit():
        db = get_db()
        
        # Check if bizzar_id already exists
        existing_bizzar = db.execute('SELECT bizzar_id FROM bizzar WHERE bizzar_id = ?', 
                                    (form.bizzar_id.data,)).fetchone()
        if existing_bizzar:
            flash('Bizzar ID already exists')
            return render_template('create_bizzar.html', form=form)
        
        db.execute('''INSERT INTO bizzar 
                     (bizzar_id, title, description, reward_pledge_amount, objectives, 
                      category, trait, characteristics, username) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (form.bizzar_id.data, form.title.data, form.description.data,
                   form.reward_pledge_amount.data, form.objectives.data,
                   form.category.data, form.traits.data, form.characteristics.data,
                   session['username']))
        db.commit()
        
        flash('Bizzar created successfully')
        return redirect(url_for('marketplace'))
    
    return render_template('create_bizzar.html', form=form)

@app.route('/edit_bizzar/<int:bizzar_id>', methods=['GET', 'POST'])
def edit_bizzar(bizzar_id):
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    db = get_db()
    bizzar = db.execute('SELECT * FROM bizzar WHERE bizzar_id = ?', (bizzar_id,)).fetchone()
    
    if not bizzar:
        flash('Bizzar not found')
        return redirect(url_for('marketplace'))
    
    form = EditForm()
    
    if form.validate_on_submit():
        db.execute('''UPDATE bizzar SET title = ?, description = ?, 
                     reward_pledge_amount = ?, objectives = ?, category = ?, 
                     trait = ?, characteristics = ? WHERE bizzar_id = ?''',
                  (form.title.data, form.description.data, form.reward_pledge_amount.data,
                   form.objectives.data, form.category.data, form.traits.data,
                   form.characteristics.data, bizzar_id))
        db.commit()
        
        flash('Bizzar updated successfully')
        return redirect(url_for('marketplace'))
    
    # Pre-populate form with existing data
    if request.method == 'GET':
        form.bizzar_id.data = bizzar['bizzar_id']
        form.title.data = bizzar['title']
        form.description.data = bizzar['description']
        form.reward_pledge_amount.data = bizzar['reward_pledge_amount']
        form.objectives.data = bizzar['objectives']
        form.category.data = bizzar['category']
        form.traits.data = bizzar['trait']
        form.characteristics.data = bizzar['characteristics']
    
    return render_template('edit_bizzar.html', form=form, bizzar=bizzar)

@app.route('/delete_bizzar/<int:bizzar_id>')
def delete_bizzar(bizzar_id):
    if 'admin_id' not in session:
        flash('Admin access required')
        return redirect(url_for('admin_login'))
    
    db = get_db()
    db.execute('DELETE FROM bizzar WHERE bizzar_id = ?', (bizzar_id,))
    db.commit()
    
    flash('Bizzar deleted successfully')
    return redirect(url_for('admin_page'))

@app.route('/remove_bizzar/<int:bizzar_id>')
def remove_bizzar(bizzar_id):
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    db = get_db()
    bizzar = db.execute('SELECT * FROM bizzar WHERE bizzar_id = ? AND username = ?', 
                       (bizzar_id, session['username'])).fetchone()
    
    if not bizzar:
        flash('Bizzar not found or you do not have permission to remove it')
        return redirect(url_for('marketplace'))
    
    db.execute('DELETE FROM bizzar WHERE bizzar_id = ?', (bizzar_id,))
    db.commit()
    
    flash('Your bizzar has been removed')
    return redirect(url_for('marketplace'))

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = ReviewForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('INSERT INTO reviews (user, review) VALUES (?, ?)',
                  (form.user.data, form.review.data))
        db.commit()
        flash('Review submitted successfully')
        return redirect(url_for('reviews'))
    
    db = get_db()
    all_reviews = db.execute('SELECT * FROM reviews ORDER BY id DESC').fetchall()
    
    return render_template('reviews.html', form=form, reviews=all_reviews)

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecommendForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('''INSERT INTO preference (criteria, interest_level, 
                     product_preference, comments) VALUES (?, ?, ?, ?)''',
                  (form.criteria.data, form.interest_level.data,
                   form.product_preference.data, form.comments.data))
        db.commit()
        flash('Preferences saved successfully')
        return redirect(url_for('recommendations'))
    
    db = get_db()
    recommended_bizzars = db.execute('SELECT * FROM recommendations').fetchall()
    
    return render_template('recommendations.html', form=form, recommendations=recommended_bizzars)

@app.route('/checkout/<int:bizzar_id>')
def checkout(bizzar_id):
    if 'user_id' not in session:
        flash('Please log in first')
        return redirect(url_for('login'))
    
    db = get_db()
    bizzar = db.execute('SELECT * FROM bizzar WHERE bizzar_id = ?', (bizzar_id,)).fetchone()
    
    if not bizzar:
        flash('Bizzar not found')
        return redirect(url_for('marketplace'))
    
    form = InvestorForm()
    return render_template('checkout.html', bizzar=bizzar, form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/thegame')
def thegame():
    return render_template('thegame.html')

@app.route('/thephase')
def thephase():
    return render_template('thephase.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        username = form.username.data
        new_password = form.password.data
        
        db = get_db()
        user = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
        
        if user:
            hashed_password = generate_password_hash(new_password)
            db.execute('UPDATE users SET password = ? WHERE username = ?',
                      (hashed_password, username))
            db.commit()
            flash('Password reset successfully')
            return redirect(url_for('login'))
        else:
            flash('Username not found')
    
    return render_template('reset_password.html', form=form)

@app.route('/reset_admin_password', methods=['GET', 'POST'])
def reset_admin_password():
    form = ResetAdminPasswordForm()
    if form.validate_on_submit():
        admin_username = form.admin_username.data
        new_password = form.admin_password.data
        
        db = get_db()
        admin = db.execute('SELECT id FROM administrator WHERE admin_username = ?', 
                          (admin_username,)).fetchone()
        
        if admin:
            hashed_password = generate_password_hash(new_password)
            db.execute('UPDATE administrator SET admin_password = ? WHERE admin_username = ?',
                      (hashed_password, admin_username))
            db.commit()
            flash('Admin password reset successfully')
            return redirect(url_for('admin_login'))
        else:
            flash('Admin username not found')
    
    return render_template('reset_admin_password.html', form=form)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    if 'admin_id' not in session:
        flash('Admin access required')
        return redirect(url_for('admin_login'))
    
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    
    flash('User deleted successfully')
    return redirect(url_for('admin_page'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route('/signout')
def signout():
    return render_template('signout.html')

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)