from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts,Category,Sub_category
from .forms import PostForm
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
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
        # context['featured_post_img']=Posts.objects.

        context['featured_post']=Posts.objects.get(slug='featured-post')

        yrs =[y.year for y in  list(Posts.objects.values_list('postingDate',flat=True))]
        uyrs=set(yrs)
        context['archives']=sorted(list(uyrs),reverse=True)
        # context['sub_category_list']=Sub_category.objects.values_list(subCategory=1)
        # print(context)
        return context

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




from PIL import Image

def pdf_generate(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    
    post=Posts.objects.all()
    cat=Category.objects.all()
    sub_cat=Sub_category.objects.all()

    c=canvas.Canvas(response)
    c.setFont('Times-Roman',14)
    c.drawString(260,700, "List of events")
    c.drawString(450,750, f"Date: {datetime.now():%d-%m-%Y}")

    img=Image.open(r"C:\Users\prash\OneDrive\Documents\Django project\news_app\static\img\Cmrit.png")
    
    c.drawInlineImage(img,25, 730)
    
    table_data=[]
    header=['Sl.No','Posted By','Posting Date','Title','Category','Sub Category']
    table_data.append(header)
    
    for j,i in enumerate(post):
        table_data.append([f"{j+1}.",i.postedBy,i.postingDate,i.postTitle,i.categoryID,i.subcategoryID])
    
    # for k,ca in enumerate(cat):
    #     table_data[k].append(ca.categoryName)

    print(table_data)

    table=Table(table_data) #,colWidths=[doc.width/3.0]*3
    table=Table(table_data)
    table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25,colors.black),('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
 
    cw=600
    ch=470

    table.wrapOn(c,cw,ch)
    table.drawOn(c,40,ch-len(table_data))


    c.showPage()
    c.save()
    return response
