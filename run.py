from src.shared.http.server import app

# If it's called directly
if __name__ == '__main__':
  # Run Flask instance -> accessible for all IP's on http://localhost:3000/
  app.run(host='0.0.0.0', port=3000, debug=True)
