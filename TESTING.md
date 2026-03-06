# Testing

[Return to README.md](README.md)

---

## Code Validation

All HTML and Django template files were validated with [W3C HTML Validator](https://validator.w3.org).

| Page           | Template File                 | Screenshot                           |
| -------------- | ---------------------------- | ------------------------------------ |
| Home           | `templates/pages/index.html`        | ![Home](/static/frontend/testing/html-home.PNG) |
| Category       | `templates/pages/category.html`     | ![Category](/static/frontend/testing/html-category.PNG) |
| Blog Details   | `templates/pages/blog_detail.html`  | ![Blog Details](/static/frontend/testing/html-blog-details.PNG) |
| About          | `templates/pages/about.html`        | ![About](/static/frontend/testing/html-page.PNG) |
| Search         | `templates/pages/search.html`       | ![Search](/static/frontend/testing/html-search.PNG) |

### CSS Validation

The project uses a single global CSS file validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator).

| CSS File                                | Template Files                                                                                   | Screenshot                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `static/frontend/assets/css/style.css`  | `index.html`, `category.html`, `blog_detail.html`, `about.html`, `search.html` (all in `templates/pages/`) | ![CSS Validation](static/frontend/testing/css-validator.PNG) |

### JS Validation  

The project’s JavaScript was validated with [JSHint](https://jshint.com/).  

| Location                  | File / Template                        | Screenshot                                         |  
| -------------------------- | -------------------------------------- | ------------------------------------------------- |  
| `static/frontend/assets/js` | `script.js` (global JavaScript file)   | ![script.js](/static/frontend/testing/script.PNG)  |  
| `templates/pages`          | `blog_detail.html` (inline JavaScript) | ![Comments JS](/static/frontend/testing/comments.png) |  


### PEP8 Validation

The project’s Python code was validated to ensure it follows the **PEP8** style guidelines for readability and consistency. Validation was performed using the **PEP8 Online** code checker.

| Location        | File / Module | Screenshot |
|-----------------|---------------|------------|
| `frontend`  | `view.py` | ![view.py](/static/pep8/frontendview.PNG) |
| `frontend`  | `urls.py` | ![urls.py](/static/pep8/frontendurl.PNG) |
| `post`  | `models.py` | ![models.py](/static/pep8/postmodel.PNG) |
| `post`  | `admin.py` | ![admin.py](/static/pep8/postadmin.PNG) |


All Python files were checked to confirm they comply with **PEP8 standards**, including:

- Proper indentation and spacing
- Correct line length
- Consistent naming conventions for variables, functions, and classes
- Removal of unused imports and variables

The results confirmed that the Python codebase follows **PEP8 guidelines**, helping maintain clean, readable, and maintainable code throughout the project.

---

## Responsiveness

Tested on desktop, tablet, and mobile devices.


| Page         | Desktop                                                                 | Mobile                                                                 | Tablet                                                                 |
|--------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Home         | ![screenshot](/static/frontend/screenshot/desktop/home-page.png)   | ![screenshot](/static/frontend/screenshot/mobile/home-page.png)   | ![screenshot](/static/frontend/screenshot/tablet/home-page.png)   |
| Category     | ![screenshot](/static/frontend/screenshot/desktop/category-page.png)| ![screenshot](/static/frontend/screenshot/mobile/category-page.png)| ![screenshot](/static/frontend/screenshot/tablet/category-page.png)|
| Blog Details | ![screenshot](/static/frontend/screenshot/desktop/blog-details.png)| ![screenshot](/static/frontend/screenshot/mobile/blog-details.png)| ![screenshot](/static/frontend/screenshot/tablet/blog-details.png)|
| Page         | ![screenshot](/static/frontend/screenshot/desktop/page.png)        | ![screenshot](/static/frontend/screenshot/mobile/page.png)        | ![screenshot](/static/frontend/screenshot/tablet/page.png)        |

---

## Browser Compatibility

Tested on Chrome, Firefox, and Safari.

| Page        | Chrome                                         | Firefox                                       | Safari                                         | Notes             |
| ----------- | ---------------------------------------------- | --------------------------------------------- | ---------------------------------------------- | ----------------- |
| Home        | ![screenshot](/static/frontend/testing/browser/chrome/chrome%20home.png)   | ![screenshot](/static/frontend/testing/browser/firefox/firefox%20home.png)    | ![screenshot](/static/frontend/testing/browser/safari/safari%20home.png)   | Works as expected |
| Category    | ![screenshot](/static/frontend/testing/browser/chrome/chrome%20category.png)    | ![screenshot](/static/frontend/testing/browser/firefox/firefox%20category.png)     | ![screenshot](/static/frontend/testing/browser/safari/safari%20category.png)    | Works as expected |
| Blog Detail | ![screenshot](/static/frontend/testing/browser/chrome/chrome%20blog%20details.png) | ![screenshot](/static/frontend/testing/browser/firefox/firefox%20blog%20details.png) | ![screenshot](/static/frontend/testing/browser/safari/safari%20blog%20details.png) | Works as expected |
| About       | ![screenshot](/static/frontend/testing/browser/chrome/chrome%20about%20us.png)  | ![screenshot](/static/frontend/testing/browser/firefox/firefox%20about%20us.png)   | ![screenshot](/static/frontend/testing/browser/safari/safari%20about%20us.png)  | Works as expected |

---


## Lighthouse Audit

Audited with Lighthouse for performance, accessibility, SEO, and best practices.

| Page        | Desktop Screenshot                                                        | Mobile Screenshot                                                        |
| ----------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Home        | ![Home Desktop](/static/frontend/testing/light-desktop-home.PNG)           | ![Home Mobile](/static/frontend/testing/light-mobile-home.PNG)           |
| Category    | ![Category Desktop](/static/frontend/testing/light-desktop-category.PNG)   | ![Category Mobile](/static/frontend/testing/light-mobile-category.PNG)   |
| Blog Detail | ![Blog Detail Desktop](/static/frontend/testing/light-desktop-blog-details.PNG) | ![Blog Detail Mobile](/static/frontend/testing/light-mobile-blog-details.PNG) |
| About/Contact us/Privacy Policy       | ![About Desktop](/static/frontend/testing/light-desktop-page.PNG)          | ![About Mobile](/static/frontend/testing/light-mobile-page.PNG)          |
| Search      | ![Search Desktop](/static/frontend/testing/light-desktop-search.PNG)       | ![Search Mobile](/static/frontend/testing/light-mobile-search.PNG)       |


---

## Defensive Programming

| Feature        | Expectation                        | Test                           | Result                 | Screenshot                                                                                  |
| -------------- | ---------------------------------- | ------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------- |
| Navigation bar | Adaptive on all devices            | Tested desktop, tablet, mobile | Works consistently     | ![screenshot](/static/frontend/features/navbar.png) ![screenshot](/static/frontend/features/mobile-navbar.png) |
| Comment form   | Blocks empty or invalid submission | Submitted empty fields         | Error prompt displayed | ![screenshot](/static/frontend/features/comment-validate.png)                                           |
| Blog slider    | Shows latest posts        | Checked posts updated          | Works as expected      | ![screenshot](/static/frontend/features/sliders.png)                                                    |
| Search modal   | Opens and filters content          | Tested search terms            | Results correct        | ![screenshot](/static/frontend/features/search-model.png) ![screenshot](/static/frontend/features/search-result.png) |
| External links | Open in new tab                    | Clicked social links           | Works as expected      | ![screenshot](/static/frontend/features/quick-link.png) ![screenshot](/static/frontend/features/quick-link-test.png) |

---

## User Story Testing

| Target  | Expectation                 | Outcome                                 | Screenshot                                 |
| ------- | --------------------------- | --------------------------------------- | ------------------------------------------ |
| Visitor | View posts by category      | Can browse category pages               | ![screenshot](/static/frontend/features/category-filter.png)  |
| Visitor | See most viewed/editor's choice posts | most viewed/editor's choice displayed                | ![screenshot](/static/frontend/features/most-viewed.png) ![screenshot](/static/frontend/features/editors-choice.png) |
| User    | Comment with edit/delete    | Works with email verification           | ![screenshot](/static/frontend/features/edit-delete.png) ![screenshot](/static/frontend/features/edit-form.png) |
| Admin   | CRUD posts                  | Create, edit, remove posts successfully | ![screenshot](/static/frontend/features/create.png) ![screenshot](/static/frontend/features/edit-update-delete.png) |
---

## Bugs

* **Navigation overlap on mobile**
  Fix: CSS media queries → Fixed

* **Blog slider broke on small screens**
  Fix: Adjusted width and flex layout → Fixed

* **Comment system not blocking invalid input**
  Fix: Added validation logic → Fixed

* **Some external links not opening in new tab**
  Fix: Added `target="_blank"` → Fixed

* **Data Based link Issues related to port at MAMP**
  Fix: Changed Port Number from 3600 to 8889  → Fixed

  
---

## Known Issues

* None identified currently. All known bugs fixed. 
