# [My Blog Django](https://minhazulmyblog-2071031bcb58.herokuapp.com/)

Developer: Md Minhazul Alam ([Md-Minhazul-Alam](https://github.com/Md-Minhazul-Alam))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django/commits/master)
[![GitHub last commit](https://img.shields.io/github/last-commit/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django)

I’m Md Minhazul Alam, and this is my **third project** as part of my journey into **full-stack development programme**.
The project is an **data-driven blogging platform** developed with **Django (Python)** as the backend and a **responsive frontend** developed in HTML, CSS, Bootstrap and custom JavaScript.

It highlights my ability to model, develop CRUD, and map backend code to a clean, user-friendly interface.
The objective was to be **simple, responsive, and accessible** and show hands-on Python + Django development capability.

---

## The 5 Planes of UX 

### 1. Strategy
**Purpose**  
This blog site showcases my backend abilities while presenting a responsive, intuitive environment for posting, categorizing, and engaging with blogs.  

**Primary User Needs**  
- View blog entries by category or popularity  
- View posts with images and featured articles  
- Comment on posts, edit or delete them (if email authenticated)  

**Business Goals**  
- Demonstrate Django development skills
- Showcase a project that has real world blog features
- Act as an academic and portfolio piece

---

### 2. Scope
**Features**  
- Responsive navbar with sidebar on mobile  
- Search modal for quick content search  
- Social media integration in navbar and footer  
- Blog slider with recent posts  
- Category based sections admin select  
- Editor's choice and most viewed posts sidebar  
- Full CRUD for posts (admin)  
- Comment section with Add/edit/delete by user
- About, Contact Us and Privacy Policy
- Copyright

**Content Requirements**  
- Post titles, images, categories, tags  
- Featured sections defined by admin  
- Social links and brand identity/logo  

---

### 3. Structure
**Information Architecture**
- **Navigation Menu**: Logo (left), categories, search, social icons, mobile sidebar
- **Homepage**: Slider, latest blogs based on category selection, editor's choice, most viewed
- **Category Page**: Filtered posts, editor's choice, most viewed
- **Blog Details**: Post image, body, categories, comments section (Comment form, Edit & Dlete)
- **Footer**: About us, categories, quick links, social icons and copyright

**User Flow**
1. User lands on homepage → browse latest/featured blogs
2. Category navigation used → filtered blogs
3. Reads a blog post → editor's choice and most viewed
4. Posts a comment (with email for add/edit/delete)
5. Makes use of search modal or social links for more interaction

---

### 4. Skeleton
Four top-level layouts on the website:
- **Homepage** → Hero slider, category based blogs, Editor's choice and most viewed content
- **Category Page** → Posts based on chosen category with sidebar (Most Viewd & Editor Choice)
- **Blog Details** → Post content with image, comments and Category with most viewed Blog
- **Pages** → About, Contact Us and Privacy Policy

User navigation is mobile responsive with sidebar.

---

### 5. Surface
**Visual Design Elements**  
- **Colors**: White background (#FFFFFF), Black text (#000000) for maximum readability  
- **Typography**: Default system UI fonts for consistency and fallback safety  
- **Balance**: Bootstrap with custom CSS ensures responsive alignment across devices  

---

### 6. Assets Structure
**Admin and Frontend**  
- I have two types of assets in this project. One is for admin and another for frontend. 
- **Frontend Assets**: Here we have a assets file under fronted includes css, image and js file. 
- **Reason of Frontend and Admin folder**: I have used two folders Admin and Frontend to clealy separate assets, such as- css, js and image.   

---

# Database Schema

This project has two main apps: **website_settings** and **post**.

---

## App 1: Website Settings

### Table: Setting
| Column                | Type       | Notes                         |
|-----------------------|-----------|-------------------------------|
| id (PK)               | Integer   | Auto-generated primary key    |
| site_name             | Char(200) | Website name                  |
| site_tagline          | Char(200) | Tagline                       |
| site_description      | Text      | Optional                      |
| site_meta_keywords    | Text      | Optional                      |
| site_meta_description | Text      | Optional                      |
| logo                  | Image     | Upload to `/media/logo/`      |

---

## App 2: Post

### Table: Category
| Column        | Type       | Notes |
|---------------|-----------|-------|
| id (PK)       | Integer   | Auto-generated primary key |
| category_name | Char(200) | Category title |
| category_slug | Slug(200) | Unique, auto-generated |
| is_active     | Boolean   | Default: True |

---

### Table: Tag
| Column    | Type       | Notes |
|-----------|-----------|-------|
| id (PK)   | Integer   | Auto-generated primary key |
| tag_name  | Char(200) | Tag title |
| tag_slug  | Slug(200) | Unique, auto-generated |
| is_active | Boolean   | Default: True |

---

### Table: Blog
| Column            | Type         | Notes |
|-------------------|-------------|-------|
| id (PK)           | Integer     | Auto-generated primary key |
| blog_name         | Char(200)   | Title of the blog post |
| blog_slug         | Slug(200)   | Unique, auto-generated |
| category_id (FK)  | ForeignKey  | → Category (nullable) |
| tags (M2M)        | ManyToMany  | → Tag |
| short_description | Text        | Optional |
| description       | HTML/Text   | Rich content |
| thumbnail         | Image       | Upload to `/media/post/` |
| keywords          | Text        | Optional |
| is_featured       | Boolean     | Default: True |
| is_active         | Boolean     | Default: True |
| views             | Integer     | Default: 0 |

---

### Table: Social
| Column      | Type       | Notes |
|-------------|-----------|-------|
| id (PK)     | Integer   | Auto-generated primary key |
| social_name | Char(200) | Name of social platform |
| social_icon | Text      | Icon (SVG or class) |
| social_link | Text      | URL link |
| is_active   | Boolean   | Default: True |

---

### Table: Page
| Column            | Type       | Notes |
|-------------------|-----------|-------|
| id (PK)           | Integer   | Auto-generated primary key |
| page_name         | Char(200) | Page title |
| page_slug         | Slug(200) | Unique, auto-generated |
| description       | Text      | Optional |
| meta_keywords     | Text      | Optional |
| meta_description  | Text      | Optional |
| is_active         | Boolean   | Default: True |

---

### Table: Comment
| Column       | Type        | Notes |
|--------------|------------|-------|
| id (PK)      | Integer    | Auto-generated primary key |
| blog_id (FK) | ForeignKey | → Blog (CASCADE delete) |
| name         | Char(200)  | Commenter name |
| email        | Email      | Commenter email |
| comment      | Text       | Comment body |
| created_at   | DateTime   | Default: now |
| updated_at   | DateTime   | Auto updated |
| is_active    | Boolean    | Default: True |

---

### Table: CategoryBlog
| Column      | Type       | Notes |
|-------------|-----------|-------|
| id (PK)     | Integer   | Auto-generated primary key |
| heading     | Char(255) | Section heading |
| category_id (FK) | ForeignKey | → Category |
| UNIQUE      | (category, heading) | Enforced |

---

## Relationships

- **Blog → Category**: Many blogs can belong to one category.  
- **Blog → Tag**: Many-to-many relationship.  
- **Blog → Comment**: One blog can have many comments.  
- **CategoryBlog → Category**: Each entry links a heading with one category.    

---

## Colour Scheme
- **Primary**: White (#FFFFFF)  
- **Text**: Black (#000000)  
- **Accent**: Bootstrap’s default utilities for buttons/alerts

This keeps the design **clean, accessible, and device-consistent**.

---

## Typography
- Fonts: System UI → Arial, Helvetica Neue, Helvetica / Sans-serif fallback  
- Icons: Font Awesome + SVG for social and UI icons  

---

## Wireframes
No wireframes were formally designed. Instead, development revolves around direct responsive layout building.

## Screenshots

| Page         | Desktop                                                                 | Mobile                                                                 | Tablet                                                                 |
|--------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Home         | ![screenshot](/static/frontend/screenshot/desktop/home-page.png)   | ![screenshot](/static/frontend/screenshot/mobile/home-page.png)   | ![screenshot](/static/frontend/screenshot/tablet/home-page.png)   |
| Category     | ![screenshot](/static/frontend/screenshot/desktop/category-page.png)| ![screenshot](/static/frontend/screenshot/mobile/category-page.png)| ![screenshot](/static/frontend/screenshot/tablet/category-page.png)|
| Blog Details | ![screenshot](/static/frontend/screenshot/desktop/blog-details.png)| ![screenshot](/static/frontend/screenshot/mobile/blog-details.png)| ![screenshot](/static/frontend/screenshot/tablet/blog-details.png)|
| Page         | ![screenshot](/static/frontend/screenshot/desktop/page.png)        | ![screenshot](/static/frontend/screenshot/mobile/page.png)        | ![screenshot](/static/frontend/screenshot/tablet/page.png)        |

---

## User Stories
| Target | Expectation | Outcome |
| --- | --- | ---
| As a visitor | I would love to see blogs by category | So that I can easily find blogs of my interest |
| As a visitor | I woild also like to see most viewed or editor's choice posts | So I can find popular or recommended content
| As a user | I want to post a comment and have the ability to edit/delete them | So that I can comment on posts in my own name and edit/delete them if requires |
| As an admin | I want to post, edit, and remove posts | So that I can manage site content effectively |

---

## Features
| Feature | Notes | Screenshot |
| --- | --- | --- |
| Navbar | Adaptive navbar with sidebar toggle on mobile, logo, categories, search, and social icons | ![screenshot](/static/frontend/features/navbar.png) |
| Blog Slider | Displays latest/featured posts with images | ![screenshot](/static/frontend/features/sliders.png) |
| Category Sections | Admin-controlled category blocks on home page | ![screenshot](/static/frontend/features/category-section.png) |
| Editor's Choice | Manually chosen featured content | ![screenshot](/static/frontend/features/editors-choice.png) |
| Most Viewed | Posts sorted by view count | ![screenshot](/static/frontend/features/most-viewed.png)
| Blog Details | Full page view with comments, related categories, and sidebar | ![screenshot](/static/frontend/features/blog-details.png) |
| Comment System | Users can add, edit, or delete comments through email verification | ![screenshot](/static/frontend/features/comment-section.png) |
| Footer | Quick links, about, and social icons included | ![screenshot](/static/frontend/features/footer.png) |

---

## Future Features
- Dark Mode toggle  
- User authentication system (login/register)  
- Tag filtering for blogs  
- Comment upvote/downvote system  

---

## Tools & Technologies
| Tool / Tech | Use |
| --- | --- |
| Django | Backend framework (Python) |
| MySQL | Posts, categories, tags, comments database |
| HTML / CSS / Bootstrap | Frontend styling |
| JavaScript | Custom interactivity scripts (search modal, sidebar, etc.) |
| Git & GitHub | Version control and hosting |
| VSCode | Local development |
| Font Awesome | Icons |
| [HackMD](https://hackmd.io/) | For README/TESTING documentation |


---

## Agile Development Process

### GitHub Projects
Used for Kanban style task management with epics and issues.

![GitHub Projects](static/frontend/project.PNG)


### GitHub Issues
All errors and improvements were logged here, including Django errors, URL mismatches, and JavaScript bugs.  

### MoSCoW Prioritization
- **Must Have**: CRUD for posts and comments  
- **Should Have**: Responsive sidebar and search modal  
- **Could Have**: Analytics for most viewed posts  
- **Won’t Have**: User login system (future feature)  

---

## Testing
- Reserved space for documenting errors and screenshots in [TESTING.md](TESTING.md).  
- Responsiveness tested across desktop, tablet, and mobile.  

---

## Deployment

- Free-tier deployment isn’t available on Heroku, so it wasn’t used.  
- Deployed on Render.com for testing, but the app may go into sleep mode according to Render policies.  
- During sleep mode, media files may not be visible until the app wakes up.  
- Final deployment will be on a proper Python-based hosting for full functionality.

### Local vs Deployment
- Minor differences may exist between the local and deployed versions.

### Local Development

#### Cloning
1. Go to the GitHub repository.  
2. Click the green "Code" button at the top and copy the URL using HTTPS, SSH, or GitHub CLI.  
3. Open Terminal or Git Bash and navigate to your desired folder.  
4. Run:  
   ```bash
   git clone <repository-url>

---

## Credits
### Content
| Source | Notes |
| --- | --- |
| ChatGPT | Helped debug and explain Django/JS issues |
| Claude AI | Helped debug and explain Django/JS issues |
| W3Schools | References for CSS/JS |
| Django Docs | Backend reference |

### Media
- [Pexels](https://pexels.com) → Stock images  
- [BBC](https://bbc.com) → Blog images and Content
- [Travel to Motom](https://www.traveltomtom.net/) → Blog images and Content
- [Heather Jasper](https://heatherjasper.com/) → Blog images and Content
- [Font Awesome](https://fontawesome.com) → Icons  

### Acknowledgements
- Code Institute resources, Slack and Discord community for inspiration.  
- Online forums for Django troubleshooting.  

---
