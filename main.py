import chardet
from flask import Flask,request
app = Flask(__name__)

@app.route("/fetch", methods=['GET'])
def home():
    try:
        # Optional params       
        file = str(request.args.get('file', "file1.txt"))
        start = int(request.args.get('line_start', 0))
        end = int(request.args.get('line_end', -1))
        
        path = f'./assets/{file}'
        with open(path, 'rb') as file:
            data = file.read()
            result = chardet.detect(data)
        
        with open(path, 'r',encoding=result['encoding']) as file:
            lines = file.readlines()[start:end] if end != -1 else file.readlines()[start:]

        html_content = '<html><body>'
        for line in lines:
            html_content += f'<p>{line}</p>'
        html_content += '</body></html>'
        return html_content
    
    except Exception as e:
        html_content = '<html><body>'
        html_content += '<h1>Error detail :: </h1>'
        html_content += f'<p>{str(e)}</p>'
        return html_content

app.run()