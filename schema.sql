DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);



DROP TABLE IF EXISTS bizzar;

CREATE TABLE bizzar(
    bizzar_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    reward_pledge_amount INTEGER,
    objectives TEXT,
    category TEXT NOT NULL,
    trait TEXT NOT NULL,
    characteristics TEXT NOT NULL,
    username TEXT
);


DROP TABLE IF EXISTS preference;

CREATE TABLE preference (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    criteria TEXT,
    interest_level TEXT,
    product_preference TEXT,
    comments TEXT
);


DROP TABLE IF EXISTS recommendations; 

CREATE TABLE recommendations (
    title TEXT NOT NULL,
    description TEXT,
    reward_pledge_amount INTEGER,
    objectives TEXT,
    category TEXT NOT NULL,
    trait TEXT NOT NULL,
    characteristics TEXT NOT NULL
);


DROP TABLE IF EXISTS reviews; 

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    review TEXT NOT NULL
);

DROP TABLE IF EXISTS administrator; 

CREATE TABLE administrator ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_username TEXT NOT NULL UNIQUE,
    admin_password TEXT NOT NULL
);

INSERT INTO recommendations (title, reward_pledge_amount, description, objectives, category, trait, characteristics) VALUES 
('Creative Odyssey', 'To create a masterpiece', 250, 'An exploration of creativity across mediums', 'Art & Design', 'color', 'Exploring the spectrum'),
('Tech Innovate', 'To develop a groundbreaking app', 500, 'Pushing the boundaries of technology', 'Technology and Innovation', 'software development', 'Revolutionizing daily tasks'),
('Eco Champion', 'To launch an environmental campaign', 300, 'Aiming for a greener planet', 'Environment & Sustainability', 'ecological issues', 'Promoting sustainability'),
('Historic Times', 'To document ancient civilizations', 450, 'Uncovering the past for the future', 'Culture and Society', 'historical perspectives', 'Bridging eras'),
('Digital Frontier', 'To pioneer in digital art', 600, 'Blending technology with art', 'Art & Design', 'digital art', 'New age artistry'),
('Sculptors Dream', 'To sculpt a landmark piece', 700, 'Carving dreams into reality', 'Crafts', 'sculpture', 'Timeless creations'),
('Future Gaze', 'To predict tech trends', 850, 'Forecasting the future of tech', 'Technology and Innovation', 'futuristic concepts', 'Tomorrows world today'),
('Cultural Kaleidoscope', 'To celebrate diverse cultures', 950, 'A journey through global cultures', 'Culture and Society', 'cultural differences', 'Unity in diversity'),
('Green Tech', 'To innovate sustainable technologies', 400, 'Technologies for a sustainable future', 'Environment & Sustainability', 'green technology', 'Eco-friendly innovations');

INSERT INTO reviews (user, review) VALUES 
('Alice', 'Absolutely loved it! The experience was unique and memorable.'),
('Bob', 'Interesting concept but could use a bit more polish.'),
('Charlie', 'Had a great time exploring the bizzar. Highly recommend it to anyone looking for something new.'),
('Dana', 'Not what I expected, but in a good way. The creativity here is top-notch.'),
('Evan', 'A bit underwhelming. Maybe I had too high expectations.');

