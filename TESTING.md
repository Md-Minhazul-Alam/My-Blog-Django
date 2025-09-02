# Testing

[Return to README.md](README.md)

---

## Code Validation



### CSS Validation



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

---

## Defensive Programming

| Feature        | Expectation                        | Test                           | Result                 | Screenshot                                                                                  |
| -------------- | ---------------------------------- | ------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------- |
| Navigation bar | Adaptive on all devices            | Tested desktop, tablet, mobile | Works consistently     | ![screenshot](/blog/static/frontend/features/navbar.png) ![screenshot](/blog/static/frontend/features/mobile-navbar.png) |
| Comment form   | Blocks empty or invalid submission | Submitted empty fields         | Error prompt displayed | ![screenshot](/blog/static/frontend/features/comment-validate.png)                                           |
| Blog slider    | Shows latest posts        | Checked posts updated          | Works as expected      | ![screenshot](/blog/static/frontend/features/sliders.png)                                                    |
| Search modal   | Opens and filters content          | Tested search terms            | Results correct        | ![screenshot](/blog/static/frontend/features/search-model.png) ![screenshot](/blog/static/frontend/features/search-result.png) |
| External links | Open in new tab                    | Clicked social links           | Works as expected      | ![screenshot](/blog/static/frontend/features/quick-link.png) ![screenshot](/blog/static/frontend/features/quick-link-test.png) |

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
