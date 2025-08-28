# [My Blog Django](https://github.com/Md-Minhazul-Alam/My-Blog-Django)

Developer: Md Minhazul Alam ([Md-Minhazul-Alam](https://github.com/Md-Minhazul-Alam))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django/commits/master)
[![GitHub last commit](https://img.shields.io/github/last-commit/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/Md-Minhazul-Alam/My-Blog-Django)](https://github.com/Md-Minhazul-Alam/My-Blog-Django)

I’m Md Minhazul Alam, and this is my **third project** as part of my journey into **full-stack development programme**.
The project is an **data-driven blogging platform** developed with **Django (Python)** as the backend and a **responsive frontend** developed in HTML, CSS, Bootstrap, and custom JavaScript.

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
- Showcase a project that has real-world blog features
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

## Colour Scheme
- **Primary**: White (#FFFFFF)  
- **Text**: Black (#000000)  
- **Accent**: Bootstrap’s default utilities for buttons/alerts

This keeps the design **clean, accessible, and device-consistent**.

---

## Typography
- Fonts: System UI → Arial / Sans-serif fallback  
- Icons: Font Awesome + SVG for social and UI icons  

---

## Wireframes
No wireframes were formally designed. Instead, development revolves around direct responsive layout building.

| Desktop | Mobile | Tablet |
| --- | --- | --- |
| Home | ![screenshot](/blog/static/frontend/screenshot/desktop/home-page.png) | ![screenshot](/blog/static/frontend/screenshot/mobile/home-page.png) | ![screenshot](/blog/static/frontend/screenshot/tablet/home-page.png) |
| Category | ![screenshot](/blog/static/frontend/screenshot/desktop/category-page.png) | ![screenshot](/blog/static/frontend/screenshot/mobile/category-page.png) | ![screenshot](/blog/static/frontend/screenshot/tablet/category-page.png) |
| Blog Details | ![screenshot](/blog/static/frontend/screenshot/desktop/blog-details.png) | ![screenshot](/blog/static/frontend/screenshot/mobile/blog-details.png) | ![screenshot](/blog/static/frontend/screenshot/tablet/blog-details.png) |
| Page | ![screenshot](/blog/static/frontend/screenshot/desktop/page.png) | ![screenshot](/blog/static/frontend/screenshot/mobile/page.png) | ![screenshot](/blog/static/frontend/screenshot/tablet/page.png) |

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
| Navbar | Adaptive navbar with sidebar toggle on mobile, logo, categories, search, and social icons | ![screenshot](/blog/static/frontend/features/navbar.png) |
| Blog Slider | Displays latest/featured posts with images | ![screenshot](/blog/static/frontend/features/sliders.png) |
| Category Sections | Admin-controlled category blocks on home page | ![screenshot](/blog/static/frontend/features/category-section.png) |
| Editor's Choice | Manually chosen featured content | ![screenshot](/blog/static/frontend/features/editors-choice.png) |
| Most Viewed | Posts sorted by view count | ![screenshot](/blog/static/frontend/features/most-viewed.png)
| Blog Details | Full page view with comments, related categories, and sidebar | ![screenshot](/blog/static/frontend/features/blog-details.png) |
| Comment System | Users can add, edit, or delete comments through email verification | ![screenshot](/blog/static/frontend/features/comment-section.png) |
| Footer | Quick links, about, and social icons included | ![screenshot](/blog/static/frontend/features/footer.png) |

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

