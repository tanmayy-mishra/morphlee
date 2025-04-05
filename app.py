from flask import Flask, render_template_string
import subprocess
import getpass
import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    
    username = getpass.getuser()
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    
    try:
        
        top_output = subprocess.check_output(
            ['top', '-b', '-n', '1'], 
            universal_newlines=True
        )
    except Exception as e:
        top_output = f"Error running top command: {str(e)}"
    
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTOP Information</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .info-item {
                margin-bottom: 10px;
            }
            .label {
                font-weight: bold;
                display: inline-block;
                width: 120px;
            }
            .top-output {
                background-color: #f8f8f8;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 3px;
                white-space: pre;
                overflow-x: auto;
                font-family: monospace;
                font-size: 12px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>System Information</h1>
            <div class="info-item">
                <span class="label">Name:</span> 
                <span>Tanmay Mishra</span>
            </div>
            <div class="info-item">
                <span class="label">Username:</span> 
                <span>{{ username }}</span>
            </div>
            <div class="info-item">
                <span class="label">Server Time:</span> 
                <span>{{ server_time }}</span>
            </div>
            <h2>Top Output:</h2>
            <div class="top-output">{{ top_output }}</div>
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(
        html_template, 
        username=username,
        server_time=server_time,
        top_output=top_output
    )

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)