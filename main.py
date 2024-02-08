from flask import Flask, request, redirect, make_response, render_template
import uuid

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
  if request.form.get('current_password') == 'smart1':
      # Create a new session cookie
      session_cookie = uuid.uuid4().hex
      response = make_response(redirect('general'))
      response.set_cookie('session', session_cookie, max_age=300, httponly=True)
      return response, 307  # Temporary Redirect
  else:
      return 'Invalid password', 401

@app.route('/general', methods=['POST','GET'])
def general():
    # Sort headers alphabetically
    sorted_headers = sorted(request.headers.items(), key=lambda x: x[0])

    # Build formatted response
    response_text = ""
    for header_name, header_value in sorted_headers:
        response_text += f"{header_name}: {header_value}\n"

    # Print form data if it exists for POST requests
    if request.method == 'POST' and request.form:
        response_text += "\nForm Data:\n"
        for field_name, field_value in request.form.items():
            response_text += f"{field_name}: {field_value}\n"

    return response_text, 200, {'Content-Type': 'text/plain'}

@app.route('/', methods=['GET'])
def home():
    print(app.template_folder)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
