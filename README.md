# BizzarBazzar

A Flask-based marketplace platform for creative projects and ideas. BizzarBazzar allows users to create, browse, and pledge to unique "bizzars" - creative ventures across various categories including Art & Design, Technology, Environment & Sustainability, and Culture.

## Features

- **User Authentication**: Secure registration and login system with password hashing
- **Admin Panel**: Administrative interface for managing users and bizzars
- **Marketplace**: Browse and explore creative projects
- **Create Bizzars**: Users can create their own projects with detailed information
- **Edit & Remove**: Full CRUD operations for managing bizzars
- **Reviews System**: Community feedback and reviews
- **Recommendations**: Personalized project recommendations based on user preferences
- **Password Reset**: User and admin password recovery

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Authentication**: Werkzeug Security
- **Forms**: WTForms
- **Session Management**: Flask-Session

## Database Schema

The application uses SQLite with the following tables:
- `users` - User accounts
- `administrator` - Admin accounts
- `bizzar` - Project listings
- `reviews` - User reviews
- `preference` - User preferences
- `recommendations` - Recommended projects

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BizzarBazzar
```

2. Install dependencies:
```bash
pip install flask flask-session werkzeug
```

3. Initialize the database:
```bash
python app.py
```

The database will be automatically initialized with sample data on first run.

## Running the Application

Start the Flask development server:
```bash
python run.py
```

Or directly:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Configuration

Before deploying to production, make sure to:
- Change the `SECRET_KEY` in [app.py](app.py:11)
- Set `FLASK_DEBUG=False` in production
- Use a production-grade database (PostgreSQL, MySQL)
- Implement proper environment variable management

## Routes

### Public Routes
- `/` - Landing page
- `/home` - Home page
- `/register` - User registration
- `/login` - User login
- `/admin_register` - Admin registration
- `/admin_login` - Admin login
- `/reset_password` - Password reset
- `/faq` - Frequently asked questions
- `/thegame` - Game information
- `/reviews` - View and submit reviews

### Protected Routes (Require Login)
- `/marketplace` - Browse all bizzars
- `/marketplace_info/<id>` - View bizzar details
- `/create_bizzar` - Create new bizzar
- `/edit_bizzar/<id>` - Edit existing bizzar
- `/remove_bizzar/<id>` - Remove your bizzar
- `/checkout/<id>` - Pledge to a bizzar
- `/recommendations` - View recommendations
- `/logout` - Sign out

### Admin Routes
- `/admin_page` - Admin dashboard
- `/delete_bizzar/<id>` - Delete any bizzar
- `/delete_user/<id>` - Delete user accounts
- `/reset_admin_password` - Admin password reset

## Project Structure

```
BizzarBazzar/
├── app.py              # Main application file
├── database.py         # Database connection utilities
├── forms.py            # WTForms form definitions
├── run.py              # Application runner
├── schema.sql          # Database schema and seed data
├── .flaskenv           # Flask environment configuration
├── static/             # Static files (CSS, images)
│   └── styles.css
├── templates/          # HTML templates
│   ├── index.html
│   ├── home.html
│   ├── marketplace.html
│   ├── create_bizzar.html
│   └── ...
└── flask_session/      # Session storage
```

## Security Considerations

- Passwords are hashed using Werkzeug's `generate_password_hash`
- Session-based authentication
- CSRF protection via WTForms
- SQL injection protection via parameterized queries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- Payment integration for pledges
- Image upload for bizzars
- Email verification
- Social media integration
- Advanced search and filtering
- User profiles and portfolios
- Real-time notifications

## Contact

For questions or support, please open an issue on GitHub.
