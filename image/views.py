from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from .models import Image


@login_required(login_url='/account')
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({'status': '1'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': '2'})
    else:
        return JsonResponse({'status':'3'})

@login_required(login_url='/account')
@csrf_exempt
@require_POST
def del_image(request):
    image_id=request.POST['image_id']
    try:
        image=Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status':"1"})
    except:
        return JsonResponse({'status': "2"})

#返回用户名下的图片列表
@login_required(login_url='/account')
def list_image(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image/list_images.html', {'images': images})

def falls_images(request):
    images=Image.objects.all()
    return render(request,'image/falls_images.html',{'images':images})
