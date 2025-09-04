
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        
        if not file or file.filename == '':
            return render_template('index.html', error='Файл не обрано')
        
        try:
            content = file.read().decode('utf-8')
            return render_template('index.html', 
                                 content=content, 
                                 filename=file.filename)
        except:
            return render_template('index.html', 
                                 error='Помилка читання файлу')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)