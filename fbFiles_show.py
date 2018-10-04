import json

with open('files.json', 'r') as f:
    files = json.load(f)
htmlstr = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css" rel="stylesheet">
</head>
<body>
    <div>
       <ol>
        {}
       </ol>
    </div>
</body>

</html>
'''
files_name = []
files_order = []
for i in files:
    files_name.append(files[i])
    files_order.append(i)

files_name.sort()
files_order.sort()

sorted_byvalue = sorted(files.keys(), key=lambda x: files[x])
anchortags = ''
for i in sorted_byvalue:
    print(f" <li> <a href='{i}' target='_blank'> {files[i]}   </a> </li> ")
    anchortags = anchortags + "\n" + \
        f" <li> <a href='{i}' target='_blank'> {files[i]}  </a> </li> "

htmlstr = htmlstr.format(anchortags)

with open("file.html", 'wb') as f:
    f.write(htmlstr.encode())
