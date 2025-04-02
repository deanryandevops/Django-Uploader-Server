from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os

@csrf_exempt  # Exempt this view from CSRF verification (use only for testing)
def upload_file(request):
    """Handles file upload and returns a success response."""
    if request.method == 'POST':
        # Check if a file is included in the request
        if 'file' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file uploaded.'}, status=400)

        uploaded_file = request.FILES['file']

        # Ensure the uploaded_files directory exists
        upload_dir = './uploaded_files'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Save the file to the server
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)