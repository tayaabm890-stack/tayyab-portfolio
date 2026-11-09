from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import ContactMessage


# ================= ADMIN SETTINGS =================

ADMIN_EMAIL = "admin@gmail.com"


# ================= PROJECTS =================

PROJECTS = [
    {
        "number": "01",
        "slug": "django-ecommerce-store",
        "category": "WEB DEVELOPMENT",
        "title": "Django E-Commerce Store",
        "description": "An online store with product browsing, categories, shopping cart, checkout, user accounts and order management.",
        "stack": ["Python", "Django", "SQLite", "Bootstrap"],
        "symbol": "🛍",
        "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1400&q=85",
        "overview": "A database-driven online shopping platform built with Django. Customers can browse products, explore categories, add items to their cart and place orders. Administrators can manage products and monitor orders.",
        "features": [
            "Product listing and category browsing",
            "Product search and featured products",
            "User registration, login and accounts",
            "Shopping cart and checkout system",
            "Order creation and order status tracking",
            "Admin product and order management",
        ],
        "workflow": [
            "Customers browse products and select what they want to buy.",
            "Selected products are added to the shopping cart.",
            "Customers proceed through checkout and create an order.",
            "The administrator reviews orders and updates their status.",
        ],
        "challenges": "Connecting product data, cart operations, user accounts and order management into one reliable Django application.",
        "result": "A complete e-commerce learning project demonstrating backend development, database operations and practical shopping workflows.",
        "github": "",
        "demo": "",
        "disclaimer": "",
    },
    {
        "number": "02",
        "slug": "catdog-ai-classifier",
        "category": "AI + WEB APP",
        "title": "CatDog AI Classifier",
        "description": "A Django image prediction application using a trained TensorFlow model to classify cats and dogs.",
        "stack": ["Django", "TensorFlow", "Python", "Keras"],
        "symbol": "🐾",
        "image": "https://images.unsplash.com/photo-1517849845537-4d257902454a?auto=format&fit=crop&w=1400&q=85",
        "overview": "An AI-powered web application where a user uploads an image and the trained deep-learning model predicts whether the image contains a cat or a dog.",
        "features": [
            "Image upload through a Django web interface",
            "Automatic image resizing for model input",
            "TensorFlow and Keras model integration",
            "Cat or dog prediction",
            "Prediction score display",
            "Simple and responsive user interface",
        ],
        "workflow": [
            "The user selects and uploads an image.",
            "Django receives the image and prepares it for prediction.",
            "The trained model processes the image.",
            "The application displays the predicted class and score.",
        ],
        "challenges": "Making sure image preprocessing in the Django application matches the preprocessing used when training the model.",
        "result": "A working image-classification project that demonstrates how a trained machine-learning model can be integrated into a Django website.",
        "github": "",
        "demo": "",
        "disclaimer": "",
    },
    {
        "number": "03",
        "slug": "medical-records-chatbot",
        "category": "DESKTOP AI",
        "title": "Medical Records Chatbot",
        "description": "A local chatbot for searching structured medical records and answering natural-language questions.",
        "stack": ["Python", "PyQt5", "Ollama", "Pandas"],
        "symbol": "🩺",
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1400&q=85",
        "overview": "A desktop application designed to search structured medical records using natural-language questions. It uses Python and Pandas to retrieve relevant records and a locally running Ollama model to help formulate understandable responses.",
        "features": [
            "Desktop interface built with PyQt5",
            "CSV medical-record data loading",
            "Patient ID and admission information lookup",
            "Natural-language question input",
            "Local Ollama model integration",
            "Concise responses instead of displaying the entire dataset",
        ],
        "workflow": [
            "The user asks a question in the desktop application.",
            "Python searches the medical records for relevant information.",
            "Matching record details are prepared for the local AI model.",
            "The chatbot generates a concise response based on the retrieved information.",
        ],
        "challenges": "Combining accurate record retrieval with natural-language responses while avoiding unnecessary output from the full dataset.",
        "result": "A local AI chatbot prototype demonstrating structured data search and integration with a locally hosted language model.",
        "github": "",
        "demo": "",
        "disclaimer": "This is an educational software prototype, not a medical advice or diagnosis system.",
    },
    {
        "number": "04",
        "slug": "lung-image-classification",
        "category": "MACHINE LEARNING",
        "title": "Lung Image Classification",
        "description": "A MobileNetV2-based educational image classification project. It is not a medical diagnostic tool.",
        "stack": ["Python", "TensorFlow", "MobileNetV2", "PyQt5"],
        "symbol": "🧠",
        "image": "https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=1400&q=85",
        "overview": "An educational machine-learning project using a MobileNetV2-based image classification model. The model was trained to classify images into four dataset categories.",
        "features": [
            "MobileNetV2-based transfer learning",
            "Four image classification categories",
            "TensorFlow and Keras model training",
            "Image prediction workflow",
            "PyQt5 desktop application interface",
            "Model evaluation using a test dataset",
        ],
        "workflow": [
            "The image dataset is organized into training, validation and test folders.",
            "The MobileNetV2-based model is trained using the training data.",
            "The model is evaluated using separate test images.",
            "A desktop application loads an image and displays the model prediction.",
        ],
        "challenges": "Improving classification performance and making sure the desktop application's image preprocessing matches the trained model.",
        "result": "An educational image-classification prototype demonstrating transfer learning and desktop AI integration.",
        "github": "",
        "demo": "",
        "disclaimer": "This project is for educational purposes only. It is not clinically validated and must not be used for medical diagnosis or treatment decisions.",
    },
]

