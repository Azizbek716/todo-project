from  django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
  <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Vazifa</title>
</head>
<body>
    <h1>Yangi vazifa yaratish</h1>
    <form>
        <label>Vazifa nomi:</label>
        <input type="text" required>
        <br><br>
        
        <label>Tavsif:</label>
        <textarea rows="4" cols="50"></textarea>
        <br><br>
        
        <label>Muddat:</label>
        <input type="date">
        <br><br>
        
        <label>Muhimlik darajasi:</label>
        <select>
            <option>Past</option>
            <option>O‘rta</option>
            <option>Yuqori</option>
        </select>
        <br><br>
        
        <button>Saqlash</button>
    </form>
</body>
</html>  
    
    """
    return HttpResponse(<!DOCTYPE html>