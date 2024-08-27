from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts,Category,Sub_category
from .forms import PostForm
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

    
class PostListView(ListView):
    model = Posts
    context_object_name = 'post_list'
    queryset = Posts.objects.filter(isActive = True)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['recent_posts']=Posts.objects.order_by('-postingDate')[:3]
        context['sub_category_list']=Sub_category.objects.all()

        context['featured_post']=Posts.objects.get(slug='featured-post')

        yrs =[y.year for y in  list(Posts.objects.values_list('postingDate',flat=True))]
        uyrs=set(yrs)
        context['archives']=sorted(list(uyrs),reverse=True)
        # context['sub_category_list']=Sub_category.objects.values_list(subCategory=1)
        # print(context)
        return context

        # print(sub_category_list.values_list('subCategory'))

    def get_queryset(self):
        self.cat=self.kwargs.get('cat',None)
        self.d=self.kwargs.get('dt',None)
        if self.cat:
            return Posts.objects.filter(id=self.cat)
        elif self.d:
            return Posts.objects.filter(postingDate__range=[datetime(int(self.d),1,1),datetime(int(self.d),12,31)])
        else:
            return Posts.objects.all()
        # print(self.d)
        # print(self.cat)

class CategoryListView(ListView):
    model=Category
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        sub_cat = Sub_category.objects.all()
        context['sub_category_list'] = sub_cat
        return context
        # count=3
        # context['count'] = count


class PostDetailView(DetailView):
    model=Posts
    context_object_name='post'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['recent_posts']=Posts.objects.order_by('-postingDate')[:3]
        context['sub_category_list']=Sub_category.objects.all()

        context['featured_post']=Posts.objects.get(slug='featured-post')

        yrs =[y.year for y in  list(Posts.objects.values_list('postingDate',flat=True))]
        uyrs=set(yrs)
        context['archives']=sorted(list(uyrs),reverse=True)
        # context['sub_category_list']=Sub_category.objects.values_list(subCategory=1)
        # print(context)
        return context


def post_form(request):
    if request.method=='POST':
        form=PostForm(request.POST )
        if form.is_valid():
            form.save()
    else:
        form=PostForm()
    return render(request,'post_form.html',{'form':form})





def pdf_generate(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'

    post=Posts.objects.all()
    cat=Posts.objects.all().values()

    c=canvas.Canvas(response)
    c.setFont('Times-Roman',14)
    c.drawString(225,800, "List of events")

    header=['Sl.No','Posted By','Title','Category','Sub Category']

    c.setFont('Times-Roman',8)
    x=100 
    for h in header:
        c.drawString(x,750,h)
        x+=100

    # data=[]
    y=750
    for p in post:
        c.drawString(150,y,f'{p.postTitle}')
        y-=100


    c.showPage()
    c.save()
    return response