# ================= SERVICES =================

SERVICES = [
    {
        "number": "01",
        "slug": "django-website-development",
        "title": "Django Website Development",
        "category": "WEB DEVELOPMENT",
        "symbol": "⌘",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1400&q=85",
        "short_description": "Custom Django websites with clean structure, database integration and useful functionality.",
        "overview": (
            "I develop custom websites using Python and Django. "
            "From a business website to a database-driven web application, "
            "the goal is to build a responsive, maintainable and user-friendly solution."
        ),
        "features": [
            "Custom Django website development",
            "Responsive pages for desktop, tablet and mobile",
            "User registration, login and authentication",
            "Database integration using SQLite or other supported databases",
            "Admin panel for managing website content",
            "Contact forms and form validation",
            "Product, category and content management where required",
        ],
        "workflow": [
            "Discuss your idea, requirements and website goals.",
            "Plan the pages, features and database structure.",
            "Build the website using Python and Django.",
            "Test the website and fix issues.",
            "Deliver the completed website and explain how to use it.",
        ],
        "technologies": ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite", "Bootstrap"],
        "deliverables": [
            "A working Django website",
            "Responsive user interface",
            "Database-connected functionality",
            "Admin management features where required",
            "Project source code",
        ],
        "github": "",
        "demo": "",
    },
    {
        "number": "02",
        "slug": "bug-fixing-and-improvements",
        "title": "Bug Fixing & Improvements",
        "category": "PYTHON / DJANGO SUPPORT",
        "symbol": "⚙",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1400&q=85",
        "short_description": "Debug Python and Django issues, improve existing features and help get your app working smoothly.",
        "overview": (
            "I help troubleshoot existing Python and Django applications. "
            "This service focuses on understanding errors, finding their causes "
            "and making carefully tested corrections without unnecessarily "
            "changing the rest of your project."
        ),
        "features": [
            "Python errors and debugging",
            "Django URL and view errors",
            "Template and NoReverseMatch issues",
            "Database and model troubleshooting",
            "Form and authentication fixes",
            "Frontend layout and CSS improvements",
            "Code cleanup and small feature improvements",
        ],
        "workflow": [
            "You share the error message and relevant project files.",
            "I inspect the affected code and identify the likely cause.",
            "I make the required correction.",
            "I test the affected functionality.",
            "I explain the changes and provide the corrected code.",
        ],
        "technologies": ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite"],
        "deliverables": [
            "Corrected code for the agreed issue",
            "Explanation of the problem and solution",
            "Testing of the affected feature",
            "Suggestions to avoid similar issues",
        ],
        "github": "",
        "demo": "",
    },
    {
        "number": "03",
        "slug": "web-app-and-database-development",
        "title": "Web App & Database",
        "category": "APPLICATION DEVELOPMENT",
        "symbol": "▤",
     "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=1400&q=85",
        "short_description": "Build forms, dashboards, CRUD features, user accounts and database-backed workflows.",
        "overview": (
            "I build database-driven web applications that help organize "
            "information and simplify everyday workflows. Applications can "
            "include dashboards, user accounts, forms and data management features."
        ),
        "features": [
            "Custom admin and user dashboards",
            "Create, read, update and delete (CRUD) operations",
            "Database models and relationships",
            "Search and filtering functionality",
            "User accounts and access control",
            "Data-entry forms and validation",
            "Organized records and management screens",
        ],
        "workflow": [
            "Understand the information and workflow your application needs.",
            "Design the database models and relationships.",
            "Build forms, views and dashboard pages.",
            "Connect the interface with the database.",
            "Test the complete workflow and deliver the application.",
        ],
        "technologies": ["Python", "Django", "SQLite", "HTML", "CSS", "Bootstrap"],
        "deliverables": [
            "A working database-driven web application",
            "Required forms and management pages",
            "Dashboard and data operations",
            "Source code",
            "Basic usage guidance",
        ],
        "github": "",
        "demo": "",
    },
]
# ================= HOME PAGE =================

