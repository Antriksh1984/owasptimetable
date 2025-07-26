from flask import Flask, render_template, jsonify, send_file, abort
import pandas as pd
import os
import pdfkit
from io import BytesIO
import tempfile

app = Flask(__name__)

def get_years_and_batches():
    """Get available years and batches from the data directory"""
    data_dir = 'data'
    years = []
    batches = {}
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        return years, batches
    
    # Get all year directories
    for item in os.listdir(data_dir):
        year_path = os.path.join(data_dir, item)
        if os.path.isdir(year_path):
            years.append(item)
            
            # Get all CSV files in the year directory
            batch_list = []
            for file in os.listdir(year_path):
                if file.endswith('.csv'):
                    batch_name = file.replace('.csv', '')
                    batch_list.append(batch_name)
            
            batches[item] = sorted(batch_list)
    
    return sorted(years), batches

def load_timetable_data(year, batch):
    """Load and process timetable data from CSV file"""
    csv_path = os.path.join('data', year, f'{batch}.csv')
    
    if not os.path.exists(csv_path):
        return None
    
    try:
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Clean data - fill missing values
        df['Subject'] = df['Subject'].fillna('Free')
        df['Room'] = df['Room'].fillna('-')
        df['Teacher'] = df['Teacher'].fillna('-')
        df['Time'] = df['Time'].fillna('-')
        df['Day'] = df['Day'].fillna('Unknown')
        
        # Group by day
        timetable = {}
        for day in df['Day'].unique():
            day_data = df[df['Day'] == day].to_dict('records')
            timetable[day] = day_data
        
        return timetable
    
    except Exception as e:
        print(f"Error loading timetable: {e}")
        return None

def generate_pdf_html(timetable_data, year, batch):
    """Generate HTML content for PDF with beautiful styling"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Timetable - {year} {batch}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
            
            body {{
                font-family: 'Inter', sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #2d3748;
                min-height: 100vh;
            }}
            
            .container {{
                background: white;
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                max-width: 1000px;
                margin: 0 auto;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 3px solid #667eea;
            }}
            
            .header h1 {{
                font-size: 2.5rem;
                font-weight: 800;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }}
            
            .batch-info {{
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                color: white;
                padding: 15px 30px;
                border-radius: 50px;
                display: inline-block;
                font-weight: 600;
                font-size: 1.2rem;
                margin-bottom: 30px;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }}
            
            thead th {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                font-weight: 600;
                padding: 20px 15px;
                text-align: center;
                font-size: 1.1rem;
            }}
            
            .day-header {{
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
                color: white !important;
                font-weight: 700;
                text-align: center;
                font-size: 1.3rem;
                padding: 15px !important;
            }}
            
            tbody td {{
                padding: 15px;
                border-bottom: 1px solid #e2e8f0;
                text-align: left;
            }}
            
            tbody tr:nth-child(even) {{
                background-color: #f8fafc;
            }}
            
            tbody tr:hover {{
                background-color: #edf2f7;
            }}
            
            .time-cell {{
                font-family: 'JetBrains Mono', monospace;
                font-weight: 600;
                background: linear-gradient(135deg, #f8f9ff, #e8f0ff);
                color: #4c51bf;
                border-radius: 8px;
                text-align: center;
                width: 120px;
            }}
            
            .subject-cell {{
                font-weight: 600;
                color: #2d3748;
            }}
            
            .room-cell {{
                color: #4a5568;
                font-weight: 500;
            }}
            
            .teacher-cell {{
                color: #2d3748;
                font-weight: 500;
            }}
            
            .footer {{
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #e2e8f0;
                color: #718096;
                font-size: 0.9rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📅 Timetable Viewer</h1>
                <div class="batch-info">
                    🎓 Year: {year} | Batch: {batch}
                </div>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>⏰ Time</th>
                        <th>📚 Subject</th>
                        <th>🏫 Room</th>
                        <th>👨‍🏫 Teacher</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Add timetable data
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for day in days:
        if day in timetable_data and timetable_data[day]:
            # Add day header
            html_content += f"""
                <tr>
                    <td colspan="4" class="day-header">📅 {day}</td>
                </tr>
            """
            
            # Add day entries
            for entry in timetable_data[day]:
                html_content += f"""
                <tr>
                    <td class="time-cell">{entry.get('Time', '-')}</td>
                    <td class="subject-cell">{entry.get('Subject', 'Free')}</td>
                    <td class="room-cell">{entry.get('Room', '-')}</td>
                    <td class="teacher-cell">{entry.get('Teacher', '-')}</td>
                </tr>
                """
    
    html_content += """
                </tbody>
            </table>
            
            <div class="footer">
                <p>Generated with ❤️ by Timetable Viewer</p>
                <p>Beautiful schedules for beautiful minds</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

@app.route('/')
def index():
    """Render the main page with years and batches data"""
    years, batches = get_years_and_batches()
    return render_template('index.html', years=years, batches=batches)

@app.route('/timetable/<year>/<batch>')
def get_timetable(year, batch):
    """Get timetable data as JSON"""
    timetable_data = load_timetable_data(year, batch)
    
    if timetable_data is None:
        abort(404)
    
    return jsonify({
        'batch': batch,
        'year': year,
        'timetable': timetable_data
    })

@app.route('/download/<year>/<batch>')
def download_timetable(year, batch):
    """Generate and serve PDF of the timetable"""
    timetable_data = load_timetable_data(year, batch)
    
    if timetable_data is None:
        abort(404)
    
    try:
        # Generate HTML content
        html_content = generate_pdf_html(timetable_data, year, batch)
        
        # Configure PDF options
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        # Generate PDF
        pdf = pdfkit.from_string(html_content, False, options=options)
        
        # Create response
        response = BytesIO(pdf)
        response.seek(0)
        
        filename = f"{year}_{batch}_timetable.pdf"
        
        return send_file(
            response,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
    
    except Exception as e:
        print(f"Error generating PDF: {e}")
        abort(500)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Timetable not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