@ensure_csrf_cookie
def home(request):
    return render(
        request,
        "portfolio/home.html",
        {
            "projects": PROJECTS,
            "services": SERVICES,
        }
    )

# ================= PROJECT DETAIL PAGE =================

def project_detail(request, slug):
    project = next(
        (item for item in PROJECTS if item["slug"] == slug),
        None
    )

    if project is None:
        raise Http404("Project not found")

    return render(
        request,
        "portfolio/project_detail.html",
        {"project": project}
    )
# ================= SERVICE DETAIL PAGE =================

def service_detail(request, slug):
    service = next(
        (item for item in SERVICES if item["slug"] == slug),
        None
    )

    if service is None:
        raise Http404("Service not found")

    return render(
        request,
        "portfolio/service_detail.html",
        {"service": service}
    )

# ================= CONTACT FORM =================

def contact(request):
    if request.method != "POST":
        return redirect("/#contact")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        messages.error(
            request,
            "Please fill in your name, email and message."
        )
        return redirect("/#contact")

    try:
        validate_email(email)
    except ValidationError:
        messages.error(request, "Please enter a valid email address.")
        return redirect("/#contact")

    if len(message) < 10:
        messages.error(
            request,
            "Please write at least 10 characters about your project."
        )
        return redirect("/#contact")

    ContactMessage.objects.create(
        name=name[:100],
        email=email,
        subject=subject[:150],
        message=message,
    )

    messages.success(
        request,
        "Thanks! Your message has been saved. I'll get back to you."
    )

    return redirect("/#contact")


# ================= ADMIN EMAIL LOGIN =================

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("dashboard")

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if email.lower() != ADMIN_EMAIL.lower() or not password:
            messages.error(request, "Invalid email or password.")
            return render(request, "portfolio/admin_login.html")

        User = get_user_model()

        try:
            user = User.objects.get(
                email__iexact=ADMIN_EMAIL,
                is_staff=True
            )
        except User.DoesNotExist:
            messages.error(request, "Admin account not found.")
            return render(request, "portfolio/admin_login.html")
        except User.MultipleObjectsReturned:
            messages.error(request, "Multiple admin accounts found.")
            return render(request, "portfolio/admin_login.html")

        authenticated_user = authenticate(
            request,
            username=user.get_username(),
            password=password
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("dashboard")

        messages.error(request, "Incorrect admin password.")

    return render(request, "portfolio/admin_login.html")


# ================= ADMIN LOGOUT =================

@require_POST
def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("home")


# ================= ADMIN DASHBOARD =================

@staff_member_required(login_url="/admin-login/")
def dashboard(request):
    total_messages = ContactMessage.objects.count()

    recent_messages = ContactMessage.objects.order_by(
        "-created_at"
    )[:10]

    latest_message_id = (
        ContactMessage.objects.order_by("-id")
        .values_list("id", flat=True)
        .first() or 0
    )

    context = {
        "total_messages": total_messages,
        "recent_messages": recent_messages,
        "latest_message_id": latest_message_id,
    }

    return render(
        request,
        "portfolio/dashboard.html",
        context
    )


# ================= LIVE MESSAGE NOTIFICATIONS =================

@staff_member_required(login_url="/admin-login/")
@require_GET
def new_messages(request):
    try:
        last_id = int(request.GET.get("since", 0))
    except (ValueError, TypeError):
        last_id = 0

    new_items = ContactMessage.objects.filter(
        id__gt=last_id
    ).order_by("id")[:20]

    data = [
        {
            "id": item.id,
            "name": item.name,
            "email": item.email,
            "subject": item.subject or "No subject",
            "message": item.message,
            "created_at": item.created_at.strftime("%d %b %Y, %I:%M %p"),
        }
        for item in new_items
    ]

    return JsonResponse({
        "messages": data
    })